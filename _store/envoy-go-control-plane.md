---
title: Envoy Go Control Plane
slug: envoy-go-control-plane
description: The Go library for building an xDS control plane — serves configuration to Envoy instances
  over the discovery APIs.
companyCount: 0
website: https://github.com/envoyproxy/go-control-plane
repository: https://github.com/envoyproxy/go-control-plane
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 1723
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: xds
  name: xDS
  role: serves
agent:
  interfaces:
  - library
  install:
    go: github.com/envoyproxy/go-control-plane
  emits:
  - xds
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Build a bespoke control plane when an off-the-shelf mesh is more than the problem needs.
  surface:
  - coding-agent
tags:
- xDS
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
