---
title: SPDX Go Tools
slug: spdx-tools-golang
description: Go packages for reading, writing and validating SPDX documents.
companyCount: 0
website: https://github.com/spdx/tools-golang
repository: https://github.com/spdx/tools-golang
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 170
lastCommit: '2026-07-23'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: parses
agent:
  interfaces:
  - library
  install:
    go: github.com/spdx/tools-golang
  consumes:
  - spdx
  emits:
  - spdx
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Handle SBOMs inside a Go supply-chain tool.
  surface:
  - coding-agent
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
