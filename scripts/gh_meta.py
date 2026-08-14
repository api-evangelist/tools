#!/usr/bin/env python3
"""Fetch and cache GitHub repository facts for candidate tools.

Every tool published to tools.apievangelist.com carries a license and an activity
signal. Both are FACTS READ FROM THE GITHUB API, never recalled — a tool that cannot
be confirmed live is not published. See the never-fabricate-apis rule.

Cache lives in scripts/cache/gh-repos.json so re-runs are free and the harvest is
reproducible. Each record carries `fetched_at` — the date the facts were actually read —
which is what `licenseVerified` on a store entry means. Nothing else may claim it.

With no arguments the repo list comes from spec-tools.yml, so the published set and the
harvested set cannot drift. Usage:

    gh_meta.py                 # fetch anything in spec-tools.yml missing from the cache
    gh_meta.py --refresh       # RE-READ every referenced repo (stars, archived, license)
    gh_meta.py --stale 14      # re-read only records older than N days
    gh_meta.py --prune         # drop cached repos spec-tools.yml no longer references
    gh_meta.py <repos.txt>     # one owner/repo or repo URL per line
    gh_meta.py --report        # dump what is cached

WHY --refresh MATTERS: the site promises that an archived repo does not ship. A repo
archived AFTER it was cached stays "archived: false" forever unless the record is re-read,
so a stale cache silently defeats the gate. Refresh before every publish.
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache", "gh-repos.json")
SPEC_TOOLS = os.path.join(HERE, "spec-tools.yml")

FIELDS = ("full_name,description,html_url,homepage,license,stargazers_count,"
          "forks_count,open_issues_count,archived,disabled,fork,pushed_at,"
          "created_at,topics,default_branch,language,subscribers_count")


def norm(ref):
    """Accept a URL or owner/repo; return owner/repo or None.

    Trailing punctuation is stripped before matching. A ref copied out of prose arrives with
    a quote or a comma stuck to it, and `github.com/owner/repo'` used to cache as a repo named
    `repo'` that could never resolve — four such ghosts were sitting in the cache.
    """
    ref = (ref or "").strip().rstrip("/")
    if not ref:
        return None
    m = re.search(r"github\.com[:/]+([^/]+)/([^/#?\s]+)", ref)
    if m:
        owner, repo = m.group(1), re.sub(r"\.git$", "", m.group(2))
    elif re.fullmatch(r"[^/\s]+/[^/\s]+", ref):
        owner, repo = ref.split("/", 1)
    else:
        return None
    owner, repo = owner.strip("\"'`,.;:)]}"), repo.strip("\"'`,.;:)]}")
    if not re.fullmatch(r"[\w.-]+", owner) or not re.fullmatch(r"[\w.-]+", repo):
        return None
    return f"{owner}/{repo}"


def spec_tools_repos():
    """Every repo spec-tools.yml references — the authoritative harvest list."""
    doc = yaml.safe_load(open(SPEC_TOOLS))
    return sorted({t["repo"] for s in doc["specifications"] for t in s["tools"]})


def load():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except Exception:
        return {}


def fetch(slug):
    """One repo. Returns a dict, or {'error': ...} — never raises, never invents."""
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{slug}", "--jq",
             "{" + ",".join(f"{k}:.{k}" for k in FIELDS.split(",")) + "}"],
            capture_output=True, text=True, timeout=45)
        if out.returncode != 0:
            err = (out.stderr or "").strip().splitlines()
            return {"slug": slug, "error": err[-1] if err else "gh api failed"}
        d = json.loads(out.stdout)
        lic = d.get("license") or {}
        return {
            "fetched_at": date.today().isoformat(),
            "slug": d.get("full_name") or slug,
            "description": d.get("description"),
            "url": d.get("html_url"),
            "homepage": (d.get("homepage") or "").strip() or None,
            "license": lic.get("spdx_id") if lic.get("spdx_id") not in ("NOASSERTION", None) else None,
            "license_name": lic.get("name"),
            "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"),
            "watchers": d.get("subscribers_count"),
            "open_issues": d.get("open_issues_count"),
            "archived": d.get("archived"),
            "disabled": d.get("disabled"),
            "is_fork": d.get("fork"),
            "pushed_at": d.get("pushed_at"),
            "created_at": d.get("created_at"),
            "language": d.get("language"),
            "topics": d.get("topics") or [],
        }
    except Exception as e:
        return {"slug": slug, "error": f"{type(e).__name__}: {e}"}


def stale_before(days):
    return (date.today() - timedelta(days=days)).isoformat()


def harvest(refs, workers=8, refresh=False, stale_days=None, prune=False):
    """Fetch what is missing; with refresh/stale_days, RE-READ what is already cached.

    A cached record is a claim about a live repository, and it decays. `stars` drifts,
    `pushed_at` goes stale, and — the one that matters — a repo can be archived after we
    cached it, which the gate can only catch if the record has been re-read.
    """
    cache = load()
    wanted = [s for s in (norm(r) for r in refs) if s]

    if refresh:
        want = sorted(set(wanted))
    elif stale_days is not None:
        cutoff = stale_before(stale_days)
        want = sorted({s for s in wanted
                       if s not in cache or (cache[s].get("fetched_at") or "") < cutoff})
    else:
        want = sorted({s for s in wanted if s not in cache})

    if want:
        print(f"fetching {len(want)} repos from the GitHub API…", file=sys.stderr)
        changes = []
        with ThreadPoolExecutor(max_workers=workers, ) as ex:
            for asked, rec in zip(want, ex.map(fetch, want)):
                prev = cache.get(rec["slug"]) or {}
                for field in ("archived", "license", "is_fork"):
                    if prev and field in prev and prev.get(field) != rec.get(field):
                        changes.append(f"{rec['slug']}: {field} {prev.get(field)!r} -> {rec.get(field)!r}")
                cache[rec["slug"]] = rec
                # GitHub follows renames silently, so `owner/repo` in spec-tools.yml can resolve
                # to a different full_name. The record caches under the CANONICAL name, which
                # would leave the gate looking up a key that is not there. Alias the old name so
                # the build keeps working, and say so — the source should be updated.
                if rec["slug"] != asked and "error" not in rec:
                    cache[asked] = dict(rec, alias_of=rec["slug"])
                    changes.append(f"{asked}: RENAMED upstream to {rec['slug']} "
                                   f"— update spec-tools.yml")
        for c in changes:
            print(f"  CHANGED  {c}", file=sys.stderr)
    else:
        print("nothing to fetch — cache is current", file=sys.stderr)

    if prune:
        # Only the ghosts: entries that never resolved AND nothing references. Resolved
        # records for repos we evaluated and chose not to publish are CURATION HISTORY —
        # they are the evidence that a candidate was considered, and dropping them would
        # quietly rewrite the harvest as though it had only ever seen what it published.
        keep = set(spec_tools_repos())
        dead = sorted(k for k, v in cache.items() if k not in keep and "error" in v)
        for k in dead:
            del cache[k]
        if dead:
            print(f"pruned {len(dead)} unresolvable ghost(s): {', '.join(dead)}", file=sys.stderr)
        else:
            print("prune: no unresolvable ghosts", file=sys.stderr)

    if want or prune:
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(CACHE, "w") as f:
            json.dump(cache, f, indent=1, sort_keys=True)

    ok = sum(1 for v in cache.values() if "error" not in v)
    oldest = min((v.get("fetched_at") or "?" for v in cache.values()), default="?")
    print(f"cache: {len(cache)} repos ({ok} resolved, {len(cache)-ok} unresolvable), "
          f"oldest read {oldest}", file=sys.stderr)
    return cache


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--report" in args:
        c = load()
        for k, v in sorted(c.items(), key=lambda kv: -(kv[1].get("stars") or 0)):
            if "error" in v:
                print(f"{'ERR':>8}  {k}  {v['error']}")
            else:
                print(f"{v['stars']:>8}  {k:<48} {v['license'] or 'NO-LICENSE':<14} "
                      f"{'ARCHIVED ' if v['archived'] else ''}pushed {v['pushed_at'][:10]} "
                      f"read {v.get('fetched_at') or '?'}")
        sys.exit(0)

    refresh = "--refresh" in args
    prune = "--prune" in args
    stale = None
    if "--stale" in args:
        stale = int(args[args.index("--stale") + 1])
    paths = [a for a in args if not a.startswith("--") and not a.isdigit()]

    # stdin is read only when asked for with `-`. Sniffing isatty() looked clever and was a
    # bug: run from build.py, stdin is not a tty and is also empty, so the harvest silently
    # became a no-op while --prune went right on ahead.
    if paths and paths[0] == "-":
        refs = sys.stdin.read().split()
    elif paths:
        refs = open(paths[0]).read().split()
    else:
        refs = spec_tools_repos()

    harvest(refs, refresh=refresh, stale_days=stale, prune=prune)
