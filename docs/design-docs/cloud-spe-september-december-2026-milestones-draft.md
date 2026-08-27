# Draft Cloud SPE Milestones: September–December 2026

**Status:** Draft — blocked on end-state architecture decision and joint approval

**Date:** 25 August 2026

**Period:** 1 September–31 December 2026

**Owner:** Cloud SPE

**Drafting work:** `netspe-vun.2`

**Blocking decision:** `netspe-vun.12` — confirm the Live Runner-centric
end-state architecture

**Resolved scope decision:** `netspe-vun.7` — the Build Track has no demand-
generation or application-adoption requirements

**Required approvals:** Network Engineering SPE (`netspe-vun.4`) and Cloud SPE
(`netspe-vun.5`)

## Purpose

This document proposes a small set of high-level milestones for the Cloud SPE's
contribution to the Network Engineering SPE Build Track. It is intended to
support scope, sequencing, funding, and review discussions while the cone of
uncertainty remains high.

This is not an approved Cloud SPE product specification. It does not assign
work to another Network Engineering SPE participant, commit a production
repository owner, or turn an upstream working draft into a Cloud SPE
obligation. The proposal cannot be agreed until `netspe-vun.12` confirms the
Live Runner-centric end-state architecture. It becomes final only after that
decision and the resolved scope decision in `netspe-vun.7` are incorporated,
the Network Engineering SPE and Cloud SPE approve the same revision, and the
accepted plan is published through `netspe-vun.6`.

## Resolved scope

Earlier working drafts contained conflicting application-adoption and live-
demand conditions. Those dated drafts remain available as provenance in the
[normalized source](../references/NetworkEngieneerSPE2-Notes-v2.md) and
[earlier outcome analysis](../references/Build-Track-Outcome-and-High-Level-Concepts.md),
but they do not define the current Build Track scope.

Mike Zupper reported on 26 August 2026 that the scope was confirmed with Rich
on 25 August 2026: the Build Track has no demand-generation or application-
adoption requirements. Decision `netspe-vun.7` records that application counts,
application recruitment or operation, traffic generation, and live-demand
evidence are not Build Track or Cloud SPE deliverables or acceptance gates. The
conflicting draft language remains cited above for provenance only.

## Planning approach

The milestones are outcome gates rather than feature lists. They describe the
state the Build Track needs from the Cloud SPE contribution while leaving room
to change architecture, repository assignments, funding mechanisms, and
implementation order as evidence improves.

The number of tasks under a milestone is determined by the distinct outcomes
needed to complete that gate, not by a fixed template count. These task lists
remain intentionally high level: each item describes a reviewable deliverable
or evidence state. Repository-level implementation tasks, sequencing, and work
status belong in Beads after the relevant scope and architecture decisions are
approved.

Each gate should eventually name:

- the Cloud-owned deliverable and accountable owner;
- affected repositories and supported deployed environments;
- external dependencies, owners, and required handoffs;
- observable completion evidence;
- capacity and budget assumptions; and
- unresolved decisions and the date by which they must be made.

## Proposed high-level milestones

| Window | Milestone | Outcome state | Indicative evidence |
| --- | --- | --- | --- |
| September | **Cloud SPE delivery boundary and target builder journey agreed** | The supported builder journey, Cloud-owned surfaces, repository boundaries, external dependencies, acceptance evidence, and budget assumptions are explicit enough to authorize delivery. | Jointly reviewed scope map; named owners and handoffs; agreed payment paths and representative capabilities; unresolved items have owners and decision dates. |
| September–October | **A supported paid-call journey works end to end** | For at least one representative capability, a builder can obtain the required credential, discover and price the service, invoke it through a supported interface, receive a result or understandable failure, and complete each confirmed required payment journey. | Reproducible production-oriented calls through each required payment path; payment evidence; exact deployed versions; documented ownership of any manual or external step. |
| October–November | **The supported builder experience is consistent and observable** | A reusable Live Runner service contract presents a coherent experience for discovery, pricing, invocation, errors, usage, and resulting charges, with enough correlation to explain an individual job. | Contract-conformance evidence; representative end-to-end evidence; an agreed correlation approach; usable cost and usage records; known exceptions documented rather than hidden. |
| November–December | **The deployed experience is documented and independently proven** | Published SDK guidance and documentation match the deployed system, and an independent builder can reproduce the supported journey from a clean environment without contacting an Operator. | Timed independent first call; documentation and SDK verification; production payment and usage evidence; operational handoff; unresolved limitations stated. |

### Milestone 1: Agree Builder Architecture and Scope

**Estimated:** September 2026

**Working budget:** TBD — no allocation should be proposed until architecture,
ownership, capacity, and delivery boundaries are decided.

- Approve the Live Runner-centric target architecture and retain batch AI,
  BYOC, LV2V, and transcoding as explicit non-goals for this scope.
- Map each of the seven builder outcomes to its authoritative component,
  repository, interface, owner, and required evidence.
- Confirm with Rich, Rick, and Josh whether December acceptance requires a
  reusable Live Runner service contract proven through at least one
  representative capability, a prescribed capability set, or one fixed
  integration; record the representative capability and any required list.
