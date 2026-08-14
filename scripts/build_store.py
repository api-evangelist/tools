#!/usr/bin/env python3
"""Generate and update tools.apievangelist.com _store entries.

Sources, in precedence order:

  spec-tools.yml        which tools implement which specification, and in what role
  tool-profiles.yml     the hand-authored agent block, use cases and body prose
  cache/gh-repos.json   license, stars, last commit, archived — read from the GitHub API
  license-overrides.yml licenses GitHub could not detect, read from the LICENSE file
  _store/*.md           whatever is already published (adoption counts, tags, alt names)

WHAT THIS PRESERVES
Existing `companyCount`, `radarRing`, `tags` and `alternativeNames` are never clobbered — those
come from the demand corpus and the vocabulary, not from here. This script owns the
specification links, licensing, repository facts and the agent block.

    build_store.py --dry     # report what would change
    build_store.py           # write
"""
import json
import os
import re
import sys
from datetime import date

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STORE = os.path.join(REPO, "_store")

OSI = {
    "Apache-2.0", "MIT", "BSD-2-Clause", "BSD-3-Clause", "GPL-2.0", "GPL-3.0",
    "LGPL-2.1", "LGPL-3.0", "AGPL-3.0", "MPL-2.0", "EPL-1.0", "EPL-2.0", "ISC",
    "Unlicense", "CDDL-1.0", "Artistic-2.0", "Zlib", "BSL-1.0",
}


def load_yaml(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p):
        return {}
    with open(p) as f:
        return yaml.safe_load(f) or {}


def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)


def dump_entry(fm, body):
    y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)
    return f"---\n{y}---\n{body}" if body.strip() else f"---\n{y}---\n"


def main():
    dry = "--dry" in sys.argv
    spec_tools = load_yaml("spec-tools.yml")
    profiles = (load_yaml("tool-profiles.yml") or {}).get("tools") or {}
    overrides = load_yaml("license-overrides.yml")
    lic_over = {k: v["license"] for k, v in (overrides.get("overrides") or {}).items()}
    not_oss = overrides.get("not_open_source") or {}
    with open(os.path.join(HERE, "cache", "gh-repos.json")) as f:
        cache = json.load(f)

    # repo -> [{spec, name, role, also, produces, note}]
    by_repo = {}
    for s in spec_tools["specifications"]:
        for t in s["tools"]:
            entry = {"slug": s["spec"], "name": s["name"], "role": t["role"]}
            for k in ("also", "produces", "note"):
                if t.get(k):
                    entry[k] = t[k]
            by_repo.setdefault(t["repo"], []).append(entry)

    # existing store, indexed by repo and by slug so we update rather than duplicate
    existing = {}
    by_existing_repo = {}
    for f in os.listdir(STORE):
        if not f.endswith(".md"):
            continue
        fm, body = split_front_matter(open(os.path.join(STORE, f)).read())
        existing[f[:-3]] = (fm, body, f)
        r = fm.get("repository")
        if r:
            m = re.search(r"github\.com/([^/]+/[^/#?]+)", r)
            if m:
                by_existing_repo[m.group(1)] = f[:-3]

    created, updated, skipped = [], [], []
    today = date.today().isoformat()

    for repo, specs in sorted(by_repo.items()):
        gh = cache.get(repo)
        if not gh or "error" in gh or gh.get("archived"):
            skipped.append((repo, "unresolved or archived"))
            continue

        prof = profiles.get(repo) or {}
        name = prof.get("title") or repo.split("/")[-1]
        slug = prof.get("slug") or by_existing_repo.get(repo) or slugify(name)

        if slug in existing:
            fm, body, fname = existing[slug]
        else:
            fm, body, fname = {}, "", f"{slug}.md"

        lic = gh.get("license") or lic_over.get(repo)
        lic_src = "github-api" if gh.get("license") else ("license-file" if lic else "unresolved")
        if repo in not_oss:
            lic, lic_src = not_oss[repo]["license"], "license-file"

        out = dict(fm)
        out["title"] = fm.get("title") or name
        out["slug"] = slug
        out["description"] = prof.get("description") or fm.get("description") or gh.get("description") or ""
        out.setdefault("companyCount", fm.get("companyCount", 0))
        if fm.get("radarRing"):
            out["radarRing"] = fm["radarRing"]
        out["website"] = prof.get("website") or gh.get("homepage") or fm.get("website") or gh["url"]
        out["repository"] = gh["url"]

        out["license"] = lic
        out["licenseSource"] = lic_src
        out["openSource"] = bool(lic and lic in OSI)
        # The date the license was actually READ from the API, carried on the cache record —
        # not the date this script last ran. Stamping today on every run restated 128 claims
        # nobody had re-verified, and buried real changes in a 128-file diff.
        out["licenseVerified"] = gh.get("fetched_at") or fm.get("licenseVerified") or today

        out["stars"] = gh.get("stars")
        out["lastCommit"] = (gh.get("pushed_at") or "")[:10] or None
        out["archived"] = bool(gh.get("archived"))

        out["specifications"] = specs
        if prof.get("agent"):
            out["agent"] = prof["agent"]
        if prof.get("useCases"):
            out["useCases"] = prof["useCases"]

        tags = fm.get("tags") or prof.get("tags") or []
        for s in specs:
            if s["name"] not in tags:
                tags.append(s["name"])
        out["tags"] = tags
        if fm.get("alternativeNames"):
            out["alternativeNames"] = fm["alternativeNames"]
        elif prof.get("alternativeNames"):
            out["alternativeNames"] = prof["alternativeNames"]

        new_body = prof.get("body", body)
        text = dump_entry(out, new_body)
        path = os.path.join(STORE, fname)
        old = open(path).read() if os.path.exists(path) else None
        if old == text:
            continue
        (updated if old else created).append(slug)
        if not dry:
            with open(path, "w") as f:
                f.write(text)

    print(f"{'DRY RUN — ' if dry else ''}{len(created)} created, {len(updated)} updated, {len(skipped)} skipped")
    if created:
        print(f"  created: {', '.join(sorted(created))}")
    for r, why in skipped:
        print(f"  SKIP {r}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
