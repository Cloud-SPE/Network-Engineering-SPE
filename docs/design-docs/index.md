# Design Document Index

Design documents capture durable constraints and cross-system choices for Mike
Zupper's Build Track deliverables. A design is authoritative only within that scope, when its
status is `Accepted` and it links to the decision that approved it.

## Current documents

| Document | Status | Purpose |
| --- | --- | --- |
| [Self-sovereign open builder stack](self-sovereign-open-builder-stack-draft.md) | Accepted; effective 30 September | Executive summary, component/repository ownership, stakeholder alignment, technical scope and acceptance |
| [Builder engine diagrams and sequences](open-builder-architecture-and-sequences.md) | Accepted architecture companion | Components, enterprise integration modes, payment operation, execution and accounting |
| [Capabilities and gap matrix](console-capability-and-gap-matrix.md) | Supporting pinned evidence | Current implementations, new homes and verification gaps |
| [Build Track December delivery task breakdown](build-track-december-2026-task-breakdown-draft.md) | Accepted delivery plan; owner Mike Zupper | Six September planning tasks plus 31 implementation tasks across five milestones, work kinds, blocking dependencies, and separate stretch goals; implementation assignees and task-level dates pending |
| [Build Track December delivery issues](build-track-december-2026-issue-proposal-draft.md) | Accepted delivery mapping; owner Mike Zupper | 45 tasks (six planning and 39 implementation) with milestone, home, acceptance, dependencies, and source-task traceability; six planning repository issues created; implementation homes, assignments, and task-level dates pending |
| [Core beliefs](core-beliefs.md) | Proposed | Agent-first and Cloud SPE delivery principles |
| [September–December milestone proposal](cloud-spe-september-december-2026-milestones-draft.md) | Historical; superseded by accepted M1–M5 plan | Input to later October–December milestone revision |
| [Builder-layer proposal extensions](builder-layer-proposal-extensions.md) | Draft for review | Access, payment credential custody, route changes, Batteries management provisioning and cost-feed delivery, as extensions of the October 1 proposal |
| [simple-infra on the builder engine](simple-infra-builder-migration.md) | Draft for review | Class-level adoption of `BuilderEngine` by the proposal's second application, behind its legacy-route facade |

Intermediate Console-replacement and enterprise deployment drafts were removed
on 23 September after consolidation. Original stakeholder evidence and its chronology remain in the
[reference catalog](../references/index.md); the accepted architecture presents the current direction.
The [approval record](../decisions/2026-09-30-build-track-architecture-and-milestones.md)
and [specification](../product-specs/build-track-2026.md) define the accepted baseline.
Historical `-draft` filenames remain for link stability. GitHub Project 13 tracks
public milestones; Beads tracks internal work.
The proposal extensions draft is review material for access, provisioning and
cost delivery on top of the October 1 builder-layer proposal. Its stories live
in Beads under `netspe-cz5` and `netspe-scr`. No draft becomes accepted by
being linked. Work state remains in Beads.
