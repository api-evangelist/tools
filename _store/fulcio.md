---
title: Fulcio
slug: fulcio
description: The certificate authority that issues short-lived signing certificates bound to an OIDC identity
  — what makes keyless signing possible.
companyCount: 0
website: https://github.com/sigstore/fulcio
repository: https://github.com/sigstore/fulcio
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 866
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: issues
agent:
  interfaces:
  - http-api
  - container
  emits:
  - x509
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Run a private Sigstore instance with an organisation's own identity provider.
  surface:
  - ci-pipeline
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
