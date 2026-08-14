---
title: OSV-SCALIBR
slug: osv-scalibr
description: An extensible library for extracting software inventory from filesystems and images, and
  the extraction engine underneath OSV-Scanner.
companyCount: 0
website: https://security.googleblog.com/2025/01/osv-scalibr-library-for-software.html
repository: https://github.com/google/osv-scalibr
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 633
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: osv-schema
  name: OSV Schema
  role: scans
agent:
  interfaces:
  - library
  - cli
  install:
    go: github.com/google/osv-scalibr
  consumes:
  - filesystem
  - oci-image
  emits:
  - json
  - spdx
  - cyclonedx
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Build custom inventory extraction into a tool rather than shelling out to a scanner.
  surface:
  - coding-agent
tags:
- OSV Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
