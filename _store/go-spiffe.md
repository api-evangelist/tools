---
title: go-spiffe
slug: go-spiffe
description: The Go library for consuming SPIFFE identities — fetches SVIDs from the Workload API and
  validates peer identities.
companyCount: 0
website: https://github.com/spiffe/go-spiffe
repository: https://github.com/spiffe/go-spiffe
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 206
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: verifies
agent:
  interfaces:
  - library
  install:
    go: github.com/spiffe/go-spiffe/v2
  consumes:
  - x509
  - jwt
  deterministic: true
  offline: true
  mutates: false
  credentials: true
useCases:
- task: Authenticate a Go service to its peers using a workload identity rather than an API key.
  surface:
  - coding-agent
tags:
- SPIFFE
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
