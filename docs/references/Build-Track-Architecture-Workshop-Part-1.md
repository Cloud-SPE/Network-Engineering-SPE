# Build Track Architecture Workshop Part 1: Outcomes and Target Architecture

**Status:** Draft facilitator guide

**Prepared:** 26 August 2026

**Duration:** 60 minutes

**Agenda blocks:** 15 minutes, 15 minutes, and 30 minutes

**Facilitator:** Mike Zupper

**Execution bead:** `netspe-vun.10`

## Suggested calendar title

> Build Track Workshop — Part 1: Builder Outcomes and Target Architecture

## Suggested calendar description

> This is the first of two decision-oriented Build Track architecture sessions.
> We will align on the seven builder outcomes and Live Runner execution scope,
> correct the current-state component model, and develop candidate end-state
> architecture and ownership boundaries.
>
> This meeting does not approve final milestones. It produces the architecture
> options, factual follow-ups, and decision packet required for Part 2.
>
> Please complete the 10–15 minute survey and review the linked current-state
> diagram before attending.

Include links to:

- [the survey](Build-Track-Architecture-Survey.md);
- [survey synthesis when available](Build-Track-Architecture-Survey.md#survey-synthesis-template);
- [current-state diagram](Build-Track-Repo-Traceability.md#component-diagram);
- [draft milestone proposal](../design-docs/cloud-spe-september-december-2026-milestones-draft.md); and
- [the complete alignment process](Build-Track-Architecture-Alignment-Process.md).

## Participants

Core participants:

- Mike Zupper — facilitator and Build Track/Cloud SPE representative;
- Rick Staa — Foundation technical gate and `go-livepeer` review perspective;
  and
- Josh Allmann — Livepeer Inc architect/technical lead and Live Runner/Operate
  Track perspective.

Invite a specialist only when their presence is needed to correct facts that
cannot responsibly wait for a follow-up. Large participant lists make it harder
to distinguish technical input from decision authority.

## Roles to assign before the meeting

| Role | Responsibility |
| --- | --- |
| Facilitator | Maintains scope, asks the decision questions, and prevents implementation detail from consuming architecture time |
| Timekeeper | Enforces the 15/15/30 minute structure and moves unresolved detail into follow-up |
| Diagram editor | Marks corrections, missing components, disputed lines, and target alternatives in real time |
| Decision recorder | Classifies statements as fact, assumption, proposal, decision, escalation, or out of scope |

One person may hold more than one role, but the recorder and diagram editor
should be identified before the meeting begins.

## Objectives

By the end of Part 1, participants should have:

1. A shared interpretation of the seven builder outcomes.
2. Confirmed Live Runner as the proposed execution focus and identified any
   objections or constraints.
3. Confirmed that batch AI, BYOC, LV2V, and transcoding are proposed non-goals.
4. Corrected the current-state component diagram and identified unverified
   systems or deployments.
5. Classified Agent 2.0, SDK Service, SDKs, gateway, ServiceRegistry,
   clearinghouse candidates, Orchestrator, and Live Runner as permanent,
   transitional, replace, outside target, or unresolved.
6. Produced one or more viable end-state architecture options.
7. Identified decisions that Rick, Josh, and Mike can make versus decisions
   that require another owner or committee.
8. Assigned factual verification and optional specialist sessions required
   before Part 2.

## Non-objectives

Part 1 should not:

- approve the final Cloud SPE milestones;
- choose detailed implementation tasks or estimate individual pull requests;
- expand the execution scope beyond Live Runner without an explicit escalation;
- treat survey responses as votes;
- reopen demand generation or application adoption as Build Track requirements;
- select a clearinghouse without understanding the relationship between hosted
  Pymthouse and `livepeer/clearinghouse`; or
- declare capabilities or prices on-chain simply because an on-chain
  ServiceRegistry already exists.

## Required pre-work

Participants should complete before the meeting:

- the [10–15 minute survey](Build-Track-Architecture-Survey.md);
- review of the seven builder outcomes;
- review of the current-state component diagram;
- identification of incorrect components, missing repositories, and deployed
  services not represented in the diagram; and
- identification of decisions they can approve and decisions requiring another
  person or team.

The facilitator should prepare:

- a survey synthesis that highlights disagreements and unknowns;
- a copy of the current-state diagram that can be edited live;
- a blank target-architecture canvas;
- the outcome-to-component matrix;
- a decision and escalation log; and
- a visible parking lot for implementation details and specialist follow-ups.

## Agenda

| Duration | Topic | Required output |
| ---: | --- | --- |
| 15 minutes | Builder outcomes, scope, and survey disagreements | Shared outcome interpretation, proposed scope and non-goals, prioritized disagreements |
| 15 minutes | Current-state architecture validation | Corrected components, paths, repositories, deployments, and factual unknowns |
| 30 minutes | Candidate target architecture and component boundaries | One or more viable end-state options, component classifications, decisions and follow-ups for Part 2 |

## Block 1 — builder outcomes, scope, and survey disagreements

**Duration:** 15 minutes

### Opening frame

Use this framing:

> The purpose of this process is to determine which end-state architecture can
> satisfy all seven builder outcomes through a Live Runner-focused execution
> path. We are separating current facts, target choices, repository ownership,
> and programme approval so the milestones can later become clear requirements.

### Confirm the builder outcomes

Display the outcomes and ask whether each is a December platform outcome,
external dependency, or disputed programme outcome:

1. Obtain one credential.
2. Discover what the network can do.
3. Understand the expected price or rate.
4. Invoke a capability through a standard interface.
5. Receive a result or understandable failure.
6. Pay without holding crypto.
7. See usage and resulting charge.

### Confirm proposed scope

Ask for explicit agreement, objection, or escalation on:

- Live Runner as the execution focus;
- batch AI as a non-goal;
- BYOC as a non-goal;
- LV2V as a non-goal; and
- transcoding as a non-goal.

Clarify that Agent 2.0, SDKs, gateway, clearinghouse, registry, discovery, and
metering remain in scope as supporting components even though other execution
paths are excluded.

### Review survey divergence

Discuss only the highest-impact differences:

- primary builder-facing interface;
- Agent 2.0's intended role;
- gateway and SDK Service permanence;
- on-chain versus runtime registry responsibilities;
- Orchestrator selection owner;
- clearinghouse relationship and likely direction; and
- missing decision authority.

### Exit criteria

This block is complete when:

- objections to the seven outcomes are recorded;
- scope and non-goals are confirmed or escalated;
- the most important architecture disagreements are visible; and
- demand generation and application adoption remain excluded under the resolved
  decision in `netspe-vun.7`.

## Block 2 — current-state architecture validation

**Duration:** 15 minutes

### Facilitation method

Walk the current-state diagram from the builder inward. Do not attempt to solve
the target design during this block. Mark each component or connection as:

- confirmed current behavior;
- incorrect;
- incomplete;
- deployed version unknown;
- repository relationship unknown; or
- outside the proposed target scope.

### Components that must be reviewed

#### Builder-facing and application layer

- Agent 2.0/Storyboard;
- Agent MCP, CLI, REST, capability registry, price estimate, error model, job
  record, usage event, and cost report;
- SDK or other supported developer interfaces; and
- published documentation and credential acquisition.

#### Routing and gateway layer

- SDK Service in `simple-infra`;
- Python gateway SDK;
- `go-livepeer` gateway;
- any hosted routing or discovery service; and
- which component currently selects an Orchestrator.

#### Registry and execution layer

- on-chain ServiceRegistry and the information it actually stores;
- gateway discovery sources;
- runtime `GetOrchestrator` response;
- Orchestrator-local Live Runner registration;
- Live Runner proxy and invocation; and
- current capability, price, health, and capacity flows.

#### Identity, payment, and evidence layer

- Elite Encoder's hosted Pymthouse;
- `livepeer/clearinghouse`;
- the relationship between those two, if known;
- remote signer and wallet path;
- Kafka or other usage events;
- OpenMeter or alternative metering; and
- ticket redemption and on-chain fee evidence.

### Required factual questions

- Which codebase and deployed revision power hosted Pymthouse?
- Is `livepeer/clearinghouse` used by Pymthouse, related by fork, an alternative,
  or unrelated?
- Which branch and version of `go-livepeer` are deployed on the relevant path?
- Is SDK Service intended to remain?
- Which current endpoint is used for Live Runner discovery and invocation?
- Which current system is authoritative for capability identifiers and price?
- Which current system issues the credential used for a successful call?
- Where does an end-to-end job identifier stop propagating?

### Exit criteria

This block is complete when:

- diagram corrections are captured;
- target-scope exclusions are visually distinct;
- unreviewed or unknown deployments have verification owners; and
- current behavior is not presented as a target decision.

## Block 3 — candidate target architecture and component boundaries

**Duration:** 30 minutes

### Architecture sequence

Build candidate designs by answering the seven outcomes in order:

1. What does the builder use and who issues the credential?
2. Which component presents the builder-facing capability catalog?
3. Where does the authoritative expected price originate?
4. Which standard interface invokes a Live Runner capability?
5. Which component returns or normalizes result and failure state?
6. Which clearinghouse or signer contract provides walletless payment?
7. Which identifier and evidence join usage to the resulting charge?

### Builder surface and Agent 2.0

Questions:

- Is Agent 2.0 the canonical builder interface, a reference integration, one
  application, or transitional?
- Should the Agent remain responsible for catalog, price estimate, error
  normalization, and cost report?
- Should it instead consume canonical gateway or clearinghouse interfaces?
- Is the Agent allowed to use application-specific metadata while the platform
  owns stable capability, price, job, and payment contracts?
- Does Agent 2.0 continue calling SDK Service or a `go-livepeer` gateway?

### ServiceRegistry, discovery, and gateway

Questions:

- What remains on-chain: identity, URI, capabilities, versions, prices, or
  something else?
- What remains dynamic: capacity, health, current price, availability?
- How does Live Runner registration at an Orchestrator become discoverable to a
  gateway or builder?
- Which component enumerates, filters, selects, retries, and fails over among
  Orchestrators?
- If gateway discovery is removed, which named component replaces each of
  those functions?
- Does the gateway expose an aggregated catalog or only perform routing?
- Who owns the canonical capability schema and versioning policy?

### Clearinghouse and payment

Questions:

- Is “clearinghouse” a generic contract or a named implementation in the target
  architecture?
- What facts are still required to compare hosted Pymthouse and
  `livepeer/clearinghouse`?
- Should one implementation be selected, should both implement a shared
  contract, or is a new implementation justified?
- Can wallet and walletless paths converge after authorization?
- Which component supplies the expected price, balance decision, payment
  authorization, usage record, and per-job charge?

### Component classification template

| Component | Current role | Target classification | Target responsibility | Repository/owner | Unknown or follow-up |
| --- | --- | --- | --- | --- | --- |
| Agent 2.0/Storyboard |  |  |  |  |  |
| SDK Service |  |  |  |  |  |
| SDK |  |  |  |  |  |
| `go-livepeer` gateway |  |  |  |  |  |
| On-chain ServiceRegistry |  |  |  |  |  |
| Runtime discovery |  |  |  |  |  |
| Orchestrator |  |  |  |  |  |
| Live Runner registry |  |  |  |  |  |
| Live Runner execution |  |  |  |  |  |
| Hosted Pymthouse |  |  |  |  |  |
| `livepeer/clearinghouse` |  |  |  |  |  |
| New clearinghouse |  |  |  |  |  |
| Metering and receipt system |  |  |  |  |  |

Target classifications are **retain**, **change**, **replace**, **transitional**,
**out of scope**, or **unresolved**.

### Exit criteria

Part 1 is successful when:

- at least one coherent target architecture can be drawn;
- competing alternatives are explicit rather than blended;
- each architecture can be traced through all seven outcomes;
- components are provisionally classified;
- clearinghouse and registry/discovery unknowns are assigned;
- decision authority is known or escalated; and
- the work required before Part 2 has owners and dates.

## Optional specialist sessions

Activate only sessions required to eliminate a Part 2 blocker. Each is 30
minutes and uses two 15-minute blocks.

### Clearinghouse specialist session

| Duration | Topic |
| ---: | --- |
| 15 minutes | Hosted Pymthouse codebase, deployment, ownership, and supported contracts |
| 15 minutes | Relationship to `livepeer/clearinghouse`, requirement gaps, and candidate direction |

### Registry and discovery specialist session

| Duration | Topic |
| ---: | --- |
| 15 minutes | On-chain ServiceRegistry, Orchestrator advertisement, and dynamic information |
| 15 minutes | Gateway discovery, selection, failover, Live Runner registration, and builder catalog |

### Agent 2.0 integration specialist session

| Duration | Topic |
| ---: | --- |
| 15 minutes | Agent, SDK Service, credential, catalog, price, and invocation responsibilities |
| 15 minutes | Job identity, errors, usage, charges, and intended end-state role |

## Decision and escalation log

| Topic | Classification | Statement | Authority | Evidence | Owner | Due date |
| --- | --- | --- | --- | --- | --- | --- |
| Scope and non-goals |  |  |  |  |  |  |
| Agent 2.0 role |  |  |  |  |  |  |
| Gateway role |  |  |  |  |  |  |
| ServiceRegistry role |  |  |  |  |  |  |
| Dynamic discovery |  |  |  |  |  |  |
| Clearinghouse relationship |  |  |  |  |  |  |
| Clearinghouse direction |  |  |  |  |  |  |
| Outcome ownership |  |  |  |  |  |  |

## Part 1 output package

Prepare and distribute before Part 2:

- meeting attendance and represented authority;
- survey synthesis;
- corrected current-state diagram;
- target architecture alternatives;
- component classification;
- decision and escalation log;
- factual corrections with cited evidence;
- specialist-session findings;
- outcome-to-component draft;
- repository and owner gaps; and
- explicit questions to decide in Part 2.

Work state and follow-up dependencies belong in Beads. The meeting document may
record decisions and evidence, but it must not become a parallel task tracker.
