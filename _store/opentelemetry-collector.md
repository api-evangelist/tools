---
title: OpenTelemetry Collector
slug: opentelemetry-collector
description: Receives, processes and exports telemetry in a vendor-agnostic pipeline — the component that
  decouples what emits telemetry from what stores it.
companyCount: 4
website: https://opentelemetry.io
repository: https://github.com/open-telemetry/opentelemetry-collector
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 7372
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: instruments
  also:
  - transforms
agent:
  interfaces:
  - container
  - cli
  invoke: otelcol --config <config.yaml>
  consumes:
  - otlp
  - prometheus
  - jaeger
  - zipkin
  emits:
  - otlp
  deterministic: false
  offline: true
  mutates: false
  credentials: true
useCases:
- task: Change observability backends without touching a line of application code.
  surface:
  - coding-agent
  - ci-pipeline
  note: The architectural reason OTLP matters. Instrument once against the standard, and the destination
    becomes a configuration decision rather than a migration.
- task: Redact or drop sensitive attributes in telemetry before it leaves the estate.
  surface:
  - ci-pipeline
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
