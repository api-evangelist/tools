---
title: AsyncAPI Studio
slug: asyncapi-studio
description: A visual editor for AsyncAPI documents with live validation and a rendered preview of the
  event-driven architecture being described.
companyCount: 0
website: https://studio.asyncapi.com
repository: https://github.com/asyncapi/studio
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 210
lastCommit: '2026-08-08'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: authors
agent:
  interfaces:
  - web-ui
  - container
  install:
    npm: '@asyncapi/studio'
  consumes:
  - asyncapi
  emits:
  - asyncapi
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Give a human a place to review and edit a contract an agent drafted.
  surface:
  - human
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
