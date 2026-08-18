---
title: Swagger UI
slug: swagger-ui
description: The original interactive OpenAPI console — renders a description as browsable documentation
  with a live "try it" client against the real API.
companyCount: 0
website: https://swagger.io
repository: https://github.com/swagger-api/swagger-ui
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 28972
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: documents
agent:
  interfaces:
  - library
  - container
  - web-ui
  install:
    npm: swagger-ui-dist
  consumes:
  - openapi
  emits:
  - html
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Embed an interactive console in an existing developer portal.
  surface:
  - human
  - coding-agent
- task: Let a human verify by hand what an agent has been calling programmatically.
  surface:
  - human
tags:
- OpenAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 75
precisionGrade: medium
precisionBasis:
- 'collision -25: a surviving needle is also claimed by standards:Swagger'
---
