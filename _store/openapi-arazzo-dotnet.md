---
title: OpenAPI Arazzo for .NET
slug: openapi-arazzo-dotnet
description: A .NET implementation of the Arazzo specification built to sit alongside Microsoft.OpenApi
  — parse, build, serialise and validate Arazzo documents that reference OpenAPI 3.0+ descriptions. Funded
  in part by the Interledger Foundation to bring Arazzo workflow support to Kiota, which is the clearest
  signal in this list that a major SDK generator intends to consume the format. Published to NuGet as
  a 1.0.0 preview.
companyCount: 0
website: https://spec.openapis.org/arazzo
repository: https://github.com/BinkyLabs/openapi-arazzo-dotnet
license: MIT
licenseSource: github-api
openSource: true
licenseVerified: '2026-09-17'
stars: 4
lastCommit: '2026-09-16'
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
  install:
    nuget: BinkyLabs.OpenApi.Arazzo
  consumes:
  - arazzo
  - openapi
  emits:
  - source-code
  deterministic: true
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Read and validate an Arazzo document from C#, or construct one programmatically.
  surface:
  - coding-agent
  - ci-pipeline
  note: Preview releases only as of September 2026; the API surface may still move.
tags:
- Arazzo
---
