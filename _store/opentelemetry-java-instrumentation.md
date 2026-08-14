---
title: OpenTelemetry Java Instrumentation
slug: opentelemetry-java-instrumentation
description: Automatic instrumentation for the JVM — attaches as a Java agent and produces telemetry from
  common frameworks with no code changes at all.
companyCount: 0
website: https://opentelemetry.io
repository: https://github.com/open-telemetry/opentelemetry-java-instrumentation
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2606
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: opentelemetry
  name: OpenTelemetry / OTLP
  role: instruments
agent:
  interfaces:
  - library
  invoke: java -javaagent:<opentelemetry-javaagent.jar> -jar <app.jar>
  emits:
  - otlp
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Instrument a Java application nobody wants to modify.
  surface:
  - coding-agent
  note: Zero source changes — the highest-value option when the agent has deployment access but not a
    mandate to edit a legacy codebase.
tags:
- OpenTelemetry / OTLP
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
