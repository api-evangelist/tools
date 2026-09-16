---
title: Tapestry
slug: tapestry
description: A visual, drag-and-drop workflow builder for Arazzo — connect API operations into sequences
  on a React Flow canvas and export or import Arazzo 1.0.1 documents. One of two visual authoring tools
  found; a web application rather than a library.
companyCount: 10
website: https://github.com/imminent-technology/tapestry
repository: https://github.com/imminent-technology/tapestry
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 0
lastCommit: '2026-04-20'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: authors
agent:
  interfaces:
  - web-ui
  consumes:
  - openapi
  emits:
  - arazzo
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Let someone who will not write YAML assemble an Arazzo workflow from an OpenAPI's operations.
  surface:
  - human
  note: Exports 1.0.1; nothing 1.1-specific yet.
tags:
- Arazzo
radarRing: Developing
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 75
precisionGrade: medium
precisionBasis:
- 'bare-channel -25: 100% of matching companies were reached only on the bare word (10 bare vs 0 phrase)'
---
