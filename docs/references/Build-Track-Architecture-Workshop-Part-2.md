# Build Track Architecture Workshop Part 2: Decisions and Requirements

**Status:** Draft facilitator guide

**Prepared:** 26 August 2026

**Duration:** 60 minutes

**Agenda blocks:** Four 15-minute blocks

**Facilitator:** Mike Zupper

**Execution bead:** `netspe-vun.11`

**Resulting decision:** `netspe-vun.12`

## Suggested calendar title

> Build Track Workshop — Part 2: Architecture Decisions and Milestone Requirements

## Suggested calendar description

> This is the second Build Track architecture session. We will use the survey,
> Part 1 outputs, and specialist findings to confirm or escalate the end-state
> architecture, map all seven builder outcomes to authoritative components and
> repositories, establish ownership and approval gates, and translate the
> architecture into milestone requirements and acceptance evidence.
>
> Please review the decision packet before attending. Part 2 is not a replay of
> Part 1 and will not spend meeting time rediscovering facts assigned for
> follow-up.

Include links to:

- [the complete process](Build-Track-Architecture-Alignment-Process.md);
- [Part 1 facilitator guide and output requirements](Build-Track-Architecture-Workshop-Part-1.md#part-1-output-package);
- the completed Part 1 output package when available;
- [the draft milestone proposal](../design-docs/cloud-spe-september-december-2026-milestones-draft.md); and
- any specialist findings or architecture alternatives included in the
  decision packet.

## Scheduling criteria

Part 2 should have a tentative calendar hold before Part 1. Confirm the meeting
when:

- the survey synthesis is complete;
- Part 1 has produced at least one coherent target architecture;
- assigned factual corrections are complete or explicitly escalated;
- required clearinghouse, registry/discovery, or Agent specialist sessions are
  complete;
- the relationship between hosted Pymthouse and `livepeer/clearinghouse` is
  verified or presented as a decision-blocking unknown;
- architecture alternatives are documented consistently; and
- attendees with decision authority are available.

If a critical fact or authority is missing, reschedule Part 2 rather than using
silence to force a decision. The reason, owner, and new target date belong in
Beads.

## Participants

Required participants:

- Mike Zupper;
- Rick Staa; and
- Josh Allmann.

Add a specialist or authority when Part 1 shows their participation is required
to decide a specific agenda item. Invitations should state the decision for
which their authority is required.

## Roles

| Role | Responsibility |
| --- | --- |
| Facilitator | Presents alternatives, asks for explicit disposition, and protects the 15-minute blocks |
| Timekeeper | Moves unresolved detail into an escalation with owner and date |
| Architecture recorder | Updates the selected diagram and records rejected alternatives |
| Requirements recorder | Converts accepted architecture statements into outcome-linked requirements and evidence |
| Decision authority | States acceptance, conditional acceptance, or escalation within their authority |

## Objectives

By the end of Part 2, the group should have:

1. Selected or explicitly escalated a Live Runner-centric target architecture.
2. Decided the intended roles of Agent 2.0, SDK, SDK Service, and gateway.
3. Decided what belongs in the on-chain ServiceRegistry and what remains
   dynamic.
4. Assigned Orchestrator discovery, capability/price retrieval, selection,
   retry, and failover responsibilities.
5. Selected a clearinghouse direction or approved a time-boxed evaluation with
   decision authority and date.
6. Mapped all seven builder outcomes to interfaces, components, repositories,
   owners, and evidence.
7. Confirmed repository approvers and deployment responsibilities.
8. Produced milestone-level requirements without prematurely decomposing them
   into implementation tasks.
9. Identified all remaining prerequisites for `netspe-vun.12`,
   `netspe-vun.4`, and `netspe-vun.5`.

## Non-objectives

Part 2 should not:

- design batch AI, BYOC, LV2V, or transcoding paths;
- select implementation details that do not affect an interface, owner,
  dependency, or acceptance criterion;
- declare a new clearinghouse necessary without an unmet requirement and
  evaluation of existing options;
- conflate the on-chain ServiceRegistry, runtime Orchestrator discovery, and
  local Live Runner registration;
- treat Agent 2.0-specific behavior as canonical without an accepted contract;
- reopen demand generation or application adoption as Build Track requirements;
  or
- approve the final Cloud SPE milestones in place of the separate Network
  Engineering SPE and Cloud SPE gates.

## Required decision packet

The facilitator distributes the packet before the meeting. It should contain:

- the seven builder outcomes and agreed scope guardrails;
- respondent and authority coverage;
- survey agreement/disagreement synthesis;
- corrected current-state diagram;
- candidate target architecture diagrams;
- differences, benefits, risks, and unresolved assumptions for each option;
- component classification;
- hosted Pymthouse and `livepeer/clearinghouse` relationship findings;
- clearinghouse alternatives against a common requirement set;
- ServiceRegistry and discovery alternatives;
- Agent 2.0, SDK Service, SDK, and gateway role alternatives;
- outcome-to-component draft;
- repository, owner, approver, and deployment map;
- decision and escalation log from Part 1;
- recommended decisions; and
- draft milestone impacts.

Every technical fact should identify its source and review date. Every
recommendation should identify who has authority to accept it.

## Agenda

| Duration | Topic | Required output |
| ---: | --- | --- |
| 15 minutes | Confirm architecture decisions | Selected architecture or explicit escalations and constraints |
| 15 minutes | Map seven outcomes to authoritative components | Complete outcome-to-interface, component, repository, owner, and evidence matrix |
| 15 minutes | Confirm repository ownership and approval gates | Named owners, implementers, approvers, deployment owners, and cross-track dependencies |
| 15 minutes | Translate architecture into milestone requirements | Revised high-level milestones, requirements, acceptance evidence, and remaining prerequisites |

## Block 1 — confirm architecture decisions

**Duration:** 15 minutes

### Decision rule

Present no more than the viable alternatives produced by Part 1. For each
decision, record one of:

- accepted;
- accepted with named constraint;
- rejected with reason;
- escalated to named authority by a date; or
- deferred because a named fact is unavailable by a date.

“Continue discussing” is not a disposition.

### Required architecture decisions

#### Builder-facing path

- What is the standard builder interface?
- Is Agent 2.0 canonical, a reference integration, one application, or
  transitional?
- Does SDK Service remain?
- Does a supported SDK or gateway API define the platform contract?

#### Live Runner path

- Does December acceptance require a reusable service contract proven with one
  representative capability, a prescribed capability set, or one fixed
  integration?
- Have Rich, Rick, and Josh each confirmed the outcome, architecture, and
  delivery interpretation respectively?
- What makes a capability “supported,” and must it satisfy the complete
  confirmed builder journey?
- How does a Live Runner register with an Orchestrator?
- Which capability identity and version contract is advertised?
- How does a builder invocation reach the selected Live Runner?
- Which job identity crosses builder, gateway, Orchestrator, Live Runner,
  payment, and metering?

#### Registry and discovery

- What information remains on-chain?
- What information is obtained dynamically?
- Which component enumerates eligible Orchestrators?
- Which component filters, selects, retries, and fails over?
- Which component presents capabilities and prices to the builder?

#### Clearinghouse and payment

- Are both wallet-funded and walletless journeys required Build Track
  acceptance paths, or is either path an external compatibility dependency?
- Who owns each required journey and what minimum observable evidence proves
  it without prematurely specifying settlement mechanics?
- Is the target hosted Pymthouse, `livepeer/clearinghouse`, both through a
  common contract, a justified new implementation, or an escalation?
- What common credential, authorization, signer, usage, and receipt contract is
  required?
- How do wallet and walletless paths converge with the Live Runner execution
  path?

### Architecture decision table

| Decision | Disposition | Selected direction | Constraint or rejected alternative | Authority | Follow-up |
| --- | --- | --- | --- | --- | --- |
| Builder-facing interface |  |  |  |  |  |
| Agent 2.0 role |  |  |  |  |  |
| SDK Service role |  |  |  |  |  |
| Gateway role |  |  |  |  |  |
| On-chain ServiceRegistry |  |  |  |  |  |
| Runtime discovery |  |  |  |  |  |
| Live Runner registration |  |  |  |  |  |
| Live Runner capability support model |  |  |  |  |  |
| Payment-path scope and ownership |  |  |  |  |  |
| Clearinghouse direction |  |  |  |  |  |
| Walletless payment contract |  |  |  |  |  |
| Job identity and evidence |  |  |  |  |  |

### Exit criteria

This block is complete when each required choice has a disposition, authority,
and follow-up. An escalation is acceptable; an unnamed ambiguity is not.

## Block 2 — map seven outcomes to authoritative components

**Duration:** 15 minutes

Complete one row per builder outcome:

| Outcome | Builder-facing interface | Authoritative component | Repository/service | Owner | External dependency | Observable evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Obtain one credential |  |  |  |  |  |  |
| Discover what the network can do |  |  |  |  |  |  |
| Understand expected price or rate |  |  |  |  |  |  |
| Invoke through a standard interface |  |  |  |  |  |  |
| Receive result or understandable failure |  |  |  |  |  |  |
| Pay without holding crypto |  |  |  |  |  |  |
| See usage and resulting charge |  |  |  |  |  |  |

### Questions for every outcome

- What exact interface does the builder observe?
- Which component is authoritative rather than merely displaying a projection?
- Which repository or deployed service implements it?
- Who owns the interface contract?
- Who owns production operation?
- Which external dependency can prevent the outcome?
- What observable fact proves completion?
- Does the evidence demonstrate a Live Runner call rather than an excluded
  execution path?

### Coherence checks

Before leaving the block, verify:

- one credential is accepted across required builder steps or the exchange is
  invisible and documented;
- the discovered capability identity matches the invoked capability;
- the quoted price can be related to the resulting charge;
- the error model can state whether payment occurred;
- the same job identity can join invocation, result, usage, and payment; and
- every required payment journey has a named owner, boundary, and minimum
  acceptance evidence; and
- walletless payment results in verifiable network payment evidence.

## Block 3 — confirm repository ownership and approval gates

**Duration:** 15 minutes

Complete the ownership matrix:

| Component or contract | Repository/service | Technical owner | Implementer | Merge approver | Release/deployment owner | Track/SPE boundary | External dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agent 2.0 integration |  |  |  |  |  |  |  |
| SDK or builder API |  |  |  |  |  |  |  |
| Gateway routing |  |  |  |  |  |  |  |
| Capability schema |  |  |  |  |  |  |  |
| On-chain ServiceRegistry |  |  |  |  |  |  |  |
| Runtime discovery and selection |  |  |  |  |  |  |  |
| Live Runner registration |  |  |  |  |  |  |  |
| Live Runner invocation |  |  |  |  |  |  |  |
| Clearinghouse interface |  |  |  |  |  |  |  |
| Hosted Pymthouse |  |  |  |  |  |  |  |
| `livepeer/clearinghouse` |  |  |  |  |  |  |  |
| Signer and network payment |  |  |  |  |  |  |  |
| Metering, usage, and receipt |  |  |  |  |  |  |  |

### Required ownership distinctions

Do not collapse these roles into “owner”:

- contract authority;
- repository maintainer;
- implementation contributor;
- merge approver;
- release approver;
- deployment operator;
- programme or SPE funding authority; and
- completion-evidence reviewer.

### Exit criteria

This block is complete when every milestone-critical component has a named
owner or a named escalation, and the Cloud SPE boundary is explicit.

## Block 4 — translate architecture into milestone requirements

**Duration:** 15 minutes

Use the existing four high-level gates as a starting hypothesis:

1. Live Runner architecture and ownership agreed.
2. A supported Live Runner paid-call journey works end to end.
3. Live Runner discovery, pricing, payment, and job evidence are coherent.
4. The deployed Live Runner builder journey is independently reproducible.

Reviewers may combine, split, reorder, or reject them. Do not preserve wording
that conflicts with the accepted architecture.

### Requirement template

| Field | Required content |
| --- | --- |
| Requirement ID | Stable identifier assigned after review |
| Builder outcome | One or more of the seven outcomes |
| Requirement | Observable “shall” statement without prescribing unnecessary implementation detail |
| Authoritative component | System responsible for satisfying the requirement |
| Repository and owner | Implementation location and accountable owner |
| External dependency | Named system, owner, and required date |
| Acceptance evidence | Reproducible observation, deployed version, job/payment identifier, or approval record |
| Non-goal | Related work explicitly excluded |
| Decision source | Architecture or programme decision authorizing the requirement |

### Milestone review table

| Proposed milestone | Architecture dependency | Cloud-owned result | External dependency | Evidence gate | Timing confidence | Required revision |
| --- | --- | --- | --- | --- | --- | --- |
| Architecture and ownership |  |  |  |  |  |  |
| Paid Live Runner call |  |  |  |  |  |  |
| Coherent discovery, price, payment, and evidence |  |  |  |  |  |  |
| Independent reproduction |  |  |  |  |  |  |

Timing confidence should be **high**, **medium**, or **low**, with the underlying
assumption. The cone of uncertainty should be explicit rather than hidden by
false precision.

### Required final checks

- Every milestone advances one or more builder outcomes.
- No milestone relies on batch AI, BYOC, LV2V, or transcoding for acceptance.
- No milestone includes demand generation, application adoption, application
  counts, traffic targets, or live-demand evidence as acceptance requirements.
- Clearinghouse work names the selected implementation or contract and owner.
- Registry and discovery work distinguishes on-chain and dynamic behavior.
- Agent 2.0 work is integration-scoped unless broader ownership is approved.
- Repository gates and external dependencies have names and dates.
- Evidence describes a deployed Live Runner path.

## Meeting output and circulation

Within two business days, circulate:

- attendance and represented authority;
- accepted target architecture or escalation record;
- updated architecture diagram;
- architecture decision table;
- outcome-to-component matrix;
- ownership and approval matrix;
- clearinghouse and discovery decisions;
- proposed requirements;
- revised milestone table;
- unresolved escalations with owners and dates; and
- implications for `netspe-vun.12`, `netspe-vun.4`, and `netspe-vun.5`, while
  preserving the resolved scope boundary in `netspe-vun.7`.

Recipients should distinguish factual corrections from decision objections.
All architecture acceptance must identify the approving authority and reviewed
revision. Work state and follow-up tasks belong in Beads, not an accumulating
Markdown action list.

## Part 2 completion evidence

Part 2 is complete when:

- every architecture decision has a disposition;
- all seven outcomes are mapped;
- critical repositories and approval gates are named;
- milestone requirements follow the architecture;
- non-goals remain explicit;
- remaining escalations have authorities and dates; and
- the output package is sufficient for an authoritative decision under
  `netspe-vun.12`.
