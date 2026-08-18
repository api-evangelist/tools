---
title: Sigstore Policy Controller
slug: sigstore-policy-controller
description: A Kubernetes admission controller that enforces signature and attestation policy on images
  before they are allowed to run.
companyCount: 0
website: https://github.com/sigstore/policy-controller
repository: https://github.com/sigstore/policy-controller
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 178
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: verifies
agent:
  interfaces:
  - container
  consumes:
  - oci-image
  - in-toto-attestation
  deterministic: true
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Refuse to run any workload that is not signed by an approved identity.
  surface:
  - ci-pipeline
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
