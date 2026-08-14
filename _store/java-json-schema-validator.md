---
title: json-schema-validator (Java)
slug: java-json-schema-validator
description: A JSON Schema validator for the JVM, tracking the current dialects.
companyCount: 0
website: https://github.com/networknt/json-schema-validator
repository: https://github.com/networknt/json-schema-validator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1077
lastCommit: '2026-07-28'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: validates
agent:
  interfaces:
  - library
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
- task: Enforce schema validation inside an existing Java service.
  surface:
  - coding-agent
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
