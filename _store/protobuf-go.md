---
title: Protocol Buffers for Go
slug: protobuf-go
description: The Go implementation of Protocol Buffers, including the `protoc-gen-go` plugin.
companyCount: 0
website: https://developers.google.com/protocol-buffers
repository: https://github.com/protocolbuffers/protobuf-go
license: BSD-3-Clause
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 3346
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: protocol-buffers
  name: Protocol Buffers
  role: generates
agent:
  interfaces:
  - library
  - cli
  install:
    go: google.golang.org/protobuf/cmd/protoc-gen-go
  consumes:
  - proto
  emits:
  - go
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Generate Go types from a Protobuf contract.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- Protocol Buffers
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
