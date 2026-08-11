---
title: jsonschema (Go)
slug: go-jsonschema
description: A JSON Schema validator for Go with full dialect coverage and detailed, structured error
  output.
companyCount: 0
website: https://github.com/santhosh-tekuri/jsonschema
repository: https://github.com/santhosh-tekuri/jsonschema
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 1255
lastCommit: '2026-08-06'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: validates
agent:
  interfaces:
  - library
  - cli
  install:
    go: github.com/santhosh-tekuri/jsonschema/v6
  consumes:
  - json-schema
  - json
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate against a schema inside a Go service or CLI.
  surface:
  - coding-agent
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
