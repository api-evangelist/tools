#!/usr/bin/env python3
"""Re-derive license-overrides.yml from source, for repos GitHub reports as NOASSERTION.

GitHub's licensee detector misses short-form Apache notices and non-standard filenames. This
reads the repository's actual LICENSE file and matches its text, so a license the site states
is always one that was READ — never one that was assumed from the ecosystem it sits in.

    resolve_licenses.py            # check every NOASSERTION repo in the cache
    resolve_licenses.py --check    # exit nonzero if any override disagrees with source

Anything that comes back UNRESOLVED must stay unlicensed on the site.
"""
import base64
import json
import os
import re
import subprocess
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache", "gh-repos.json")
OVERRIDES = os.path.join(HERE, "license-overrides.yml")

# Ordered: the first pattern that matches wins, so the most specific text is tried first.
SIGNATURES = [
    ("BSD-3-Clause", r"Redistributions in binary form.*?(nor the names|names of its contributors)"),
    ("BSD-2-Clause", r"Redistribution and use in source and binary forms"),
    ("MIT", r"Permission is hereby granted, free of charge"),
    ("Apache-2.0", r"(Apache License\s*,?\s*Version 2\.0|Licensed under the Apache License, Version 2\.0)"),
    ("MPL-2.0", r"Mozilla Public License Version 2\.0"),
    ("GPL-3.0", r"GNU GENERAL PUBLIC LICENSE\s*Version 3"),
    ("ISC", r"Permission to use, copy, modify, and/or distribute this software"),
]


def read_license(slug):
    out = subprocess.run(["gh", "api", f"repos/{slug}/license"],
                         capture_output=True, text=True, timeout=45)
    if out.returncode != 0:
        return None, None
    d = json.loads(out.stdout)
    txt = base64.b64decode(d.get("content", "")).decode("utf8", "replace")
    return d.get("path"), re.sub(r"\s+", " ", txt)


def identify(flat):
    for name, pat in SIGNATURES:
        if re.search(pat, flat, re.S | re.I):
            return name
    return None


def main():
    check = "--check" in sys.argv
    with open(CACHE) as f:
        cache = json.load(f)
    with open(OVERRIDES) as f:
        current = (yaml.safe_load(f) or {}).get("overrides") or {}

    targets = sorted(s for s, v in cache.items()
                     if "error" not in v and not v.get("license"))
    print(f"{len(targets)} repos with no SPDX id from GitHub\n")
    resolved, unresolved, drift = {}, [], []
    for slug in targets:
        path, flat = read_license(slug)
        if not flat:
            unresolved.append((slug, "no license endpoint"))
            print(f"  UNRESOLVED  {slug:<40} no LICENSE file")
            continue
        lic = identify(flat)
        if not lic:
            unresolved.append((slug, "unrecognised text"))
            print(f"  UNRESOLVED  {slug:<40} {flat[:70]}")
            continue
        resolved[slug] = {"license": lic, "file": path}
        was = (current.get(slug) or {}).get("license")
        flag = ""
        if was and was != lic:
            drift.append((slug, was, lic))
            flag = f"  <-- DRIFT, file says {lic}, override says {was}"
        print(f"  {lic:<14} {slug:<40} [{path}]{flag}")

    print(f"\nresolved {len(resolved)}, unresolved {len(unresolved)}")
    if drift:
        print(f"{len(drift)} override(s) disagree with source:")
        for s, w, g in drift:
            print(f"  {s}: override={w} source={g}")
    if check and (drift or unresolved):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
