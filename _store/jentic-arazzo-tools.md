---
title: Jentic Arazzo Tools
slug: jentic-arazzo-tools
description: A TypeScript monorepo of five packages for Arazzo — parser, resolver, validator, runner and
  UI. It resolves the references an Arazzo document makes into the OpenAPI descriptions it orchestrates,
  and it EXECUTES the resulting steps; the runner is easy to miss because it lives in the packages directory
  rather than the README. Apache-2.0, and the upstream the separately listed Arazzo Toolkit was founded
  on.
companyCount: 0
website: https://arazzo-ui.jentic.com
repository: https://github.com/jentic/jentic-arazzo-tools
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 20
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - runs
  - validates
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
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Resolve an Arazzo workflow into the concrete operations it calls, so an agent can execute the
    steps.
  surface:
  - coding-agent
  note: Resolution is the hard part of consuming Arazzo — a workflow document is mostly pointers into
    other documents.
- task: Execute the resolved steps against the live APIs the workflow describes.
  surface:
  - coding-agent
  note: The `jentic-arazzo-runner` package makes real calls with real credentials. The resolver and parser
    alone are read-only; the runner is not.
- task: Render a workflow as documentation a human can review before it is automated.
  surface:
  - human
tags:
- Arazzo
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
