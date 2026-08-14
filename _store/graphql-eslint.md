---
title: GraphQL ESLint
slug: graphql-eslint
description: An ESLint parser, plugin and rule set for GraphQL — lints both schema definitions and the
  operation documents written against them, using the schema itself as the source of truth. Rules cover
  naming, deprecation, field usage and a set of known GraphQL foot-guns, and it runs wherever ESLint already
  runs.
companyCount: 0
website: https://the-guild.dev/graphql/eslint
repository: https://github.com/graphql-hive/graphql-eslint
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 831
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: validates
agent:
  interfaces:
  - library
  - cli
  - ci-action
  install:
    npm: '@graphql-eslint/eslint-plugin'
  consumes:
  - graphql
  - javascript
  emits:
  - json
  - sarif
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Check a GraphQL schema or query document against a team style guide before merge.
  surface:
  - ci-pipeline
  - coding-agent
- task: Catch an operation that references a field the schema no longer has.
  surface:
  - coding-agent
  - ide
tags:
- GraphQL
---
