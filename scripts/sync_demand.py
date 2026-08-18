#!/usr/bin/env python3
"""Make the tools store a complete, accurate representation of the insights tool vocabulary.

The store is the UNION of two things: every tool in the demand vocabulary, plus the ones added
to support a specification. This script owns the first half.

`companyCount`, `radarRing` and the `precision*` fields are owned by insights-work, not by this
repo: they come from the job corpus via extract-from-corpus.js -> backport-source.js ->
score-precision.py -> rederive-radar-ring.js. This is the last step of that chain, and the only
place the tools site should ever get a count from.

PRECISION is a second, independent axis added 2026-08-18: how trustworthy the tool's NAME is as a
corpus needle, regardless of how many companies said it. The two filter together and the cell that
matters is where they disagree — a low precision on a high count is the shape of every false
positive this pipeline has published. A tool graded `unmeasurable` ships companyCount: null rather
than a number, because a count nobody can defend is worse than no count.

Matching is by name and alternativeNames, normalised — the store slug and the vocabulary name do
not always agree, and a mismatch here silently freezes a tool at its previous quarter's number.

WHAT IT CREATES
A vocabulary entry with no store entry used to be invisible: sync only ever updated what already
existed, so the store could silently fall behind the vocabulary and nothing reported it. Missing
entries are now CREATED from the vocabulary record (description, tags, url, founded,
alternativeNames, radarRing, companyCount). Six had gone missing this way.

WHAT IT WILL NOT TOUCH
For a tool that is also spec-linked, the curated profile owns `description`, `website` and `tags`
— a hand-written profile beats a vocabulary blurb, and build_store.py is the authority there.
This script only ever writes the demand fields on those entries.

    sync_demand.py --dry
    sync_demand.py --quarter q3-2026
"""
import argparse
import collections
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STORE = os.path.join(REPO, "_store")
VOCAB = os.path.abspath(os.path.join(REPO, "..", "..", "insights-work", "_data", "tools.yml"))


def norm(s):
    """Aggressive fold, for fuzzy matching only. NOTE it destroys `#` and `++`, so `C#` and
    `C++` both become `c`. Never resolve on this alone — see exact()."""
    return re.sub(r"[^a-z0-9]+", "", str(s or "").lower())


