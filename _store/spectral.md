---
title: Spectral
slug: spectral
description: The API style-guide linter — validates OpenAPI, AsyncAPI and Arazzo documents against rulesets
  you write yourself, and emits machine-readable findings with source locations.
companyCount: 31
website: https://stoplight.io/spectral
repository: https://github.com/stoplightio/spectral
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 3175
lastCommit: '2026-08-08'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: validates
  note: The de facto API style-guide linter; also the only mature Arazzo validator.
- slug: arazzo
  name: Arazzo
  role: validates
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    npm: '@stoplight/spectral-cli'
  invoke: npx @stoplight/spectral-cli lint <spec.yaml> --ruleset <.spectral.yaml> --format json
  consumes:
  - openapi
  - asyncapi
  - arazzo
  - json
  - yaml
  emits:
  - json
  - junit
  - sarif
  - github-actions
  - pretty
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Check an API description against an organisation's own design rules before it ships.
  surface:
  - coding-agent
  - ci-pipeline
  note: The highest-leverage agent use of any tool here — the output is a structured list of findings
    with paths and line numbers, so the agent can go fix them rather than summarise them.
- task: Prove a third-party API description is fit to build against before generating a client from it.
  surface:
  - coding-agent
- task: Author a ruleset that encodes a governance policy, then run it across an estate.
  surface:
  - coding-agent
  - ci-pipeline
- task: Validate an Arazzo workflow document — currently the most capable option for doing so.
  surface:
  - coding-agent
tags:
- OpenAPI
- Arazzo
radarRing: Established
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
