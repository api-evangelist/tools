---
title: TUF-on-CI
slug: tuf-on-ci
description: Runs a TUF repository and its signing ceremonies inside CI, with hardware-token signing and
  review gates.
companyCount: 0
website: https://github.com/theupdateframework/tuf-on-ci
repository: https://github.com/theupdateframework/tuf-on-ci
license: MIT
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 51
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: tuf
  name: The Update Framework
  role: signs
agent:
  interfaces:
  - ci-action
  - cli
  consumes:
  - tuf-metadata
  emits:
  - tuf-metadata
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Operate a TUF repository without building bespoke signing infrastructure.
  surface:
  - ci-pipeline
tags:
- The Update Framework
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
