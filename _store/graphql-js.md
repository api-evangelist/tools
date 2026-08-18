---
title: GraphQL.js
slug: graphql-js
description: The JavaScript reference implementation of GraphQL — the parser, type system, validator and
  execution engine the specification is realised in.
companyCount: 0
website: http://graphql.org/graphql-js/
repository: https://github.com/graphql/graphql-js
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 20345
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: serves
  note: The reference implementation.
agent:
  interfaces:
  - library
  install:
    npm: graphql
  consumes:
  - graphql
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Parse and validate a GraphQL schema or query without standing up a server.
  surface:
  - coding-agent
- task: Check whether a query is valid against a schema before it is ever sent.
  surface:
  - coding-agent
  - ci-pipeline
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
