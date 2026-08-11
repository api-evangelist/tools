---
title: Ajv
slug: ajv
description: The fastest JSON Schema validator for JavaScript — compiles schemas to validation functions
  and supports every modern dialect.
companyCount: 0
website: https://ajv.js.org
repository: https://github.com/ajv-validator/ajv
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 14798
lastCommit: '2026-05-12'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: validates
agent:
  interfaces:
  - library
  - cli
  install:
    npm: ajv
  consumes:
  - json-schema
  - json
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate a payload against a schema before sending it or after receiving it.
  surface:
  - coding-agent
- task: Check that structured output from a model conforms to an expected schema.
  surface:
  - coding-agent
  - ai-platform
  note: Directly relevant to agent plumbing — this is what turns "the model returned something JSON-shaped"
    into a checkable guarantee.
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
