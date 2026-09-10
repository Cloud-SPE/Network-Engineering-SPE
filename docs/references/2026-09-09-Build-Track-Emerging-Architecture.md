# Emerging Build Track Architecture

**Status:** Working architecture hypothesis; not an approved target design or
delivery assignment

**Date:** 9 September 2026

**Execution bead:** `netspe-vun.20`

## Purpose

This document presents the emerging high-level architecture needed to satisfy
the Build Track's builder outcomes while preserving the Cloud SPE's limited
scope. It translates the recent survey, repository review, and stakeholder
discussions into a single visual model of:

- the three emerging access paths;
- the common open builder interfaces;
- walletless and wallet-funded payment handling;
- capability discovery and routing;
- Live Runner-backed execution;
- result, failure, usage, and charge feedback; and
- Build Track, Operate Track, commercial-product, and protocol boundaries.

The image is an architecture discussion artifact. A box indicates that a
logical function is needed; it does not prove that a repository implements it,
assign its delivery to the Cloud SPE, or approve its production operation.

## Architecture image

![Emerging Build Track architecture showing builders and applications branching into hosted Agent, generic walletless, and self-hosted paths; converging on shared builder interfaces, clearinghouse or wallet payment, discovery, Remote Signer, Orchestrators, Live Runner, and capability backends](../assets/build-track-emerging-architecture-2026-09-09.png)

The [standalone PNG](../assets/build-track-emerging-architecture-2026-09-09.png)
is 1672 by 941 pixels and can be shared independently of this document.

### Visual language

- Violet and teal boxes show the emerging common architecture and aligned
  directional components.
- Amber labels mark decisions or handoffs that remain unresolved.
- Dashed containers show responsibility or dependency boundaries rather than
  repository ownership.
- Solid arrows show the logical builder and invocation journey.
- The dashed payment-authorization arrow distinguishes Remote Signer's payment
  role from execution of the requested capability.

## Evidence basis

The model synthesizes:

- the [Build Track builder outcomes](Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise);
- the [repository traceability review](Build-Track-Repo-Traceability.md);
- the [8 September Rick discussion](2026-09-08-Rick-Build-Track-Survey-Discussion-Consolidated-Notes.md);
- the [8 September Network Engineering SPE meeting summary](2026-09-08-NE-SPE-Weekly-Meeting-summary.md); and
- the [9 September Doug alignment findings](2026-09-09-Doug-Agent-GTM-Build-Track-Alignment-Meeting-Findings.md).

Source material under `docs/references/` remains evidence and working material.
Production behavior, approved decisions, and accepted specifications have
higher precedence.

## Architecture at a glance

Builders, agent harnesses, and applications should not be forced into a single
commercial product. They should be able to reach the same open network
substrate through three paths:

1. a hosted and opinionated Agent product;
2. a generic walletless builder service; or
3. a self-hosted, wallet-funded open stack.

Those paths converge on a coherent set of builder interfaces. The walletless
path uses a clearinghouse to translate an ordinary credential, usage, and
charge experience into network payment. The self-hosted path uses a builder-
controlled funded wallet. Both depend on accurate discovery, pricing,
eligibility, and routing information.

The builder-side gateway or SDK invokes an eligible `go-livepeer` Orchestrator.
Remote Signer supports discovery and authorizes network payment; it does not
execute the job. The Orchestrator uses Live Runner and the appropriate
capability backend to perform the work. Results or understandable failures,
usage, and resulting charges flow back to the builder-facing layer.

## Access paths

### Hosted Agent Product

**Classification:** Commercial product outside Cloud SPE delivery

Livepeer Inc intends to offer an opinionated, hosted Agent product focused on
agentic media creation. It can provide an ordinary account, hosted operation,
credit-card access, support, reliability enhancements, and a simplified user
journey.

The Build Track should verify that the product consumes compatible open
interfaces where those interfaces are part of the agreed network substrate.
It does not own the Agent product's GTM, customer acquisition, application
adoption, or product-specific features.

### Generic Walletless Service

**Classification:** Required builder outcome; implementation and operator
unresolved

This path allows an application to use raw network capabilities without
holding crypto or adopting the opinionated Agent product. The emerging logical
component is a minimal Open Clearinghouse that provides:

- account or credential issuance;
- a capability and expected-price view;
- request authorization and submission;
- network-payment abstraction;
- usage records; and
- the resulting builder charge.

A hosted walletless service is not fully self-sovereign because its operator
controls payment abstraction and service availability. The implementation
should nevertheless be independently deployable so that multiple operators or
commercial providers can offer the service.

### Self-Hosted Open Stack

