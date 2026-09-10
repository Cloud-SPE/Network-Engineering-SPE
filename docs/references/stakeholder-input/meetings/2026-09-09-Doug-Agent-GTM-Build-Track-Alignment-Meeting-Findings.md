# Doug Agent GTM and Build Track Alignment Meeting Findings

**Status:** Evidence-qualified meeting synthesis; inputs to Thursday alignment,
not an approved architecture or milestone plan

**Meeting date:** 9 September 2026

**Prepared:** 9 September 2026

**Participants:** Doug Petkanics and Mike Zupper

**Execution bead:** `netspe-vun.18`

## Sources and purpose

This document consolidates Build Track findings from:

- the [meeting context](../../facilitation/meeting-guides/2026-09-09-Doug-Agent-GTM-Build-Track-Alignment-Meeting-Context.md);
- a participant-provided meeting transcript reviewed locally on 9 September
  and intentionally excluded from version control;
- the [seven builder outcomes](../../analysis/2026-08-27-Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise);
- the [8 September discussion with Rick](2026-09-08-Rick-Build-Track-Survey-Discussion-Consolidated-Notes.md); and
- the [draft September–December milestones](../../../design-docs/cloud-spe-september-december-2026-milestones-draft.md).

Its purpose is to preserve what Doug and Mike aligned on, identify the likely
effect on the Cloud SPE's Build Track contribution, and isolate the decisions
that still require technical owners or joint approval. It does not assign work
to Livepeer Inc, the Foundation, the Operate Track, John Mull, or another
Network Engineering SPE participant.

## Evidence limitations

The supplied transcript is an automated record. It labels Doug primarily as
“Me,” labels Mike as “Mike Zoop,” and contains recognition errors in project
and product names. This synthesis normalizes obvious terminology but does not
treat uncertain wording as an exact quotation.

Doug and Mike described themselves as fully aligned at the strategic level.
That is evidence of participant alignment, not approval by the Network
Engineering SPE, Cloud SPE, Livepeer Foundation, Livepeer Inc, or the owners of
affected repositories. Statements about current software also require
verification against the relevant repository, commit, and deployment.

The classifications used below are:

- **established scope** — already supported by a separate recorded decision;
- **meeting alignment** — Doug and Mike converged on the direction;
- **stated commitment** — a participant described a commitment within their
  area, but the artifact, owner, date, or acceptance evidence may be missing;
- **proposal** — a candidate architecture, responsibility, or delivery;
- **reported current state** — a claim that requires technical verification;
- **unresolved** — the decision, evidence, owner, or authority is missing; and
- **out of Cloud SPE scope** — relevant context owned elsewhere.

## Executive conclusion

Doug and Mike aligned on a separation between a commercial, opinionated Agent
product and an open, reusable network substrate:

- Livepeer Inc intends to build and take a hosted Livepeer Agent product to
  market around agentic media creation.
- The Build Track should make the underlying open network path functional,
  independently deployable, understandable, and documented.
- The open path must not be limited to Livepeer Agent. Other applications and
  demand bets should be able to build and invoke capabilities through the same
  public components and contracts.
- The Build Track enables demand but does not own marketing, application
  adoption, traffic, or demand generation.
- An open Agent MCP or equivalent Agent access point belongs in the documented
  stack, but Agent-specific product development remains with Livepeer Inc.

The discussion makes a plausible December deliverable much clearer: an
independent builder should be able to deploy and use a documented open stack to
discover, price, invoke, and pay for Live Runner-backed capabilities through
wallet-funded and walletless paths. The open Agent is a supported access point
and reference consumer, while the underlying interfaces remain reusable.

The meeting did **not** finalize the repositories, component contracts,
capability set, delivery owners, funding, hosted-service obligations, security
acceptance, or joint definition of done.

## Aligned product and infrastructure boundary

### Commercial Livepeer Agent product

**Classification:** Stated commitment and out of Cloud SPE scope

Doug described Livepeer Inc as committed to a hosted Agent product designed for
the easiest path to agentic media creation. Its commercial experience may
include hosting, an ordinary account or API key, credit-card payment, product
support, reliability enhancements, and an opinionated user journey.

Livepeer Inc owns that product strategy and GTM execution. The Build Track does
not own its customer acquisition, marketing, application adoption, or traffic.
The commercial product can consume and contribute to the open network stack
without defining every public interface around its own application behavior.

The exact Agent product artifact, repository, release, named owner, and
delivery date were not established in this meeting.

### Open network substrate

**Classification:** Meeting alignment

