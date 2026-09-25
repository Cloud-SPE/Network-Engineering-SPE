# Cloud SPE — Network Engineering SPE Workstream

[![Documentation](https://github.com/Cloud-SPE/Network-Engineering-SPE/actions/workflows/docs.yml/badge.svg)](https://github.com/Cloud-SPE/Network-Engineering-SPE/actions/workflows/docs.yml)
[![License](https://img.shields.io/github/license/Cloud-SPE/Network-Engineering-SPE)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/commits/main)
[![Open issues](https://img.shields.io/github/issues/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues)
[![Open pull requests](https://img.shields.io/github/issues-pr/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/pulls)
[![Contributors](https://img.shields.io/github/contributors/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/graphs/contributors)
[![Repository size](https://img.shields.io/github/repo-size/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE)
[![Stars](https://img.shields.io/github/stars/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/stargazers)
[![Forks](https://img.shields.io/github/forks/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/forks)
[![Watchers](https://img.shields.io/github/watchers/Cloud-SPE/Network-Engineering-SPE)](https://github.com/Cloud-SPE/Network-Engineering-SPE/watchers)
[![Work tracking: Beads](https://img.shields.io/badge/work%20tracking-Beads-5c4ee5)](https://github.com/gastownhall/beads)
[![Status: working repository](https://img.shields.io/badge/status-working%20repository-f59e0b)](#project-status)

This repository is the Cloud SPE's focused work ledger for its participation in
the wider Network Engineering Special Purpose Entity (SPE). It documents and
tracks the tasks, deliverables, evidence, dependencies, and handoffs owned by or
assigned to the Cloud SPE.

> **Scope boundary:** the Cloud SPE is one participating member of the Network
> Engineering SPE. This repository is not the source of truth for the Network
> Engineering SPE as a whole, its other members, or work owned by other tracks.

The production systems touched by Cloud SPE deliverables remain in their
respective Livepeer repositories and deployment environments.

## Motivation

The wider Network Engineering SPE coordinates work across several participants,
systems, and tracks. The Cloud SPE needs a narrow, durable place to make its own
commitments legible: what it agreed to deliver, why the work matters, which
external decisions it depends on, and what evidence demonstrates completion.

The current Cloud SPE material is most developed around the builder journey,
where identity, capability discovery, pricing, invocation, payment, metering,
settlement, and support cross multiple repositories. Within its assigned
portion of that work, the Cloud SPE contributes toward a journey in which a
developer, application, or agent can:

1. obtain one ordinary credential;
2. discover available network capabilities and usable supply;
3. understand a price, estimate, or bounded rate before execution;
4. invoke a capability through a stable interface;
5. receive a result or an actionable failure;
6. pay without managing a crypto wallet; and
7. inspect usage and the resulting charge.

The wider programme's intended outcome is broader than shipping individual
services. This repository narrows that outcome to the Cloud SPE deliverables
that help produce and verify real, attributable network usage. Programme-wide
targets remain context and dependencies unless explicitly assigned to the Cloud
SPE.

## Project status

The current review package is Mike Zupper's
[open builder-engine proposal](docs/design-docs/self-sovereign-open-builder-stack-draft.md),
with [technical diagrams](docs/design-docs/open-builder-architecture-and-sequences.md)
and a [capability/evidence matrix](docs/design-docs/console-capability-and-gap-matrix.md).
It proposes reusable packages and HTTP/MCP services, a reference application,
and enterprise extensions that leave the shared core unchanged.

The 24 September stakeholder meeting established conceptual alignment on this
shared foundation and the separation of network costs from enterprise billing.
Detailed architecture approval, upstream contracts, hosted-payment operation,
representative capability acceptance, and long-term maintenance remain open.
The repository has no accepted product specification or architecture decision
record yet. Demand generation and application adoption are excluded from this
workstream's delivery requirements.

The [quality review](docs/QUALITY.md) distinguishes current proposal gaps from
historical findings. August repository observations remain dated evidence, not
claims about today's Agent or payment deployment. Work state and dependencies
are maintained in Beads.

## Cloud SPE scope

This repository should contain only work that the Cloud SPE owns, has accepted,
or must track as a direct dependency of its deliverables. The current working
surface may include Cloud SPE contributions to:

- builder identity and credentials;
- capability discovery and invocation;
- walletless payment through the clearinghouse;
- usage, cost, and attribution visibility;
- SDKs, interface documentation, and integration support; and
- evidence that the builder journey works across supported capabilities.

This repository does **not** own or represent:

- the complete Network Engineering SPE roadmap, status, governance, or budget;
- deliverables assigned to other participating members or track owners;
- the authoritative status of every Build, Operate, Delegate, or Validate task;
- the Livepeer Agent framework, general marketing, protocol design, or unrelated
  operator tooling; or
- implementation history that belongs in a production service repository.

External work may be recorded as a dependency or handoff when it directly
blocks a Cloud SPE deliverable, but its owner and external source of truth must
remain explicit.

## Components and source references

The [architecture component map](docs/design-docs/self-sovereign-open-builder-stack-draft.md#components-repositories-and-ownership)
identifies proposed deliverables and dependencies: a new builder-engine
repository, reference application, Python gateway SDK, `go-livepeer` and
`clearinghouse-batteries`. Existing maintainers retain upstream ownership.

The [repository roles section](docs/design-docs/self-sovereign-open-builder-stack-draft.md#repositories-and-application-roles)
separately identifies the Console prototype as reference material and
`livepeer/simple-infra` as closed-source Inc material awaiting access and review.
Neither is a required runtime dependency of the proposed engine. Earlier
Storyboard and `livepeer/clearinghouse` mappings remain in historical references;
they do not define the current proposal or establish current deployed behavior.

## Repository structure

```text
AGENTS.md                 concise instructions and navigation for agents
ARCHITECTURE.md           information model and source-of-truth boundaries
CONTRIBUTING.md           contribution and attribution policy
docs/
├── index.md              documentation catalog
├── design-docs/          durable principles and accepted designs
├── product-specs/        approved outcomes and acceptance contracts
├── decisions/            accepted decisions and rationale
├── references/           chronological index and categorized working evidence
│   ├── source-material/  upstream and historical source evidence
│   ├── stakeholder-input/ meeting findings and survey responses
│   ├── analysis/         scope, traceability, and architecture synthesis
│   └── facilitation/     surveys, workshops, and meeting guides
└── QUALITY.md            repository and Cloud SPE delivery-readiness review
.beads/                   durable issue graph and project memory
scripts/                  dependency-free repository validation
.github/workflows/        automated documentation and policy checks
```

Read [ARCHITECTURE.md](ARCHITECTURE.md) for the complete information hierarchy
and [docs/index.md](docs/index.md) for the knowledge map.

## Knowledge conventions

This repository deliberately separates four kinds of information:

| Kind | Location | Meaning |
| --- | --- | --- |
| Evidence and source material | [`docs/references/index.md`](docs/references/index.md) | Chronologically indexed observations, inputs, and working analyses; not automatically normative |
| Product specifications | `docs/product-specs/` | Approved intended outcomes, scope, and acceptance evidence |
| Designs and decisions | `docs/design-docs/`, `docs/decisions/` | Durable constraints, choices, owners, and rationale |
| Work state | Beads | Tasks, dependencies, blockers, discoveries, progress, and handoffs |

Do not create Markdown TODO lists or parallel roadmap files. Use links instead
of copying large passages between documents, and promote repeated rules into
automated checks when possible.

## Using the repository

### Read the current proposal

Start with:

1. [Architecture and executive summary](docs/design-docs/self-sovereign-open-builder-stack-draft.md)
2. [Technical diagrams and accounting requirements](docs/design-docs/open-builder-architecture-and-sequences.md)
3. [Capability evidence and verification gaps](docs/design-docs/console-capability-and-gap-matrix.md)
4. [Quality review](docs/QUALITY.md)

The [reference index](docs/references/index.md) preserves earlier outcomes,
meeting evidence, surveys, and programme context. Historical plans are inputs
to review rather than additional delivery commitments.

### Work with Beads

Install the `bd` CLI, then use the repository work graph:

```bash
bd prime
bd ready
bd blocked
bd show <issue-id>
bd update <issue-id> --claim
```

Create a bead before making a substantive change. Record newly discovered work
as a linked bead rather than silently expanding the current scope.

### Validate changes

The checks use only Python's standard library:

```bash
python3 scripts/check_docs.py
python3 scripts/check_attribution.py --all-history
git diff --check
```

The documentation check verifies required knowledge-map files, one top-level
heading per Markdown document, and local links. The attribution check rejects
`Co-authored-by` trailers and equivalent co-author messages.

## Contributing

Contributions are welcome when they improve evidence quality, clarify an
approved decision, tighten acceptance criteria, or advance a tracked Cloud SPE
deliverable.

Before opening a pull request:

1. create or claim the relevant Beads issue;
2. identify whether the change is evidence, a proposal, an accepted decision,
   or implementation guidance;
3. cite repository commits, deployed environments, and reproduction steps for
   technical claims;
4. update indexes and cross-links without duplicating source text;
5. run the validation commands above; and
6. explain the outcome and evidence in the pull request.

Do not include `Co-authored-by` trailers or any equivalent co-author attribution
in commits or pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full
workflow and authorship policy.

## Coordination and evidence

Decisions affecting Cloud SPE scope or delivery should be recorded with their
deciders, rationale, alternatives, consequences, and affected Beads issues.
Completion claims should include reproducible evidence at the relevant system
boundary; a local merge in one component is not sufficient proof of an
end-to-end deliverable.

Programme-wide governance remains outside this repository. When a wider SPE
decision affects Cloud SPE work, link to its authoritative record and capture
only the resulting Cloud SPE commitment, dependency, or constraint here.

## License

This repository is available under the [MIT License](LICENSE).
