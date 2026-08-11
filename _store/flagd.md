---
title: flagd
slug: flagd
description: A feature-flag daemon that evaluates flags from files, HTTP or Kubernetes resources and serves
  them over the OpenFeature Remote Evaluation Protocol.
companyCount: 0
website: https://flagd.dev
repository: https://github.com/open-feature/flagd
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 966
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: openfeature
  name: OpenFeature
  role: serves
agent:
  interfaces:
  - cli
  - container
  - http-api
  invoke: flagd start --uri file:<flags.json>
  consumes:
  - json
  - yaml
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Run feature flags with no vendor and no account, from a file in the repository.
  surface:
  - coding-agent
  - ci-pipeline
  note: Notable for agent work because it runs entirely offline — flags become testable configuration
    rather than a hosted dependency.
- task: Gate a risky change behind a flag so it can be turned off without a redeploy.
  surface:
  - coding-agent
tags:
- OpenFeature
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
