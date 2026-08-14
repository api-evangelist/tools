---
title: Syft
slug: syft
description: Generates a software bill of materials from container images and filesystems, emitting SPDX
  or CycloneDX — the most widely used SBOM generator there is.
companyCount: 3
website: https://github.com/anchore/syft
repository: https://github.com/anchore/syft
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 9377
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: generates
  produces:
  - sbom
  note: The most-used SBOM generator; emits SPDX and CycloneDX.
agent:
  interfaces:
  - cli
  - container
  - library
  - ci-action
  install:
    brew: syft
    go: github.com/anchore/syft/cmd/syft
  invoke: syft <image-or-dir> -o spdx-json=<sbom.spdx.json>
  consumes:
  - oci-image
  - filesystem
  emits:
  - spdx
  - cyclonedx
  - json
  - table
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Answer "what is actually inside this image?" with a machine-readable artifact.
  surface:
  - coding-agent
  - ci-pipeline
  note: Where a supply-chain conversation starts. Pipe the output into Grype and the same artifact answers
    "and what is wrong with it?".
- task: Produce the SBOM a customer or regulator is asking for, in the format they named.
  surface:
  - ci-pipeline
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
