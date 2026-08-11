---
title: in-toto for Go
slug: in-toto-golang
description: The Go implementation of in-toto, used by supply-chain tooling written in Go.
companyCount: 0
website: https://in-toto.io/
repository: https://github.com/in-toto/in-toto-golang
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-11'
stars: 151
lastCommit: '2026-07-10'
archived: false
specifications:
- slug: in-toto
  name: in-toto
  role: attests
agent:
  interfaces:
  - library
  install:
    go: github.com/in-toto/in-toto-golang
  emits:
  - in-toto-attestation
  deterministic: true
  offline: true
  mutates: false
  credentials: true
useCases:
- task: Generate or verify attestations from a Go supply-chain tool.
  surface:
  - coding-agent
tags:
- in-toto
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
