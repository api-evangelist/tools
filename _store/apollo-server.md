---
title: Apollo Server
slug: apollo-server
description: A spec-compliant GraphQL server for Node.js, with a plugin system covering caching, tracing
  and persisted queries.
companyCount: 3
website: https://www.apollographql.com/docs/apollo-server/
repository: https://github.com/apollographql/apollo-server
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 13944
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: graphql
  name: GraphQL
  role: serves
agent:
  interfaces:
  - library
  install:
    npm: '@apollo/server'
  consumes:
  - graphql
  emits:
  - http
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Stand up a production GraphQL endpoint from a schema and resolvers.
  surface:
  - coding-agent
tags:
- GraphQL
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
