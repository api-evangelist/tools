---
title: Prometheus
slug: prometheus
companyCount: 226
description: The monitoring system and time-series database that defined the exposition format OpenMetrics
  standardised — scrapes metrics endpoints and stores them for querying.
tags:
- Monitoring
- Observability
- Time Series
- Alerting
- Metrics
- OpenMetrics
website: https://prometheus.io/
founded: 2012
radarRing: Optimizing
alternativeNames:
- Prom
- prom
- prometheus
repository: https://github.com/prometheus/prometheus
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 65738
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: openmetrics
  name: OpenMetrics
  role: scrapes
agent:
  interfaces:
  - container
  - cli
  - http-api
  install:
    brew: prometheus
  consumes:
  - openmetrics
  - prometheus
  emits:
  - json
  - openmetrics
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Query operational metrics over an HTTP API to answer questions about a system's behaviour.
  surface:
  - coding-agent
  - ai-platform
  note: The PromQL HTTP API is a genuinely good agent surface — a precise query language with JSON results,
    which beats scraping dashboards.
- task: Verify that a change actually improved a measured quantity.
  surface:
  - coding-agent
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
