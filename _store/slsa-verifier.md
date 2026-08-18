---
title: SLSA Verifier
slug: slsa-verifier
description: Verifies SLSA provenance against expectations — that an artifact came from the source repository
  and builder it claims.
companyCount: 0
website: https://github.com/slsa-framework/slsa-verifier
repository: https://github.com/slsa-framework/slsa-verifier
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 344
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: slsa
  name: SLSA
  role: verifies
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    go: github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier
  invoke: slsa-verifier verify-artifact <artifact> --provenance-path <provenance> --source-uri <repo>
  consumes:
  - in-toto-attestation
  emits:
  - json
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Check the provenance of a dependency before installing it.
  surface:
  - coding-agent
  - ci-pipeline
  note: The consumer side, and the one that actually reduces risk. Generating provenance nobody verifies
    changes nothing.
tags:
- SLSA
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