Doug and Mike agreed that the common technical foundation should be open and
extensible. Product teams may operate hosted implementations and add commercial
services around it, but core capability, payment, discovery, metering, and
integration work should not be embedded as proprietary application-only
behavior.

The Build Track's contribution is therefore best framed as stewardship and
integration of a usable builder path. It should answer:

- what each component does;
- how the components connect;
- how a builder deploys or accesses them;
- how capabilities and prices are discovered;
- how work is invoked and paid for;
- how results, failures, usage, and charges are understood; and
- which stable interfaces allow Agent and other applications to coexist.

This responsibility does not give the Cloud SPE authority over repositories or
services owned by other teams. Those boundaries and handoffs must be accepted
by the relevant owners.

## Three access paths

The discussion produced the following three-path model. The paths share core
network components but differ in product opinion, payment abstraction, and
operational control.

| Path | Builder experience | Likely operator | Build Track relevance | Unresolved boundary |
| --- | --- | --- | --- | --- |
| Hosted Agent product | Obtain a hosted credential, add the Agent MCP to a harness, and use an opinionated media-creation experience | Livepeer Inc | Verify compatibility with the open stack; document the open Agent handoff where approved | Product repository, open-source release, handoff date, and commercial/open feature boundary |
| Generic walletless builder access | Obtain an ordinary credential, select raw capabilities, invoke them through a supported SDK or HTTP interface, and see usage and cost without holding crypto | A clearinghouse provider; possibly a temporary evaluation deployment and later a commercial operator | Define and prove the generic walletless journey | Clearinghouse repository, operator, funding, custody, liability, service level, and post-December ownership |
| Fully self-operated access | Run the supported open components and use a builder-controlled, wallet-funded network path | Builder or application operator | Document and prove independent deployment and invocation | Canonical gateway, minimum required components, security model, and support boundary |

The generic walletless path gives the application builder control over the
application and its use of raw capabilities, but it still depends on a third
party for payment abstraction when that service is hosted. It should not be
described as fully self-sovereign in the same sense as the wallet-funded path.

All three paths were treated as valid. The meeting did not decide that the
Cloud SPE must productionize or operate all three. The Build Track must define
which paths it delivers, which it demonstrates, and which it supports only
through an external handoff.

## Role of the open Agent

**Classification:** Meeting alignment on inclusion; unresolved delivery
boundary

The open Agent MCP is now a material part of the Build Track architecture. It
provides an agent-harness access point for a concrete use case and can
demonstrate the same underlying capability, discovery, invocation, and payment
contracts used by other applications.

The existing scope statement that the Build Track does not primarily fund
development of the Agent framework remains useful but is incomplete. A more
precise boundary supported by this meeting is:

> Livepeer Inc owns Agent product strategy and Agent-specific features. Subject
> to an accepted handoff, the Build Track may integrate, harden, package,
> validate, and document the open Agent components required for independent use
> of the public Livepeer stack.

Mike stated willingness to take a substantially complete open-source Agent
artifact and finish the self-hosted integration and documentation. Doug
indicated that he entered the conversation expecting that kind of handoff and
that the Agent should already be open source and presented as a Livepeer
project. This is strong directional alignment, but not yet a scoped delivery
agreement.

Before work is accepted, the handoff must identify:

- the exact repository and revision;
- the Livepeer Inc owner and Build Track recipient;
- which functions are complete and which require Build Track work;
- compatibility with the SDK, clearinghouse, remote signer, and Live Runner;
- release and support expectations;
- security constraints; and
- completion evidence and review authority.

## Capability platform and Operate Track interface

**Classification:** Meeting alignment with an unresolved RACI

The open platform must support both sides of capability use:

1. developers and Orchestrators can introduce and operate capabilities; and
2. applications and agents can discover and invoke those capabilities.

Mike described the Build Track as assembling the ecosystem's components into a
working and documented builder model. Doug agreed and emphasized coordination
with Josh and the Operate Track. The working boundary is:

- the Operate Track provides node-side plumbing for declaring, deploying,
  discovering, pricing, and successfully running capabilities; and
- the Build Track consumes stable interfaces and provides the coherent
  builder-facing journey, integration evidence, and documentation.

The tracks must converge by December for any end-to-end Build Track outcome to
work. Neither track can independently define the other's repository contract.
The exact ownership of registration, catalog projection, pricing, routing,
retry, failover, errors, metering, and release compatibility remains unresolved.

