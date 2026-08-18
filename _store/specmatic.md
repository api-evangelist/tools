---
title: Specmatic
slug: specmatic
description: Executes contracts for both testing and mocking, and is the only Arazzo implementation that
  will span REST and events in a single workflow — OpenAPI and AsyncAPI stitched into one document. It
  turns a specification into an executable contract, so the same artifact drives a test run and a stub
  server.
companyCount: 1
website: https://specmatic.io
repository: https://github.com/specmatic/specmatic
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 394
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: tests
  also:
  - mocks
- slug: arazzo
  name: Arazzo
  role: tests
  also:
  - runs
  - mocks
- slug: asyncapi
  name: AsyncAPI
  role: tests
  also:
  - mocks
agent:
  interfaces:
  - cli
  - container
  - library
  install:
    docker: specmatic/specmatic
    maven: io.specmatic:specmatic-core
  consumes:
  - arazzo
  - openapi
  - asyncapi
  emits:
  - json
  - http
  - text
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Test a workflow that goes asynchronous halfway through, without pretending it does not.
  surface:
  - ci-pipeline
  - coding-agent
  note: Most business flows worth documenting cross from REST into events. This is the one runner that
    does not force you to split them into two artifacts.
- task: Stand up a stub server from a contract so a consumer can build before the provider ships.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- OpenAPI
- Arazzo
- AsyncAPI
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 92
precisionGrade: high
precisionBasis:
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
