# tools.apievangelist.com

Open source tooling for the specifications that describe, secure and ship APIs — published as
structured data an AI agent can resolve against, not as a directory of names.

The pages are a rendering of the data. The data is the product:

| Artifact | What it is |
|---|---|
| [`/tools.json`](https://tools.apievangelist.com/tools.json) | Every tool: license, specification bindings, agent block, use cases |
| [`/roles.json`](https://tools.apievangelist.com/roles.json) | The controlled vocabulary — what a tool does *to* a specification |
| [`/tool.schema.json`](https://tools.apievangelist.com/tool.schema.json) | The JSON Schema every entry conforms to |
| [`/llms.txt`](https://tools.apievangelist.com/llms.txt) | How to resolve from an artifact to a tool |
| [`/reference/`](https://tools.apievangelist.com/reference/) | The long version, including what the numbers don't mean |

## The rules

**Nothing is published that was not read.** Every repository is resolved live against the GitHub
API. Licenses come from the repository — from the API, or from the LICENSE file directly when
GitHub's detector fails. A repo that 404s or is archived does not ship, and
`validate_spec_tools.py` fails the build rather than letting one through.

**Install coordinates are verified against the registry**, or omitted. An agent that runs a
hallucinated install command burns a turn and loses trust.

**`companyCount` is a demand signal, not a deployment count** — companies whose job postings name
the tool. Comparable only within a quarter.

**Three licensing states, kept distinct**: OSI-approved (`openSource: true`), source-available
(`openSource: false` — BUSL, Elastic), and no license file at all (`license: null`, which is not
permissive).

## Pipeline

Hand-authored inputs are `scripts/spec-tools.yml` (which tools implement which specification, in
what role) and `scripts/tool-profiles.yml` (titles, descriptions, agent blocks, use cases).
Everything else is generated.

```bash
# 1. resolve every referenced repo against the GitHub API (cached)
python3 scripts/gh_meta.py <repos.txt>
python3 scripts/gh_orgs.py asyncapi sigstore …    # rank a spec's governing org, to pick from
python3 scripts/resolve_licenses.py               # read LICENSE where GitHub says NOASSERTION

# 2. THE GATE — unresolvable repo, archived project, unknown role or bad standard slug fails here
python3 scripts/validate_spec_tools.py

# 3. write _store entries (preserves companyCount, radarRing, tags, alternativeNames)
python3 scripts/build_store.py --dry
python3 scripts/build_store.py

# 4. the two-way link: standards/_data/spec_tools.yml + local _data/spec_index.yml
python3 scripts/link_standards.py

# 5. build and validate the published data against its own schema
bundle exec jekyll build --destination /tmp/toolsite
python3 -c "import json,jsonschema; s=json.load(open('tool.schema.json')); \
  d=json.load(open('/tmp/toolsite/tools.json')); V=jsonschema.Draft202012Validator(s); \
  bad=[t['slug'] for t in d['tools'] if list(V.iter_errors(t))]; \
  print(f'{len(d[\"tools\"])} entries, {len(bad)} invalid', bad[:5])"
```

## Adoption counts

`companyCount` comes from the API Evangelist job corpus in `insights-work`, not from here. To
refresh it for a new quarter, follow `insights-work/Q3-PIPELINE.md` §2–3, then re-run
`build_store.py`.

**Read `insights-work/_data/insights/ambiguity-report.json` before publishing new counts.** It
lists every term matched only on a bare one-word needle, which is how a tool ends up credited for
an ordinary English word — `ats` for Apache Traffic Server matching "Applicant Tracking System",
`operators` for Kubernetes Operators matching "furnace operators". High single-only counts are a
prompt to go sample the matched text, not proof on their own.

## Where the tools come from

The specification inventory is `research/linux-foundation/standards.md`. Tools are harvested from
each specification's own governing GitHub organisation and its canonical tooling registry
(openapi.tools, json-schema.org's tooling data, the AsyncAPI directory), then curated to the ones
that carry the ecosystem — 5–8 per specification. Where an ecosystem genuinely is thin, it is left
thin. A short list is a finding, not a gap to pad.
