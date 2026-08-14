---
title: Archivista
slug: archivista
description: A storage and graph service for in-toto attestations — makes attestations queryable instead
  of leaving them scattered across build logs.
companyCount: 1
website: https://github.com/in-toto/archivista
repository: https://github.com/in-toto/archivista
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 116
lastCommit: '2026-08-08'
archived: false
specifications:
- slug: in-toto
  name: in-toto
  role: stores
agent:
  interfaces:
  - container
  - http-api
  consumes:
  - in-toto-attestation
  emits:
  - json
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Ask what is known about an artifact's origin, across every build that touched it.
  surface:
  - coding-agent
  - ci-pipeline
  note: Attestations are only useful if you can find them later. This is the part most supply-chain rollouts
    skip and then regret.
tags:
- in-toto
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
