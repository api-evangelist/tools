---
title: arazzo-maestro
slug: arazzo-maestro
description: A single Go binary that lints and renders Arazzo workflows. Lint validates against the official
  JSON Schema, applies semantic rules (unique IDs, resolvable `$steps` references) and cross-checks steps
  against the referenced OpenAPI contracts; render produces human-readable output for the rest of the
  team. Apache-2.0 by its LICENSE file, which GitHub's detector does not report. Also published as a container
  image.
companyCount: 0
website: https://emmanuelperu.github.io/arazzo-maestro/
repository: https://github.com/emmanuelperu/arazzo-maestro
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-09-16'
stars: 8
lastCommit: '2026-09-07'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: validates
  also:
  - documents
  - tests
agent:
  interfaces:
  - cli
  - container
  install:
    go: github.com/emmanuelperu/arazzo-maestro
  consumes:
  - arazzo
  - openapi
  emits:
  - text
  - html
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Fail a CI job when an Arazzo document references an operation its OpenAPI does not define.
  surface:
  - ci-pipeline
  - coding-agent
  note: The cross-file check is the thing Spectral's schema rules do not do.
tags:
- Arazzo
---
