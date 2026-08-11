---
title: AsyncAPI Parser
slug: asyncapi-parser
description: Parses and validates AsyncAPI documents into a stable intermediate model, resolving references
  — the library every other AsyncAPI tool is built on.
companyCount: 0
website: https://github.com/asyncapi/parser-js
repository: https://github.com/asyncapi/parser-js
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 144
lastCommit: '2026-08-09'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: parses
agent:
  interfaces:
  - library
  install:
    npm: '@asyncapi/parser'
  consumes:
  - asyncapi
  emits:
  - json
  deterministic: true
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Reason about an event contract programmatically instead of parsing YAML by hand.
  surface:
  - coding-agent
  note: Use this rather than a raw YAML load — it resolves references and normalises across specification
    versions, which is where hand-rolled parsing quietly goes wrong.
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
