---
title: OpenAPI Generator
slug: openapi-generator
description: Generates client SDKs, server stubs and documentation from an OpenAPI description across
  more than fifty languages — the most widely deployed code generator in the ecosystem.
companyCount: 0
website: https://openapi-generator.tech
repository: https://github.com/OpenAPITools/openapi-generator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 26663
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: generates
  produces:
  - sdk
  - server-stub
  - documentation
agent:
  interfaces:
  - cli
  - container
  - ci-action
  - library
  install:
    npm: '@openapitools/openapi-generator-cli'
    brew: openapi-generator
  invoke: npx @openapitools/openapi-generator-cli generate -i <spec.yaml> -g <generator> -o <out-dir>
  consumes:
  - openapi
  emits:
  - source-code
  deterministic: true
  offline: false
  mutates: true
  credentials: false
useCases:
- task: Produce a typed client for an API the agent is about to integrate against.
  surface:
  - coding-agent
  note: Writes a whole tree of files — an agent should generate into a scratch directory and diff, never
    straight over a working source tree.
- task: Scaffold a server implementation from an agreed contract, so design-first actually happens.
  surface:
  - coding-agent
  - ci-pipeline
- task: Regenerate clients when a provider publishes a new version of its description.
  surface:
  - ci-pipeline
tags:
- OpenAPI
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
