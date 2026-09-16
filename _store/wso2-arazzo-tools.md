---
title: WSO2 Arazzo Tools
slug: wso2-arazzo-tools
description: 'WSO2''s collection of developer tools for Arazzo — a VS Code extension with a workflow designer
  and visualizer, validation, real-time execution and utilities. The first mainstream API gateway vendor
  to publish open source Arazzo tooling under its own org, alongside Arazzo support in its agent portal.
  Early: two stars and active commits.'
companyCount: 0
website: https://github.com/wso2/arazzo-tools
repository: https://github.com/wso2/arazzo-tools
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 2
lastCommit: '2026-09-11'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: authors
  also:
  - validates
  - documents
  - runs
agent:
  interfaces:
  - editor-extension
  consumes:
  - arazzo
  - openapi
  emits:
  - html
  - json
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Author and visualise an Arazzo workflow in VS Code, then execute it from the editor.
  surface:
  - ide
  - human
  note: Built from source per the README; not yet found on the VS Code Marketplace.
tags:
- Arazzo
---
