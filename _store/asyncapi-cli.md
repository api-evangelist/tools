---
title: AsyncAPI CLI
slug: asyncapi-cli
description: The single entry point to the AsyncAPI toolchain — validates, converts, bundles, diffs and
  generates from AsyncAPI documents, and opens Studio locally.
companyCount: 0
website: https://www.asyncapi.com/tools/cli
repository: https://github.com/asyncapi/cli
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 272
lastCommit: '2026-08-09'
archived: false
specifications:
- slug: asyncapi
  name: AsyncAPI
  role: validates
  also:
  - generates
  - transforms
agent:
  interfaces:
  - cli
  - container
  - ci-action
  install:
    npm: '@asyncapi/cli'
  invoke: npx @asyncapi/cli validate <asyncapi.yaml>
  consumes:
  - asyncapi
  emits:
  - json
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate an event-driven API description before anything is generated from it.
  surface:
  - coding-agent
  - ci-pipeline
- task: Convert an older AsyncAPI document up to the current version of the specification.
  surface:
  - coding-agent
- task: Diff two versions of an event contract to find what changed for consumers.
  surface:
  - ci-pipeline
  note: Event contracts break consumers as badly as HTTP ones do, and almost nobody diffs them.
tags:
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
