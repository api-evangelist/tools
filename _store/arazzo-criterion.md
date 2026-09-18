---
title: Arazzo Criterion
slug: arazzo-criterion
description: A parser, validator and evaluator for the Arazzo Criterion Object — the success-criteria
  conditions in `simple`, `regex`, `jsonpath` and `xpath` types that decide whether a step succeeded.
  Isolates the one piece of Arazzo where two runners are most likely to disagree, which is exactly what
  a conformance suite would test.
companyCount: 0
website: https://github.com/swaggerexpert/arazzo-criterion
repository: https://github.com/swaggerexpert/arazzo-criterion
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-18'
stars: 2
lastCommit: '2026-09-15'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: evaluates
  also:
  - parses
  - validates
agent:
  interfaces:
  - library
  install:
    npm: '@swaggerexpert/arazzo-criterion'
  consumes:
  - arazzo
  emits:
  - javascript
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Evaluate a step's success criteria against a captured response the same way across tools.
  surface:
  - coding-agent
  - ci-pipeline
  note: The maintainer has written about the one condition type no tool can evaluate safely; read that
    before trusting regex criteria.
tags:
- Arazzo
---
