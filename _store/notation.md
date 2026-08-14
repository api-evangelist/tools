---
title: Notation
slug: notation
description: Signs and verifies OCI artifacts against a trust policy, storing signatures in the registry
  alongside what they sign.
companyCount: 0
website: https://notaryproject.dev
repository: https://github.com/notaryproject/notation
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 493
lastCommit: '2026-08-03'
archived: false
specifications:
- slug: notary-project
  name: Notary Project
  role: signs
  also:
  - verifies
agent:
  interfaces:
  - cli
  - library
  install:
    brew: notation
  invoke: notation verify <registry>/<image>:<tag>
  consumes:
  - oci-image
  emits:
  - json
  - text
  deterministic: true
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Verify an image is signed by a trusted identity before deploying it.
  surface:
  - ci-pipeline
  - coding-agent
- task: Sign artifacts with keys from an existing enterprise PKI rather than a new trust root.
  surface:
  - ci-pipeline
  note: The practical difference from Sigstore — Notation fits organisations that already have a CA and
    intend to keep using it.
tags:
- Notary Project
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "JavaScript Object Notation (JSON)", "Big O notation" The bare name is blocked in the matcher,
  so this count reflects only qualified matches. Real adoption needs another source.
---
