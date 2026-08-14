---
title: Modelina
slug: modelina
description: Generates typed data models from AsyncAPI, OpenAPI, JSON Schema and other inputs — models
  only, deliberately not a whole application framework.
companyCount: 0
website: https://modelina.org
repository: https://github.com/asyncapi/modelina
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 444
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: generates
  produces:
  - types
agent:
  interfaces:
  - cli
  - library
  install:
    npm: '@asyncapi/modelina'
  consumes:
  - asyncapi
  - openapi
  - json-schema
  emits:
  - source-code
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Get message payload types in a target language without adopting a full generator's opinions.
  surface:
  - coding-agent
- task: Keep model classes in sync with schemas across several languages at once.
  surface:
  - ci-pipeline
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
