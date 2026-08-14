---
title: Istio
slug: istio
companyCount: 67
description: The service mesh whose control plane is the largest production consumer of xDS — programs
  Envoy sidecars and gateways across a cluster.
tags:
- Service Mesh
- Microservices
- Kubernetes
- Cloud Native
- xDS
website: https://istio.io
radarRing: Established
alternativeNames:
- istio
repository: https://github.com/istio/istio
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 38352
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: xds
  name: xDS
  role: serves
  note: The largest production xDS control plane.
agent:
  interfaces:
  - container
  - cli
  install:
    brew: istioctl
  consumes:
  - kubernetes
  - xds
  emits:
  - json
  - openmetrics
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Apply mTLS, routing and policy across services without changing any of them.
  surface:
  - ci-pipeline
- task: Inspect what configuration a mesh has actually pushed to a proxy when behaviour is wrong.
  surface:
  - coding-agent
  note: '`istioctl proxy-config` is the debugging surface — it dumps the effective xDS state.'
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
