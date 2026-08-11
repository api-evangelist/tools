---
title: protovalidate
slug: protovalidate
description: Declares and enforces validation rules inside `.proto` definitions themselves, evaluated
  at runtime with CEL expressions.
companyCount: 0
website: https://protovalidate.com
repository: https://github.com/bufbuild/protovalidate
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 1550
lastCommit: '2026-07-27'
archived: false
specifications:
- slug: protocol-buffers
  name: Protocol Buffers
  role: validates
agent:
  interfaces:
  - library
  consumes:
  - proto
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Put validation rules in the contract rather than reimplementing them in every service.
  surface:
  - coding-agent
tags:
- Protocol Buffers
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
