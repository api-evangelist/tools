---
title: OpenTelemetry Operator
slug: opentelemetry-operator
description: A Kubernetes operator that manages Collector deployments and injects auto-instrumentation
  into workloads.
companyCount: 0
website: https://github.com/open-telemetry/opentelemetry-operator
repository: https://github.com/open-telemetry/opentelemetry-operator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1747
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: deploys
agent:
  interfaces:
  - container
  consumes:
  - kubernetes
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Roll out instrumentation across a cluster declaratively rather than per service.
  surface:
  - ci-pipeline
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