**Classification:** Aligned direction; exact deployment contract unresolved

This path allows a builder or application operator to deploy the supported open
components and use a funded wallet under their own control. It is the clearest
expression of direct, self-sovereign network access.

The required minimum component set is not yet settled. In particular, the
relationship among Agent MCP, the Python SDK, HTTP interfaces, `go-livepeer`
gateway behavior, and Remote Signer still needs an accepted deployment and
security model.

## Emerging component model

| Component or function | Role in the journey | Current architectural treatment | Build Track relationship |
| --- | --- | --- | --- |
| Hosted Agent Product | Opinionated commercial entry point for agentic media creation | Livepeer Inc commitment described by Doug; exact artifact and release need confirmation | External product and reference consumer |
| Open Agent MCP | Agent-harness interface over the open capability substrate | Material access point; security and repository handoff unresolved | Candidate integration, hardening, validation, and documentation work after accepted handoff |
| Python Gateway SDK | Programmatic discovery, selection, payment coordination, and invocation | Existing architectural pillar; supported version and canonical contract unresolved | Likely builder-facing dependency and documented interface |
| Supported HTTP API | Language-neutral credential, catalog, invocation, and evidence surface | Logical interface; authoritative schema and hosting boundary unresolved | Candidate builder interface, potentially exposed by a clearinghouse or gateway |
| Open Clearinghouse | Ordinary credentials, walletless payment abstraction, usage, and charge | Needed logical component; repository, owner, custody model, and operator unresolved | Proposed Build Track component subject to Cloud SPE scope and approval |
| Funded Wallet Path | Builder-controlled network funding and payment | Required alongside walletless access; security and setup experience unresolved | Self-hosted journey to document and prove |
| Capability Discovery and Routing | Finds eligible supply and presents capability, price, capacity, and health information | Registry versus runtime sources and routing ownership unresolved | Cross-track contract consumed by the builder journey |
| Remote Signer | Supports Orchestrator discovery and network-payment authorization | Existing critical dependency; exact responsibility and stable release boundary unresolved | Integrated dependency, not the job executor |
| `go-livepeer` Orchestrator | Accepts eligible work and coordinates node-side execution and network payment | Existing network component owned outside the Cloud SPE | Operate Track and repository-owner dependency |
| Live Runner | Executes the Build Track's supported capability contract | Emerging execution focus; repository and release integration require confirmation | Primary execution dependency for end-to-end evidence |
| Capability Backends | Perform GPU/model, deterministic-compute, or approved API-pass-through work | Capability set and December representative capability unresolved | Operate Track or capability-owner dependency |
| Protocol and on-chain services | Provide durable service identity, payment tickets, and settlement | External protocol dependency; service-registry and runtime boundary unresolved | Consumed dependency, not general Cloud SPE protocol ownership |
| Usage and charge evidence | Correlates invocation, execution, network payment, usage, and builder charge | Required outcome; identifiers, metering authority, and retention unresolved | Build Track integration and acceptance evidence |

Logical component names such as Open Clearinghouse and Capability Discovery do
not select a repository. In particular, neither Pymthouse nor
`livepeer/clearinghouse` becomes the accepted implementation merely by being
related to the function.

## Logical interaction sequence

### Common builder journey

1. A builder selects a hosted Agent, generic walletless, or self-hosted path.
2. The builder obtains an ordinary credential or configures a funded wallet.
3. The builder interface requests the available capabilities and eligible
   supply.
4. Discovery combines the accepted durable service data with current runtime
   capability, price, capacity, and health information.
5. The builder receives the most honest available expected price or rate.
6. The SDK or gateway selects an eligible Orchestrator and submits the request.
7. Remote Signer authorizes the required network payment for the selected
   execution path.
8. The Orchestrator dispatches the job through Live Runner to the selected
   capability backend.
9. The result or an understandable execution or payment failure returns to the
   builder interface.
10. The walletless layer records usage and presents the resulting charge; the
    self-hosted path retains the corresponding network-payment evidence.

### Walletless payment path

The builder authenticates to a clearinghouse using an ordinary credential. The
clearinghouse or its delegated gateway uses a funded network-payment path on
the builder's behalf. It must correlate the builder identity and request with
the network execution, usage, and resulting charge without exposing ticket or
settlement mechanics to the builder.

This requires a defined custody model, credit or balance semantics, loss
limits, abuse controls, and an accountable operator before it can be treated as
a production service.

### Wallet-funded path

The builder or application operator controls the funded wallet and deploys the
required open components. The SDK or gateway uses Remote Signer or the accepted
equivalent to authorize network payment, then invokes an eligible Orchestrator.

