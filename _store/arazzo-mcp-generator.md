---
title: Arazzo MCP Generator
slug: arazzo-mcp-generator
description: 'A CLI that turns an Arazzo document and its referenced OpenAPI files into a fully Dockerised
  Python MCP server — each workflow becomes a tool an agent can call. The most direct bridge yet between
  the two specifications: Arazzo describes the sequence, MCP exposes it. Validates the Arazzo input first,
  with Spectral when available.'
companyCount: 0
website: https://github.com/wso2/arazzo-mcp-generator
repository: https://github.com/wso2/arazzo-mcp-generator
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-16'
stars: 2
lastCommit: '2026-08-19'
archived: false
specifications:
- slug: arazzo
  name: Arazzo
  role: generates
agent:
  interfaces:
  - cli
  consumes:
  - arazzo
  - openapi
  emits:
  - source-code
  - oci-image
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Expose an existing Arazzo workflow to agents as an MCP tool without hand-writing the server.
  surface:
  - coding-agent
  note: Generation is offline; the generated server makes real calls when an agent invokes it.
tags:
- Arazzo
---
