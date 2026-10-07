---
title: pyarazzo
slug: pyarazzo
description: A Python CLI that generates human-readable documentation from an Arazzo document — `pyarazzo
  doc generate` turns a workflow file into an output folder of docs. Installable from PyPI; early (0.0.x)
  but current.
companyCount: 0
website: https://github.com/b-lab-io/pyarazzo
repository: https://github.com/b-lab-io/pyarazzo
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-10-06'
stars: 1
lastCommit: '2026-09-21'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: documents
agent:
  interfaces:
  - cli
  install:
    pip: pyarazzo
  consumes:
  - arazzo
  emits:
  - html
  - markdown
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Publish documentation for an Arazzo workflow alongside the API docs it orchestrates.
  surface:
  - ci-pipeline
  - coding-agent
tags:
- Arazzo
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
precision: 92
precisionGrade: high
precisionBasis:
- 'bare-only -8: no qualified phrase survives, though the bare needle is otherwise unremarkable'
---
