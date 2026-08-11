---
title: Tornjak
slug: tornjak
description: A management UI and API over SPIRE, for viewing and administering workload identities.
companyCount: 0
website: https://github.com/spiffe/tornjak
repository: https://github.com/spiffe/tornjak
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 99
lastCommit: '2026-06-22'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: manages
agent:
  interfaces:
  - web-ui
  - http-api
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Let a human see and audit what identities exist across trust domains.
  surface:
  - human
tags:
- SPIFFE
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
