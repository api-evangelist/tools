---
title: sigstore-js
slug: sigstore-js
description: The Sigstore client for JavaScript, underneath npm's provenance and attestation support.
companyCount: 0
website: https://github.com/sigstore/sigstore-js
repository: https://github.com/sigstore/sigstore-js
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 181
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: signs
agent:
  interfaces:
  - library
  - cli
  install:
    npm: sigstore
  emits:
  - signature
  - json
  deterministic: false
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Verify npm package provenance before adding a dependency.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
