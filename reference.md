---
layout: default
title: Agent Reference
nav: All Tools
permalink: /reference/
description: How to resolve from an artifact you are holding to a tool that acts on it — the vocabulary, the structured data, and what the numbers on this site do and do not mean.
---

# Agent Reference

This site exists because a list of tool names is not much use to an agent. Knowing that Spectral
exists does not tell you whether it can read the file in front of you, whether it runs without
network access, whether it writes to disk, or whether its output is something you can act on
rather than paraphrase.

So every tool here carries the answers to those questions as structured data, and the pages you
are reading are a rendering of that data rather than the source of it.

## Don't scrape this site

| Artifact | What it is |
|---|---|
| [`/tools.json`](/tools.json) | Every tool: license, specification bindings, invocation, use cases |
| [`/roles.json`](/roles.json) | The controlled vocabulary — roles, artifacts, interfaces, surfaces |
| [`/tool.schema.json`](/tool.schema.json) | The JSON Schema every entry conforms to |
| [`/llms.txt`](/llms.txt) | The short version of this page |

### Two catalogues in one file — read `sources` before you read anything else

This site is the union of two catalogues, and `/tools.json` publishes both. Every entry carries a
`sources` array saying which one it came from, because they carry different guarantees.

| `sources` value | What it means | What the entry carries |
|---|---|---|
| `specification-catalog` | The repository was resolved live against the GitHub API, its license was read from it, and it is bound to a specification with a role | `license`, `repository`, `stars`, `lastCommit`, `specifications`, `agent`, `useCases` |
| `demand-corpus` | The tool is in the API Evangelist insights vocabulary, measured against the job corpus | `companyCount`, `companyCountQuarter`, `radarRing` |

Most entries carry one. An entry carrying **both** is a tool that was read *and* measured, and it
is the only kind where you can put licensing and adoption in the same sentence.

**Do not assume a field is present.** A demand-corpus entry has no license and no repository —
nothing was read, so nothing is claimed. A specification-catalog entry with no `companyCount` has
not been measured yet, which is not the same as measuring zero. An entry with an empty `sources`
array is in neither and is being reported rather than hidden.

Measuring what companies hire for and cataloguing what implements a specification are different
jobs. Keeping them labelled, in one file, is what lets you ask questions that need both.

## How to resolve

You are holding an artifact and you have a goal. Resolve in four steps.

**1. Artifact to specification.** An `openapi.yaml` is OpenAPI. A `.proto` is Protocol Buffers. An
`asyncapi.yaml` is AsyncAPI. An SBOM is SPDX or CycloneDX. A `.sig` next to a container image is
probably Sigstore or Notary. Each specification has an entry on
[standards.apievangelist.com](https://standards.apievangelist.com) describing what it actually
specifies, and this site lists the tools that implement it.

**2. Goal to role.** The role vocabulary is deliberately small and verb-shaped, because the point
is to be resolvable rather than expressive:

| You want to… | Role |
|---|---|
| know whether a document is correct, or meets your rules | `validates` |
| turn a document into something you can traverse | `parses` |
| find out whether the running API matches its description | `tests` |
| get a client, server, types or an SBOM out of it | `generates` |
| change a contract without forking it | `transforms` |
| get a working endpoint before the real one exists | `mocks` |
| know whether to trust an artifact | `verifies` |
| record how an artifact was built | `attests` |
| find known problems in it | `scans` |

The full set, with what each role returns and where agents get it wrong, is in
[`/roles.json`](/roles.json).

**3. Specification plus role to tool.** Filter `/tools.json` on `specifications[].slug` and
`specifications[].role`. Usually you will get more than one answer; that is the point.

**4. Check the runtime facts before you run anything.**

| Field | Why you care |
|---|---|
| `agent.offline` | Whether it works in a sandbox with no egress |
| `agent.mutates` | Whether it writes to disk or to a remote system — confirm before running unattended |
| `agent.credentials` | Whether you need to plan for secrets rather than just running the command |
| `agent.emits` | Whether output is machine-readable (`json`, `sarif`, `junit`) or only pretty-printed |
| `agent.deterministic` | Whether you can cache or diff results across runs |
| `archived` | Never recommend an archived project for new work |

`agent.deterministic: false` deserves a second look. A vulnerability scanner returns different
results for identical input as its database moves — which is correct behaviour, and means a
verdict must never be cached and treated as still true.

## What the numbers mean, and what they don't

**`companyCount` is a demand signal, not a deployment count.** It is the number of distinct
companies whose job postings name the tool, taken from the API Evangelist job corpus. A company
hiring for a tool is good evidence it uses one — but a tool nobody hires specifically for can
still be everywhere, and open source projects have no employer at all. Kubernetes can never have
a job corpus of its own.

Counts are **only comparable within a single quarter**. Corpus size and extraction method both
change between quarters, so a rise from one quarter to the next may be the corpus growing rather
than the tool spreading.

**`stars` is a popularity proxy, not a quality measure**, and it is heavily biased toward age and
toward tools that developers personally choose over tools their employer imposes.

**`lastCommit` and `archived` are the honest liveness signals.** A finished specification's SDK may
sit untouched for a year because it is done. A tool that has drifted for three years usually has
not.

**`nameCollision: true` means the count is a floor, not a measurement.** Eight tools are named with
ordinary English words — Distribution, Witness, Prism, vacuum, Notation, Scalar, Buf, Cosign. In a
job corpus "distribution" is a distribution center and "witness" is witness testing, so the bare
name is blocked in the matcher and these tools count only their unambiguous matches. A low number
on one of these says the matcher could not see it, not that nobody uses it.

## Licensing

Every license on this site is **read from the repository**, not inferred from the ecosystem it
sits in. Three distinctions matter, and directories routinely collapse them:

- **`openSource: true`** — an OSI-approved license.
- **`openSource: false`** — a source-available license such as BUSL or the Elastic License. You can
  read the code; you cannot necessarily use it the way you intend to. Several widely-listed API
  tools are in this category and are described as open source anyway.
- **`license: null`** — no license file was found. This is not permissive. Without a license there
  is no grant to use the code at all, and that includes some very widely used tools.

Where GitHub's own detector fails — a short-form Apache notice, a file named `LICENSE.code` —
the license text is read directly and the entry is marked `licenseSource: license-file`, with the
evidence recorded in the repository behind this site.

## Where this comes from

The specification inventory is the API Evangelist [Linux Foundation
research](https://apievangelist.com), covering the specifications the LF stewards through the
OpenAPI Initiative, AsyncAPI Initiative, GraphQL Foundation, OpenJS, CNCF, OpenSSF, SPDX and OCI.
Tools are harvested from each specification's own governing GitHub organisation and its canonical
tooling registry, then verified live against the GitHub API. A repository that does not resolve,
or that is archived, is not published.
