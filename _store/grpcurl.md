---
title: grpcurl
slug: grpcurl
description: The curl of gRPC — calls gRPC services from the command line, discovering their methods by
  server reflection so no `.proto` file or generated client is needed.
companyCount: 0
website: https://www.fullstory.com/resources/content/fullstory-engineering-blog/
repository: https://github.com/fullstorydev/grpcurl
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 12780
lastCommit: '2026-07-27'
archived: false
specifications:
- slug: grpc
  name: gRPC
  role: tests
  note: The curl of gRPC — how an agent calls a gRPC service without generating a client.
agent:
  interfaces:
  - cli
  install:
    brew: grpcurl
    go: github.com/fullstorydev/grpcurl/cmd/grpcurl
  invoke: grpcurl -plaintext <host:port> list
  consumes:
  - proto
  - grpc
  emits:
  - json
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Discover what methods a gRPC service exposes when there is no documentation.
  surface:
  - coding-agent
  note: The single most useful gRPC tool for an agent. Server reflection means it can enumerate an unknown
    service's whole interface and call it, with no build step at all.
- task: Call one gRPC method to check behaviour without generating a client.
  surface:
  - coding-agent
tags:
- gRPC
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 92
precisionGrade: high
precisionBasis:
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
