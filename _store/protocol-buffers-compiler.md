---
title: Protocol Buffers
slug: protocol-buffers-compiler
description: The Protocol Buffers compiler and runtime libraries — parses `.proto` definitions and generates
  serialisation code across languages.
companyCount: 25
website: http://protobuf.dev
repository: https://github.com/protocolbuffers/protobuf
license: BSD-3-Clause
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-11'
stars: 71718
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: protocol-buffers
  name: Protocol Buffers
  role: parses
  also:
  - generates
agent:
  interfaces:
  - cli
  - library
  install:
    brew: protobuf
  invoke: protoc --proto_path=<dir> --<lang>_out=<out-dir> <file.proto>
  consumes:
  - proto
  emits:
  - source-code
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Generate message types from a `.proto` contract.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- Protocol Buffers
radarRing: Developing
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
