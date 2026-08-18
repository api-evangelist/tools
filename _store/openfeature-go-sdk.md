---
title: OpenFeature Go SDK
slug: openfeature-go-sdk
description: Evaluates feature flags in Go against any OpenFeature provider.
companyCount: 0
website: https://openfeature.dev
repository: https://github.com/open-feature/go-sdk
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 245
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: openfeature
  name: OpenFeature
  role: evaluates
agent:
  interfaces:
  - library
  install:
    go: github.com/open-feature/go-sdk
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Add vendor-neutral feature flagging to a Go service.
  surface:
  - coding-agent
tags:
- OpenFeature
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
