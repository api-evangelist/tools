---
title: apitapviz
slug: apitapviz
description: A small Python command-line tool that renders an Arazzo file as Markdown or a Mermaid diagram
  — a human-readable view of the workflow you can drop into documentation or a pull request. A mirror
  of the maintainer's main repository; last touched March 2025.
companyCount: 0
website: https://github.com/lornajane/apitapviz
repository: https://github.com/lornajane/apitapviz
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 5
lastCommit: '2025-03-12'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: documents
agent:
  interfaces:
  - cli
  consumes:
  - arazzo
  emits:
  - markdown
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Put a diagram of an Arazzo workflow into a README or PR description.
  surface:
  - coding-agent
  - ci-pipeline
  note: Run from source with uv; no published package.
tags:
- Arazzo
---
