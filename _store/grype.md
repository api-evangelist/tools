---
title: Grype
slug: grype
description: Scans container images, filesystems and SBOMs for known vulnerabilities, reading OSV and
  other vulnerability sources.
companyCount: 3
website: https://github.com/anchore/grype
repository: https://github.com/anchore/grype
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 12735
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: scans
- slug: osv-schema
  name: OSV Schema
  role: scans
agent:
  interfaces:
  - cli
  - container
  - ci-action
  install:
    brew: grype
    go: github.com/anchore/grype/cmd/grype
  invoke: grype sbom:<sbom.spdx.json> -o json
  consumes:
  - oci-image
  - spdx
  - cyclonedx
  - filesystem
  emits:
  - json
  - sarif
  - table
  deterministic: false
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Find known vulnerabilities in an artifact before it ships.
  surface:
  - ci-pipeline
  - coding-agent
- task: Re-scan an existing SBOM as new vulnerabilities are published, without rebuilding.
  surface:
  - ci-pipeline
  note: Results change over time for identical input — the vulnerability database moves. Never cache a
    verdict and treat it as still true.
tags:
- SPDX
- OSV Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 87
precisionGrade: high
precisionBasis:
- 'acronym-shape -5: shortest bare needle is 5 characters, halved — it neither collides nor appears in
  the corpus frequency table'
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
