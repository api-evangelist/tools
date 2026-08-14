---
title: Arazzo CLI
slug: arazzo-cli
description: A command-line runner for Arazzo workflow documents — executes the steps a workflow describes
  against real APIs.
companyCount: 0
website: https://strefethen.github.io/arazzo-cli/
repository: https://github.com/strefethen/arazzo-cli
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 7
lastCommit: '2026-08-12'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: tests
  also:
  - runs
agent:
  interfaces:
  - cli
  consumes:
  - arazzo
  emits:
  - json
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Actually execute an Arazzo workflow rather than only validating it.
  surface:
  - coding-agent
  note: Read the maturity signals on this page before depending on it. Executing a workflow makes real
    calls against real APIs, with whatever side effects those carry.
tags:
- Arazzo
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
