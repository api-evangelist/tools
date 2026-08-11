---
title: NTIA Conformance Checker
slug: ntia-conformance-checker
description: Checks an SPDX SBOM against the NTIA minimum elements and CISA guidance — whether it satisfies
  the baseline regulators actually ask for.
companyCount: 0
website: https://spdx.github.io/ntia-conformance-checker/
repository: https://github.com/spdx/ntia-conformance-checker
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 89
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: validates
agent:
  interfaces:
  - cli
  - library
  install:
    pypi: ntia-conformance-checker
  consumes:
  - spdx
  emits:
  - json
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Prove an SBOM meets a named compliance baseline, not just that it parses.
  surface:
  - ci-pipeline
  - coding-agent
  note: A well-formed SBOM and a compliant one are different things. This is the check that distinguishes
    them, and it is the one procurement will run.
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
