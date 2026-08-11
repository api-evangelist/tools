---
title: Envoy Gateway
slug: envoy-gateway
description: Manages Envoy as a Kubernetes Gateway API implementation, turning standard Gateway resources
  into xDS configuration.
companyCount: 2
website: https://gateway.envoyproxy.io
repository: https://github.com/envoyproxy/gateway
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 2951
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: xds
  name: xDS
  role: proxies
agent:
  interfaces:
  - container
  consumes:
  - kubernetes
  - xds
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Run an API gateway configured through the standard Kubernetes Gateway API.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- xDS
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
