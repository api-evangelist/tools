---
title: SPIRE
slug: spire
companyCount: 14
description: The SPIFFE Runtime Environment — attests workloads and issues them short-lived cryptographic
  identities, so services authenticate to each other without shared secrets.
tags:
- Security
- Identity
- Authentication
- Zero Trust
- Cloud Native
- SPIFFE
website: https://spiffe.io
radarRing: Developing
alternativeNames:
- spire
- SPIFFE Runtime Environment
repository: https://github.com/spiffe/spire
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2486
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: issues
  note: The reference SPIFFE runtime — what actually mints workload identities.
agent:
  interfaces:
  - cli
  - container
  - http-api
  invoke: spire-server entry create -spiffeID <spiffe://trust-domain/workload> -parentID <id> -selector
    <selector>
  emits:
  - x509
  - jwt
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Replace long-lived service credentials with identities that expire in minutes.
  surface:
  - coding-agent
  - ci-pipeline
  note: 'The direction of travel for agent-to-service authentication: an agent that holds no static secret
    cannot leak one.'
- task: Establish mutual TLS between services across clusters and clouds without a shared CA per environment.
  surface:
  - ci-pipeline
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
