---
title: SPIRE Controller Manager
slug: spire-controller-manager
description: Reconciles workload registration in Kubernetes, so SPIFFE identities are declared as cluster
  resources rather than registered by hand.
companyCount: 0
website: https://github.com/spiffe/spire-controller-manager
repository: https://github.com/spiffe/spire-controller-manager
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 74
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: spiffe
  name: SPIFFE
  role: deploys
agent:
  interfaces:
  - container
  consumes:
  - kubernetes
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Manage identity registration declaratively alongside the workloads themselves.
  surface:
  - ci-pipeline
tags:
- SPIFFE
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
