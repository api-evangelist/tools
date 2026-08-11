---
title: SPDX Java Library
slug: spdx-java-library
description: The Java object model for SPDX, underneath the SPDX Java tooling.
companyCount: 0
website: https://github.com/spdx/Spdx-Java-Library
repository: https://github.com/spdx/Spdx-Java-Library
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 69
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: parses
agent:
  interfaces:
  - library
  consumes:
  - spdx
  emits:
  - spdx
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Read or emit SPDX from a JVM build plugin or service.
  surface:
  - coding-agent
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
