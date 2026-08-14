---
title: Scalar
slug: scalar
description: A modern OpenAPI documentation and API client suite — renders a reference site from a description
  and ships an interactive client alongside it.
companyCount: 0
website: https://scalar.com
repository: https://github.com/scalar/scalar
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 15885
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
    npm: '@scalar/cli'
  invoke: npx @scalar/cli document validate <spec.yaml>
  consumes:
  - openapi
  emits:
  - html
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Stand up documentation with an embedded client without running a portal product.
  surface:
  - coding-agent
  - human
- task: Validate and bundle a description as a build step.
  surface:
  - ci-pipeline
tags:
- OpenAPI
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were An ordinary mathematics and computing term. The bare name is blocked in the matcher, so
  this count reflects only qualified matches. Real adoption needs another source.
---
