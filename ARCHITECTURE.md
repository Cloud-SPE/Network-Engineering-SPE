# Repository Architecture

## Purpose

This is the Cloud SPE's coordination and evidence repository for its
participation in the wider Network Engineering SPE, not a monolithic application
or a programme-wide tracker. Its job is to make the Cloud SPE's assigned tasks,
deliverables, decisions, dependencies, handoffs, and acceptance evidence
legible.

The wider Network Engineering SPE and other participating members retain their
own sources of truth. Production behavior remains authoritative in the
repositories and deployed systems that implement the Livepeer Agent,
clearinghouse, gateways, SDKs, network nodes, runners, Explorer, and related
services.

## Information architecture

```text
AGENTS.md                 concise agent map and operating rules
README.md                 human entry point
ARCHITECTURE.md           repository boundaries and knowledge model
CONTRIBUTING.md           contribution and authorship policy
docs/
├── index.md              documentation catalog
├── design-docs/          durable principles and approved designs
├── product-specs/        outcome and acceptance contracts
├── decisions/            accepted decisions and their rationale
├── references/           evidence, source notes, and working drafts
└── QUALITY.md            review findings and scaffold health
.beads/                   durable work graph and project memory
scripts/check_docs.py     local documentation validation
.github/workflows/        automated feedback loops
```

## Source-of-truth hierarchy

When documents disagree, use this order:

1. Deployed behavior and reproducible evidence establish what is true now.
2. Accepted Cloud SPE decision records establish choices and ownership within
   this workstream.
3. Cloud SPE product specifications establish its intended deliverables and
   acceptance evidence.
4. Cloud SPE design documents establish durable implementation constraints.
5. Files under `docs/references/` provide inputs and historical evidence; their
   claims must be re-verified before they drive a decision or payout.
6. Beads records work state, dependencies, discoveries, and handoffs.

The hierarchy separates facts, intent, and work state. A draft does not become
approved merely because another document links to it.

## Delivery model

The Cloud SPE's portion of the work can span independently deployed
repositories. This repository should map only the contracts, dependencies, and
acceptance evidence needed for Cloud SPE deliverables without copying
implementation details that will immediately drift. A delivery bead should link
to the relevant specification or decision and name the external repository,
owner, acceptance evidence, and dependencies.

Use Beads for execution plans and dependency ordering. Do not create Markdown
roadmaps, TODO files, or status checklists that compete with the work graph.

## Feedback loops

- `python3 scripts/check_docs.py` checks required knowledge-map files, one H1 per
  Markdown document, and local Markdown links.
- `python3 scripts/check_attribution.py --all-history` rejects co-author
  messages in commit history; CI also checks pull-request titles and bodies.
- CI runs both policies for relevant pull requests and pushes.
- Technical claims in references should carry a review date, repository commit,
  and reproducible evidence where practical.
- When a documented rule repeatedly fails, promote it to an automated check.

## Boundaries

This repository should not contain programme-wide status presented as if owned
by the Cloud SPE, work assigned to other participants, secrets, production
credentials, copied service source code, or an invented canonical API that has
not been accepted by the owning projects. Sensitive operational details belong
in an approved secret store; implementation changes belong in their service
repositories.
