---
title: Sourcey
slug: sourcey
description: Builds a self-hosted static documentation site from OpenAPI descriptions, alongside Markdown
  guides and other code-reference sources.
companyCount: 0
website: https://sourcey.com
repository: https://github.com/sourcey/sourcey
license: AGPL-3.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-28'
stars: 1361
lastCommit: '2026-08-25'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: documents
agent:
  interfaces:
  - cli
  - library
  - container
  - ci-action
  install:
    npm: sourcey
  invoke: npx sourcey build <openapi.yaml> -o <output-dir>
  consumes:
  - openapi
  emits:
  - html
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Build a portable API reference site from an OpenAPI description without a hosted documentation
    service.
  surface:
  - coding-agent
  - ci-pipeline
- task: Publish API reference and Markdown guides as one static site that can be deployed anywhere.
  surface:
  - ci-pipeline
tags:
- OpenAPI
---
