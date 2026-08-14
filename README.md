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
what role), `scripts/tool-profiles.yml` (titles, descriptions, agent blocks, use cases) and
`scripts/roles.yml` (the vocabulary). Everything else is generated.

**Run the whole thing with one command.** It refreshes, gates, and regenerates in order, and stops
dead on the first failure:

```bash
python3 scripts/build.py            # refresh from GitHub, gate, regenerate everything
python3 scripts/build.py --check    # verify only: no writes, nonzero if stale or invalid
python3 scripts/build.py --offline  # regenerate from the cache as-is, no GitHub calls
```

That is steps 1–4 below. Run them individually only when debugging one of them:

```bash
# 1. RE-READ every referenced repo (list comes from spec-tools.yml — no repos.txt needed)
python3 scripts/gh_meta.py --refresh --prune
python3 scripts/gh_meta.py --stale 14             # or: only records older than N days
python3 scripts/gh_orgs.py asyncapi sigstore …    # rank a spec's governing org, to pick from
python3 scripts/resolve_licenses.py               # read LICENSE where GitHub says NOASSERTION

# 2. render the published vocabulary from roles.yml
python3 scripts/build_roles.py

# 3. THE GATE — unresolvable, archived, forked, unknown vocabulary or drifted roles.json
python3 scripts/validate_spec_tools.py

# 4. write _store entries, then the two-way link into the standards site
python3 scripts/build_store.py --dry && python3 scripts/build_store.py
python3 scripts/link_standards.py

# 5. build and validate the published data against its own schema
bundle exec jekyll build --destination /tmp/toolsite
python3 -c "import json,jsonschema; s=json.load(open('tool.schema.json')); \
  d=json.load(open('/tmp/toolsite/tools.json')); V=jsonschema.Draft202012Validator(s); \
  bad=[t['slug'] for t in d['tools'] if list(V.iter_errors(t))]; \
  print(f'{len(d[\"tools\"])} entries, {len(bad)} invalid', bad[:5])"
```

**Always refresh before publishing.** A cached record is a claim about a live repository and it
decays. The rule that an archived repo does not ship can only be enforced against a record that
has been re-read — a repo archived *after* it was cached stays `archived: false` forever. `stars`
and `lastCommit` go stale the same way. `licenseVerified` on a store entry is the date the facts
were actually read, carried on the cache record; it is not the date the build last ran.

**The store is the UNION of two catalogues**, and `/tools.json` publishes both with a `sources`
array on every entry:

- `specification-catalog` — read live from the GitHub API, licensed, bound to a specification with
  a role. Owned by `spec-tools.yml` + `tool-profiles.yml` via `build_store.py`.
- `demand-corpus` — in the insights tool vocabulary, so it carries a `companyCount` and
  `radarRing`. Owned by `insights-work/_data/tools.yml` via `sync_demand.py`.

Only entries in both can put licensing and adoption in the same sentence. Never assume a field is
present — a demand-corpus entry has no license because nothing was read, and a specification-catalog
entry with no count has not been measured, which is not a measured zero.

`sync_demand.py` reports coverage against the vocabulary on every run and **creates** any store
entry the vocabulary has and the store lacks, so the two cannot silently drift apart.

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
