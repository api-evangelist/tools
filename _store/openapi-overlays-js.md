---
title: openapi-overlays-js
slug: openapi-overlays-js
description: A small, focused JavaScript implementation of the OpenAPI Overlay specification — applies
  an overlay to a base document and nothing else.
companyCount: 0
website: https://github.com/lornajane/openapi-overlays-js
repository: https://github.com/lornajane/openapi-overlays-js
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 28
lastCommit: '2025-05-20'
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
    npm: openapi-overlays-js
  invoke: npx openapi-overlays-js <spec.yaml> <overlay.yaml>
  consumes:
  - openapi
  - openapi-overlay
  emits:
  - openapi
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Apply an Overlay with a single dependency and no surrounding toolchain.
  surface:
  - coding-agent
  - ci-pipeline
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
