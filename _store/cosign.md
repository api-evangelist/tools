---
title: Cosign
slug: cosign
description: Signs and verifies containers, blobs and SBOMs with keyless signing backed by OIDC identity
  and a public transparency log — no long-lived signing key to manage or lose.
companyCount: 0
website: https://github.com/sigstore/cosign
repository: https://github.com/sigstore/cosign
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 6207
lastCommit: '2026-08-14'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: signs
  also:
  - verifies
  note: The entry point — keyless signing and verification of containers and blobs.
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    brew: cosign
    go: github.com/sigstore/cosign/v2/cmd/cosign
  invoke: cosign verify <registry>/<image>:<tag> --certificate-identity <identity> --certificate-oidc-issuer
    <issuer>
  consumes:
  - oci-image
  - filesystem
  - spdx
  emits:
  - json
  - signature
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Verify an artifact before consuming it, and know which identity actually signed it.
  surface:
  - coding-agent
  - ci-pipeline
  note: '`verify` requires naming the expected identity and issuer. A verification that does not pin those
    checks only that SOMEBODY signed it — which is not a security property.'
- task: Sign a release from CI with no key material stored anywhere.
  surface:
  - ci-pipeline
- task: Attach an SBOM or attestation to an image and sign it in one step.
  surface:
  - ci-pipeline
tags:
- Sigstore
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "co-sign", which appears in lending and finance postings. The bare name is blocked in the
  matcher, so this count reflects only qualified matches. Real adoption needs another source.
---