Doug also cautioned that Livepeer Inc must be able to iterate quickly in
response to Agent users without railroading shared network architecture or
breaking other consumers. This creates a requirement for explicit compatibility
contracts and regular coordination with Josh, Rick, and affected repository
owners; it does not authorize the Cloud SPE to control Livepeer Inc's product
roadmap.

## Proposed minimal Open Clearinghouse

**Classification:** Meeting alignment on the need; proposed implementation and
ownership

The discussion reinforced the gap identified in the Rick meeting: the Build
Track needs a small, generic, independently deployable walletless layer rather
than treating a full commercial Payment House product as the open reference
implementation.

The proposed Open Clearinghouse would wrap the necessary remote-signer and
network-payment behavior and provide:

- account or API credential issuance;
- capability and price discovery;
- job submission;
- network-payment abstraction;
- result or understandable-failure handling;
- per-builder and preferably per-job usage records; and
- the resulting charge.

Livepeer Inc could operate its own instance or equivalent payment abstraction
behind Agent Product. BlueClaw or another application could do the same. John
Mull could build a larger commercial Pymthouse/Payment House product above the
common component without making its enterprise integrations mandatory for the
open reference path.

Doug supported the architectural concept but raised a sustainability concern:
a production walletless clearinghouse processes payments, user information,
and potentially custodial value. It therefore needs a motivated operator,
revenue model, security posture, and liability boundary. A Cloud SPE-hosted
instance might serve as an evaluation or transition deployment, but this
meeting did not approve it as a durable public service.

Still to determine:

- whether to create a new repository or simplify `livepeer/clearinghouse`;
- the exact division between clearinghouse and remote signer;
- whether Pymthouse consumes the common layer or remains separate;
- John's accepted Build Track scope;
- the wallet and credit custody model;
- abuse controls, legal responsibilities, and loss limits;
- the evaluation deployment owner and funding; and
- the shutdown, commercial transition, or continued-funding plan.

## Marketing and presentation

**Classification:** Out of Cloud SPE scope with an architectural dependency

Doug prefers Livepeer Agent as the near-term commercial wedge because a
specific media-creation user journey is easier to position than a generic
capability marketplace. Mike argued that the generic toolbox remains necessary
because the same network can support different products and new capabilities.
Both positions were accepted as compatible.

The technical stack should therefore support both the opinionated Agent path
and generic capability access. The question of what `livepeer.org` presents as
the primary entry point belongs to Livepeer Foundation and relevant product or
GTM owners. It should not determine whether the common technical interfaces are
reusable.

Existing applications such as BlueClaw or Frameworks may provide useful
integration evidence. They are not Build Track deliverables, required demand
bets, or traffic targets.

## Effect on the seven builder outcomes

| Outcome | Finding from this meeting | Remaining decision |
| --- | --- | --- |
| Obtain one credential | Required for each supported hosted or walletless journey | Whether one credential spans only one clearinghouse or multiple access paths |
| Discover what the network can do | Must expose generic network capabilities, not only an Agent-specific list | Authoritative catalog, freshness, eligibility, and Operate Track handoff |
| Understand expected price or rate | Required before capability invocation | Price authority, units, validity, and path-specific markup presentation |
| Invoke through a standard interface | SDK, HTTP, gateway, and Agent MCP roles were discussed | Canonical contract and whether Agent MCP and `go-livepeer` gateway are both supported entry points |
| Receive a result or understandable failure | Explicitly reinforced, including cross-track error handling | Error ownership, retry, failover, and compatibility requirements |
| Pay without holding crypto | Required through the hosted Agent or generic clearinghouse path | Provider, custody, credits, funding, and production operating model |
| See usage and resulting charge | Explicitly reinforced for the walletless path | Correlation identifiers, metering authority, storage, and reconciliation evidence |

The meeting also confirmed a wallet-funded path. That path supplements rather
than removes the walletless outcome. “One credential” should mean one ordinary
credential for a selected supported journey, not an unsupported claim that one
credential works across every independently operated service.

## Expected performance, failure, and recourse

**Classification:** Unresolved

Hunter's earlier concern about expected performance and recourse was not
resolved. The conversation treated SLAs, enhanced reliability, support, and
guarantees as likely commercial-product features, while understandable errors
and working failure handling remained part of the open stack.

The Build Track still needs a high-level decision on whether December requires:

- truthful availability or capacity information only;
- defined timeout, retry, and failover behavior;
- expected performance ranges;
- a support or escalation path; or
- financial or operational recourse.

No open-network SLA or financial-recourse obligation should be inferred from
this meeting.

## Agent security constraint

**Classification:** Reported current state and material unresolved risk

