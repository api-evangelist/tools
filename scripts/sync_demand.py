#!/usr/bin/env python3
"""Sync hiring-demand counts from the insights corpus into the tools store.

`companyCount` and `radarRing` are owned by insights-work, not by this repo: they come from the
job corpus via extract-from-corpus.js -> backport-source.js -> rederive-radar-ring.js. This is the
last step of that chain, and the only place the tools site should ever get a count from.

Matching is by name and alternativeNames, normalised — the store slug and the vocabulary name do
not always agree, and a mismatch here silently freezes a tool at its previous quarter's number.
Anything in the store that does NOT match the vocabulary is reported, never left to rot quietly.

    sync_demand.py --dry
    sync_demand.py --quarter q3-2026
"""
import argparse
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STORE = os.path.join(REPO, "_store")
VOCAB = os.path.abspath(os.path.join(REPO, "..", "..", "insights-work", "_data", "tools.yml"))


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s or "").lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--quarter", default="q3-2026")
    ap.add_argument("--basis", default=("uncapped full-corpus read, hardened word-boundary matcher, "
                                        "qualified corpora only"))
    a = ap.parse_args()

    if not os.path.exists(VOCAB):
        print(f"vocabulary not found: {VOCAB}")
        return 1
    vocab = [x for x in (yaml.safe_load(open(VOCAB)) or []) if x and x.get("name")]
    unmeasurable = (yaml.safe_load(open(os.path.join(HERE, "unmeasurable-names.yml"))) or {}
                    ).get("unmeasurable") or {}

    # name -> record, including alternativeNames so store titles that use a different form still match
    index = {}
    for x in vocab:
        for n in [x["name"]] + list(x.get("alternativeNames") or []):
            index.setdefault(norm(n), x)

    changed, same, unmatched = [], 0, []
    for f in sorted(os.listdir(STORE)):
        if not f.endswith(".md"):
            continue
        path = os.path.join(STORE, f)
        text = open(path).read()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)

        keys = [fm.get("title"), fm.get("slug")] + list(fm.get("alternativeNames") or [])
        rec = next((index[norm(k)] for k in keys if k and norm(k) in index), None)
        if rec is None:
            unmatched.append(fm.get("title") or f[:-3])
            continue

        # A tool whose name is an ordinary English word cannot be matched in a job-postings corpus
        # without crediting it for unrelated prose, so its bare needle is blocked and it counts 0.
        # The count is published as 0 like any other; `nameCollision` carries the caveat so the
        # references can be found another way rather than the problem being forgotten.
        # See unmeasurable-names.yml for the sampled evidence behind each one.
        if fm.get("title") in unmeasurable:
            u = unmeasurable[fm["title"]]
            if fm.get("companyCount") == 0 and fm.get("nameCollision"):
                same += 1
                continue
            changed.append((fm.get("title"), fm.get("companyCount"), 0))
            fm["companyCount"] = 0
            fm["companyCountQuarter"] = a.quarter
            fm["nameCollision"] = True
            fm["nameCollisionNote"] = (
                "The name is an ordinary English word, so the job-corpus matcher cannot use it — "
                f"sampled matches were {u['actually']} The bare name is blocked in the matcher, so "
                "this count reflects only qualified matches. Real adoption needs another source.")
            if not a.dry:
                y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100,
                                   default_flow_style=False)
                open(path, "w").write(f"---\n{y}---\n{body}" if body.strip() else f"---\n{y}---\n")
            continue

        new_count = rec.get("companyCount") or 0
        new_ring = rec.get("radarRing")
        if fm.get("companyCount") == new_count and fm.get("radarRing") == new_ring \
                and fm.get("companyCountQuarter") == a.quarter:
            same += 1
            continue

        changed.append((fm.get("title"), fm.get("companyCount"), new_count))
        fm["companyCount"] = new_count
        if new_ring:
            fm["radarRing"] = new_ring
        fm["companyCountQuarter"] = a.quarter
        fm["companyCountBasis"] = a.basis
        if not a.dry:
            y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100,
                               default_flow_style=False)
            open(path, "w").write(f"---\n{y}---\n{body}" if body.strip() else f"---\n{y}---\n")

    changed.sort(key=lambda c: -(c[2] or 0))
    print(f"{'DRY RUN — ' if a.dry else ''}{len(changed)} updated, {same} unchanged, "
          f"{len(unmatched)} with no vocabulary entry")
    print("\nbiggest moves (old -> new):")
    for t, o, n in changed[:20]:
        print(f"  {str(t)[:34]:<34} {str(o):>5} -> {n:>5}")
    if unmatched:
        print(f"\nno vocabulary entry — these keep their previous count and will go stale:")
        print("  " + ", ".join(sorted(unmatched)[:40]))
        if len(unmatched) > 40:
            print(f"  …and {len(unmatched)-40} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
