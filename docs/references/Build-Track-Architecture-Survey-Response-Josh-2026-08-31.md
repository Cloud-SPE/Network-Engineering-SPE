# Build Track Architecture Survey Response

**Expected completion time:** 10–15 minutes

**Survey version:** `3ce5ec9d31551ee52e8fae8031010f3c35a62a57`

**Respondent:** `Josh`

**Role:** `Orchestrator Track owner; architect/technical lead and Operate Track representative`

**Date completed:** `2026-08-31`

Read the [survey instructions](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3ce5ec9d31551ee52e8fae8031010f3c35a62a57/docs/references/Build-Track-Architecture-Survey-Instructions.md)
before beginning. Preserve the original questions and answer choices. Replace
the answer placeholders, mark unanswerable items as **Unknown**, and review the
completed file yourself before returning it.

## Section 1: Respondent context and authority

### 1. Role and relevant authority

Briefly describe your role:

**Answer:** Orchestrator Track owner; architect/technical lead and Operate Track representative.

Mark every area where you can provide authoritative facts, architectural
direction, repository approval, or programme approval:

- [ ] Build Track outcome or milestone authority
- [ ] Cloud SPE scope authority
- [x] `go-livepeer` architecture
- [x] `go-livepeer` merge or release approval
- [x] Live Runner architecture
- [x] Live Runner merge or release approval
- [ ] Agent 2.0/Storyboard
- [ ] SDK Service
- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] ServiceRegistry contracts
- [x] Deployment or operations
- [ ] Other: None

**Classification:** Current fact

**Confidence:** Medium

**Basis/source:** Respondent's stated authority; Operate Track mandate; `Build-Track-Architecture-Alignment-Process.md` participant/authority map and `NetworkEngieneerSPE2-Notes-v2.md` governance table at survey version `3ce5ec9d`.

### 2. Missing decision makers

Who else must participate or approve before the end-state architecture can be
accepted? Name the person, team, repository, and decision where possible.

**Answer:** Mike Zupper for Build Track outcomes, Cloud SPE boundaries, and milestone capture; Rick Staa for the Foundation technical gate, cross-track decisions, and `go-livepeer` review perspective; Rich O'Grady for programme outcome intent, payment-path scope, and Foundation final authority; the Network Engineering SPE and Cloud SPE for final milestone approval. John Mull or another Elite Encoder representative must verify hosted Pymthouse. The Agent-originated capability owners, SDK Service owner, `livepeer/clearinghouse` maintainers, and relevant deployment owners must verify their respective current facts and delivery boundaries.

**Classification:** Current fact

**Confidence:** Medium

**Basis/source:** `Build-Track-Architecture-Alignment-Process.md`, `Build-Track-Architecture-Survey.md`, and the draft milestones at survey version `3ce5ec9d`; these are planning drafts rather than final approvals.

**Required owner or follow-up:** Mike to confirm the final participant/authority map; Rich to confirm outcome and payment scope; Rick to confirm cross-track technical gates; John Mull/Elite Encoder and the named repository/deployment owners to provide missing implementation evidence.

## Section 2: Outcomes and scope

### 3. Live Runner execution focus

Should the September–December target architecture use Live Runner as its
execution focus?

- [ ] Yes
- [ ] No
- [x] Yes, with constraints
- [ ] Unknown

**Constraints or explanation:** “Reusable Live Runner service contract” is not an existing accepted API and must not remain a slogan. It should be defined as a capability-agnostic platform contract covering: stable capability identity and version; discoverable supply, availability, capacity, health, and current rate; credential and authorization behavior; invocation and job lifecycle; result and normalized failure state, including whether payment occurred; stable request/job/payment correlation identifiers; payment authorization; recorded usage; and a per-job charge record. “Reusable” means that a new capability implements this same lifecycle and evidence contract—typically through a capability declaration and runner adapter—without creating a new credential, discovery, pricing, payment, usage-and-charge reporting, error, or client-integration stack. The Agent product is not part of this contract.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's consolidated architecture decision; Operate Track mandate; `Build-Track-Outcome-and-High-Level-Concepts.md`; `Build-Track-Repo-Traceability.md`; draft milestones at survey version `3ce5ec9d`.

What should “supported Live Runner service types” mean for December acceptance?

- [x] A reusable Live Runner service contract proven through at least one
      representative capability
