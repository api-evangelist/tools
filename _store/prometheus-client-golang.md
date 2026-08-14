---
title: Prometheus Go Client
slug: prometheus-client-golang
description: Instruments Go applications to expose metrics in the OpenMetrics exposition format.
companyCount: 0
website: https://pkg.go.dev/github.com/prometheus/client_golang
repository: https://github.com/prometheus/client_golang
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 6017
lastCommit: '2026-08-12'
archived: false
specifications:
- slug: openmetrics
  name: OpenMetrics
  role: instruments
agent:
  interfaces:
  - library
  install:
    go: github.com/prometheus/client_golang
  emits:
  - openmetrics
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Expose custom application metrics from a Go service.
  surface:
  - coding-agent
tags:
- OpenMetrics
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
