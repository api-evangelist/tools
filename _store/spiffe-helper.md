---
title: SPIFFE Helper
slug: spiffe-helper
description: Fetches SVIDs from the Workload API and writes them to disk, restarting or signalling a process
  on rotation — how software that cannot speak SPIFFE still gets a SPIFFE identity.
companyCount: 0
website: https://github.com/spiffe/spiffe-helper
repository: https://github.com/spiffe/spiffe-helper
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 75
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: issues
agent:
  interfaces:
  - cli
  - container
  emits:
  - x509
  - jwt
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Give workload identity to a legacy application that only knows how to read a certificate file.
  surface:
  - ci-pipeline
  - coding-agent
  note: The pragmatic adoption path — no application change, just certificates appearing on disk and being
    rotated underneath.
tags:
- SPIFFE
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
