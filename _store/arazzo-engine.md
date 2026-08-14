---
title: Arazzo Engine
slug: arazzo-engine
description: A Python runner and generator for Arazzo, and the closest thing the specification has to
  a reference runtime. The runner handles authentication across API key, OAuth2, basic and bearer, resolves
  servers dynamically, evaluates runtime expressions, and carries conditional logic and error handling;
  the generator drafts workflows from an OpenAPI description. Built for agents calling a described workflow
  rather than for a test suite asserting one still passes.
companyCount: 0
website: https://docs.jentic.com/reference/arazzo-engine/overview/
repository: https://github.com/jentic/arazzo-engine
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 62
lastCommit: '2026-06-12'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: runs
  also:
  - generates
  - documents
agent:
  interfaces:
  - cli
  - library
  install:
    pip: arazzo-runner
  consumes:
  - arazzo
  - openapi
  emits:
  - json
  - http
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Let an agent execute a described workflow, including the authentication handshake.
  surface:
  - coding-agent
  - ai-platform
  note: Beta by its own labelling, and the repository has been quiet since June 2026. Real calls, real
    credentials, real side effects.
- task: Draft a first Arazzo workflow from an existing OpenAPI description.
  surface:
  - coding-agent
  note: A generated draft is a starting point — the operations are real, the sequence is a guess.
tags:
- Arazzo
---
