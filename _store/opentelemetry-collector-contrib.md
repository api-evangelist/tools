---
title: OpenTelemetry Collector Contrib
slug: opentelemetry-collector-contrib
description: The community distribution of the Collector, carrying the long tail of receivers, processors
  and exporters for specific vendors and systems.
companyCount: 0
website: https://opentelemetry.io
repository: https://github.com/open-telemetry/opentelemetry-collector-contrib
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 4851
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: instruments
agent:
  interfaces:
  - container
  - cli
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
- task: Find a ready-made receiver or exporter for a specific system instead of writing one.
  surface:
  - coding-agent
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
