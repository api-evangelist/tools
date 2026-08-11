#!/usr/bin/env python3
"""List a specification's governing GitHub org(s), ranked, so tool selection is evidence-based.

The candidate pool for "top tools for spec X" comes from the org that actually stewards the
spec, read live from the GitHub API — not from recall. Archived repos, forks and the spec
document repos themselves are reported but flagged, so a dead project is never published as
a live tool.

    gh_orgs.py asyncapi open-telemetry sigstore
"""
import json
import subprocess
import sys


def org_repos(org):
    out = subprocess.run(
        ["gh", "api", "--paginate", f"orgs/{org}/repos?per_page=100&sort=updated"],
        capture_output=True, text=True, timeout=180)
    if out.returncode != 0:
        # not an org — try a user account
        out = subprocess.run(
            ["gh", "api", "--paginate", f"users/{org}/repos?per_page=100&sort=updated"],
            capture_output=True, text=True, timeout=180)
        if out.returncode != 0:
            print(f"  !! {org}: {out.stderr.strip().splitlines()[-1:]}", file=sys.stderr)
            return []
    repos = []
    for chunk in out.stdout.replace("][", "]\x00[").split("\x00"):
        try:
            repos.extend(json.loads(chunk))
        except Exception:
            pass
    return repos


if __name__ == "__main__":
    for org in sys.argv[1:]:
        repos = org_repos(org)
        live = [r for r in repos if not r.get("archived") and not r.get("fork")]
        live.sort(key=lambda r: -(r.get("stargazers_count") or 0))
        print(f"\n===== {org} — {len(repos)} repos, {len(live)} live non-fork =====")
        for r in live[:14]:
            lic = ((r.get("license") or {}).get("spdx_id") or "—")
            lic = "—" if lic == "NOASSERTION" else lic
            print(f"  {r['stargazers_count']:>6}★ {lic:<13} {r['full_name']:<44} "
                  f"pushed {r['pushed_at'][:10]}  {(r.get('description') or '')[:72]}")
        dead = [r for r in repos if r.get("archived")]
        if dead:
            print(f"  [archived: {', '.join(r['name'] for r in sorted(dead, key=lambda r:-(r.get('stargazers_count') or 0))[:8])}]")
