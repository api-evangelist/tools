#!/usr/bin/env python3
"""Render scripts/roles.yml into the published /roles.json.

roles.json is the vocabulary half of the product — the thing an agent resolves a goal
against before it picks a tool. It had no generator: it was a hand-kept mirror of roles.yml,
which meant the published vocabulary could disagree with the one the gate validates against
and nothing would notice.

Everything here is a rendering. roles.yml is the source of truth.

    build_roles.py --dry     # report whether the published file is current
    build_roles.py           # write roles.json
"""
import collections
import json
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(HERE, "roles.yml")
OUT = os.path.join(REPO, "roles.json")

HEADER = {
    "$id": "https://tools.apievangelist.com/roles.json",
    "name": "API Evangelist tool role vocabulary",
    "description": (
        "What a tool DOES to a specification. An agent holding an artifact and a goal "
        "resolves to a role, and from the role to a shortlist of tools, without reading prose."
    ),
    "schema": "https://tools.apievangelist.com/tool.schema.json",
}

# roles.yml keys, in published order. Anything added there must be listed here to ship.
SECTIONS = ("roles", "produces", "artifacts", "interfaces", "surfaces")


def flat(v):
    """Collapse YAML folded scalars to one line — the JSON is read by machines, not diffed."""
    return " ".join(str(v).split())


def render():
    src = yaml.safe_load(open(SRC))
    missing = [s for s in SECTIONS if s not in src]
    if missing:
        raise SystemExit(f"roles.yml is missing section(s): {', '.join(missing)}")

    out = collections.OrderedDict(HEADER)
    roles = collections.OrderedDict()
    for name, r in src["roles"].items():
        e = collections.OrderedDict()
        for field in ("verb", "question", "returns", "agent_note"):
            if r.get(field):
                e[field] = flat(r[field])
        roles[name] = e
    out["roles"] = roles
    for section in SECTIONS[1:]:
        out[section] = collections.OrderedDict(
            (k, flat(v)) for k, v in src[section].items())
    return out


def main():
    dry = "--dry" in sys.argv
    out = render()
    text = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    current = open(OUT).read() if os.path.exists(OUT) else None

    counts = "  ".join(f"{s}={len(out[s])}" for s in SECTIONS)
    if current == text:
        print(f"roles.json current — {counts}")
        return 0
    if dry:
        print(f"DRY RUN — roles.json is STALE, would rewrite ({counts})")
        return 1
    with open(OUT, "w") as f:
        f.write(text)
    print(f"wrote roles.json — {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
