# Rick Build Track Survey Discussion — Consolidated Notes

**Status:** Consolidated working evidence; not an approved architecture or milestone plan

**Meeting date:** 8 September 2026

**Meeting time:** 8:30 a.m. America/New_York

**Participants:** Mike Zupper and Rick Staa

**Prepared from source records:** 8 September 2026

**Related work:** `netspe-vun.9`, `netspe-vun.12`, and `netspe-vun.18`

## Purpose

This document consolidates the Build Track discussion that followed Rick
Staa's architecture survey response. It records the strongest working
direction, candidate December deliverables, Cloud SPE implications, external
dependencies, and unresolved decisions without treating the discussion as
programme-wide approval.

The source records were a participant-provided meeting transcript and two
automated meeting-note variants reviewed locally on 8 September. Those raw
records are intentionally excluded from version control; this consolidated
record preserves the Build Track-relevant findings and evidence limitations.

The [meeting agenda](../../facilitation/meeting-guides/2026-09-08-Rick-Build-Track-Survey-Discussion-Agenda.md),
[Rick's survey response](../surveys/2026-09-07-Build-Track-Architecture-Survey-Response-Rick-Staa.md),
and [Rich, Doug, and Hunter feedback](2026-09-02-Rich-Doug-Hunter-Build-Track-Feedback.md)
provide context but are not substitutes for the meeting record.

## Evidence limitations

The transcript has no speaker labels and appears to omit or compress portions
of the exchange. It contains repeated recaps and apparent agreement, but not
every statement can be attributed confidently to Mike or Rick.

The Gemini notes add speaker attribution and label several items as decisions.
They are useful navigation aids, but some of those labels are stronger than the
underlying transcript supports. In particular:

- excluding Storyboard from the proposed Build Track does not prove that the
  owning organization formally deprecated the product;
- a proposal that Cloud SPE host a clearinghouse is not an approved Cloud SPE
  commitment until scope, budget, operations, and acceptance are approved;
- a proposed new clearinghouse architecture is not yet an accepted repository
  or funded delivery assignment; and
- apparent agreement between meeting participants is not Network Engineering
  SPE and Cloud SPE approval.

This consolidation therefore uses these classifications:

- **established scope** — already supported by a separate recorded decision;
- **meeting working alignment** — the discussion appears to converge, but no
  formal approval is inferred;
- **proposal** — a candidate direction or commitment raised in the meeting;
- **reported current state** — a claim requiring repository or deployment
  verification; and
- **unresolved** — evidence, ownership, or authority is missing.

## Executive summary

The meeting converged on a simpler Build Track direction: enable the smallest
usable, open-source path from a builder without crypto expertise to a paid Live
Runner invocation. A builder should be able to obtain an API credential,
discover available capabilities and prices, invoke work through a supported
interface, receive a result or understandable failure, and see usage and cost.

The proposed foundation is:

```text
Open Clearinghouse
        ↓ builder credential, catalog, usage, and cost
Python SDK or supported HTTP interface
        ↓ invocation
Remote Signer
        ↓ discovery and network-payment authorization
Live Runner and eligible Orchestrators
        ↓ execution
Result or understandable failure
```

The three existing architectural pillars discussed were the Python SDK, remote
signer, and Live Runner. The principal missing Build Track component was
described as a simple, generic, self-hostable Open Clearinghouse built around
those pillars. The current Pymthouse/Payment House direction and the contents
of `livepeer/clearinghouse` were not accepted as sufficient merely because they
exist.

The meeting also refined—but did not resolve—Doug's self-sovereign Agent idea.
The working interpretation became an independently operated MCP server or agent
using open Livepeer interfaces, rather than making Agent 2.0/Storyboard the
authoritative platform. Only Doug can confirm whether that interpretation is
correct.

## Scope reaffirmed

### Demand generation remains outside the Build Track

The discussion reaffirmed the established scope decision that the Build Track
does not own demand generation, application adoption, application counts,
traffic targets, or live-demand evidence.

The intended division is:

- the Build Track supplies usable network plumbing, SDK/API access,
  documentation, and evidence;
- a separate demand, credits, go-to-market, or solutions-engineering effort
  finds, funds, and supports builders; and
- independent or commercial companies package capabilities into products,
  workflows, customer support, and service-level offerings.

Requirements from real builders may inform capability selection, but acquiring
those builders is an external input rather than a Build Track acceptance gate.

### Application products remain above the platform boundary

BlueClaw, Flip Suite, Agent 2.0, Storyboard, and other applications were
discussed as examples of consumers or product layers. They are not Build Track
deliverables. Reported BlueClaw usage was offered as market context, not as
Build Track acceptance evidence.

## Architectural direction

### Live Runner as the execution focus

**Classification:** Meeting working alignment

Live Runner was treated as the target execution mechanism for the Build Track.
The Build Track should use capabilities exposed through Live Runner rather
than extend the older Batch AI, BYOC, Storyboard, or application-specific
execution stacks.

Audio transcription, text-to-speech, LLM inference, video-to-video, and other
capabilities were mentioned. The discussion did not approve a December
capability list. Current availability, deployment, price units, and
Orchestrator support must be verified before any capability is named in
acceptance criteria.

The useful high-level direction is:

- select at least one real capability to prove the full builder journey;
- do not turn the representative capability into an adoption obligation; and
- require any capability called supported to conform to the agreed credential,
  discovery, price, invocation, result/failure, payment, usage, and charge
  journey.

Capability implementation and Orchestrator-side operation remain primarily
Operate Track dependencies. The Build Track consumes their supported
interfaces and records the handoff.

### Python SDK as a core builder interface

**Classification:** Meeting working alignment

The conversation treated the Python SDK as a retained architectural pillar and
the likely primary programmatic builder interface. A simple HTTP or cURL path
was also contemplated through the clearinghouse.

The intended experience is that a builder can:

- use one ordinary credential;
- inspect available capabilities and price information;
- submit a Live Runner job;
- receive the result or an understandable failure; and
- correlate the job with its usage and cost.

This narrows the ambiguity in Rick's survey, where both a supported SDK and
“Unknown” were selected. It does not yet define the canonical interface
contract, supported SDK versions, or whether other language SDKs must exist.

### Remote Signer as a critical dependency

**Classification:** Meeting working alignment with reported current-state claims

The remote signer was treated as central to:

- abstracting the network-funded wallet from an ordinary builder;
- authorizing Livepeer network payments;
- discovering eligible Orchestrators;
- exposing current capability and price information; and
- supporting SDK-based invocation.

The Build Track should depend on a stable contract rather than assume that the
current location inside `go-livepeer` will remain permanent. If Josh and the
Operate Track extract or reorganize Live Runner or remote-signer behavior, the
Build Track must follow an agreed interface and release path.

The meeting did not settle whether the remote signer should be only a payment
component, also serve as the canonical discovery aggregator, or delegate some
of that responsibility to another control plane.

### `go-livepeer` and Operate Track boundary

**Classification:** Unresolved boundary with a proposed handoff

The discussion reframed rather than fully resolved the disagreement between
Rick's survey and Josh's response. The Build Track would consume the Python
SDK, remote signer, and Live Runner behavior, while Josh's Operate Track would
own the evolution of the node-side implementation and any move out of
`go-livepeer`.

Still unresolved:

- whether the `go-livepeer` gateway mode is deprecated or remains a permanent
  control-plane component;
- whether selection, routing, retry, and failover belong in each SDK or a
  shared gateway/control plane;
- whether Josh's proposed combined Live Runner and SDK repository is an
  approved plan; and
- which repository and owner provide stable releases to the Build Track.

## Proposed Open Clearinghouse

### Problem being addressed

**Classification:** Meeting working alignment on the gap; implementation
direction remains a proposal

The meeting identified no currently verified, independently deployable
clearinghouse that satisfies the seven builder outcomes with the desired
simplicity.

The current `livepeer/clearinghouse` repository was described as containing
useful examples and integration pieces but not a minimal, usable template.
Pymthouse/Payment House was described as a larger, tightly integrated product
direction that should not automatically define the Build Track architecture.
These are reported assessments and must be verified against the relevant
repositories, deployments, and owners.

### Proposed responsibilities

The Open Clearinghouse would provide:

- self-service account or credential creation;
- one ordinary API credential for the supported journey;
- a builder-facing capability and price view;
- authorization and submission of Live Runner work;
- integration with a remote signer and network payment path;
- per-builder and preferably per-job usage recording;
- calculation or presentation of resulting cost;
- a result or understandable payment or execution failure; and
- a reproducible self-hosted deployment.

The intended builder experience is:

1. Visit a hosted or self-operated clearinghouse.
2. Sign up and obtain an API key.
3. Discover supported Live Runner capabilities and expected rates.
4. Invoke a capability using the Python SDK or supported HTTP API.
5. Receive a result or understandable failure.
6. See metered usage and the resulting cost without handling Livepeer crypto
   mechanics directly.

### Proposed modularity

The initial clearinghouse should avoid making enterprise infrastructure
mandatory. Authentication, metering, storage, and events would be interfaces
with replaceable implementations.

| Concern | Minimal starting point | Optional deployment-specific implementation |
| --- | --- | --- |
| Authentication | Simple built-in credential store | Auth0 or another identity provider |
| Metering | Application-owned records and queries | OpenMeter or another metering platform |
| Storage | SQLite or PostgreSQL | A separately operated production database |
| Events | Direct or simple internal handling | Kafka or another event platform |
| API ingress | Direct application endpoint | Kong or another API gateway |

This is a proposed design principle, not an accepted technology selection.
Security, credential lifecycle, tenancy, auditability, migration, and
production operations still require definition.

### Relationship to Pymthouse and John Mull

**Classification:** Proposed boundary requiring agreement

The meeting proposed that:

- the Build Track define the minimal Open Clearinghouse architecture and
  contract;
- Build Track-funded work by John conform to that contract;
- John remain free to operate Pymthouse/Payment House as a larger commercial or
  hosted product above the common layer; and
- enterprise integrations be adapters rather than welded requirements in the
  minimal implementation.

No agreement from John is established by this meeting. A written RACI and
funding agreement are required to define:

- John's Build Track deliverables;
- repository and architectural authority;
- compensation and acceptance;
- compatibility or migration from Pymthouse;
- deployment responsibility; and
- the fallback if John does not accept or deliver the scoped work.

### Proposed Cloud SPE-hosted deployment

**Classification:** Proposal requiring Cloud SPE approval

Mike proposed that the Cloud SPE operate an initial clearinghouse instance
during the September–December period. The purpose would be to provide a real
URL for documentation and an independently testable builder journey without
waiting for a separate commercial deployment.

The proposal would need to define:

- approved Cloud SPE scope and budget;
- production or evaluation service level;
- wallet funding and loss limits;
- credential issuance and abuse controls;
- credit, balance, top-up, and exhaustion behavior;
- monitoring, incidents, backups, and support;
- deployment owner and repository revision;
- acceptance evidence; and
- shutdown, handoff, or continued-operation policy after December.

The Gemini summary's phrase “Cloud SPE clearing house hosting established” is
therefore too strong. Hosting was proposed as a way to prevent an external
dependency from blocking validation.

## Self-sovereign Agent

### Working interpretation from the discussion

**Classification:** Hypothesis requiring Doug

Doug was not present, so the meeting could not confirm his intended meaning.
The discussion developed a plausible interpretation: a self-sovereign Agent
may be an independently operated MCP server or agent application that consumes
the open Python SDK, remote signer, Live Runner, and clearinghouse interfaces.

Under that interpretation:

- the Build Track enables agents rather than building an end-user Agent
  product;
- an individual can operate an MCP server or similar client independently of
  Livepeer Inc;
- the canonical behavior belongs in network and builder interfaces rather than
  Storyboard; and
- a reference agent may be useful as documentation or validation evidence
  without becoming the authoritative architecture.

### Storyboard and Agent 2.0 treatment

**Classification:** Meeting recommendation for Build Track scope; external
product status remains unverified

The participants treated Storyboard and its Agent 2.0-specific infrastructure
as unsuitable for the target Build Track because of reported BYOC coupling,
product-specific services, complexity, and security concerns. The Python SDK
and independently useful Live Runner capability work should be evaluated
separately from the Storyboard product.

The meeting supports excluding Storyboard from the proposed authoritative
Build Track architecture. It does not establish a formal deprecation decision
for a product or repository owned outside the Cloud SPE.

### Questions only Doug can resolve

1. Does “self-sovereign Agent” mean a self-hosted version of the current Agent
   product, a new reference MCP server, open network primitives usable by any
   agent, an easy wallet-funded payment path, or a combination?
2. Is any Agent application or framework itself a December deliverable?
3. Is Storyboard relevant as reusable code, a reference, or only historical
   evidence?
4. Is x402 an example to investigate, a preferred direction, or a required
   compatibility target?
5. Must the self-sovereign path work without Livepeer Inc, Foundation, or
   another centrally operated service?

## Discovery, pricing, and Orchestrator readiness

### Current-state claims

**Classification:** Reported current state requiring verification

The discussion reported that:

- remote-signer discovery works in some form;
- AI service registry adoption is incomplete;
- only a small set of Orchestrators currently advertise the relevant service
  information;
- the currently used list may include static entries rather than complete
  registry-driven enumeration; and
- a temporary static Orchestrator list may be required for initial integration.

Rick was expected to provide the relevant Orchestrator list or reference URI.
The exact endpoints, registry version, fields, freshness, signatures, and
deployed behavior must be reproduced before these claims become baseline facts.

### Desired transition

The intended direction is to move from manually curated or hard-coded service
URIs toward an authoritative, maintainable discovery path. At minimum, the
architecture needs to define:

- durable Orchestrator identity and service URI;
- current Live Runner capability and version;
- capacity, availability, and health;
- price or rate with units and validity;
- selection and incompatibility filtering;
- retry and failover ownership; and
- the source, operator, signature, and freshness of each field.

The Build Track should not claim to own all Orchestrator registration or
operator tooling. Those are explicit Operate Track dependencies and handoffs.

## Pricing, usage, and payment implications

### Work-unit variability

The discussion recognized that capabilities may be charged using different
units, including seconds, pixels, tokens, or other workload-specific measures.
Live Runner and the clearinghouse must not hide these differences behind an
incorrect universal formula.

Still required:

- authoritative price source;
- unit and currency definitions;
- price validity or quote behavior;
- maximum exposure for long-running work;
- recorded actual usage;
- quote-to-charge reconciliation; and
- stable identifiers across invocation, execution, payment, usage, and charge.

### Walletless outcome versus minimal implementation

The proposed clearinghouse deliberately excludes mandatory Stripe and other
enterprise integrations, while the builder promise requires payment without
holding crypto. This creates an unresolved acceptance question:

- Is an externally funded credit balance sufficient for the December proof?
- Must a builder be able to purchase or replenish balance using fiat?
- Is fiat onboarding an external hosted-provider responsibility?
- Must the wallet-funded path also be demonstrated?
- What network settlement evidence is required when ticket redemption is
  probabilistic?

The meeting did not answer these questions or supersede Rich's required
payment-scope confirmation.

## Performance, failure, and recourse

**Classification:** Unresolved

Hunter's concern about expected performance and late job failure was not fully
resolved. SDK selection and failover do not by themselves answer what happens
when a long-running job fails after consuming substantial resources.

The target architecture still needs high-level ownership and acceptance for:

- capacity, availability, and expected completion information;
- timeout, cancellation, retry, and failover;
- partial work and checkpoint behavior, where applicable;
- failure classification and retryability;
- whether network payment or builder charge occurred;
- no-charge, partial-charge, credit, refund, or dispute behavior; and
- the boundary between protocol behavior, Build Track infrastructure, Operate
  Track reliability, clearinghouse policy, and commercial service recourse.

Enterprise SLAs, account management, and customer support were treated as
possible commercial layers above the core network. That boundary does not
remove the Build Track's need to return an understandable technical and
financial state after failure.

## Provisional December deliverables

These are the best current interpretation of the meeting, not approved
milestones.

| Candidate deliverable | Provisional content | Approval or evidence still required |
| --- | --- | --- |
| Target architecture and responsibility map | Open Clearinghouse, Python SDK, remote signer, Live Runner, Orchestrators, repositories, interfaces, Build/Operate boundaries, and external handoffs | Rick/Josh technical reconciliation; Rich outcome confirmation; joint SPE approval |
| Minimal Open Clearinghouse | Open-source, self-hostable credential, discovery, authorization, invocation, usage, and cost layer with replaceable auth, metering, storage, and event adapters | Repository decision, security and contract specification, owner, budget, and acceptance |
| Reference hosted deployment | A documented URL where an independent builder can obtain a credential and exercise the supported journey | Cloud SPE approval, operations plan, funding, limits, incident ownership, and post-December disposition |
| Supported Live Runner builder interface | A released Python SDK and/or stable HTTP contract for capability discovery, pricing, invocation, result/failure, usage, and cost | Exact contract, version, repository owner, release approver, and gateway/control-plane decision |
| Representative capability proof | At least one verified Live Runner capability completes the entire journey | Capability selection, deployed supply, rate semantics, Operate Track handoff, and repeatable evidence |
| Payment-path proof | Confirmed wallet-funded and/or walletless path produces authorization, usage, charge, and aggregate on-chain settlement evidence | Rich payment-scope decision, funding model, clearinghouse boundary, and probabilistic-ticket evidence definition |
| Discovery and service-assurance behavior | Eligible Orchestrators, capabilities, price, capacity, health, selection, retry/failover, and understandable failure state | Registry baseline, authoritative runtime owner, security, performance/recourse scope, and acceptance thresholds |
| Builder documentation and independent test | Exact versions, deployment instructions, signup, SDK/API usage, result/failure, payment, usage, cost, known limitations, and clean-environment evidence | Test protocol, independent tester, evidence bundle, documentation owner, and final acceptance authority |

## Proposed Cloud SPE delivery boundary

The meeting suggests that the Cloud SPE could own or coordinate:

- the Build Track architecture and dependency record for its assigned portion;
- specification or implementation of the minimal Open Clearinghouse;
- an initial hosted reference deployment;
- end-to-end integration and evidence across the supported builder journey;
- documentation and independent reproduction; and
- a RACI for external clearinghouse, repository, and operational work.

The Cloud SPE should not silently assume ownership of:

- Live Runner or Orchestrator implementation owned by the Operate Track;
- `go-livepeer` architecture or releases;
- product demand generation, application recruitment, or credits programmes;
- Storyboard or Agent 2.0 product development;
- John's independent Pymthouse/Payment House roadmap;
- commercial customer support or SLAs; or
- programme-wide architecture approval.

## Unresolved decisions blocking final milestones

1. **Doug's intent:** Define self-sovereign Agent and the relevance of
   Storyboard, MCP servers, self-hosting, and x402.
2. **Outcome and payment authority:** Rich confirms whether both wallet-funded
   and walletless journeys are required and which acceptance evidence applies.
3. **SDK versus control plane:** Rick and Josh resolve the authoritative owner
   of discovery policy, selection, routing, retry, failover, and error
   normalization.
4. **Live Runner delivery:** Josh confirms repository, release, interface,
   capability, and Operate Track handoffs.
5. **Clearinghouse direction:** Decide whether to replace, rewrite, simplify,
   or create a repository and establish a common contract before implementation.
6. **John's participation:** Agree a written RACI, funded scope, architectural
   boundary, acceptance, and fallback.
7. **Cloud hosting:** Approve budget, operational responsibilities, security,
   funding limits, support boundary, and post-December disposition.
8. **Discovery baseline:** Verify the service registry, remote-signer endpoint,
   Orchestrator list, capability metadata, price data, security, and freshness.
9. **Capability selection:** Name the representative capability and the owner
   of any external builder-requirement input without creating an adoption gate.
10. **Pricing and receipts:** Define units, quote behavior, payment correlation,
    usage, resulting charge, and probabilistic settlement evidence.
11. **Service assurance:** Decide the minimum expected-performance, failure,
    retry/failover, payment-state, and recourse behavior required in December.
12. **Joint approval:** Network Engineering SPE and Cloud SPE approve the same
    milestone revision, responsibilities, evidence, and budget.

## Meeting-derived follow-up ownership

This table captures proposed follow-up routing. Work status and dependencies
remain in Beads.

| Topic | Required participant or authority | Intended output |
| --- | --- | --- |
| Self-sovereign Agent and x402 | Doug, with Rich and Mike | Confirmed meaning, scope, component boundary, and December relevance |
| Live Runner, SDK, gateway, and repository boundary | Rick, Josh, and Mike | Preferred architecture, repositories, stable contracts, and Build/Operate handoffs |
| Clearinghouse scope and Pymthouse relationship | John, Mike, and relevant payment owners | Verified current state, common contract, funded RACI, and fallback |
| Payment-path scope | Rich, informed by Doug and technical owners | Required paths, Cloud SPE boundary, and acceptance evidence |
| Product requirements input | Product/GTM owner and candidate builders | Requirements input and decision date, explicitly outside Build Track adoption scope |
| Performance and recourse | Hunter, Rick, Josh, clearinghouse owner, and Mike | High-level service-assurance contract, owner, and December evidence |
| Service registry and active supply | Rick, Josh, and relevant Orchestrator owners | Reproducible current baseline and transition from static to authoritative discovery |
| Cloud SPE commitment | Cloud SPE | Approved scope, budget, hosting, operations, and acceptance responsibilities |
| Final milestone plan | Network Engineering SPE and Cloud SPE | Approved common milestone revision |

## Material not carried into Build Track conclusions

The meeting also discussed a recent security incident, validation-track
concerns, operator onboarding, individual products, personnel availability, and
broader network strategy. Those items are not recorded here as Build Track
deliverables unless they create a named dependency or handoff for the Cloud
SPE's portion.

The Gemini notes include at least one apparent date inconsistency in the
availability summary. Personnel dates should be confirmed directly before they
are used for scheduling or delivery planning.

## Bottom line

The meeting produced a credible working direction: the Build Track should make
Live Runner usable through a minimal open builder stack, with the Python SDK,
remote signer, and Live Runner as existing pillars and a simple Open
Clearinghouse as the principal missing layer.

The likely December proof is an independent builder obtaining an API key from
a hosted or self-operated clearinghouse, discovering a verified Live Runner
capability and price, invoking it, receiving a result or understandable
failure, and seeing usage and cost without managing crypto mechanics.

That direction is not final until the clearinghouse contract, payment scope,
self-sovereign Agent intent, Build/Operate handoffs, owners, funding,
deployment, service assurance, acceptance evidence, and joint approvals are
resolved.
