---
title: Buf
slug: buf
description: A modern Protobuf toolchain — lints `.proto` files, detects breaking changes against a previous
  version, manages dependencies through a schema registry, and generates code without hand-written protoc
  invocations.
companyCount: 0
website: https://buf.build
repository: https://github.com/bufbuild/buf
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 11334
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: protocol-buffers
  name: Protocol Buffers
  role: validates
  also:
  - generates
  - transforms
- slug: grpc
  name: gRPC
  role: validates
agent:
  interfaces:
  - cli
  - container
  - ci-action
  install:
    brew: bufbuild/buf/buf
    npm: '@bufbuild/buf'
  invoke: buf lint && buf breaking --against <ref>
  consumes:
  - proto
  emits:
  - json
  - text
  - source-code
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Catch a breaking change to a Protobuf contract before it is merged.
  surface:
  - ci-pipeline
  - coding-agent
  note: Breaking-change detection is the standout capability here, and it is what most estates are missing.
    Protobuf's compatibility rules are subtle enough that humans get them wrong.
- task: Lint `.proto` files against a consistent style without writing custom tooling.
  surface:
  - ci-pipeline
- task: Generate code from Protobuf without maintaining fragile protoc command lines.
  surface:
  - coding-agent
tags:
- Protocol Buffers
- gRPC
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were Three letters, commonly an abbreviation of "buffer". The bare name is blocked in the matcher,
  so this count reflects only qualified matches. Real adoption needs another source.
---
