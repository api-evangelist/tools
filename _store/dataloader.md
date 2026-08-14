---
title: DataLoader
slug: dataloader
description: Batches and caches backend requests within a single GraphQL execution — the standard answer
  to the N+1 query problem GraphQL resolvers create.
companyCount: 4
website: https://github.com/graphql/dataloader
repository: https://github.com/graphql/dataloader
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 13389
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
    npm: dataloader
  consumes:
  - javascript
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Fix a GraphQL server making one database call per item in a list.
  surface:
  - coding-agent
  note: A specific, recognisable performance bug with a standard fix — good ground for an agent, because
    the problem and the remedy are both well defined.
tags:
- GraphQL
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
