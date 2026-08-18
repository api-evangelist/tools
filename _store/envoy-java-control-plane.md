---
title: Envoy Java Control Plane
slug: envoy-java-control-plane
description: The Java implementation of an xDS control plane for Envoy.
companyCount: 0
website: https://github.com/envoyproxy/java-control-plane
repository: https://github.com/envoyproxy/java-control-plane
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 312
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: xds
  name: xDS
  role: serves
agent:
  interfaces:
  - library
  emits:
  - xds
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Serve xDS configuration from an existing JVM platform service.
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
