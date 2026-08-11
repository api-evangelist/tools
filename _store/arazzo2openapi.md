---
title: arazzo2openapi
slug: arazzo2openapi
description: Converts an Arazzo workflow description into an OpenAPI description, so a multi-step workflow
  can be exposed as a conventional API surface.
companyCount: 0
website: https://frankkilcommins.github.io/arazzo2openapi/
repository: https://github.com/frankkilcommins/arazzo2openapi
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 5
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: converts
agent:
  interfaces:
  - cli
  consumes:
  - arazzo
  emits:
  - openapi
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Expose an orchestrated workflow to consumers that only understand OpenAPI.
  surface:
  - coding-agent
tags:
- Arazzo
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
