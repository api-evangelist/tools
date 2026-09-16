---
title: Itarazzo
slug: itarazzo
description: A Java library that executes Arazzo workflows inside an integration-test context — the steps
  run as automated end-to-end tests with detailed logging, and a companion client wraps it as a standalone
  executor. The only Java runner found. The repository has not been committed to since November 2024,
  so it predates Arazzo 1.1; treat it as a working 1.0 runner rather than a current one.
companyCount: 0
website: https://github.com/leidenheit/itarazzo-client
repository: https://github.com/leidenheit/itarazzo-library
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 9
lastCommit: '2024-11-17'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: tests
  also:
  - runs
  - parses
  - validates
agent:
  interfaces:
  - library
  - cli
  consumes:
  - arazzo
  - openapi
  emits:
  - text
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Run an Arazzo 1.0 workflow as a JUnit-style integration test against a live API.
  surface:
  - ci-pipeline
  note: No published Maven coordinates were found; build from source. Real calls, real side effects.
tags:
- Arazzo
---
