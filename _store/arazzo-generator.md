---
title: Arazzo Generator
slug: arazzo-generator
description: An npm CLI that drafts Arazzo workflows from an OpenAPI document — point it at the description
  and it writes a starting workflow file. A generated draft is a guess at the sequence, not a description
  of one; useful as scaffolding.
companyCount: 0
website: https://github.com/JaredCE/Arazzo-Generator
repository: https://github.com/JaredCE/Arazzo-Generator
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 0
lastCommit: '2026-03-10'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: generates
agent:
  interfaces:
  - cli
  install:
    npm: arazzo-generator
  consumes:
  - openapi
  emits:
  - arazzo
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Scaffold a first Arazzo file from an OpenAPI so a human can edit the sequence.
  surface:
  - coding-agent
  note: v0.0.x; the operations it emits are real, the order is inferred.
tags:
- Arazzo
---
