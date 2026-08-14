---
title: sigstore-python
slug: sigstore-python
description: A Sigstore client for Python, used for signing and verifying Python package releases.
companyCount: 0
website: https://pypi.org/p/sigstore
repository: https://github.com/sigstore/sigstore-python
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 332
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: signs
agent:
  interfaces:
  - cli
  - library
  install:
    pypi: sigstore
  invoke: python -m sigstore verify identity <artifact> --cert-identity <id> --cert-oidc-issuer <issuer>
  emits:
  - signature
  - json
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Verify the Sigstore signatures PyPI publishes for a release.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
