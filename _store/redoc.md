---
title: Redoc
slug: redoc
description: Renders an OpenAPI description as a single-page reference documentation site, with no server-side
  component.
companyCount: 0
website: https://redocly.github.io/redoc/
repository: https://github.com/Redocly/redoc
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 25862
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: documents
agent:
  interfaces:
  - cli
  - library
  - web-ui
  install:
    npm: '@redocly/cli'
  invoke: npx @redocly/cli build-docs <spec.yaml> -o <index.html>
  consumes:
  - openapi
  emits:
  - html
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Publish readable reference documentation as a build artifact from the contract itself.
  surface:
  - ci-pipeline
  - coding-agent
- task: Give a human reviewer something to look at when an agent has changed an API description.
  surface:
  - coding-agent
tags:
- OpenAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
