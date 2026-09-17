---
title: API Flows Studio
slug: api-flows-studio
description: A web application that loads an Arazzo workflow file and displays it — the workflow viewer
  for people who need to see the sequence rather than read it. Backed by a companion Java parser from
  the same org.
companyCount: 0
website: https://api-flows.com/
repository: https://github.com/API-Flows/api-flows-studio
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-17'
stars: 7
lastCommit: '2026-09-10'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: documents
agent:
  interfaces:
  - web-ui
  consumes:
  - arazzo
  emits:
  - html
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Show a non-developer what an Arazzo workflow does, step by step.
  surface:
  - human
tags:
- Arazzo
---
