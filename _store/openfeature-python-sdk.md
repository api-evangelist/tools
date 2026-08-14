---
title: OpenFeature Python SDK
slug: openfeature-python-sdk
description: Evaluates feature flags in Python against any OpenFeature provider.
companyCount: 0
website: https://openfeature.dev
repository: https://github.com/open-feature/python-sdk
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 107
lastCommit: '2026-07-14'
archived: false
specifications:
- slug: openfeature
  name: OpenFeature
  role: evaluates
agent:
  interfaces:
  - library
  install:
    pypi: openfeature-sdk
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Gate behaviour in a Python service or model-serving pipeline behind a flag.
  surface:
  - coding-agent
  - ai-platform
tags:
- OpenFeature
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
