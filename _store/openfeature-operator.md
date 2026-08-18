---
title: OpenFeature Operator
slug: openfeature-operator
description: A Kubernetes operator that injects flagd into workloads and manages flag configuration as
  cluster resources.
companyCount: 0
website: https://openfeature.dev
repository: https://github.com/open-feature/open-feature-operator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 309
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: openfeature
  name: OpenFeature
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
- task: Deliver flag configuration to every workload in a cluster without embedding a client per service.
  surface:
  - ci-pipeline
tags:
- OpenFeature
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