- [ ] A prescribed minimum set of named capabilities
- [ ] One fixed capability without a general extensibility commitment
- [ ] Another support model: None
- [ ] Unknown

The working assumption is the reusable-contract option. It requires
confirmation from Rich on outcome intent and from Rick and Josh on architecture
and delivery feasibility before it becomes an accepted requirement.

**Representative capability or selection owner:** Select a separately identifiable network capability produced during the Agent development effort, or another suitable Live Runner capability, after an inventory and contract-conformance check. Josh owns Live Runner feasibility; final selection is a joint Build/Operate architecture decision with Rick and Mike, subject to Rich's outcome confirmation.

**Required named capability list, if any:** None. One representative capability proves the contract; additional named capabilities are not an acceptance requirement.

**Do all supported capabilities have to satisfy the complete confirmed builder journey?** Yes.

**Confirmation or follow-up required from Rich, Rick, and Josh:** Josh confirms the architecture and delivery interpretation in this response. Rich must confirm outcome intent and payment-path scope. Rick must confirm the cross-repository technical interpretation. The group must publish the actual contract and choose the representative capability rather than relying on the phrase “reusable contract.”

### 4. Proposed execution non-goals

For each path, enter **Exclude**, **Include**, or **Unknown**. Identify required
compatibility or migration work even when execution is excluded.

| Execution path | Your answer | Classification | Confidence | Constraint, basis, or follow-up |
| --- | --- | --- | --- | --- |
| Batch AI | Exclude | Target recommendation | High | Not a December execution path. Preserve only explicitly required compatibility or migration behavior; do not make it a Build Track acceptance deliverable. |
| BYOC | Exclude | Target recommendation | High | Same constraint. Existing code remains current-state evidence, not target scope. |
| LV2V | Exclude | Target recommendation | High | Same constraint. Existing signer/payment coupling must not define the new contract accidentally. |
| Transcoding | Exclude | Target recommendation | High | Same constraint. |

### 5. Seven builder outcomes

For each outcome, name the component that should be authoritative in the
intended architecture. Use **Unknown** rather than guessing.

| Builder outcome | Intended authoritative component | Classification | Confidence | Basis or required follow-up |
| --- | --- | --- | --- | --- |
| Obtain one credential | Common identity/credential service at the clearinghouse boundary; exact implementation undecided | Target recommendation | Medium | One credential or invisible exchange must work across the complete journey. Select implementation after clearinghouse verification. |
| Discover what the network can do | Canonical builder catalog exposed by the supported SDK/API and backed by gateway/control-plane runtime discovery | Target recommendation | Medium | Catalog must reflect real network supply, not an Agent-maintained registry. |
| Understand the expected price or rate | Gateway/control-plane quote interface sourced from current Orchestrator/Live Runner rates and normalized by the canonical API | Target recommendation | Medium | Must present a fixed price, bound, or rate before invocation and relate it to the final charge. |
| Invoke a capability through a standard interface | Supported SDK/API over the `go-livepeer` gateway using the canonical Live Runner service contract | Target recommendation | High | Multiple interfaces may sit over the same platform contract. |
| Receive a result or understandable failure | Canonical gateway job/result/error contract, surfaced consistently by supported SDKs | Target recommendation | Medium | Must normalize validation, availability, execution, payment, and settlement failure and state whether payment occurred. |
| Pay without holding crypto | Common clearinghouse and remote-signer contract; implementation undecided | Target recommendation | Medium | Evaluate hosted Pymthouse and `livepeer/clearinghouse` only after verifying code, deployment, and ownership. |
| See usage and resulting charge | Clearinghouse or payment-accounting service producing a per-job usage-and-charge receipt through the canonical API | Target recommendation | Medium | Requires one stable job identifier across invocation, execution, ticket, usage, and the resulting charge record. |

## Section 3: Builder-facing components

### 6. Primary builder-facing interface

What should an independent builder call in the target architecture?

- [ ] Agent 2.0/Storyboard
- [ ] A supported SDK
- [ ] A hosted gateway API
- [ ] A direct `go-livepeer` gateway API
- [x] Multiple supported interfaces over one common platform contract
- [ ] Another interface: None
- [ ] Unknown

