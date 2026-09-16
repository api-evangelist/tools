---
title: Arazzo IntelliJ Plugin
slug: arazzo-idea-plugin
description: A plugin for IntelliJ IDEA and other JetBrains IDEs that detects Arazzo YAML and JSON files,
  validates them live against the official JSON Schema with inspections and quick fixes, and offers completion
  and preview. The JetBrains counterpart to WSO2's VS Code extension.
companyCount: 0
website: https://plugins.jetbrains.com/plugin/28079-arazzo
repository: https://github.com/Pakisan/arazzo-idea-plugin
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 4
lastCommit: '2025-08-04'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: authors
  also:
  - validates
agent:
  interfaces:
  - editor-extension
  consumes:
  - arazzo
  emits:
  - text
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Get schema validation and completion while hand-authoring Arazzo in a JetBrains IDE.
  surface:
  - ide
  - human
  note: Last commit August 2025; check it against the 1.1 schema before relying on its inspections.
tags:
- Arazzo
---
