---
title: ORAS
slug: oras
companyCount: 0
description: Pushes and pulls arbitrary artifacts through an OCI registry — Helm charts, SBOMs, signatures,
  models — using the registry as general artifact storage rather than image storage.
tags:
- Container Registry
- OCI
- Artifact Storage
- Cloud Native
- OCI Image, Runtime and Distribution
website: https://oras.land
radarRing: Initial
alternativeNames:
- oras
- OCI Registry As Storage
repository: https://github.com/oras-project/oras
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2384
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: transfers
  note: Pushes and pulls arbitrary artifacts through an OCI registry, not just images.
agent:
  interfaces:
  - cli
  - library
  install:
    brew: oras
  invoke: oras push <registry>/<repo>:<tag> <file>:<media-type>
  consumes:
  - filesystem
  emits:
  - oci-image
  deterministic: true
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Store a non-image artifact where the infrastructure already has auth, mirroring and retention.
  surface:
  - coding-agent
  - ci-pipeline
  note: The reason the Distribution spec matters beyond containers — registries turn out to be the artifact
    store organisations already run.
- task: Attach an SBOM or attestation to an image as a referring artifact.
  surface:
  - ci-pipeline
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 90
precisionGrade: high
precisionBasis:
- 'acronym-shape -10: shortest bare needle is 4 characters, halved — it neither collides nor appears in
  the corpus frequency table'
---
