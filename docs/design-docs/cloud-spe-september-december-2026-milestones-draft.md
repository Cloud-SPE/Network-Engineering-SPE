# Draft Cloud SPE Milestones: September–December 2026

**Status:** Draft — blocked on application-adoption scope decision

**Date:** 25 August 2026

**Period:** 1 September–31 December 2026

**Owner:** Cloud SPE

**Drafting work:** `netspe-vun.2`

**Blocking decision:** `netspe-vun.7` — determine whether live-demand
application adoption belongs in the Build Track

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
obligation. The proposal cannot be agreed until `netspe-vun.7` resolves the
disputed application-adoption condition. It becomes final only after that
decision is incorporated, the Network Engineering SPE and Cloud SPE approve the
same revision, and the accepted plan is published through `netspe-vun.6`.

## Source outcome and disputed condition

The latest normalized Network Engineering SPE II source draft describes the
Build outcome as a developer going from a clean machine to a working, paid call
using published documentation and without contacting an Operator. It says both
the wallet-default and pymthouse payment paths work, and that the Livepeer Agent
and at least two further applications send live demand through the network
rather than test traffic. See the
[source draft](../references/NetworkEngieneerSPE2-Notes-v2.md#four-new-tracks-to-focus-work).

The earlier Build Track working document instead says the Livepeer Agent plus
four additional demand sources generate real, attributable traffic through the
clearinghouse. See the
[earlier outcome draft](../references/Build-Track-Outcome-and-High-Level-Concepts.md#intended-outcome).
The difference is not limited to the number of applications. The source also
says that the SPE does not fund the Agent framework or demand generation, and
its detailed Build milestone list does not include delivering applications or
generating demand. Whether application adoption belongs in the Build Track at
all is therefore disputed.

Decision `netspe-vun.7` must determine whether this condition is a Build Track
deliverable, externally supplied validation evidence, limited integration or
onboarding work, or work owned entirely by another programme. Until that
decision is recorded, this proposal excludes the application-adoption condition
from its milestones and does not use either application count as a Cloud SPE
commitment or acceptance gate.

## Planning approach

The milestones are outcome gates rather than feature lists. They describe the
state the Build Track needs from the Cloud SPE contribution while leaving room
to change architecture, repository assignments, funding mechanisms, and
implementation order as evidence improves.

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
| September–October | **A supported paid-call journey works end to end** | For at least one representative capability, a builder can obtain the required credential, discover and price the service, invoke it through a supported interface, receive a result or understandable failure, and pay through the agreed path. | Reproducible production-oriented calls; payment evidence; exact deployed versions; documented ownership of any manual or external step. |
| October–November | **The supported builder experience is consistent and observable** | Supported service types present a coherent experience for discovery, pricing, invocation, errors, usage, and resulting charges, with enough correlation to explain an individual job. | Representative cross-service evidence; an agreed correlation approach; usable cost and usage records; known exceptions documented rather than hidden. |
| November–December | **The deployed experience is documented and independently proven** | Published SDK guidance and documentation match the deployed system, and an independent builder can reproduce the supported journey from a clean environment without contacting an Operator. | Timed independent first call; documentation and SDK verification; production payment and usage evidence; operational handoff; unresolved limitations stated. |

These four gates intentionally do not require the Cloud SPE to build, fund,
recruit, operate, or generate traffic for the Livepeer Agent or additional
applications. Any such obligation may be added only if `netspe-vun.7` assigns it
explicitly and the resulting scope, budget, ownership, and evidence changes are
approved.

The windows indicate sequencing, not fixed implementation deadlines. Reviewers
may combine, split, or reorder gates without changing the intended progression:
agree the contract, connect the path, make it coherent, and prove it works.

## Disputed application-adoption condition

The latest source draft includes an Agent-plus-two-applications condition, but
whether it belongs to the Build Track is unresolved. It must not be treated as
a Build Track or Cloud SPE definition of done merely because it appears in the
working draft. The prerequisite decision must distinguish:

- Cloud SPE responsibility for enabling, integrating, documenting, or
  evidencing a reusable builder platform;
- another programme's responsibility for recruiting, funding, and operating
  applications that produce live demand; and
- the minimum traffic, duration, fee, and identity evidence needed to
  distinguish live use from tests or demonstrations.

Until that decision is approved and incorporated, application adoption and live
demand remain outside the proposed milestones. The source language is retained
here for provenance, not endorsement.

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
| Livepeer Agent | Reference builder integration and possible adoption evidence | The Agent framework is funded separately; confirm integration and evidence responsibilities only. |
| Operate Track registry and discovery surfaces | Capability, hardware, pricing, and supply discovery | Treat as a cross-track contract and handoff, not implied Cloud SPE ownership. |

These boundaries should be re-verified against current repositories and
deployments before implementation work is funded or accepted.

## Prerequisite decision and review questions

Decision `netspe-vun.7` must be resolved before either SPE review begins. It
must identify whether application adoption belongs in the Build Track, the
accountable programme and owners, any resulting Cloud SPE responsibility, and
the definitions and evidence required for any retained application condition.

After that decision is incorporated, the joint reviews need to resolve the
remaining questions before the plan can be accepted:

1. Which portions of the wallet-default and pymthouse paths are Cloud SPE
   deliverables?
2. Which repositories, deployed services, and interfaces are within the Cloud
   SPE scope?
3. Which discovery and capability-contract work belongs to the Operate Track or
   another owner?
4. What evidence qualifies a paid call, an independent builder, and successful
   completion of each milestone?
5. Which external owners, delivery dates, capacity assumptions, and budget
   allocations are required for the plan to remain credible?

## Review and approval

After `netspe-vun.7` is resolved, Network Engineering SPE approval must confirm
that the proposal reflects that decision, supports the authoritative Build
Track outcome, and represents programme and cross-track dependencies correctly.
Cloud SPE approval must then confirm that the decision is represented without
creating an implicit Cloud obligation and that Cloud-owned deliverables,
repositories, evidence, capacity, and budget assumptions are realistic
commitments.

Approval state and requested changes are tracked in Beads rather than copied
into a competing Markdown status list:

- `netspe-vun.7` — prerequisite application-adoption scope decision;
- `netspe-vun.4` — Network Engineering SPE review and approval;
- `netspe-vun.5` — Cloud SPE review and approval; and
- `netspe-vun.6` — publication of the jointly approved product specification.

Both approval beads are blocked by `netspe-vun.7`. Their approval records must
identify the same reviewed revision and confirm that it reflects the
prerequisite decision. A review that requests unresolved changes is not
sign-off. The final plan should preserve the draft and its source history while
linking the accepted specification to the decision and both approval records.

## Change history

| Date | State | Change |
| --- | --- | --- |
| 25 August 2026 | Draft | Initial four-gate proposal prepared for Network Engineering SPE and Cloud SPE review. |
| 25 August 2026 | Revised draft | Made the application-adoption scope decision an explicit prerequisite and excluded the disputed condition from proposed milestones pending that decision. |
