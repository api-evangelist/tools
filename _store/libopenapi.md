---
title: libopenapi
slug: libopenapi
description: A high-performance Go library for OpenAPI 2.0, 3.0, 3.1 and 3.2 that also reads Overlay and
  Arazzo documents into a typed model. The largest codebase in this list by a wide margin and the one
  most likely to already be a dependency of the Go tooling you run; its Arazzo support rides on the same
  document model as its OpenAPI support, which is what makes it the natural parser for a Go-based runner.
companyCount: 0
website: https://pb33f.io/libopenapi/
repository: https://github.com/pb33f/libopenapi
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-18'
stars: 875
lastCommit: '2026-09-18'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - validates
agent:
  interfaces:
  - library
  install:
    go: github.com/pb33f/libopenapi
  consumes:
  - arazzo
  - openapi
  - openapi-overlay
  emits:
  - go
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Load an Arazzo document into a typed Go model alongside the OpenAPI it references.
  surface:
  - coding-agent
  - ci-pipeline
  note: A parser, not a runner — it reads the document; executing the steps is your code.
tags:
- Arazzo
---
