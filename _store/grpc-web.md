---
title: gRPC-Web
slug: grpc-web
description: Lets browser clients call gRPC services through a proxy, since browsers cannot speak the
  gRPC wire protocol directly.
companyCount: 0
website: https://grpc.io
repository: https://github.com/grpc/grpc-web
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 9251
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: grpc
  name: gRPC
  role: serves
agent:
  interfaces:
  - library
  consumes:
  - proto
  emits:
  - http
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Reach a gRPC backend from a browser application.
  surface:
  - coding-agent
tags:
- gRPC
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
