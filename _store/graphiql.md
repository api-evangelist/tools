---
title: GraphiQL
slug: graphiql
description: The reference GraphQL IDE — an in-browser query editor with schema introspection, autocomplete
  and documentation, plus the language server behind editor integrations.
companyCount: 0
website: https://github.com/graphql/graphiql
repository: https://github.com/graphql/graphiql
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 16892
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: authors
  also:
  - documents
agent:
  interfaces:
  - web-ui
  - library
  - lsp
  install:
    npm: graphiql
  consumes:
  - graphql
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Explore an unfamiliar GraphQL API's schema before writing queries against it.
  surface:
  - human
  - ide
- task: Provide schema-aware autocomplete to a copilot editing GraphQL documents.
  surface:
  - copilot
  - ide
tags:
- GraphQL
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
