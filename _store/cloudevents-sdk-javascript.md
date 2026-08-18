---
title: CloudEvents JavaScript SDK
slug: cloudevents-sdk-javascript
description: Encodes and decodes CloudEvents in JavaScript and TypeScript.
companyCount: 0
website: https://cloudevents.github.io/sdk-javascript/
repository: https://github.com/cloudevents/sdk-javascript
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 400
lastCommit: '2026-02-16'
archived: false
specifications:
- slug: cloudevents
  name: CloudEvents
  role: encodes
agent:
  interfaces:
  - library
  install:
    npm: cloudevents
  consumes:
  - cloudevents
  emits:
  - cloudevents
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Receive CloudEvents in a Node service or serverless function.
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
