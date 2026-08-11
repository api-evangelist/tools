---
title: notation-go
slug: notation-go
description: The Go libraries behind Notation, for signing and verifying OCI artifacts.
companyCount: 0
website: https://github.com/notaryproject/notation-go
repository: https://github.com/notaryproject/notation-go
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 45
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: notary-project
  name: Notary Project
  role: signs
agent:
  interfaces:
  - library
  install:
    go: github.com/notaryproject/notation-go
  consumes:
  - oci-image
  deterministic: true
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Embed signature verification in a Go admission controller or deployment tool.
  surface:
  - coding-agent
tags:
- Notary Project
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
