---
title: OpenTelemetry Go
slug: opentelemetry-go
description: The Go API and SDK for producing traces, metrics and logs in OTLP.
companyCount: 0
website: https://opentelemetry.io/docs/languages/go
repository: https://github.com/open-telemetry/opentelemetry-go
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 6508
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: instruments
agent:
  interfaces:
  - library
  install:
    go: go.opentelemetry.io/otel
  emits:
  - otlp
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Instrument a Go service so its telemetry works with any OTLP-compatible backend.
  surface:
  - coding-agent
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
