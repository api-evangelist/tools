---
title: Arazzo Runtime Expression
slug: arazzo-runtime-expression
description: A parser, validator, extractor and interpolator for Arazzo Runtime Expressions — the `$inputs.x`,
  `$steps.y.outputs.z`, `$response.body#/pointer` syntax every step, output and criterion depends on.
  A small, exact library for the part of the specification that runners most often get subtly wrong, from
  the maintainer of the ApiDOM Arazzo namespace.
companyCount: 0
website: https://github.com/swaggerexpert/arazzo-runtime-expression
repository: https://github.com/swaggerexpert/arazzo-runtime-expression
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 5
lastCommit: '2026-09-15'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - validates
  - evaluates
agent:
  interfaces:
  - library
  install:
    npm: '@swaggerexpert/arazzo-runtime-expression'
  consumes:
  - arazzo
  emits:
  - javascript
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate or evaluate the runtime expressions in an Arazzo document without writing a grammar.
  surface:
  - coding-agent
  - ci-pipeline
  note: Covers the expression grammar across Arazzo 1.0 and 1.1; it does not resolve HTTP messages for
    you.
tags:
- Arazzo
---
