---
title: JSON Schema Test Suite
slug: json-schema-test-suite
description: The language-agnostic conformance suite every JSON Schema implementation is measured against
  — the tests that decide whether a validator is actually correct.
companyCount: 0
website: https://github.com/json-schema-org/JSON-Schema-Test-Suite
repository: https://github.com/json-schema-org/JSON-Schema-Test-Suite
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 739
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: tests
  note: The language-agnostic conformance suite every implementation is measured against.
agent:
  interfaces:
  - library
  consumes:
  - json-schema
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Verify a validator's dialect claims rather than trusting its README.
  surface:
  - coding-agent
- task: Test a new or modified JSON Schema implementation against the same bar as everyone else.
  surface:
  - ci-pipeline
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
