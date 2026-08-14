---
title: Envoy
slug: envoy
companyCount: 43
description: The cloud-native L7 proxy whose configuration APIs became xDS — reconfigures itself dynamically
  from a control plane with no restart.
tags:
- Envoy
- xDS
radarRing: Established
alternativeNames:
- Envoy Proxy
- envoy
website: https://www.envoyproxy.io
repository: https://github.com/envoyproxy/envoy
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 28758
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: xds
  name: xDS
  role: proxies
agent:
  interfaces:
  - container
  - cli
  - http-api
  consumes:
  - xds
  - yaml
  emits:
  - openmetrics
  - json
  deterministic: false
  offline: true
  mutates: false
  credentials: true
useCases:
- task: Put a programmable proxy in the request path for routing, retries or rate limiting.
  surface:
  - coding-agent
- task: Change routing at runtime through a control plane rather than by redeploying.
  surface:
  - ci-pipeline
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
