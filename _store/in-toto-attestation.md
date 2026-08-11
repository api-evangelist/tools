---
title: in-toto Attestation Framework
slug: in-toto-attestation
description: The specification and schemas for the attestation format — the statement-and-predicate envelope
  SLSA provenance and most supply-chain claims are carried in.
companyCount: 0
website: https://github.com/in-toto/attestation
repository: https://github.com/in-toto/attestation
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-11'
stars: 363
lastCommit: '2026-08-04'
archived: false
specifications:
- slug: in-toto
  name: in-toto
  role: authors
agent:
  interfaces:
  - library
  consumes:
  - in-toto-attestation
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Read the schema before emitting attestations, so they are actually consumable by other tools.
  surface:
  - coding-agent
tags:
- in-toto
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
