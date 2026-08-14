---
title: jsonschema (Python)
slug: python-jsonschema
description: The reference JSON Schema validator for Python, covering every published dialect.
companyCount: 0
website: https://python-jsonschema.readthedocs.io
repository: https://github.com/python-jsonschema/jsonschema
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 4971
lastCommit: '2026-08-10'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: validates
agent:
  interfaces:
  - library
  - cli
  install:
    pypi: jsonschema
  invoke: python -m jsonschema -i <instance.json> <schema.json>
  consumes:
  - json-schema
  - json
  emits:
  - text
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Validate data against a schema from a Python pipeline or notebook.
  surface:
  - coding-agent
  - ci-pipeline
tags:
- JSON Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
