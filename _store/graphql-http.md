---
title: graphql-http
slug: graphql-http
description: A zero-dependency, spec-compliant implementation of the GraphQL over HTTP specification,
  plus an audit suite for checking a server against it.
companyCount: 0
website: https://graphql-http.com
repository: https://github.com/graphql/graphql-http
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 364
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: serves
agent:
  interfaces:
  - library
  - cli
  install:
    npm: graphql-http
  consumes:
  - graphql
  emits:
  - http
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Audit whether a GraphQL server actually conforms to GraphQL over HTTP.
  surface:
  - ci-pipeline
  - coding-agent
  note: One of the few real conformance suites in this whole reference. Most specifications here have
    none.
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
