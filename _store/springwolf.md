---
title: Springwolf
slug: springwolf
description: Generates an AsyncAPI document from a running Spring Boot application by inspecting its listeners
  and publishers — code-first rather than design-first.
companyCount: 0
website: https://www.springwolf.dev
repository: https://github.com/springwolf/springwolf-core
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 347
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: generates
  note: Code-first — derives the AsyncAPI document from a running Spring application.
agent:
  interfaces:
  - library
  - web-ui
  consumes:
  - java
  emits:
  - asyncapi
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Get an AsyncAPI document out of an existing Spring service that never had one.
  surface:
  - coding-agent
  note: 'The realistic path for most estates: the events already exist, the contract does not. Deriving
    it from the code is how you get to a document at all.'
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 92
precisionGrade: high
precisionBasis:
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
