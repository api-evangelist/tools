---
title: Distribution
slug: oci-distribution
description: The reference implementation of the OCI Distribution Specification — the registry server
  most private registries are built from.
companyCount: 0
website: https://distribution.github.io/distribution
repository: https://github.com/distribution/distribution
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 10560
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: stores
agent:
  interfaces:
  - container
  - http-api
  emits:
  - oci-image
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Run a local registry to test a publishing pipeline without touching a real one.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- OCI Image, Runtime and Distribution
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "distribution center", "Distribution Centers, Corporate Offices, or Retail Stores" The
  bare name is blocked in the matcher, so this count reflects only qualified matches. Real adoption needs
  another source.
---
