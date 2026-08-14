---
title: openapi-format
slug: openapi-format
description: Formats, filters, sorts and applies Overlays to OpenAPI documents — the most complete Overlay
  implementation in the JavaScript ecosystem.
companyCount: 0
website: https://openapi-format.com
repository: https://github.com/thim81/openapi-format
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 176
lastCommit: '2026-08-02'
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
    npm: openapi-format
  invoke: npx openapi-format <spec.yaml> -o <out.yaml> --overlayFile <overlay.yaml>
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
- task: Apply an Overlay to a provider's description instead of forking and hand-editing it.
  surface:
  - coding-agent
  - ci-pipeline
  note: 'The pattern an agent should prefer whenever it needs to change a contract it does not own: the
    Overlay is a small reviewable file, and the base description stays upstream and updatable.'
- task: Strip internal or unreleased operations out of a description before publishing it.
  surface:
  - ci-pipeline
- task: Normalise ordering and formatting so contract diffs show real changes only.
  surface:
  - ci-pipeline
tags:
- OpenAPI Overlay
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