**Rationale or constraints:** The canonical object is the platform contract, not an application or one language SDK. Supported SDKs and APIs may expose it, while the `go-livepeer` gateway remains the permanent network component behind them. The contract must cover the complete lifecycle defined in question 3. Agent-product abstractions, registries, pricing, storage, and orchestration must not become canonical by accident.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's consolidated architecture decision and correction; `Build-Track-Repo-Traceability.md` shows that consistency currently exists only inside the Agent while lower layers have incompatible identity, discovery, invocation, pricing, and payment behavior.

### 7. Agent 2.0 role

What should Agent 2.0/Storyboard be by December?

- [ ] The canonical builder-facing interface
- [ ] A reference integration over canonical platform APIs
- [ ] One sample or reference application
- [ ] A transitional implementation
- [x] Outside the Build Track architecture
- [ ] Unknown

For capability catalog, price estimate, invocation, error normalization,
credential handling, job tracking, usage, and cost reporting, identify what
should remain in Agent 2.0 and what should move to canonical services.

**Answer:** None of these responsibilities should remain authoritative in the Agent product. Identity, capability catalog, current price/rate, invocation lifecycle, normalized platform errors, stable job identity, payment, usage, and charge records belong in canonical services and interfaces. Separately identify the network capabilities, runner implementations, adapters, capability declarations, and other platform artifacts created during the Agent development process. Those artifacts are not the Agent product. They may be retained as representative capability implementations or input to the canonical contract only after they are inventoried, decoupled from Agent-specific infrastructure, assigned owners, and shown to conform end to end.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent correction: the Agent product is not salvageable as the target architecture; `Build-Track-Repo-Traceability.md` documents its product-specific registry, pricing, credit, event, and SDK Service layers as disconnected projections rather than authoritative network contracts.

**Required owner or follow-up:** Agent-development owners must inventory and separate reusable network capabilities/platform artifacts from the Agent product. Josh and Rick should determine technical eligibility and contract conformance; Mike should ensure that reuse does not reintroduce Agent-product or application-adoption requirements.

### 8. SDK Service and gateway roles

Classify each component as **Permanent**, **Transitional**, **Replace**, **Not
in target**, or **Unknown**.

| Component | Classification in target | Current fact, target recommendation, or unknown | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| SDK Service in `simple-infra` | Transitional | Target recommendation | High | The Agent currently calls it, but target routing and catalog functions move to the canonical gateway/control plane. Inventory any capability implementations or adapters before retirement. |
| Python gateway SDK | Transitional | Target recommendation | Medium | A supported SDK remains useful, but the current three-family API must converge on the canonical contract rather than acting as its own bespoke gateway. |
| `go-livepeer` gateway | Permanent | Target recommendation | High | Permanent network component behind supported SDK/API surfaces; exact public boundary still requires design. |
| Hosted routing or discovery service | Replace | Target recommendation | Medium | Replace the current ad hoc/unverified service with a named canonical gateway or Live Runner control-plane responsibility. The routing/discovery function itself is permanent. |

**Intended owner of Orchestrator selection and failover:** The `go-livepeer` gateway or a named Live Runner control plane—not Agent 2.0, the SDK Service, or each client SDK. The architecture decision must choose one owner and repository.

## Section 4: ServiceRegistry and discovery

### 9. On-chain ServiceRegistry role

What should be represented on-chain in the target architecture? Mark all that
apply, then distinguish current facts from target recommendations.

- [x] Orchestrator identity or address
- [x] Service URI
- [ ] Live Runner capability identifiers
- [ ] Capability versions
- [ ] Hardware information
- [ ] Capacity
- [ ] Health
- [ ] Prices or rates
- [ ] None of these
- [ ] Another field: None
- [ ] Unknown

**Current facts:** The current implementation uses the on-chain ServiceRegistry as a durable Orchestrator identity/address and service-URI source. Runtime `GetOrchestrator`, local registration, and other discovery paths carry capabilities, constraints, hardware-related data, ticket parameters, prices, capacity, and availability. Exact deployed versions still require verification.

**Target recommendations:** Keep only durable identity/address and service URI on-chain. Keep capability identifiers and versions, capacity, health, availability, and current prices dynamic unless a separately justified durable capability identity/version commitment is accepted.

**Confidence:** High

**Basis/source:** Respondent's consolidated decision; `Build-Track-Architecture-Alignment-Process.md` registry terminology; `Build-Track-Repo-Traceability.md` current implementation review.

### 10. Dynamic discovery and selection