The exact wallet permissions, signer separation, secret handling, supported
deployment topology, and upgrade process are part of the unresolved security
boundary.

### Result and evidence path

Execution results should return independently of payment authorization. The
builder-facing layer must be able to distinguish:

- a valid result;
- an understandable capability or validation failure;
- unavailable or ineligible supply;
- a timeout or execution failure;
- a payment-authorization or balance failure; and
- a usage or billing-record failure.

The architecture needs stable identifiers across the credential, request,
selected capability, Orchestrator execution, payment authorization, measured
usage, and resulting charge. The detailed fields remain a later contract
decision.

## Responsibility boundaries

### Build Track and Cloud SPE

The emerging Build Track responsibility is the coherent open builder
experience: interfaces, integration, reproducible deployment, documentation,
and evidence that the agreed journeys work. The Cloud SPE owns only the
deliverables formally assigned to it after architecture, budget, repository,
and acceptance approval.

The Build Track does not own:

- commercial Agent GTM;
- application adoption or demand generation;
- application counts or traffic targets;
- every capability implementation;
- general Orchestrator operation;
- Livepeer protocol design; or
- indefinite operation of a hosted clearinghouse without separate approval.

### Operate Track

The Operate Track is expected to provide healthy, discoverable capability
supply and the node-side mechanisms for declaring, pricing, selecting, and
running capabilities. The Build Track depends on stable contracts and release
handoffs from this work.

The exact RACI for registration, discovery, routing, retry, failover,
availability, pricing, and errors still requires agreement with Josh and the
affected repository owners.

### Livepeer Inc and other products

Livepeer Inc and other application teams may build commercial products on the
common substrate, operate their own clearinghouses or gateways, and add
application-specific support and guarantees. Their products can provide useful
compatibility evidence without becoming Cloud SPE deliverables.

### Protocol and on-chain dependencies

The Build Track consumes protocol functions for identity, payment tickets, and
settlement. It may require an agreed ServiceRegistry projection or payment
interface but does not thereby own general protocol changes.

## Unresolved decisions represented in the image

### Canonical builder contract

The target relationship among Agent MCP, Python SDK, HTTP API, and gateway
behavior remains unsettled. The architecture needs one coherent contract even
if several transports or clients expose it.

### Open Agent security and handoff

The Agent repository, release, open-source boundary, threat model, wallet
isolation, vulnerability handling, and Build Track handoff must be established
before independent deployment can be accepted.

### Clearinghouse implementation and operating model

The Build Track must select whether to simplify `livepeer/clearinghouse`, create
a new minimal implementation, or accept another repository. A separate
decision must identify who operates any evaluation or production instance and
what happens after December.

### Registry and runtime discovery split

Durable identity and service declarations may be on-chain, while capability
availability, prices, capacity, health, and route selection may require current
runtime data. The authoritative source, freshness rules, and ownership of each
field are unresolved.

### Performance, recovery, and recourse

The image includes capacity, health, and understandable failures but does not
promise an SLA or financial recourse. The Build and Operate Tracks still need
to determine the minimum expected-performance information, retry or failover
behavior, and support boundary. Commercial guarantees should remain distinct
from open-network behavior.

### December capability proof

The architecture is capability-agnostic, but December acceptance needs at
least one representative Live Runner capability that proves the entire agreed
journey. Selecting that capability is a technical validation decision, not an
application-adoption or demand-generation target.

## What the image does not decide

The image deliberately does not:

- approve the three paths as equal Cloud SPE delivery obligations;
- select Pymthouse, `livepeer/clearinghouse`, or a new clearinghouse repository;
- state that Remote Signer is the permanent catalog or routing authority;
- make Agent MCP the only builder interface;
- assign `go-livepeer` or Live Runner development to the Cloud SPE;
- prescribe Auth0, OpenMeter, Kafka, Kong, Stripe, or a database;
- promise production SLAs or recourse;
- prescribe a December capability list;
- require a particular application, application count, or traffic volume; or
- represent final Network Engineering SPE or Cloud SPE approval.

## Intended next use

This visual and component description should be used to obtain agreement on:

- the delivered, demonstrated, and externally supported access paths;
- the canonical builder contract;
- the open Agent artifact and security handoff;
- the Build/Operate component RACI;
- the minimal clearinghouse repository and operator;
- the registry and runtime-discovery boundary;
- the representative December capability; and
- the final acceptance evidence and approval authorities.

Once those choices are approved, the resulting decisions should be recorded in
`docs/decisions/`, incorporated into the relevant product specification and
milestones, and represented as implementation dependencies in Beads. This
working reference should remain as provenance for the architecture discussion.
