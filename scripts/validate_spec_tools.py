#!/usr/bin/env python3
"""Enforce the rules spec-tools.yml declares about itself, before anything is published.

Checks, in order of how badly each one would embarrass us:

  1. Every `repo` resolved live against the GitHub API — an unresolvable repo is a tool that
     does not exist, and publishing it is fabrication.
  2. No archived and no forked repos — a dead project listed as live tooling is worse than
     an omission, because an agent will try to use it.
  3. Every `spec` is a real slug in api-evangelist/standards/_store — otherwise the two-way
     link renders as a 404 and the standards page never gains its tooling section.
  4. Every `role` and `produces` value is in the roles.yml controlled vocabulary — the
     vocabulary is the product; an unlisted verb is not machine-readable.
  5. Licensing is present. A tool with no detectable license is reported, not silently
     published as though it were open source.

Exits nonzero on any failure so it can gate the generator.
"""
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STANDARDS_STORE = os.path.abspath(os.path.join(REPO, "..", "standards", "_store"))
CACHE = os.path.join(HERE, "cache", "gh-repos.json")


def load(p):
    with open(p) as f:
        return yaml.safe_load(f)


def main():
    import json
    spec_tools = load(os.path.join(HERE, "spec-tools.yml"))
    roles_doc = load(os.path.join(HERE, "roles.yml"))
    roles = set(roles_doc["roles"])
    produces_vocab = set(roles_doc["produces"])
    with open(CACHE) as f:
        cache = json.load(f)

    known_standards = {f[:-3] for f in os.listdir(STANDARDS_STORE) if f.endswith(".md")}

    errors, warnings, seen_repos = [], [], set()
    n_specs = n_tools = 0

    for s in spec_tools["specifications"]:
        n_specs += 1
        slug = s["spec"]
        if slug not in known_standards:
            errors.append(f"spec `{slug}` has no entry at standards/_store/{slug}.md")
        for sib in s.get("sibling_specs") or []:
            if sib not in known_standards:
                errors.append(f"sibling_spec `{sib}` (under {slug}) has no standards entry")

        for t in s["tools"]:
            n_tools += 1
            repo = t["repo"]
            seen_repos.add(repo)
            rec = cache.get(repo)
            if rec is None:
                errors.append(f"{slug}: `{repo}` is not in the GitHub cache — run gh_meta.py")
            elif "error" in rec:
                errors.append(f"{slug}: `{repo}` did not resolve — {rec['error']}")
            else:
                if rec.get("archived"):
                    errors.append(f"{slug}: `{repo}` is ARCHIVED — do not publish as live tooling")
                if rec.get("is_fork"):
                    errors.append(f"{slug}: `{repo}` is a fork, not the canonical home")
                if not rec.get("license"):
                    warnings.append(f"{slug}: `{repo}` has NO detectable OSI license "
                                    f"({rec.get('license_name') or 'none'}) — do not call it open source")
            for r in [t["role"]] + (t.get("also") or []):
                if r not in roles:
                    errors.append(f"{slug}/{repo}: role `{r}` is not in roles.yml")
            for p in t.get("produces") or []:
                if p not in produces_vocab:
                    errors.append(f"{slug}/{repo}: produces `{p}` is not in roles.yml")

    print(f"{n_specs} specifications, {n_tools} tool bindings, {len(seen_repos)} distinct repos")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} failure(s) — nothing generated.")
        return 1
    print(f"\nclean{f' ({len(warnings)} warning(s))' if warnings else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
