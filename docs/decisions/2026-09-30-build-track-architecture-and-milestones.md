# Build Track Architecture and Milestone Acceptance

**Status:** Accepted\
**Effective:** 30 September 2026\
**Recorded:** 1 October 2026\
**Delivery owner and decision recorder:** Mike Zupper

## Context and evidence

Mike circulated the final architecture and executive summary to the Network
Engineering SPE, Livepeer Inc and the Livepeer Agent team for review from
27–30 September. He reports no feedback or objections during that window.
On 30 September he notified the Discord groups that development would proceed,
with the first deliverable on 16 October, treating the absence of objections as
agreement. Mike corrected an earlier report of 1 October to 30 September.

Mike separately reports sending the milestones to the NE-SPE committee on
28 September, Eastern time. Rick said he was good with the plans; other members
were silent or gave thumbs-up reactions. Mike accepts these responses as
committee signoff and explicitly accepts the delivery plan as its owner.

This record relies on Mike's account and instructions in the internal planning
conversation. Discord messages were not independently retrieved. It records the
no-objection approval process, not affirmative written responses from every
stakeholder or proof that every recipient read the documents.

## Decision

The [architecture and executive summary](../design-docs/self-sovereign-open-builder-stack-draft.md),
[technical companion](../design-docs/open-builder-architecture-and-sequences.md),
[supporting capability inventory](../design-docs/console-capability-and-gap-matrix.md),
and [M1–M5 delivery plan](../design-docs/build-track-december-2026-task-breakdown-draft.md)
are the accepted implementation baseline. The
[delivery issue mapping](../design-docs/build-track-december-2026-issue-proposal-draft.md)
defines task acceptance and dependencies. The
[accepted specification](../product-specs/build-track-2026.md) indexes the contract.

The repository snapshot preceding this acceptance-documentation update is
`a3ce4313a01ef1b558a89b73a7d845ee281ef94b`. It preserves the document set and the
29 September addition of M1. The exact revision originally sent on Discord was
not supplied; this snapshot identifies the current accepted set, not a claim
about the revision circulated on 28 September.

Remaining implementation decisions are resolved as their milestones require.
Late feedback will be considered, with changes to scope, dates or acceptance
recorded explicitly. The earlier requirement for individual affirmative
architecture and milestone approvals is superseded by this recorded process.

## Alternatives and consequences

Waiting for individual written responses was not selected. Mike chose to proceed
following the completed review window and committee responses. Architecture
acceptance does not establish runtime compatibility, grant source reuse rights,
commit upstream maintainers to new work, or assign an ongoing hosted service.

The required scope remains all seven builder outcomes, SQLite persistence,
shared package and service interfaces, and the minimum reference application.
PostgreSQL, additional streaming, hard spending guarantees and a complete Console
port remain stretch scope. Demand generation, application adoption and production
retail commerce remain outside the delivery baseline.

[GitHub Project 13](https://github.com/orgs/Cloud-SPE/projects/13) tracks public
milestones for ecosystem transparency. Beads tracks Mike's internal tasks,
dependencies and follow-up work. Project draft-item type and historical `-draft`
filenames do not change the accepted status of the linked documents.

## Review and change history

- 30 September 2026: approval effective following the review process described above.
- 1 October 2026: Mike confirmed the final document set and M1–M5 plan; this record
  documents that acceptance. Remaining decisions are handled during milestone execution.