def exact(s):
    """Case-fold and collapse whitespace, but keep every distinguishing character."""
    return re.sub(r"\s+", " ", str(s or "").strip().lower())


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

    # Resolution is ordered from certain to fuzzy, and REFUSES to guess when a key is claimed by
    # more than one vocabulary record. The previous index folded names and alternativeNames
    # together and took first-wins, which published C++'s hiring count on the C# page, SonarQube's
    # on Sonar's, and Apache's on Apache HTTP Server's — 11x, 3x and 33x overstatements.
    by_exact, exact_claims = {}, collections.defaultdict(set)
    by_slug = {}
    by_norm, norm_claims = {}, collections.defaultdict(set)
    by_alt, alt_claims = {}, collections.defaultdict(set)
    for x in vocab:
        exact_claims[exact(x["name"])].add(x["name"])
        by_exact.setdefault(exact(x["name"]), x)
        norm_claims[norm(x["name"])].add(x["name"])
        by_norm.setdefault(norm(x["name"]), x)
        if x.get("slug"):
            by_slug.setdefault(exact(x["slug"]), x)
        for n in x.get("alternativeNames") or []:
            alt_claims[norm(n)].add(x["name"])
            by_alt.setdefault(norm(n), x)

    ambiguous = {
        "exact": {k for k, v in exact_claims.items() if len(v) > 1},
        "norm": {k for k, v in norm_claims.items() if len(v) > 1},
        "alt": {k for k, v in alt_claims.items() if len(v) > 1},
    }

    def resolve(fm):
        """Most certain match wins; an ambiguous key is skipped, never guessed."""
        title, slug = fm.get("title"), fm.get("slug")
        k = exact(title)
        if k and k in by_exact and k not in ambiguous["exact"]:
            return by_exact[k]
        k = exact(slug)
        if k and k in by_slug:
            return by_slug[k]
        k = norm(title)
        if k and k in by_norm and k not in ambiguous["norm"]:
            return by_norm[k]
        for n in [title] + list(fm.get("alternativeNames") or []):
            k = norm(n)
            if k and k in by_alt and k not in ambiguous["alt"]:
                return by_alt[k]
        return None

    changed, same, unmatched, resynced = [], 0, [], []
    seen_vocab = set()
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

        rec = resolve(fm)
        if rec is None:
            unmatched.append((fm.get("title") or f[:-3], bool(fm.get("specifications"))))
            continue
        seen_vocab.add(rec["name"])

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
        new_prec = rec.get("precision")
        new_grade = rec.get("precisionGrade")
        new_basis = rec.get("precisionBasis") or []
        if not isinstance(new_basis, list):
            new_basis = [new_basis]
        # An unmeasurable name must not ship a number — whatever the matcher produced for it is
        # an artifact of an ordinary word, not evidence of hiring.
        if new_grade == "unmeasurable":
            new_count = None

        # For a demand-only entry the vocabulary also owns the descriptive fields, and nothing used
        # to carry a later correction across — fix a description in the vocabulary and the store
        # kept the old one forever. A spec-linked entry is left alone: build_store.py's curated
        # profile is deliberately better than a vocabulary blurb.
        desc_updates = {}
        if not fm.get("specifications"):
            for store_key, vocab_key in (("description", "description"), ("tags", "tags"),
                                         ("website", "url"), ("founded", "founded"),
                                         ("alternativeNames", "alternativeNames")):
                want = rec.get(vocab_key)
                if isinstance(want, str):
                    want = want.strip()
                if want in (None, "", []):
                    continue
                if fm.get(store_key) != want:
                    desc_updates[store_key] = want

        if not desc_updates and fm.get("companyCount") == new_count \
                and fm.get("radarRing") == new_ring \
                and fm.get("companyCountQuarter") == a.quarter \
                and fm.get("precision") == new_prec \
                and fm.get("precisionGrade") == new_grade:
            same += 1
            continue

        if desc_updates:
            resynced.append((fm.get("title"), sorted(desc_updates)))
            fm.update(desc_updates)
        if not (fm.get("companyCount") == new_count and fm.get("radarRing") == new_ring
                and fm.get("companyCountQuarter") == a.quarter):
            changed.append((fm.get("title"), fm.get("companyCount"), new_count))
        fm["companyCount"] = new_count
        if new_ring:
            fm["radarRing"] = new_ring
        fm["companyCountQuarter"] = a.quarter
        fm["companyCountBasis"] = a.basis
        if new_prec is not None:
            fm["precision"] = new_prec
            fm["precisionGrade"] = new_grade
            fm["precisionBasis"] = new_basis
        if not a.dry:
            y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100,
                               default_flow_style=False)
            open(path, "w").write(f"---\n{y}---\n{body}" if body.strip() else f"---\n{y}---\n")

    # Anything in the vocabulary with no store entry at all. The store is meant to represent the
    # whole vocabulary, so a gap here is a missing tool, not a judgement call.
    existing_slugs = {f[:-3] for f in os.listdir(STORE) if f.endswith(".md")}
    created = []
    for rec in vocab:
        if rec["name"] in seen_vocab or rec.get("show") is False:
            continue
        slug = rec.get("slug") or re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-",
                                                            rec["name"].lower())).strip("-")
        if not slug or slug in existing_slugs:
            continue
        fm = {
            "title": rec["name"],
            "slug": slug,
            "companyCount": rec.get("companyCount") or 0,
            "description": (rec.get("description") or "").strip(),
            "tags": list(rec.get("tags") or []),
        }
        if rec.get("url"):
            fm["website"] = rec["url"]
        if rec.get("founded"):
            fm["founded"] = rec["founded"]
        if rec.get("radarRing"):
            fm["radarRing"] = rec["radarRing"]
        if rec.get("alternativeNames"):
            fm["alternativeNames"] = list(rec["alternativeNames"])
        fm["companyCountQuarter"] = a.quarter
        fm["companyCountBasis"] = a.basis
        created.append((rec["name"], slug, fm["companyCount"]))
        existing_slugs.add(slug)
        if not a.dry:
            y = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100,
                               default_flow_style=False)
            open(os.path.join(STORE, f"{slug}.md"), "w").write(f"---\n{y}---\n")

    changed.sort(key=lambda c: -(c[2] or 0))
    print(f"{'DRY RUN — ' if a.dry else ''}{len(created)} created, {len(changed)} recounted, "
          f"{len(resynced)} resynced, {same} unchanged, {len(unmatched)} with no vocabulary entry")

    listable = {r["name"] for r in vocab if r.get("show") is not False}
    covered = (seen_vocab | {n for n, _s, _c in created}) & listable
    hidden = seen_vocab - listable
    print(f"\ncoverage: {len(covered)}/{len(listable)} listable vocabulary entries have a store "
          f"entry{'' if len(covered) == len(listable) else '  <-- INCOMPLETE'}")
    gaps = sorted(listable - covered)
    if gaps:
        print("  MISSING: " + ", ".join(gaps[:30]) + (f" …and {len(gaps)-30} more" if len(gaps) > 30 else ""))
    if hidden:
        print(f"  note: {len(hidden)} store entr(ies) map to a `show: false` vocabulary record "
              f"({', '.join(sorted(hidden))}) — published here but hidden in insights.")

    if created:
        print("\ncreated from the vocabulary (name, slug, companyCount):")
        for n, s, c in sorted(created, key=lambda c: -(c[2] or 0)):
            print(f"  {str(n)[:34]:<34} {s:<24} {c:>5}")
    if resynced:
        print(f"\ndescriptive fields pulled from the vocabulary ({len(resynced)}):")
        for t, fields in sorted(resynced)[:20]:
            print(f"  {str(t)[:34]:<34} {', '.join(fields)}")
    if changed:
        print("\nbiggest moves (old -> new):")
        for t, o, n in changed[:20]:
            print(f"  {str(t)[:34]:<34} {str(o):>5} -> {'withheld' if n is None else n:>5}")
    if unmatched:
        spec_linked = [t for t, s in unmatched if s]
        orphans = [t for t, s in unmatched if not s]
        if spec_linked:
            print(f"\n{len(spec_linked)} spec-linked tool(s) not in the demand vocabulary — "
                  f"expected, they were added to support a specification, but they will carry "
                  f"no companyCount until the vocabulary covers them:")
            print("  " + ", ".join(sorted(spec_linked)))
        if orphans:
            print(f"\n{len(orphans)} ORPHAN(S) — in neither the vocabulary nor any specification. "
                  f"These keep their previous count and will go stale:")
            print("  " + ", ".join(sorted(orphans)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
