---
title: quicktype
slug: quicktype
description: Generates typed models in many languages from JSON Schema, sample JSON, or other inputs —
  including inferring a schema from example data.
companyCount: 0
website: https://app.quicktype.io
repository: https://github.com/glideapps/quicktype
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 13839
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: generates
  produces:
  - types
agent:
  interfaces:
  - cli
  - library
  - web-ui
  install:
    npm: quicktype
  invoke: npx quicktype --src <data.json> --lang <language> -o <Model.ts>
  consumes:
  - json-schema
  - json
  emits:
  - source-code
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Turn an undocumented API's sample responses into types and a schema.
  surface:
  - coding-agent
  note: The tool for the common agent situation of having real responses and no contract at all. Inference
    is a starting point, not a specification — treat the output as a draft.
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
