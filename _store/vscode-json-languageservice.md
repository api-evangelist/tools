---
title: VS Code JSON Language Service
slug: vscode-json-languageservice
description: The JSON language service behind VS Code and the Monaco editor — schema validation, completion,
  hover, document symbols and Go to Definition for JSON and JSONC. Version 6 (prerelease) adds JSON Schema
  2019-09 vocabularies and 2020-12 $dynamicRef support.
companyCount: 0
website: https://github.com/microsoft/vscode-json-languageservice
repository: https://github.com/microsoft/vscode-json-languageservice
license: MIT
licenseSource: license-file
openSource: true
licenseVerified: '2026-09-17'
stars: 326
lastCommit: '2026-09-14'
archived: false
specifications:
- slug: json-schema
  name: JSON Schema
  role: validates
  note: The engine behind JSON validation, completion and hover in VS Code and Monaco. Added 2019-09 and
    2020-12 ($dynamicRef) support in 6.0.0-next.2 (July 2026).
agent:
  interfaces:
  - library
  - lsp
  install:
    npm: vscode-json-languageservice
  consumes:
  - json-schema
  - json
  emits:
  - json
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Predict what VS Code will flag in a JSON or JSONC file that declares a schema, before a developer
    opens it.
  surface:
  - coding-agent
  - ci-pipeline
  note: 6.x is ESM-only and still tagged `next`. As of 2026-09, npm's `latest` tag also points at a 6.0.0
    prerelease, so pin the version you test against.
- task: Give an editor schema-driven completion, hover and diagnostics for JSON.
  surface:
  - ide
posts:
- title: VS Code Is Finally Catching Up With JSON Schema 2020-12
  url: https://apievangelist.com/2026/09/17/vs-code-is-finally-catching-up-with-json-schema-2020-12/
  date: 2026-09-17
tags:
- JSON Schema
---
