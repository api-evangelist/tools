---
title: tuf-js
slug: tuf-js
description: The JavaScript implementation of The Update Framework, used in the npm supply-chain stack.
companyCount: 0
website: https://github.com/theupdateframework/tuf-js
repository: https://github.com/theupdateframework/tuf-js
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 83
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: tuf
  name: The Update Framework
  role: verifies
agent:
  interfaces:
  - library
  install:
    npm: tuf-js
  consumes:
  - tuf-metadata
  deterministic: true
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Verify TUF metadata from Node tooling.
  surface:
  - coding-agent
tags:
- The Update Framework
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
