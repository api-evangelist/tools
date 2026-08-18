---
title: GraphQL Inspector
slug: graphql-inspector
description: Validates a GraphQL schema, compares two versions of one and reports what changed, and flags
  which changes are breaking. It also validates stored operations against a schema, which is how you find
  out that a deploy will break a client before it does.
companyCount: 0
website: https://the-guild.dev/graphql/inspector
repository: https://github.com/graphql-hive/graphql-inspector
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1757
lastCommit: '2026-06-17'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: validates
  also:
  - tests
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    npm: '@graphql-inspector/cli'
  consumes:
  - graphql
  emits:
  - json
  - text
  - markdown
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Determine whether a schema change is breaking before it ships.
  surface:
  - ci-pipeline
  - coding-agent
  note: Breaking-change detection needs BOTH versions of the schema. An agent holding only the new one
    can validate it, but cannot answer this question.
- task: Validate a set of client operations against the schema they will run against.
  surface:
  - ci-pipeline
tags:
- GraphQL
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
