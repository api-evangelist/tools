---
title: A2A CLI
slug: a2a-cli
description: The official command-line client for Agent2Agent (A2A) agents, from the A2A project. Fetches
  an agent card, sends a message and streams the task to completion, and runs a local A2A server from
  any stdin/stdout program with `--echo` or `--exec`. Built on the A2A Go SDK, speaks protocol v1.0, and
  prints protocol-native JSON with predictable exit codes so a shell script, a CI step or a coding assistant
  can hand work to a remote agent without bespoke integration code.
companyCount: 0
website: https://github.com/a2aproject/a2a-cli
repository: https://github.com/a2aproject/a2a-cli
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-10-06'
stars: 152
lastCommit: '2026-10-01'
archived: false
specifications:
- slug: agent2agent
  name: Agent2Agent (A2A)
  role: runs
  also:
  - serves
  - parses
  note: '`a2a card get` fetches an agent card, `a2a send` messages an agent and streams the task, and
    `a2a server --exec` turns any stdin/stdout program into an A2A server for testing. JSON output and
    predictable exit codes are the point.'
agent:
  interfaces:
  - cli
  install:
    brew: a2aproject/a2a-cli/a2a
    winget: a2aproject.a2acli
    go: github.com/a2aproject/a2a-cli
  consumes:
  - agent-card
  - http
  - text
  emits:
  - json
  - text
  deterministic: false
  offline: false
  mutates: true
  credentials: false
useCases:
- task: Hand a task off to a remote A2A agent from a coding assistant, a shell script or a pipeline, and
    read the result back as JSON.
  surface:
  - coding-agent
  - ci-pipeline
  note: Sending a message creates a task on the remote agent, so treat `a2a send` as a write. Agents that
    require auth take it through the CLI's configuration; nothing is needed to read a public agent card.
- task: Fetch and inspect an agent card before deciding whether to delegate to that agent.
  surface:
  - coding-agent
- task: Stand up a throwaway A2A server from a plain script (`a2a server --exec`) to test a client, a
    workflow or a card without an SDK.
  surface:
  - coding-agent
  - ci-pipeline
  note: The `--echo` and `--exec` server modes are for learning, demos and tests, not production.
posts:
- title: 427 Agent Cards, How They Talk And What They Do
  url: https://apievangelist.com/2026/09/21/427-agent-cards-how-they-talk-and-what-they-do/
  date: 2026-09-21
- title: A2A Adoption Is 421 Of 27,840, And Most Of Them Arrived With The Card
  url: https://apievangelist.com/2026/09/21/a2a-adoption-is-421-of-27840-and-most-of-them-arrived-with-the-card/
  date: 2026-09-21
- title: Most Published Agent Cards Are Not Actually A2A
  url: https://apievangelist.com/2026/07/29/most-published-agent-cards-are-not-actually-a2a/
  date: 2026-07-29
tags:
- Agent2Agent (A2A)
---
