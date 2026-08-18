---
title: GraphQL Tools
slug: graphql-tools
description: Builds, stitches and transforms GraphQL schemas — merges several schemas into one and rewrites
  them without touching the underlying services.
companyCount: 0
website: https://www.graphql-tools.com
repository: https://github.com/ardatan/graphql-tools
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 5431
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: transforms
agent:
  interfaces:
  - library
  install:
    npm: '@graphql-tools/schema'
  consumes:
  - graphql
  emits:
  - graphql
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Compose several existing GraphQL services into one schema for consumers.
  surface:
  - coding-agent
- task: Present a filtered view of a schema to a different audience without forking it.
  surface:
  - coding-agent
tags:
- GraphQL
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
