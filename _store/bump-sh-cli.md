---
title: Bump.sh CLI
slug: bump-sh-cli
description: Deploys, diffs and previews OpenAPI, AsyncAPI and Arazzo documentation, and detects breaking
  changes between two versions of a description.
companyCount: 0
website: https://bump.sh
repository: https://github.com/bump-sh/cli
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 70
lastCommit: '2026-07-01'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: documents
agent:
  interfaces:
  - cli
  - ci-action
  install:
    npm: bump-cli
  invoke: npx bump-cli diff <old-spec.yaml> <new-spec.yaml>
  consumes:
  - openapi
  - asyncapi
  - arazzo
  emits:
  - json
  - text
  - html
  deterministic: true
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Answer "is this change breaking?" before a contract change is merged.
  surface:
  - ci-pipeline
  - coding-agent
  note: The `diff` subcommand works without an account; deploying documentation needs a token.
- task: Preview rendered documentation for a description an agent has just modified.
  surface:
  - coding-agent
tags:
- Arazzo
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
