---
title: SpecLynx
slug: speclynx
redirect_from:
- /store/apidom/
description: An open source API tooling project, Apache-2.0 throughout, for authors and maintainers of
  OpenAPI, AsyncAPI and Arazzo — a VS Code OpenAPI toolkit, a browser editor, a CLI and a language service,
  all built on ApiDOM, its semantic parser. ApiDOM ships a dedicated Arazzo 1.x namespace plus JSON and
  YAML parser adapters, so an Arazzo document becomes a structure you walk rather than text you match;
  the Arazzo Toolkit and Jentic's parser are built on it. Maintained by Vladimír Gorej and contributors,
  with no paid tier.
companyCount: 0
website: https://speclynx.com/
repository: https://github.com/speclynx/apidom
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-17'
stars: 7
lastCommit: '2026-09-17'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: parses
  also:
  - validates
agent:
  interfaces:
  - library
  - cli
  - editor-extension
  install:
    npm: '@speclynx/apidom-ns-arazzo-1'
  consumes:
  - arazzo
  - openapi
  - asyncapi
  - json-schema
  emits:
  - javascript
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Traverse or refactor an Arazzo document by its semantic structure rather than by regex.
  surface:
  - coding-agent
  note: Install the ApiDOM Arazzo namespace plus the parser adapter for the serialisation you hold.
- task: Edit and validate Arazzo alongside the OpenAPI it references, in VS Code or the browser.
  surface:
  - ide
  - human
  note: The editor and VS Code toolkit run locally; specifications never leave the machine.
tags:
- Arazzo
---
