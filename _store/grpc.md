---
title: gRPC
slug: grpc
companyCount: 121
description: The core gRPC implementation covering C++, Python, Ruby, Objective-C, PHP and C# — HTTP/2
  based RPC using Protobuf contracts.
tags:
- RPC
- API
- Protocol Buffers
- HTTP/2
- Microservices
- gRPC
website: https://grpc.io
radarRing: Optimizing
alternativeNames:
- grpc
- GRPC
- Google RPC
repository: https://github.com/grpc/grpc
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 45283
lastCommit: '2026-08-14'
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
- task: Implement a gRPC client or server in one of the core-supported languages.
  surface:
  - coding-agent
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 30
precisionGrade: very-low
precisionBasis:
- 'acronym-shape -20: shortest bare needle is 4 characters'
- 'collision -25: a surviving needle is also claimed by standards:gRPC'
- 'bare-channel -25: 100% of matching companies were reached only on the bare word (126 bare vs 0 phrase)'
---
