---
title: OSV Schema
slug: osv-schema
description: The JSON schema describing open-source vulnerabilities in a way that is precise about which
  versions are affected, across every package ecosystem.
companyCount: 0
website: https://ossf.github.io/osv-schema/
repository: https://github.com/ossf/osv-schema
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 266
lastCommit: '2026-08-06'
archived: false
specifications:
- slug: osv-schema
  name: OSV Schema
  role: authors
agent:
  interfaces:
  - library
  consumes:
  - json-schema
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Parse vulnerability data from any OSV-compatible source with one schema.
  surface:
  - coding-agent
  note: 'The reason this schema won: version ranges are expressed exactly, so "is my version affected?"
    is a computation rather than a judgement call about a CVE description.'
tags:
- OSV Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
