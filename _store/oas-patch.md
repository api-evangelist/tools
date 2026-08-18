---
title: oas-patch
slug: oas-patch
description: A Python CLI and library for applying OpenAPI Overlays and JSON Patch documents to OpenAPI
  descriptions.
companyCount: 0
website: https://github.com/mcroissant/oas_patcher
repository: https://github.com/mcroissant/oas_patcher
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 9
lastCommit: '2026-03-17'
archived: false
specifications:
- slug: openapi-overlays
  name: OpenAPI Overlay
  role: transforms
agent:
  interfaces:
  - cli
  - library
  install:
    pypi: oas-patch
  consumes:
  - openapi
  - openapi-overlay
  emits:
  - openapi
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Apply Overlays from a Python pipeline without introducing a Node toolchain.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- OpenAPI Overlay
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
