#!/usr/bin/env python3
"""Run the whole tools.apievangelist.com pipeline, in order, and fail loudly.

The steps were always documented, but only ever run by hand. On 2026-08-12 a standards-store
rename broke the gate; because the gate is step 2 and nobody ran steps 3-4, the site simply
stopped being regenerated and said nothing. Three days of edits went nowhere. One command that
runs everything and exits nonzero is the fix.

    build.py --check      # verify only: no writes, nonzero if anything is stale or invalid
    build.py              # refresh the cache, gate, and regenerate everything
    build.py --offline    # regenerate from the cache as-is, no GitHub calls

Order matters and is not negotiable:

    1. gh_meta      re-read every referenced repo, so archived/license/stars are current
    2. build_roles  render roles.json from roles.yml, so the gate checks what we publish
    3. validate     THE GATE — unresolvable, archived, unknown vocabulary all stop here
    4. build_store  write _store entries for the specification catalogue
    5. sync_demand  reconcile the store against the insights tool vocabulary, and create
                    any entry the vocabulary has and the store lacks
    6. link_standards  the two-way link into the standards site

sync_demand runs AFTER build_store because the two own disjoint fields and build_store
preserves whatever demand fields it finds. It needs insights-work checked out alongside;
pass --no-demand if it is not there, and know the store will be incomplete without it.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *args, allow_fail=False):
    label = f"{script} {' '.join(args)}".strip()
    print(f"\n\033[1m── {label}\033[0m", flush=True)
    r = subprocess.run([sys.executable, os.path.join(HERE, script), *args])
    if r.returncode and not allow_fail:
        print(f"\n\033[31mFAILED at {label} (exit {r.returncode}) — pipeline stopped, "
              f"nothing downstream ran.\033[0m", file=sys.stderr)
        sys.exit(r.returncode)
    return r.returncode


def main():
    check = "--check" in sys.argv
    offline = "--offline" in sys.argv or check

    if not offline:
        run("gh_meta.py", "--refresh", "--prune")
    run("build_roles.py", *(["--dry"] if check else []))
    run("validate_spec_tools.py")
    run("build_store.py", *(["--dry"] if check else []))
    if "--no-demand" in sys.argv:
        print("\n\033[33m── sync_demand.py SKIPPED (--no-demand) — the store will not be "
              "reconciled against the insights vocabulary\033[0m")
    else:
        run("sync_demand.py", *(["--dry"] if check else []))
    run("link_standards.py", *(["--dry"] if check else []))

    print(f"\n\033[32m{'CHECK CLEAN' if check else 'PIPELINE COMPLETE'}\033[0m — "
          f"{'nothing written' if check else 'store, roles.json and the standards link are current'}")
    if not check:
        print("Next: bundle exec jekyll build, then commit tools/ and standards/ together.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
