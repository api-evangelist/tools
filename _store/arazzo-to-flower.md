---
title: Arazzo to Flower
slug: arazzo-to-flower
description: A Ruby gem from Bump.sh that transforms Arazzo workflow files into Flower, Bump.sh's own
  workflow format. Listed because it is the concrete artefact behind a vendor deciding to build an alternative
  after hitting gaps in Arazzo — the case the specification's maintainers cite when asking implementers
  to contribute back rather than fork the idea.
companyCount: 0
website: https://github.com/bump-sh/arazzo-to-flower
repository: https://github.com/bump-sh/arazzo-to-flower
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-17'
stars: 0
lastCommit: '2026-03-31'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: converts
agent:
  interfaces:
  - library
  - cli
  consumes:
  - arazzo
  emits:
  - yaml
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Move an Arazzo workflow into Bump.sh's Flower format.
  surface:
  - coding-agent
  note: The gem is not on rubygems.org as of September 2026; install from the repository.
tags:
- Arazzo
---
