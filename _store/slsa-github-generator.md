---
title: SLSA GitHub Generator
slug: slsa-github-generator
description: Generates SLSA provenance for artifacts built in GitHub Actions, using reusable workflows
  that produce non-forgeable attestations.
companyCount: 0
website: https://github.com/slsa-framework/slsa-github-generator
repository: https://github.com/slsa-framework/slsa-github-generator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 591
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: slsa
  name: SLSA
  role: attests
agent:
  interfaces:
  - ci-action
  emits:
  - in-toto-attestation
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Attach verifiable provenance to a release without building attestation infrastructure.
  surface:
  - ci-pipeline
tags:
- SLSA
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
