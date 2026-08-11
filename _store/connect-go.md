---
title: Connect for Go
slug: connect-go
description: Builds RPC services in Go that speak gRPC, gRPC-Web and its own simpler HTTP protocol from
  one implementation — callable with plain curl.
companyCount: 0
website: https://connectrpc.com
repository: https://github.com/connectrpc/connect-go
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 4033
lastCommit: '2026-08-01'
archived: false
specifications:
- slug: protocol-buffers
  name: Protocol Buffers
  role: serves
agent:
  interfaces:
  - library
  install:
    go: connectrpc.com/connect
  consumes:
  - proto
  emits:
  - http
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Expose an RPC service that an agent can call over ordinary HTTP without a gRPC client.
  surface:
  - coding-agent
  note: Materially easier for agents than plain gRPC — a Connect endpoint answers a normal HTTP POST with
    JSON, so no code generation is needed to make one call.
tags:
- Protocol Buffers
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
