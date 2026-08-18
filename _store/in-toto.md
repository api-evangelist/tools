---
title: in-toto
slug: in-toto
description: The reference implementation of the in-toto framework — records signed attestations about
  each step of a build, so the finished artifact can be traced to how it was made.
companyCount: 2
website: https://in-toto.io
repository: https://github.com/in-toto/in-toto
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 1028
lastCommit: '2026-08-05'
archived: false
specifications:
- slug: in-toto
  name: in-toto
  role: attests
agent:
  interfaces:
  - cli
  - library
  install:
    pypi: in-toto
  emits:
  - in-toto-attestation
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Prove a released artifact came from the pipeline it claims to, and not from somewhere else.
  surface:
  - ci-pipeline
tags:
- in-toto
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 75
precisionGrade: medium
precisionBasis:
- 'collision -25: a surviving needle is also claimed by standards:in-toto'
---
