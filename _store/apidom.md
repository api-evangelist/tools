---
title: ApiDOM
slug: apidom
description: 'A semantic parser that turns API description documents — OpenAPI, AsyncAPI, JSON Schema
  and Arazzo among them — into a single traversable document object model. Ships a dedicated Arazzo 1.x
  namespace plus JSON and YAML parser adapters, and is the model the Arazzo Toolkit and Jentic''s parser
  build on: a document becomes a structure you walk, not text you match.'
companyCount: 0
website: https://speclynx.com/apidom/
repository: https://github.com/speclynx/apidom
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 7
lastCommit: '2026-09-16'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - validates
agent:
  interfaces:
  - library
  install:
    npm: '@speclynx/apidom-ns-arazzo-1'
  consumes:
  - arazzo
  - openapi
  - asyncapi
  - json-schema
  emits:
  - javascript
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Traverse or refactor an Arazzo document by its semantic structure rather than by regex.
  surface:
  - coding-agent
  note: The Arazzo namespace is one of many packages; install the adapter for the serialisation you hold.
tags:
- Arazzo
---
