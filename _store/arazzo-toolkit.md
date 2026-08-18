---
title: Arazzo Toolkit
slug: arazzo-toolkit
description: A JavaScript/TypeScript monorepo that parses, resolves, validates and RUNS Arazzo documents
  — separate parser, resolver, validator and runner packages behind one CLI. The parser and runner originate
  in Jentic's Arazzo tools, Apache-2.0, and are carried forward here under a dedicated org; the parser
  produces a SpecLynx ApiDOM model, so a document can be traversed rather than string-matched. Supports
  Arazzo 1.0.0 and 1.0.1 with OpenAPI 2.0, 3.0 and 3.1 source descriptions.
companyCount: 0
website: https://usearazzo.com
repository: https://github.com/usearazzo/arazzo-toolkit
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 3
lastCommit: '2026-08-12'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: runs
  also:
  - parses
  - validates
agent:
  interfaces:
  - cli
  - library
  consumes:
  - arazzo
  - openapi
  emits:
  - json
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Execute an Arazzo workflow against live APIs and get a per-step trace back.
  surface:
  - coding-agent
  note: A run makes real calls with real credentials and carries whatever side effects those calls have
    — that is the claim validation cannot make. The toolkit is PRE-1.0 by its own statement, with no npm
    release and no tag yet, so there are deliberately no install coordinates here. The one to watch in
    this tier, not the one to pin a pipeline to.
- task: Parse an Arazzo document into a traversable model before reasoning about it.
  surface:
  - coding-agent
- task: Validate an Arazzo document against the specification with located violations.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- Arazzo
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