- Confirm the working assumption that both wallet-funded and walletless payment
  journeys are required, then assign the Cloud-owned boundary, external
  dependencies, interface convergence, and minimum evidence for each.
- Select the target clearinghouse direction and define the supported credential,
  walletless payment, balance, metering, usage, and charge boundaries.
- Define the on-chain ServiceRegistry, runtime capability and price discovery,
  gateway selection, and failover responsibilities.
- Confirm the roles and boundaries of Agent 2.0, the builder-facing SDK or
  gateway, Live Runner, `go-livepeer`, and any hosted services.
- Record Cloud-owned deliverables, external dependencies and handoffs,
  repository approvers, decision owners, delivery assumptions, and budget
  inputs.
- Obtain Network Engineering SPE and Cloud SPE approval of the same milestone
  plan revision before implementation commitments are treated as final.

### Milestone 2: Deliver Paid Live Runner Call

**Estimated:** September–October 2026

**Working budget:** TBD — allocate after Milestone 1 establishes the Cloud-owned
repositories, external dependencies, and supported payment path or paths.

- Enable a builder to obtain one supported credential through the agreed
  self-service boundary.
- Expose a supported way to discover the representative Live Runner capability
  and the information required to invoke it.
- Present an understandable expected price or rate before invocation, using the
  agreed authoritative pricing source.
- Invoke the representative capability through the agreed standard
  builder-facing interface and return a result or an understandable failure.
- Complete the representative call through each payment journey confirmed in
  Milestone 1, including a walletless journey that does not require the builder
  to hold crypto.
- Make the builder's usage and resulting charge available through the agreed
  interface or record.
- Correlate credential, request, execution, payment, usage, and charge evidence
  sufficiently to explain one end-to-end call.
- Record the exact deployed versions, external steps, owner handoffs, and known
  limitations required to reproduce the journey.

### Milestone 3: Unify Discovery Pricing and Evidence

**Estimated:** October–November 2026

**Working budget:** TBD — refine after end-to-end evidence identifies the
integration, reliability, and observability work actually required.

- Apply the agreed capability, discovery, price, invocation, and payment
  contracts to the representative Live Runner capability and define how any
  additional supported capability conforms without creating a parallel
  identity, discovery, payment, or metering stack.
- Define stable request, job, execution, payment, and billing identifiers that
  allow an individual invocation to be traced across component boundaries.
- Standardize builder-understandable validation, capacity, execution, payment,
  and settlement failures for supported interfaces.
- Make usage quantities, rates, and resulting charges consistent enough for a
  builder and operator to reconcile the same invocation.
- Validate orchestrator discovery, eligibility, selection, health, and failover
  behavior against the approved ServiceRegistry and runtime-discovery split.
- Establish production-oriented observability and evidence retention for the
  supported journey without making unrelated programme operations a Cloud SPE
  obligation.
- Document supported behavior, declared exceptions, external dependencies, and
  any residual manual steps rather than masking them as completed automation.

### Milestone 4: Prove Independent Builder Journey

**Estimated:** November–December 2026

**Working budget:** TBD — finalize after earlier milestones establish the
documentation, release, operational-handoff, and validation effort.

- Publish builder guidance for credential acquisition, capability discovery,
  expected pricing, invocation, failures, walletless payment, usage, and
  resulting charges.
- Verify that supported SDKs, examples, schemas, endpoints, and documentation
  match the deployed versions and agreed architecture.
- Have an independent builder reproduce the supported paid Live Runner journey
  from a clean environment without contacting an Operator.
- Capture timed first-call evidence, result or understandable-failure evidence,
  payment evidence, and reconcilable usage and charge records.
- Complete the agreed release and operational handoffs, including named owners
  for supported services, repositories, incidents, and documentation.
- State known limitations, unsupported capabilities, external dependencies, and
  unresolved follow-up work explicitly.
- Obtain final Network Engineering SPE and Cloud SPE acceptance against the
  approved scope and evidence gates, distinct from the Milestone 1 approval
  that authorized the plan.

These four gates do not require the Build Track or Cloud SPE to build, fund,
recruit, or operate applications, generate application traffic, or provide
live-demand evidence. This is a resolved scope boundary recorded in
`netspe-vun.7`, not a pending milestone option.

The windows indicate sequencing, not fixed implementation deadlines. Reviewers
may combine, split, or reorder gates without changing the intended progression:
agree the contract, connect the path, make it coherent, and prove it works.

## Application-adoption exclusion

The Agent-plus-applications conditions in the working source drafts are not
part of the Build Track. No application count, application recruitment or
operation, demand generation, traffic threshold, or live-demand evidence may
be used as a milestone deliverable or definition of done. This exclusion does
not prevent sample or reference applications, runnable examples, or controlled
technical integrations from demonstrating how to use the supported Build Track
interfaces. Those artifacts are documentation and validation aids; they create
no application-adoption, production-demand, traffic-volume, funding, or ongoing
application-operation requirement. The source language is retained for
provenance, not endorsement.

## Repository and system boundaries to confirm

