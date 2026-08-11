---
title: oapi-codegen
slug: oapi-codegen
description: Generates idiomatic Go server boilerplate and clients from an OpenAPI description, wiring
  into the common Go HTTP routers.
companyCount: 0
website: https://github.com/oapi-codegen/oapi-codegen
repository: https://github.com/oapi-codegen/oapi-codegen
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 8509
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: generates
  produces:
  - server-stub
  - client
agent:
  interfaces:
  - cli
  - library
  install:
    go: github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen
  invoke: oapi-codegen -generate types,client -package <pkg> <spec.yaml> > <client.gen.go>
  consumes:
  - openapi
  emits:
  - go
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Generate a Go client or server that reads like hand-written Go rather than generated code.
  surface:
  - coding-agent
- task: Keep generated types in sync with a contract via `go generate` in CI.
  surface:
  - ci-pipeline
tags:
- OpenAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
