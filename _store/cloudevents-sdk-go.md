---
title: CloudEvents Go SDK
slug: cloudevents-sdk-go
description: Encodes and decodes CloudEvents in Go, with bindings for HTTP, Kafka, NATS, AMQP and Pub/Sub.
companyCount: 0
website: https://cloudevents.github.io/sdk-go/
repository: https://github.com/cloudevents/sdk-go
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 960
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: cloudevents
  name: CloudEvents
  role: encodes
agent:
  interfaces:
  - library
  install:
    go: github.com/cloudevents/sdk-go/v2
  consumes:
  - cloudevents
  emits:
  - cloudevents
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Emit events in a format any CloudEvents consumer can read, rather than a bespoke envelope.
  surface:
  - coding-agent
- task: Consume events from a system that already speaks CloudEvents without writing a parser.
  surface:
  - coding-agent
tags:
- CloudEvents
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
