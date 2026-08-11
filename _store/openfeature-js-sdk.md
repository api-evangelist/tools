---
title: OpenFeature JavaScript SDK
slug: openfeature-js-sdk
description: Evaluates feature flags in JavaScript and TypeScript against any provider, so flag code is
  written once and the vendor stays swappable.
companyCount: 0
website: https://openfeature.dev
repository: https://github.com/open-feature/js-sdk
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 275
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: openfeature
  name: OpenFeature
  role: evaluates
agent:
  interfaces:
  - library
  install:
    npm: '@openfeature/server-sdk'
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Write flag evaluation that survives changing flag vendors.
  surface:
  - coding-agent
tags:
- OpenFeature
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