The current traceability report identifies the following systems on or near the
builder journey. Inclusion here indicates a possible interface or dependency,
not confirmed Cloud SPE ownership:

| System or repository | Possible relevance to the milestones | Boundary requiring confirmation |
| --- | --- | --- |
| `livepeer/clearinghouse` | Credential, walletless payment, balance, usage, and metering surfaces | Confirm the target clearinghouse, deployed version, self-service boundary, and Cloud SPE ownership. |
| `livepeer/livepeer-python-gateway` | Builder-facing gateway SDK and remote-signer integration | Confirm supported capability types, public interfaces, documentation scope, and release responsibility. |
| `livepeer/go-livepeer` | Gateway, orchestrator, job, ticket, signer, and network payment behavior | Confirm which changes are Cloud deliverables and which require upstream ownership and review. |
| SDK Service in `simple-infra` | The service currently called by the Livepeer Agent for capability routing | Confirm whether it is in scope, who owns it, and which deployed code must be reviewed. |
| Livepeer Agent | Possible reference builder integration | The Agent framework is funded separately; any technical integration must not create an application-adoption or demand-generation requirement. |
| Operate Track registry and discovery surfaces | Capability, hardware, pricing, and supply discovery | Treat as a cross-track contract and handoff, not implied Cloud SPE ownership. |

These boundaries should be re-verified against current repositories and
deployments before implementation work is funded or accepted.

## Prerequisite decision and review questions

Decision `netspe-vun.7` is resolved: application adoption and demand generation
are excluded from the Build Track. Decision `netspe-vun.12` must now map the
seven builder outcomes to an agreed Live Runner-centric architecture,
repositories, owners, and evidence before either SPE review begins. The
[survey and workshop process](../references/Build-Track-Architecture-Alignment-Process.md)
defines the preparation for the architecture decision.

After that decision is incorporated, the joint reviews need to resolve the
remaining questions before the plan can be accepted:

1. Does Rich confirm that both wallet-funded and walletless journeys are
   required December acceptance paths, and which portions of each are Cloud SPE
   deliverables, external dependencies, or compatibility obligations?
2. Which repositories, deployed services, and interfaces are within the Cloud
   SPE scope?
3. Which discovery and capability-contract work belongs to the Operate Track or
   another owner?
4. What evidence qualifies a paid call, an independent builder, and successful
   completion of each milestone?
5. Which external owners, delivery dates, capacity assumptions, and budget
   allocations are required for the plan to remain credible?

## Review and approval

After `netspe-vun.12` is resolved, Network Engineering SPE approval must confirm
that the proposal reflects the accepted architecture and the application-
adoption exclusion, supports the authoritative Build Track outcome, and
represents programme and cross-track dependencies correctly. Cloud SPE approval
must then confirm that the scope boundaries do not create an implicit Cloud
obligation and that Cloud-owned deliverables, repositories, evidence, capacity,
and budget assumptions are realistic commitments.

Approval state and requested changes are tracked in Beads rather than copied
into a competing Markdown status list:

- `netspe-vun.7` — resolved application-adoption scope decision;
- `netspe-vun.12` — prerequisite Live Runner-centric architecture decision;
- `netspe-vun.4` — Network Engineering SPE review and approval;
- `netspe-vun.5` — Cloud SPE review and approval; and
- `netspe-vun.6` — publication of the jointly approved product specification.

The application-adoption prerequisite is satisfied through `netspe-vun.7`;
both approval beads remain blocked by `netspe-vun.12`. Their approval records
must identify the same reviewed revision and confirm that it reflects the
resolved exclusion and accepted architecture. A review that requests unresolved
changes is not sign-off. The final plan should preserve the draft and its source
history while linking the accepted specification to the decisions and both
approval records.

## Change history

| Date | State | Change |
| --- | --- | --- |
| 25 August 2026 | Draft | Initial four-gate proposal prepared for Network Engineering SPE and Cloud SPE review. |
| 25 August 2026 | Revised draft | Made the application-adoption scope decision an explicit prerequisite and excluded the disputed condition from proposed milestones pending that decision. |
| 26 August 2026 | Revised draft | Added the Live Runner-centric end-state architecture decision and two-part survey/workshop process as approval prerequisites. |
| 26 August 2026 | Revised draft | Expanded the four milestone gates into estimated windows, unallocated working budgets, and scope-driven lists of outcome-oriented deliverables. |
| 26 August 2026 | Revised draft | Recorded the confirmed exclusion of demand generation and application adoption from the Build Track, removed it from Milestone 1, and cleared `netspe-vun.7` as a blocker. |
| 27 August 2026 | Revised draft | Removed superseded demand and application-count details from active planning text while preserving the dated upstream drafts as clearly marked historical evidence. |
| 27 August 2026 | Revised draft | Recorded both wallet-funded and walletless payment journeys as a working assumption pending Rich's confirmation, with ownership and minimum evidence to be decided before milestone approval. |
| 27 August 2026 | Revised draft | Proposed a reusable Live Runner service contract proven with at least one representative capability, pending confirmation from Rich, Rick, and Josh. |
