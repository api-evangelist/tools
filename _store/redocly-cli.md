---
title: Redocly CLI
slug: redocly-cli
description: The most production-ready way to EXECUTE an Arazzo document today, and the one most teams
  already have installed. `redocly respect` sends real requests to a real server, evaluates each step's
  successCriteria against the actual responses, and returns a pass/fail plus a HAR file. The same CLI
  lints OpenAPI against configurable rulesets, bundles and splits descriptions, and builds reference documentation.
companyCount: 0
website: https://redocly.com/docs/cli/
repository: https://github.com/Redocly/redocly-cli
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1501
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: validates
  also:
  - documents
  - transforms
  - tests
- slug: arazzo
  name: Arazzo
  role: tests
  also:
  - runs
  - validates
  - documents
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    npm: '@redocly/cli'
  invoke: npx @redocly/cli@latest respect <workflow.arazzo.yaml> --input <name>=<value>
  consumes:
  - arazzo
  - openapi
  emits:
  - json
  - text
  - html
  - http
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Prove in CI that a published Arazzo workflow still describes how the API behaves.
  surface:
  - ci-pipeline
  - coding-agent
  note: The framing is contract testing — the value is the verdict, not the side effects. It still makes
    real calls, so point it at an environment where that is safe.
- task: Lint an OpenAPI description against a team ruleset before it merges.
  surface:
  - ci-pipeline
- task: Bundle a multi-file OpenAPI description into one document an agent can read whole.
  surface:
  - coding-agent
tags:
- OpenAPI
- Arazzo
---
