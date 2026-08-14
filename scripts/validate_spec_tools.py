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

    # Resolve licensing exactly the way build_store.py does. The gate used to read only the cache
    # record, so all nine repos whose license had ALREADY been read out of their LICENSE file and
    # recorded in license-overrides.yml warned on every single run. Nine permanent false warnings
    # is how a warning list stops being read.
    overrides = load(os.path.join(HERE, "license-overrides.yml"))
    lic_over = {k: v["license"] for k, v in (overrides.get("overrides") or {}).items()}
    not_oss = overrides.get("not_open_source") or {}

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
                if not (rec.get("license") or lic_over.get(repo) or repo in not_oss):
                    warnings.append(f"{slug}: `{repo}` has NO license GitHub or a LICENSE file "
                                    f"can resolve ({rec.get('license_name') or 'none'}) — not open "
                                    f"source, and not recorded in license-overrides.yml")
            for r in [t["role"]] + (t.get("also") or []):
                if r not in roles:
                    errors.append(f"{slug}/{repo}: role `{r}` is not in roles.yml")
            for p in t.get("produces") or []:
                if p not in produces_vocab:
                    errors.append(f"{slug}/{repo}: produces `{p}` is not in roles.yml")

    # 6. The agent block is the load-bearing artifact for an agent, and its vocabularies went
    #    unchecked for as long as they existed — so a one-off `surface: copilot` shipped and
    #    nothing resolved it. consumes/emits/interfaces/surface are now gated like roles.
    profiles = (load(os.path.join(HERE, "tool-profiles.yml")) or {}).get("tools") or {}
    artifacts = set(roles_doc["artifacts"])
    interfaces = set(roles_doc["interfaces"])
    surfaces = set(roles_doc["surfaces"])
    published = {t["repo"] for s in spec_tools["specifications"] for t in s["tools"]}

    for repo, prof in sorted(profiles.items()):
        if repo not in published:
            warnings.append(f"tool-profiles.yml has `{repo}`, which spec-tools.yml does not "
                            f"publish — orphan profile")
        agent = prof.get("agent") or {}
        for field, vocab in (("consumes", artifacts), ("emits", artifacts),
                             ("interfaces", interfaces)):
            for v in agent.get(field) or []:
                if v not in vocab:
                    errors.append(f"{repo}: agent.{field} `{v}` is not in roles.yml")
        for uc in prof.get("useCases") or []:
            for s in uc.get("surface") or []:
                if s not in surfaces:
                    errors.append(f"{repo}: useCase surface `{s}` is not in roles.yml")

    # 7. roles.json is what agents actually read. If it has drifted from roles.yml, the
    #    vocabulary being validated here is not the vocabulary being published.
    published_vocab = os.path.join(REPO, "roles.json")
    if os.path.exists(published_vocab):
        with open(published_vocab) as f:
            pub = json.load(f)
        for section in ("roles", "produces", "artifacts", "interfaces", "surfaces"):
            if set(pub.get(section) or {}) != set(roles_doc.get(section) or {}):
                errors.append(f"roles.json `{section}` has drifted from roles.yml — "
                              f"run build_roles.py")

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
