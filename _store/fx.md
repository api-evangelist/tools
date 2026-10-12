---
title: fx
slug: fx
description: A tiny, open, native coding agent from Vercel Labs — a roughly 6MB Zig binary that reads
  code, edits files and runs commands interactively or as a single `fx ask` request. It is model-agnostic
  (ChatGPT and Grok subscriptions, Vercel AI Gateway, or any OpenAI-compatible endpoint including a local
  Ollama), an MCP client with a published coverage table, an Agent Client Protocol server for editors,
  and an embeddable runtime (libfx) for Node.js and the browser through WebAssembly. Experimental, Apache-2.0.
companyCount: 0
website: https://fx.sh
repository: https://github.com/vercel-labs/fx
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-10-13'
stars: 3381
lastCommit: '2026-10-12'
archived: false
specifications:
- slug: model-context-protocol
  name: Model Context Protocol (MCP)
  role: runs
  note: A native coding-agent CLI that is an MCP client over stdio, Streamable HTTP and legacy HTTP+SSE
    — tools, resources, prompts, completion, subscriptions and elicitation — and says plainly that it
    does not implement MCP Tasks, MCP Apps, Skills over MCP or the enterprise auth extensions, and does
    not expose itself as an MCP server.
agent:
  interfaces:
  - cli
  - library
  install:
    npm: libfx
  invoke: fx ask --json "<prompt>"
  consumes:
  - mcp
  - agent-skill
  - source-code
  - filesystem
  - markdown
  - text
  emits:
  - json
  - markdown
  - text
  deterministic: false
  offline: false
  mutates: true
  credentials: true
useCases:
- task: Run one non-interactive coding task from a script or CI step and read the result back as JSON
    with `fx ask --json`.
  surface:
  - ci-pipeline
  - coding-agent
  note: It edits files and runs commands, so treat every run as a write. The default permission mode sends
    unrecognised commands and every MCP tool call to a review model first; set rules in ~/.fx/settings.json
    rather than relying on that in a pipeline.
- task: Connect an API provider's MCP server (stdio or Streamable HTTP, with browser OAuth or a bearer
    token) and let the agent find and call its tools, resources and prompts while it works.
  surface:
  - coding-agent
  - human
- task: Drive the same agent from an editor through the Agent Client Protocol with `fx acp`.
  surface:
  - ide
- task: Embed the agent runtime in a Node.js service or a web page through libfx, with your own JavaScript
    functions as tools and sessions that survive restarts.
  surface:
  - ai-platform
tags:
- Model Context Protocol (MCP)
posts:
- title: fx Is A Coding Agent That Tells You Which Parts Of MCP It Does Not Do
  url: https://apievangelist.com/2026/10/13/fx-is-a-coding-agent-that-tells-you-which-parts-of-mcp-it-does-not-do/
---
