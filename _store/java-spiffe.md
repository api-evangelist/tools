---
title: java-spiffe
slug: java-spiffe
description: The Java library for consuming SPIFFE identities and validating peers.
companyCount: 0
website: https://github.com/spiffe/java-spiffe
repository: https://github.com/spiffe/java-spiffe
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 45
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: verifies
agent:
  interfaces:
  - library
  consumes:
  - x509
  - jwt
  deterministic: true
  offline: true
  mutates: false
  credentials: true
useCases:
- task: Adopt workload identity inside an existing JVM service.
  surface:
  - coding-agent
tags:
- SPIFFE
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
