---
title: oas-overlay-java
slug: oas-overlay-java
description: A Java implementation of the OpenAPI Overlay specification.
companyCount: 0
website: https://github.com/IBM/oas-overlay-java
repository: https://github.com/IBM/oas-overlay-java
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 3
lastCommit: '2026-08-06'
archived: false
specifications:
- slug: openapi-overlay
  name: OpenAPI Overlay
  role: transforms
agent:
  interfaces:
  - library
  consumes:
  - openapi
  - openapi-overlay
  emits:
  - openapi
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Apply Overlays inside an existing JVM build or service.
  surface:
  - ci-pipeline
tags:
- OpenAPI Overlay
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
