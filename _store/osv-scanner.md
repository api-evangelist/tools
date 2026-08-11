---
title: OSV-Scanner
slug: osv-scanner
description: Scans lockfiles, SBOMs, container images and directories against the OSV database, and reports
  vulnerabilities in the OSV schema.
companyCount: 0
website: https://google.github.io/osv-scanner/
repository: https://github.com/google/osv-scanner
license: Apache-2.0
licenseSource: github-api
openSource: true
licenseVerified: '2026-08-11'
stars: 10805
lastCommit: '2026-08-11'
archived: false
specifications:
- slug: osv-schema
  name: OSV Schema
  role: scans
agent:
  interfaces:
  - cli
  - ci-action
  - container
  install:
    brew: osv-scanner
    go: github.com/google/osv-scanner/cmd/osv-scanner
  invoke: osv-scanner scan --lockfile <package-lock.json> --format json
  consumes:
  - lockfile
  - spdx
  - cyclonedx
  - oci-image
  emits:
  - json
  - sarif
  - table
  deterministic: false
  offline: false
  mutates: false
  credentials: false
useCases:
- task: Find known vulnerabilities in a project's declared dependencies.
  surface:
  - coding-agent
  - ci-pipeline
  note: Reads lockfiles directly, so an agent can scan a repository it has just cloned with no build and
    no install step.
- task: Produce SARIF a code-hosting platform will render inline on a pull request.
  surface:
  - ci-pipeline
tags:
- OSV Schema
radarRing: Initial
companyCountQuarter: q3-2026
companyCountBasis: uncapped full-corpus read, hardened word-boundary matcher, qualified corpora only
---
