---
title: Prometheus Java Client
slug: prometheus-client-java
description: Instruments JVM applications to expose metrics in the OpenMetrics exposition format.
companyCount: 0
website: http://prometheus.github.io/client_java/
repository: https://github.com/prometheus/client_java
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2285
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: openmetrics
  name: OpenMetrics
  role: instruments
agent:
  interfaces:
  - library
  emits:
  - openmetrics
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Expose custom metrics from a JVM service.
  surface:
  - coding-agent
tags:
- OpenMetrics
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
