---
title: Jentic Arazzo Tools
slug: jentic-arazzo-tools
description: A parser, resolver and renderer for Arazzo workflow documents — resolves the references an
  Arazzo document makes into the OpenAPI descriptions it orchestrates.
companyCount: 0
website: https://arazzo-ui.jentic.com
repository: https://github.com/jentic/jentic-arazzo-tools
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 20
lastCommit: '2026-08-07'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - documents
agent:
  interfaces:
  - library
  - cli
  consumes:
  - arazzo
  - openapi
  emits:
  - json
  deterministic: true
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Resolve an Arazzo workflow into the concrete operations it calls, so an agent can execute the
    steps.
  surface:
  - coding-agent
  note: Resolution is the hard part of consuming Arazzo — a workflow document is mostly pointers into
    other documents.
- task: Render a workflow as documentation a human can review before it is automated.
  surface:
  - human
tags:
- Arazzo
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
