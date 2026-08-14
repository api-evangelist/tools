---
title: Prism
slug: prism
description: Turns an OpenAPI description into a running mock server that validates requests and returns
  example or dynamic responses — an API you can call before one exists.
companyCount: 0
website: https://stoplight.io/open-source/prism
repository: https://github.com/stoplightio/prism
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-14'
stars: 5004
lastCommit: '2026-08-13'
archived: false
specifications:
- slug: openapi
  name: OpenAPI
  role: mocks
agent:
  interfaces:
  - cli
  - container
  - library
  install:
    npm: '@stoplight/prism-cli'
  invoke: npx @stoplight/prism-cli mock <spec.yaml> --port 4010
  consumes:
  - openapi
  emits:
  - http
  deterministic: false
  offline: true
  mutates: false
  credentials: false
useCases:
- task: Exercise an integration end to end with no credentials, no cost and no production side effects.
  surface:
  - coding-agent
  note: The safest way for an autonomous agent to verify its own integration code. A mock cannot charge
    a card, send an email, or delete a record.
- task: Unblock frontend work while the backend is still being built.
  surface:
  - coding-agent
  - human
- task: Run contract validation in proxy mode against a real API to find where it diverges from its description.
  surface:
  - ci-pipeline
tags:
- OpenAPI
companyCountQuarter: q3-2026
nameCollision: true
nameCollisionNote: The name is an ordinary English word, so the job-corpus matcher cannot use it — sampled
  matches were "Raytheon financial systems (i.e. IPDS, APEX, Prism)", "Workday Report Writer … Prism"
  The bare name is blocked in the matcher, so this count reflects only qualified matches. Real adoption
  needs another source.
---
