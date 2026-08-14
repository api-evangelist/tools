---
title: AsyncAPI Generator
slug: asyncapi-generator
description: Generates documentation, code and configuration from an AsyncAPI document using a template
  system — the output is whatever template you point it at.
companyCount: 0
website: https://asyncapi.com/docs/tools/generator
repository: https://github.com/asyncapi/generator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1070
lastCommit: '2026-08-08'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: generates
agent:
  interfaces:
  - cli
  - library
  install:
    npm: '@asyncapi/generator'
  invoke: npx @asyncapi/generator <asyncapi.yaml> <template> -o <out-dir>
  consumes:
  - asyncapi
  emits:
  - source-code
  - html
  - markdown
  deterministic: true
  offline: false
  mutates: true
  credentials: false
useCases:
- task: Produce documentation for an event-driven API from its contract.
  surface:
  - ci-pipeline
  - coding-agent
- task: Scaffold a producer or consumer against an agreed event contract.
  surface:
  - coding-agent
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
