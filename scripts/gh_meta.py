#!/usr/bin/env python3
"""Fetch and cache GitHub repository facts for candidate tools.

Every tool published to tools.apievangelist.com carries a license and an activity
signal. Both are FACTS READ FROM THE GITHUB API, never recalled — a tool that cannot
be confirmed live is not published. See the never-fabricate-apis rule.

Cache lives in scripts/cache/gh-repos.json so re-runs are free and the harvest is
reproducible. Usage:

    gh_meta.py <repos.txt>     # one owner/repo or repo URL per line
    gh_meta.py --report        # dump what is cached
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache", "gh-repos.json")

FIELDS = ("full_name,description,html_url,homepage,license,stargazers_count,"
          "forks_count,open_issues_count,archived,disabled,fork,pushed_at,"
          "created_at,topics,default_branch,language,subscribers_count")


def norm(ref):
    """Accept a URL or owner/repo; return owner/repo or None."""
    ref = (ref or "").strip().rstrip("/")
    if not ref:
        return None
    m = re.search(r"github\.com[:/]+([^/]+)/([^/#?]+)", ref)
    if m:
        return f"{m.group(1)}/{re.sub(r'\.git$', '', m.group(2))}"
    if re.fullmatch(r"[\w.-]+/[\w.-]+", ref):
        return ref
    return None


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


def harvest(refs, workers=8):
    cache = load()
    want = []
    for r in refs:
        s = norm(r)
        if s and s not in cache:
            want.append(s)
    want = sorted(set(want))
    if want:
        print(f"fetching {len(want)} repos from the GitHub API…", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=workers) as ex:
            for rec in ex.map(fetch, want):
                cache[rec["slug"]] = rec
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(CACHE, "w") as f:
            json.dump(cache, f, indent=1, sort_keys=True)
    ok = sum(1 for v in cache.values() if "error" not in v)
    print(f"cache: {len(cache)} repos ({ok} resolved, {len(cache)-ok} unresolvable)", file=sys.stderr)
    return cache


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--report":
        c = load()
        for k, v in sorted(c.items(), key=lambda kv: -(kv[1].get("stars") or 0)):
            if "error" in v:
                print(f"{'ERR':>8}  {k}  {v['error']}")
            else:
                print(f"{v['stars']:>8}  {k:<48} {v['license'] or 'NO-LICENSE':<14} "
                      f"{'ARCHIVED ' if v['archived'] else ''}pushed {v['pushed_at'][:10]}")
        sys.exit(0)
    src = sys.argv[1] if len(sys.argv) > 1 else None
    refs = open(src).read().split() if src else sys.stdin.read().split()
    harvest(refs)
