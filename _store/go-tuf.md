---
title: go-tuf
slug: go-tuf
description: The Go implementation of The Update Framework, used by Sigstore's trust root.
companyCount: 0
website: https://theupdateframework.com
repository: https://github.com/theupdateframework/go-tuf
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 711
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: tuf
  name: The Update Framework
  role: verifies
agent:
  interfaces:
  - library
  - cli
  install:
    go: github.com/theupdateframework/go-tuf/v2
  consumes:
  - tuf-metadata
  deterministic: true
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Add TUF-secured updates to a Go application or distribution system.
  surface:
  - coding-agent
tags:
- The Update Framework
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
