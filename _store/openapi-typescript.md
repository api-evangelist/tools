---
title: openapi-typescript
slug: openapi-typescript
description: Generates TypeScript types directly from an OpenAPI description — types only, no client runtime
  and no generated transport code.
companyCount: 0
website: https://openapi-ts.dev
repository: https://github.com/openapi-ts/openapi-typescript
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 8307
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: generates
  produces:
  - types
agent:
  interfaces:
  - cli
  - library
  install:
    npm: openapi-typescript
  invoke: npx openapi-typescript <spec.yaml> -o <schema.d.ts>
  consumes:
  - openapi
  emits:
  - typescript
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Get compile-time safety against an API contract without adopting a generated SDK.
  surface:
  - coding-agent
  note: Often the right choice for an agent over a full SDK generator — one file, no runtime dependency,
    and the diff is reviewable.
- task: Detect a breaking provider change as a type error in CI rather than at runtime.
  surface:
  - ci-pipeline
tags:
- OpenAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
