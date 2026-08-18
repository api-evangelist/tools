---
title: runc
slug: runc
description: The reference OCI runtime — spawns and runs containers per the Runtime Specification, and
  the thing Docker and containerd ultimately call.
companyCount: 1
website: https://www.opencontainers.org/
repository: https://github.com/opencontainers/runc
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 13402
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: runs
agent:
  interfaces:
  - cli
  consumes:
  - oci-runtime-bundle
  deterministic: false
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Understand what a container runtime is actually doing beneath a higher-level tool.
  surface:
  - coding-agent
tags:
- OCI Image, Runtime and Distribution
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 82
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
