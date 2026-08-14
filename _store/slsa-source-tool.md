---
title: SLSA Source Tool
slug: slsa-source-tool
description: A proof-of-concept implementation of the SLSA Source Track, attesting to source-side controls.
companyCount: 0
website: https://github.com/slsa-framework/source-tool
repository: https://github.com/slsa-framework/source-tool
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 18
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: slsa
  name: SLSA
  role: attests
agent:
  interfaces:
  - cli
  emits:
  - in-toto-attestation
  deterministic: false
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Experiment with attesting source-repository controls, not just build steps.
  surface:
  - ci-pipeline
  note: A proof of concept — evaluate before depending on it.
tags:
- SLSA
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
