---
title: SPDX Java Tools
slug: spdx-tools-java
description: Command-line tools for converting, comparing and validating SPDX documents on the JVM.
companyCount: 0
website: https://github.com/spdx/tools-java
repository: https://github.com/spdx/tools-java
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 100
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: parses
agent:
  interfaces:
  - cli
  - library
  consumes:
  - spdx
  emits:
  - spdx
  - json
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Compare two SBOMs to see what changed between releases.
  surface:
  - ci-pipeline
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
