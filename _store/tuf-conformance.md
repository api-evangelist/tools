---
title: TUF Conformance Suite
slug: tuf-conformance
description: A conformance test suite for TUF clients, checking them against the specification.
companyCount: 0
website: https://theupdateframework.github.io/tuf-conformance/
repository: https://github.com/theupdateframework/tuf-conformance
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 9
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: tuf
  name: The Update Framework
  role: tests
agent:
  interfaces:
  - cli
  - library
  emits:
  - json
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Check whether a TUF client implementation is actually correct before trusting it.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- The Update Framework
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
