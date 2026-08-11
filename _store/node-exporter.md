---
title: Node Exporter
slug: node-exporter
description: Exposes hardware and operating-system metrics from a host in the OpenMetrics format.
companyCount: 0
website: https://prometheus.io/
repository: https://github.com/prometheus/node_exporter
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 13687
lastCommit: '2026-08-08'
archived: false
specifications:
- slug: openmetrics
  name: OpenMetrics
  role: instruments
agent:
  interfaces:
  - container
  - cli
  emits:
  - openmetrics
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Get host-level metrics without writing any collection code.
  surface:
  - ci-pipeline
tags:
- OpenMetrics
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
