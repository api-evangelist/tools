---
title: Zot
slug: zot
companyCount: 0
description: A production OCI-native registry that stores only OCI images and artifacts, with built-in
  vulnerability scanning and a search API.
tags:
- Decentralized
- Social Networking
- Federation
- Privacy
- OCI Image, Runtime and Distribution
website: https://zotregistry.dev
radarRing: Initial
alternativeNames:
- zot
repository: https://github.com/project-zot/zot
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 2600
lastCommit: '2026-08-11'
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
  - json
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Run a registry that is strictly spec-conformant, including the referrers API.
  surface:
  - ci-pipeline
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
