---
title: Speakeasy OpenAPI
slug: speakeasy-openapi
description: A Go library and CLI for parsing, validating and transforming OpenAPI, Arazzo and Overlay
  documents — one of the few toolchains that treats all three OpenAPI Initiative specifications as first-class.
companyCount: 0
website: https://www.speakeasy.com
repository: https://github.com/speakeasy-api/openapi
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 275
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - validates
  - transforms
- slug: openapi-overlay
  name: OpenAPI Overlay
  role: transforms
agent:
  interfaces:
  - cli
  - library
  install:
    go: github.com/speakeasy-api/openapi
  consumes:
  - openapi
  - arazzo
  - openapi-overlay
  emits:
  - json
  - yaml
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Work with Arazzo or Overlay documents from Go, where almost nothing else exists.
  surface:
  - coding-agent
- task: Apply an Overlay to a base description programmatically as part of a pipeline.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- Arazzo
- OpenAPI Overlay
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
