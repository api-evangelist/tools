---
title: Witness
slug: witness
description: Wraps any build command and produces a signed in-toto attestation about what it observed
  — the materials, the products, and the environment.
companyCount: 0
website: https://witness.dev
repository: https://github.com/in-toto/witness
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 545
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: in-toto
  name: in-toto
  role: attests
- slug: slsa
  name: SLSA
  role: attests
agent:
  interfaces:
  - cli
  - library
  - ci-action
  install:
    go: github.com/in-toto/witness
  invoke: witness run -s <step-name> -o <attestation.json> -- <build-command>
  emits:
  - in-toto-attestation
  - json
  deterministic: false
  offline: true
  mutates: true
  credentials: true
useCases:
- task: Add provenance to an existing build without restructuring the pipeline.
  surface:
  - ci-pipeline
  note: Wrapping the command is what makes this adoptable — the build does not have to change, it just
    gets observed.
- task: Enforce that a build ran the steps a policy requires, in order.
  surface:
  - ci-pipeline
tags:
- in-toto
- SLSA
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "you'll witness first-hand", "Factory witness testing (FWT)" The bare name is blocked in
  the matcher, so this count reflects only qualified matches. Real adoption needs another source.
---
