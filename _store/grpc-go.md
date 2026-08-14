---
title: gRPC for Go
slug: grpc-go
description: The Go implementation of gRPC, and the substrate under much of the CNCF landscape.
companyCount: 0
website: https://grpc.io
repository: https://github.com/grpc/grpc-go
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 23037
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: grpc
  name: gRPC
  role: serves
agent:
  interfaces:
  - library
  install:
    go: google.golang.org/grpc
  consumes:
  - proto
  emits:
  - http
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Implement a gRPC service in Go.
  surface:
  - coding-agent
tags:
- gRPC
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
