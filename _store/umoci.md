---
title: umoci
slug: umoci
description: Creates and modifies OCI images directly, without a container runtime or daemon.
companyCount: 0
website: https://umo.ci
repository: https://github.com/opencontainers/umoci
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 949
lastCommit: '2026-03-27'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: transforms
agent:
  interfaces:
  - cli
  consumes:
  - oci-image
  emits:
  - oci-image
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Manipulate image layers in a build system that has no Docker available.
  surface:
  - ci-pipeline
tags:
- OCI Image, Runtime and Distribution
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
