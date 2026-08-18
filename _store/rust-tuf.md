---
title: rust-tuf
slug: rust-tuf
description: The Rust implementation of The Update Framework.
companyCount: 0
website: https://crates.io/crates/tuf
repository: https://github.com/theupdateframework/rust-tuf
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 196
lastCommit: '2026-07-20'
archived: false
specifications:
- slug: tuf
  name: The Update Framework
  role: verifies
agent:
  interfaces:
  - library
  consumes:
  - tuf-metadata
  deterministic: true
  offline: false
  mutates: false
  credentials: true
useCases:
- task: Verify TUF metadata from a Rust client.
  surface:
  - coding-agent
tags:
- The Update Framework
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 100
precisionGrade: high
precisionBasis:
- 'no penalty: an unambiguous, sufficiently long name'
---