Doug reported that recent Agent security findings created a risk that public
patch commits could expose wallet-controlling Agent installations before their
operators upgraded. He said this caused the repository to be closed while the
risk was handled.

This is a direct constraint on an open, self-hosted, wallet-funded Agent path.
It must be verified with the Agent repository owner, then addressed through an
agreed security model covering:

- separation between agent execution and funds;
- wallet permissions and loss limits;
- secret and credential isolation;
- responsible disclosure and embargoed fixes;
- signed releases and supported upgrade behavior;
- security review and incident ownership; and
- the conditions under which the repository and releases can remain public.

The Build Track should not accept an Agent handoff or promise independent
deployment without an explicit security boundary and release process.

## Provisional December outcome

**Classification:** Synthesis proposal requiring joint approval

The meeting supports the following candidate outcome:

> By December, an independent builder can deploy and use a documented open
> Livepeer builder stack to discover, price, invoke, and pay for supported
> Live Runner capabilities through an agreed wallet-funded path and an ordinary-
> credential walletless path. The open Agent MCP is a supported access point and
> reference consumer, while the underlying interfaces remain reusable by other
> applications. The builder can receive an understandable result or failure and
> inspect usage and resulting cost.

Likely evidence includes:

- an accepted component and ownership map;
- a minimal independently deployable clearinghouse or equivalent walletless
  component;
- a supported SDK or HTTP contract;
- remote-signer and Live Runner integration;
- capability and expected-price discovery;
- result and understandable-failure behavior;
- usage and charge correlation;
- a documented wallet-funded journey;
- a documented walletless journey;
- an open Agent MCP integration or explicit handoff boundary; and
- independent reproduction from a clean environment.

The evidence may use a representative application or controlled invocation.
It must not include an application count, production-traffic threshold, demand-
generation target, or ongoing application-operation obligation.

## Decisions still required

| Decision | Why it is required | Candidate authority or evidence source |
| --- | --- | --- |
| Approve the three-path model and identify delivered versus demonstrated paths | Prevents all three paths from silently becoming full Cloud SPE products | Network Engineering SPE and Cloud SPE, informed by Rich and Doug |
| Define Agent Product versus open Agent ownership | Establishes the handoff and prevents product work from becoming unbounded Build Track scope | Livepeer Inc Agent owner, Build Track owner, Rich, and repository approvers |
| Select the canonical builder and gateway contracts | Resolves Agent MCP, SDK, HTTP, `go-livepeer` gateway, and remote-signer overlap | Josh, Rick, Build Track owner, and affected maintainers |
| Accept the Build/Operate RACI | Makes December cross-track dependencies testable | Josh, Build Track owner, Network Engineering SPE |
| Select the Open Clearinghouse repository and owner | Authorizes implementation rather than relying on a conceptual component | Build Track and Cloud SPE, John Mull if assigned, repository owner |
| Approve any hosted clearinghouse deployment | Defines funding, custody, security, support, and post-December operation | Cloud SPE and funding authority; deployment and security owners |
| Define the Agent security release boundary | Determines whether the open self-hosted Agent can safely be delivered | Livepeer Inc security and Agent owners, repository maintainer, Build Track recipient |
| Choose December representative capabilities | Keeps capability proof concrete without creating adoption scope | Build and Operate Tracks with Rich, Rick, and Josh |
| Decide minimum expected-performance and recourse behavior | Prevents commercial SLAs from being confused with open-stack failure behavior | Product, Build, and Operate owners with Hunter's concern considered |
| Approve the final milestone and acceptance revision | Converts this evidence into authorized Cloud SPE work | Network Engineering SPE and Cloud SPE |

## Light-paper dependency

**Classification:** Meeting alignment with a narrow caveat

Doug and Mike did not expect the light paper's incentive and protocol design to
materially change the near-term Build Track software thesis. Doug identified a
possible future touchpoint if payment-protocol or probabilistic-micropayment
changes affect client software. No such implementation was established for the
September–December scope.

The Build Track can continue architecture clarification without waiting for the
entire light paper, while recording any accepted payment or protocol change as
an explicit dependency rather than assuming it will arrive before December.

## Overall assessment

This meeting resolves the strategic concern that the Build Track might have to
choose between Livepeer Agent and a generic builder platform. The aligned
direction is to support a reusable open substrate and treat Agent as an
important, opinionated consumer and access point above it.

The next alignment step should not revisit that strategic premise unless a
decision authority rejects it. It should convert the premise into a bounded
component map, accepted ownership, security constraints, representative
capability evidence, and a December definition of done.
