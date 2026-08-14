---
title: Skopeo
slug: skopeo
description: Inspects, copies, signs and deletes container images between registries and storage backends
  — without a daemon and without pulling the image to run it.
companyCount: 1
website: https://github.com/podman-container-tools/skopeo
repository: https://github.com/podman-container-tools/skopeo
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 11151
lastCommit: '2026-08-05'
archived: false
specifications:
- slug: oci
  name: OCI Image, Runtime and Distribution
  role: transfers
agent:
  interfaces:
  - cli
  - container
  install:
    brew: skopeo
  invoke: skopeo inspect docker://<registry>/<image>:<tag>
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
- task: Read an image's manifest, labels and digests without a container runtime present.
  surface:
  - coding-agent
  note: Daemonless is the point for agents. In a sandbox with no Docker socket, this still works.
- task: Copy an image between registries during a migration or mirror.
  surface:
  - ci-pipeline
tags:
- OCI Image, Runtime and Distribution
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
