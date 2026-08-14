---
title: Gitsign
slug: gitsign
description: Signs Git commits and tags with Sigstore keyless signing, requiring no GPG key.
companyCount: 0
website: https://github.com/sigstore/gitsign
repository: https://github.com/sigstore/gitsign
license: Apache-2.0
licenseSource: license-file
openSource: true
licenseVerified: '2026-08-14'
stars: 1115
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: sigstore
  name: Sigstore
  role: signs
agent:
  interfaces:
  - cli
  install:
    brew: gitsign
    go: github.com/sigstore/gitsign
  emits:
  - signature
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Sign commits without the GPG key management that stops most teams from signing at all.
  surface:
  - coding-agent
  - human
- task: Establish which identity authored a commit, when an agent may be the one committing.
  surface:
  - coding-agent
  note: 'Increasingly relevant as agents commit code: signing answers "who or what produced this change"
    in a way an author field cannot.'
tags:
- Sigstore
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
