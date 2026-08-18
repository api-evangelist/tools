---
title: crane / go-containerregistry
slug: crane
description: A Go library and the `crane` CLI for working with container registries and images directly
  over the Distribution API — list tags, read manifests, copy and mutate images.
companyCount: 0
website: https://github.com/google/go-containerregistry
repository: https://github.com/google/go-containerregistry
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 4008
lastCommit: '2026-08-12'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: transfers
  note: Ships `crane` — the tool an agent reaches for to inspect a registry without a daemon.
agent:
  interfaces:
  - cli
  - library
  install:
    go: github.com/google/go-containerregistry/cmd/crane
  invoke: crane manifest <registry>/<image>:<tag>
  consumes:
  - oci-image
  emits:
  - json
  - oci-image
  deterministic: true
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Enumerate the tags a registry holds, to find what versions actually exist.
  surface:
  - coding-agent
- task: Rewrite an image's config or append a layer without a full rebuild.
  surface:
  - ci-pipeline
tags:
- OCI Image, Runtime and Distribution
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
