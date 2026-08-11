---
title: SPDX Python Tools
slug: spdx-tools-python
description: Parses, validates and creates SPDX documents in Python, covering SPDX 2 and 3.
companyCount: 0
website: http://spdx.org
repository: https://github.com/spdx/tools-python
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 253
lastCommit: '2026-03-13'
archived: false
specifications:
- slug: spdx
  name: SPDX
  role: validates
  also:
  - parses
agent:
  interfaces:
  - cli
  - library
  install:
    pypi: spdx-tools
  consumes:
  - spdx
  emits:
  - spdx
  - json
  deterministic: true
  offline: true
  mutates: true
  credentials: false
useCases:
- task: Validate that an SBOM somebody supplied is actually well-formed SPDX.
  surface:
  - coding-agent
  - ci-pipeline
- task: Convert an SPDX document between its tag-value, JSON, YAML and RDF serialisations.
  surface:
  - coding-agent
tags:
- SPDX
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
