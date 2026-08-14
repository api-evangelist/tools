---
title: Prometheus Python Client
slug: prometheus-client-python
description: Instruments Python applications to expose metrics in the OpenMetrics exposition format.
companyCount: 0
website: https://github.com/prometheus/client_python
repository: https://github.com/prometheus/client_python
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 4356
lastCommit: '2026-07-24'
archived: false
specifications:
- slug: openmetrics
  name: OpenMetrics
  role: instruments
agent:
  interfaces:
  - library
  install:
    pypi: prometheus-client
  emits:
  - openmetrics
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Expose custom metrics from a Python service or job.
  surface:
  - coding-agent
tags:
- OpenMetrics
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
