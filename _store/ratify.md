---
title: Ratify
slug: ratify
companyCount: 7
description: Verifies artifacts and their referenced metadata at admission time in Kubernetes, so unsigned
  or unattested workloads never start.
tags:
- Security
- Kubernetes
- Supply Chain
- Policy Enforcement
- Artifact Verification
- Notary Project
website: https://ratify.dev
radarRing: Developing
alternativeNames:
- ratify
repository: https://github.com/notaryproject/ratify
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 308
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: notary-project
  name: Notary Project
  role: verifies
agent:
  interfaces:
  - container
  consumes:
  - oci-image
  - in-toto-attestation
  emits:
  - json
  deterministic: true
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Block a deployment whose image is unsigned or fails policy, at the cluster boundary.
  surface:
  - ci-pipeline
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