Identify the intended owner for each responsibility. Candidate owners include
the on-chain registry, `go-livepeer` gateway, SDK, SDK Service, clearinghouse,
Live Runner control plane, or a separate service.

| Responsibility | Intended owner | Classification | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| Enumerate eligible Orchestrators | `go-livepeer` gateway or named Live Runner control plane, seeded by the on-chain registry | Target recommendation | Medium | Choose the exact repository in the architecture decision. |
| Obtain current Live Runner capabilities | Orchestrator-local Live Runner registry exposed through runtime discovery | Target recommendation | High | Capability data is dynamic and must use stable IDs/versions. |
| Obtain capacity and health | Live Runner control plane/runtime discovery | Target recommendation | High | Do not place dynamic operational state on-chain. |
| Obtain prices or rates | Runtime discovery/quote path owned by the gateway or control plane | Target recommendation | Medium | Must normalize units and relate quote to final charge. |
| Filter incompatible or unavailable supply | `go-livepeer` gateway or Live Runner control plane | Target recommendation | High | Keep policy out of each client. |
| Select an Orchestrator | `go-livepeer` gateway or Live Runner control plane | Target recommendation | High | Exact boundary requires one named owner. |
| Retry or fail over | Same component that selects the Orchestrator | Target recommendation | High | Selection and failover must not split across unrelated layers. |
| Expose a builder-facing capability catalog | Supported SDK/API backed by the gateway/control plane | Target recommendation | High | Must reflect eligible current supply, not an Agent registry projection. |

## Section 5: Clearinghouse and payment

### 11. Hosted Pymthouse and `livepeer/clearinghouse`

What is their relationship?

- [ ] Pymthouse deploys `livepeer/clearinghouse`
- [ ] Pymthouse is a fork or derivative of that repository
- [ ] They are separate implementations
- [ ] One is intended to replace the other
- [ ] Another relationship: None asserted
- [x] Unknown

**Classification:** Unknown

**Confidence:** High

**Basis/source:** `Build-Track-Repo-Traceability.md` explicitly did not verify hosted Pymthouse's codebase, deployed revision, ownership, or relationship to `livepeer/clearinghouse`.

**Person who can verify:** John Mull or another Elite Encoder representative, together with the `livepeer/clearinghouse` maintainer and deployment owner.

### 12. Clearinghouse direction

Which direction should the architecture process evaluate as the likely target?

- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] Both behind a common clearinghouse contract
- [ ] A new Build Track implementation
- [ ] No clearinghouse in the target architecture
- [x] Unknown pending requirements and deployment evidence

**Rationale:** Define the common credential, authorization, balance, signer, job-correlation, usage, and per-job charge-receipt contract first. Verify hosted Pymthouse and `livepeer/clearinghouse` against the same evidence. Do not select an implementation—or assume that both must run—until their relationship, deployed behavior, production readiness, ownership, and unmet requirements are known.

**Unmet requirement requiring a new implementation, if selected:** Not applicable. No new implementation should be selected without a documented unmet requirement and evaluation of existing options.

**Classification:** Target recommendation

**Confidence:** High

**Required owner or follow-up:** Mike and Rich for requirements/scope authority; John Mull/Elite Encoder and `livepeer/clearinghouse` maintainers for implementation evidence; named identity, signer, payment-accounting, and deployment owners for contract feasibility.

### 13. Payment-path scope and walletless definition of done

The working assumption is that both wallet-funded and walletless payment
journeys are in the December target, pending confirmation from Rich. This does
not assume that the Cloud SPE implements every part of both journeys or that
hosted Pymthouse is the selected walletless implementation.

Which payment-path scope should the architecture and milestone process use?
Select one.

- [ ] Both journeys are required Build Track acceptance paths
- [x] Both are required in the target architecture, but one or more paths are
      external dependencies or compatibility obligations rather than Cloud SPE
      deliverables
- [ ] Walletless is required; wallet-funded compatibility is not a Build Track
      acceptance path
- [ ] Another scope: None
- [ ] Unknown; Rich or another named authority must confirm

**Required authority or confirmation:** Rich must confirm programme outcome intent and the payment-path scope. Network Engineering SPE and Cloud SPE approval must confirm ownership boundaries.

**Wallet-funded path owner and minimum acceptance evidence:** Owner to confirm: `go-livepeer`/network-payment maintainers and the wallet-funded gateway operator, potentially as an external compatibility dependency. Minimum evidence: one reproducible Live Runner call using wallet-funded authorization with a payment ticket, result or understandable failure, correlated job identity, network payment evidence, usage, and resulting charge.

