---
title: Microcks
slug: microcks
description: A mocking and contract-testing platform that imports OpenAPI, AsyncAPI, gRPC and Postman
  artifacts and serves mocks plus conformance tests from them.
companyCount: 0
website: https://microcks.io
repository: https://github.com/microcks/microcks
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2013
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: mocks
  also:
  - tests
- slug: asyncapi
  name: AsyncAPI
  role: mocks
agent:
  interfaces:
  - container
  - http-api
  - web-ui
  - cli
  invoke: docker run -p 8080:8080 quay.io/microcks/microcks-uber:latest
  consumes:
  - openapi
  - asyncapi
  - grpc
  - postman
  emits:
  - http
  - json
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Mock synchronous and event-driven APIs from one place, instead of two separate tools.
  surface:
  - coding-agent
  - ci-pipeline
- task: Run contract tests against a deployed service and get a conformance verdict back over an API.
  surface:
  - ci-pipeline
  note: Microcks has its own HTTP API, so an agent can drive the whole loop without a UI.
tags:
- OpenAPI
- AsyncAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
