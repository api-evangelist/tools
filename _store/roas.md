---
title: roas
slug: roas
description: Rust crates for OpenAPI, AsyncAPI, Overlay and Arazzo — every version of each — with a validation
  CLI. Documents are parsed into typed Rust, validated against the specification, converted between versions,
  and, in Arazzo's case, executed by a dedicated executor crate. One of two Rust implementations found
  and the only one with a detectable license and current commits.
companyCount: 0
website: https://github.com/sv-tools/roas?tab=readme-ov-file#roas-workspace
repository: https://github.com/sv-tools/roas
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-18'
stars: 6
lastCommit: '2026-09-16'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: validates
  also:
  - parses
  - runs
  - converts
agent:
  interfaces:
  - cli
  - library
  install:
    cargo: roas
  consumes:
  - arazzo
  - openapi
  - asyncapi
  - openapi-overlay
  emits:
  - json
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate an Arazzo document from a Rust toolchain, or embed the typed model in a Rust service.
  surface:
  - ci-pipeline
  - coding-agent
  note: Validation is offline and deterministic; the executor crate makes real calls and is not.
tags:
- Arazzo
---
