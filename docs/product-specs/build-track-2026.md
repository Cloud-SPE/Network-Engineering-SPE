# Build Track 2026 Delivery Specification

**Status:** Accepted\
**Owner:** Mike Zupper\
**Approval effective:** 30 September 2026\
**Documentation updated:** 1 October 2026\
**Decision:** [Architecture and milestone acceptance](../decisions/2026-09-30-build-track-architecture-and-milestones.md)

## Outcome and scope

Deliver the shared builder engine and minimum reference application so developers,
applications and agents can obtain access, discover capabilities, understand
prices, invoke work, receive results or actionable failures, pay without managing
a wallet, and inspect usage and network cost. Enterprises integrate their own
identity and commercial features through public interfaces without core changes.

The accepted contract is defined by these linked documents, rather than a second
copy of their requirements:

| Document | Contract |
| --- | --- |
| [Architecture and executive summary](../design-docs/self-sovereign-open-builder-stack-draft.md) | Components, repository roles, Mike's ownership, integration boundaries and seven outcomes |
| [Technical companion](../design-docs/open-builder-architecture-and-sequences.md) | Package/service behavior, persistence, execution and accounting boundaries |
| [Capability inventory](../design-docs/console-capability-and-gap-matrix.md) | Dated source evidence and remaining verification gaps; not proof of implementation |
| [Delivery plan](../design-docs/build-track-december-2026-task-breakdown-draft.md) | M1–M5 dates, required tasks, acceptance gates, upstream dependencies and stretch scope |
| [Delivery issue mapping](../design-docs/build-track-december-2026-issue-proposal-draft.md) | Task-level acceptance, implementation homes and dependencies |

SQLite is required. PostgreSQL, additional streaming, hard spending guarantees
and a full Console port are stretch goals. Production retail commerce, demand
generation, application adoption and an ongoing public hosted service are excluded.
Upstream components remain with their existing owners; integration approval does
not assign them new delivery obligations.

## Delivery and acceptance

The plan runs from September planning through 31 December delivery. M2's first
implementation deliverable is due 16 October. Milestone completion requires the
linked evidence gates; architecture approval is not implementation acceptance.
Unresolved contracts, representative jobs, deployment details and final-release
review arrangements are settled before accepting their dependent work.

[GitHub Project 13](https://github.com/orgs/Cloud-SPE/projects/13) provides public
milestone tracking. Beads is Mike's internal work tracker. Late feedback and plan
changes are assessed during delivery and recorded when they affect this baseline.

## Review and change history

- 30 September 2026: architecture and milestone approval effective under the
  process recorded in the linked decision.
- 1 October 2026: accepted specification published in the repository; existing
  document paths retained to preserve links and Git history.
