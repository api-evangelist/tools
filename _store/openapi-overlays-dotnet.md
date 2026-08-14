---
title: openapi-overlays-dotnet
slug: openapi-overlays-dotnet
description: A .NET implementation of the OpenAPI Overlay specification, shipped with the Clio CLI.
companyCount: 0
website: https://github.com/BinkyLabs/openapi-overlays-dotnet
repository: https://github.com/BinkyLabs/openapi-overlays-dotnet
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 6
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: openapi-overlays
  name: OpenAPI Overlay
  role: transforms
agent:
  interfaces:
  - cli
  - library
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
- task: Apply Overlays inside a .NET build without leaving the ecosystem.
  surface:
  - ci-pipeline
tags:
- OpenAPI Overlay
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
