---
title: OpenTelemetry Python
slug: opentelemetry-python
description: The Python API and SDK for OTLP telemetry.
companyCount: 0
website: https://opentelemetry.io
repository: https://github.com/open-telemetry/opentelemetry-python
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2587
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: instruments
agent:
  interfaces:
  - library
  - cli
  install:
    pypi: opentelemetry-sdk
  emits:
  - otlp
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Instrument a Python service or AI application pipeline.
  surface:
  - coding-agent
  - ai-platform
  note: Increasingly the substrate for LLM observability — OpenTelemetry's GenAI semantic conventions
    are where model calls, tokens and costs are being standardised.
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