**Walletless path owner and minimum acceptance evidence:** Owner to confirm after clearinghouse selection: common clearinghouse, identity, signer, payment-accounting, and deployment owners. Minimum evidence: a new builder obtains one ordinary credential without operator help, receives authorization subject to a real balance/allowance, invokes the same Live Runner contract, produces a signed payment ticket and visible network-payment evidence, and receives a correlated per-job usage-and-charge receipt or an understandable payment failure.

After authorization, should both paths use the same builder-facing invocation,
job, result, usage, and charge interfaces?

- [x] Yes
- [ ] No; the required differences are: None
- [ ] Unknown

For the walletless journey, which evidence is required before “pay without
holding crypto” is satisfied? Mark all that apply.

- [x] One ordinary builder credential
- [x] Self-service credential issuance
- [x] Balance or allowance enforcement
- [x] Successful signer authorization
- [x] A payment ticket attached to the job
- [x] Winning-ticket redemption or fee visible on-chain
- [x] Usage recorded by the clearinghouse
- [x] Per-job usage and charge receipt
- [x] Understandable insufficient-funds or payment failure
- [ ] Another requirement: None
- [ ] Unknown

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's consolidated payment decision; seven builder outcomes; draft milestones; current gaps in `Build-Track-Repo-Traceability.md`.

**Comments or constraints:** “Walletless” is an outcome, not a product name. Both paths should converge after authorization. Compatibility with the wallet-funded path may be externally owned; that does not remove the requirement for a named owner and observable acceptance evidence.

## Section 6: Risks and next participants

### 14. Largest unresolved concern

What single unresolved fact, architecture choice, ownership boundary, or
dependency is most likely to prevent clear December requirements?

**Answer:** The canonical platform contract and its repository/operational owners are not yet defined. Without an explicit contract joining capability identity, dynamic discovery and price, invocation/job lifecycle, both payment paths, stable correlation identifiers, normalized errors, usage, and per-job charge evidence, the programme risks preserving the current disconnected stacks under a new “reusable” label. Clearinghouse implementation uncertainty is the highest-impact instance of this broader contract-and-ownership gap.

**Classification:** Current fact

**Confidence:** High

**Required owner or follow-up:** Mike, Rick, Josh, and Rich must turn the placeholder into an accepted contract/owner map through `netspe-vun.12`; specialists must verify clearinghouse, SDK Service, capability-artifact, and deployment facts before Part 2.

### 15. Specialist follow-up

Which targeted 25–30 minute discussion is likely to be required after Workshop
Part 1? Mark all that apply and name the required participants.

- [x] Hosted Pymthouse and `livepeer/clearinghouse`
- [x] ServiceRegistry, gateway discovery, and Live Runner registration
- [x] Agent 2.0 and SDK Service integration
- [x] Identity, signer, and payment
- [x] Repository ownership and deployment
- [ ] No specialist session expected
- [x] Another session: Inventory and ownership of network capabilities/platform artifacts created during Agent development, separate from the Agent product
- [ ] Unknown

**Required participants:** John Mull or another Elite Encoder representative; `livepeer/clearinghouse` maintainer and deployment owner; Josh and Rick for `go-livepeer`, Live Runner, registry/discovery, and release gates; SDK Service and Agent-development capability owners; identity, signer, payment-accounting, and payment owners; Mike for Build Track/Cloud SPE boundary; Rich where outcome or payment scope authority is required.

**Rationale:** These sessions verify facts needed to select a clearinghouse, name the canonical runtime and routing owners, retire or replace Agent/SDK Service product coupling without discarding independently useful network capabilities, and establish repository/deployment accountability.

## Respondent confirmation

Review the entire response before completing this section.

- [x] I reviewed the completed Markdown and it accurately represents my answers.
- [ ] The original questions and answer choices were preserved. One specialist-session option was intentionally shortened at the respondent's request.
- [x] I distinguished current facts, target recommendations, and unknowns.
- [x] I did not include credentials, tokens, private keys, private contact data,
      or security-sensitive operational details.
- [x] I understand that this response is diagnostic input, not a vote or
      architecture approval.

**Confirmed by:** `Josh`

**Confirmation date:** `2026-08-31`
