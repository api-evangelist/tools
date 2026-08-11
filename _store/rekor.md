---
title: Rekor
slug: rekor
description: The immutable, append-only transparency log that records signing events, so a signature can
  be verified after the short-lived certificate that made it has expired.
companyCount: 0
website: https://sigstore.dev
repository: https://github.com/sigstore/rekor
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 1189
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: stores
agent:
  interfaces:
  - cli
  - http-api
  - container
  emits:
  - json
  deterministic: true
  offline: false
  mutates: true
  credentials: false
useCases:
- task: Prove a signature existed at a point in time, independent of certificate lifetime.
  surface:
  - ci-pipeline
  - coding-agent
- task: Query the log for every entry associated with an artifact.
  surface:
  - coding-agent
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
