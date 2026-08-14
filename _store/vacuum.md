---
title: vacuum
slug: vacuum
description: An extremely fast OpenAPI linter written in Go, Spectral-ruleset compatible, built to lint
  very large specifications and whole estates in the time a CI step can afford.
companyCount: 0
website: https://quobix.com/vacuum
repository: https://github.com/daveshanley/vacuum
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1113
lastCommit: '2026-08-01'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: validates
- slug: openapi-overlays
  name: OpenAPI Overlay
  role: validates
agent:
  interfaces:
  - cli
  - library
  - container
  install:
    go: github.com/daveshanley/vacuum
    npm: '@quobix/vacuum'
  invoke: vacuum lint <spec.yaml> --ruleset <ruleset.yaml> --details
  consumes:
  - openapi
  emits:
  - json
  - sarif
  - junit
  - html
  - pretty
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Lint hundreds or thousands of OpenAPI documents in one pass, where Spectral would be too slow.
  surface:
  - ci-pipeline
  - coding-agent
- task: Produce an HTML governance report for a human reviewer from a machine run.
  surface:
  - ci-pipeline
- task: Reuse an existing Spectral ruleset without rewriting it, on a faster runtime.
  surface:
  - coding-agent
tags:
- OpenAPI
- OpenAPI Overlay
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "Sweep, mop, and vacuum floors", "repairing advanced vacuum systems" The bare name is blocked
  in the matcher, so this count reflects only qualified matches. Real adoption needs another source.
---
