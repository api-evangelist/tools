---
title: OSV.dev
slug: osv-dev
description: The vulnerability database and API behind the OSV schema — aggregates advisories across ecosystems
  and serves them in one consistent format.
companyCount: 0
website: https://osv.dev
repository: https://github.com/google/osv.dev
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2880
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: osv-schema
  name: OSV Schema
  role: stores
agent:
  interfaces:
  - http-api
  - web-ui
  invoke: curl -sX POST https://api.osv.dev/v1/query -d '{"package":{"name":"<pkg>","ecosystem":"<eco>"}}'
  emits:
  - json
  deterministic: false
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Ask directly whether one specific package version is affected by anything known.
  surface:
  - coding-agent
  - ai-platform
  note: A free, unauthenticated JSON API — one of the easiest external data sources for an agent to consult
    mid-task.
tags:
- OSV Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
