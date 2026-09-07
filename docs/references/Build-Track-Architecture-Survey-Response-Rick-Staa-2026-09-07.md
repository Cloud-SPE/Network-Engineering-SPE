# Build Track Architecture Survey Response

**Expected completion time:** 10–15 minutes

**Survey version:** `9b0dda0`

**Respondent:** Rick Staa

**Role:** Network Engineering SPE technical gate (as stated in the SPE proposal)

**Date completed:** 2026-09-07

Read the [survey instructions](Build-Track-Architecture-Survey-Instructions.md)
before beginning. Preserve the original questions and answer choices. Replace
the answer placeholders, mark unanswerable items as **Unknown**, and review the
completed file yourself before returning it.

## Section 1: Respondent context and authority

### 1. Role and relevant authority

Briefly describe your role:

**Answer:** As stated in the SPE proposal: ensures code reviews are completed in a timely fashion, and rules on architectural decisions that cross track boundaries where owners cannot agree.

Mark every area where you can provide authoritative facts, architectural
direction, repository approval, or programme approval:

- [ ] Build Track outcome or milestone authority
- [ ] Cloud SPE scope authority
- [x] `go-livepeer` architecture (where needed)
- [x] `go-livepeer` merge or release approval (where needed)
- [x] Live Runner architecture (where needed)
- [x] Live Runner merge or release approval (where needed)
- [ ] Agent 2.0/Storyboard
- [x] SDK Service
- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [x] ServiceRegistry contracts
- [x] Deployment or operations
- [x] Other: Cross-track architecture arbitration where owners cannot agree

**Classification:** Current fact

**Confidence:** High

**Basis/source:** Network Engineering SPE proposal (role definition)

### 2. Missing decision makers

Who else must participate or approve before the end-state architecture can be
accepted? Name the person, team, repository, and decision where possible.

**Answer:** The missing participants are the product side and the teams of potential builders, not more approvers.

1. The product team, to own the research into which potential builders exist and how strong their demand actually is. Architecture should be designed for builders whose demand has been validated, not for builders we assume exist. There is no use in building an SDK or architecture without initial clients to gather feedback from. The ecosystem has worked too much in a silo of what it thinks it should build, so this is more about outreach and battle-testing than about approvals.
2. The teams of the potential builders themselves, so their requirements shape the architecture before it is fixed.
3. Shane, as an addition on the product side. He owns the validation track, which will provide important data, and he has strong product intuition.
4. John, on payments, as he owns the hosted clearinghouse track that abstracts away crypto payments.

To be clear, this does not reopen the decision that demand generation and application adoption are not Build Track requirements. It means the architecture still needs requirements from validated builders, and someone outside the Build Track must own finding and validating them. Once that research is done, the list of missing owners will change.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's judgment from cross-track experience; John's stated plan for a hosted clearinghouse

**Required owner or follow-up:** Mike to include Shane and John in the process; the product team to validate demand from potential builders before the architecture is fixed

## Section 2: Outcomes and scope

### 3. Live Runner execution focus

Should the September–December target architecture use Live Runner as its
execution focus?

- [ ] Yes
- [ ] No
- [x] Yes, with constraints
- [ ] Unknown

**Constraints or explanation:** Live Runner in its initial form, combined with the Python SDK, is the right direction. Every orchestrator I have talked with said it was a breeze to set up and they onboarded new workflows in minutes. It is an initial prototype, so a lot still has to be done, but it is a solid start. However, as Josh leads this track, he already stated months ago that he would like to create a new Live Runner repo combined with the SDK to make it more maintainable. The focus should be on going after this track.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's conversations with orchestrators; Josh's stated plan for a new Live Runner repo combined with the SDK

What should “supported Live Runner service types” mean for December acceptance?

- [ ] A reusable Live Runner service contract proven through at least one
      representative capability
- [ ] A prescribed minimum set of named capabilities
- [ ] One fixed capability without a general extensibility commitment
- [x] Another support model: Requirements-driven. Thinking in capabilities or models has no use without knowing who you are building for, and that is still highly unclear. Livepeer is a decentralised compute network, not an end-user product. Finding people to build on the network, gathering their requirements, and then improving the network is more valuable than trying to build something like Daydream, chutes.ai, or the Livepeer Agent ourselves. It will be very hard to compete on a capability spectrum.
- [ ] Unknown

The working assumption is the reusable-contract option. It requires
confirmation from Rich on outcome intent and from Rick and Josh on architecture
and delivery feasibility before it becomes an accepted requirement.

**Representative capability or selection owner:** Mike selects the capability, based on real-world input from a demand researcher. That input is currently missing: there is no role that researches the demand space, identifies which potential builders represent credible demand spikes, and feeds that to Mike and Josh. That is an ownership gap. A demand-research owner, possibly a new role or assigned to the product team, should provide this input so the representative capability is chosen against real possible demand rather than assumed demand.

**Required named capability list, if any:** None

**Do all supported capabilities have to satisfy the complete confirmed builder journey?** Yes

**Confirmation or follow-up required from Rich, Rick, and Josh:** Josh and Mike kickoff on the network software the builder track needs (see question 15)

### 4. Proposed execution non-goals

For each path, enter **Exclude**, **Include**, or **Unknown**. Identify required
compatibility or migration work even when execution is excluded.

| Execution path | Your answer | Classification | Confidence | Constraint, basis, or follow-up |
| --- | --- | --- | --- | --- |
| Batch AI | Exclude | Current fact | High | Being deprecated; a pull request is already open for Josh. |
| BYOC | Exclude | Current fact | High | Being deprecated; a pull request is already open for Josh. |
| LV2V | Exclude from Build Track execution | Current fact | High | Only needs a security check; will be maintained by Livepeer Inc. The SDK remains focused on Live Runner and LV2V. |
| Transcoding | Exclude | Current fact | High | Security update, then maintenance mode; will be deprecated in the future. |

### 5. Seven builder outcomes

For each outcome, name the component that should be authoritative in the
intended architecture. Use **Unknown** rather than guessing.

| Builder outcome | Intended authoritative component | Classification | Confidence | Basis or required follow-up |
| --- | --- | --- | --- | --- |
| Obtain one credential | A clearinghouse on top of a remote signer, with Pymthouse as the community-maintained one | Target recommendation | High | Respondent's architecture view; John's hosted clearinghouse plan |
| Discover what the network can do | Remote signer, exposed through client SDKs. Orchestrators also have a discovery endpoint. The ServiceRegistry can be combined with, or replaced by, the AI service registry. The go-livepeer gateway is deprecated. | Target recommendation | High | Respondent's architecture view; current remote-signer and orchestrator discovery endpoints |
| Understand the expected price or rate | Orchestrator, as a fixed price per second. Keep it as easy as possible for orchestrators: one price per GPU type, not per job, so setup stays minimal. App pricing logic must never live in the core software; Livepeer is a compute network, not an end-user product. | Target recommendation | High | Respondent's architecture view |
| Invoke a capability through a standard interface | Python SDK. A gateway is only needed if an end-user or B2B app wants extra logic such as load balancing; they can build that themselves, we do not provide it. The SDK alone is a good starting point and can already do this. | Target recommendation | High | Respondent's example integration; current Python SDK capability |
| Receive a result or understandable failure | Same path: SDK only, with a gateway on top if the client needs it. Ideally the SDK and orchestrators aggregate data about the network to an aggregator, which can then inform and help SDK selection. | Target recommendation | High | Respondent's architecture view |
| Pay without holding crypto | A clearinghouse hosted by the client using the remote signer, or Pymthouse for those who do not want to set this up. | Target recommendation | High | Respondent's architecture view; John's hosted clearinghouse plan |
| See usage and resulting charge | Same as payment: client-hosted clearinghouse or Pymthouse. | Target recommendation | High | Respondent's architecture view |

## Section 3: Builder-facing components

### 6. Primary builder-facing interface

What should an independent builder call in the target architecture?

- [ ] Agent 2.0/Storyboard
- [x] A supported SDK
- [ ] A hosted gateway API
- [ ] A direct `go-livepeer` gateway API
- [ ] Multiple supported interfaces over one common platform contract
- [ ] Another interface: `{DESCRIBE}`
- [x] Unknown

**Rationale or constraints:** This really depends on the network-wide go-to-market. Making the network agent-enabled, so that agents can discover or perform network capabilities, is interesting from a network product perspective. However, products like the Livepeer Agent, Blueclaw, Roboflow, or Studio are things built on top, B2B. They are important, but we are a compute network enabling compute, not an end-user product. So enable other products to build on top. These products need a good SDK to discover, select, pay, and do the jobs they want. The rest is go-to-market on top.

**Classification:** Target recommendation for the SDK; unknown until the network-wide go-to-market is decided

**Confidence:** Medium

**Basis/source:** Respondent's view of Livepeer as a compute network; dependency on the network-wide go-to-market decision

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

**Answer:** The Livepeer Agent should be enabled, not built. The network should enable its go-to-market by ensuring discovery is compatible and orchestrators can run the needed jobs performantly and securely. Everything on top is end-user go-to-market. There is a Hugging Face-like angle of making Livepeer fully agent-enabled by allowing classes of jobs, for example diffusers, ComfyUI, Roboflow, transformers, and LLMs, to be picked up by agents directly. That might be interesting, but it should not overshadow the compute network itself.

NAAP and Storyboard should not be used. We should have the minimal required components to enable the Livepeer Agent go-to-market, but not over-optimise or complicate. Nothing from the listed functions should remain in Agent 2.0 as a canonical service; catalog, price, invocation, errors, credentials, job tracking, usage, and cost reporting belong to the SDK, orchestrator, and clearinghouse.

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's view; Storyboard is understood to be deprecated

**Required owner or follow-up:** Confirm with Steph on product direction and the Storyboard deprecation

### 8. SDK Service and gateway roles

Classify each component as **Permanent**, **Transitional**, **Replace**, **Not
in target**, or **Unknown**.

| Component | Classification in target | Current fact, target recommendation, or unknown | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| SDK Service in `simple-infra` | Not in target | Target recommendation | Medium | Made by Inc; respondent has not looked into it much, but there is no need to base the architecture on their infra. |
| Python gateway SDK | Permanent | Target recommendation | High | The SDK is the builder-facing interface (see questions 5 and 6). |
| `go-livepeer` gateway | Not in target | Current fact | High | Deprecated. Clients make their own gateways if they need one. |
| Hosted routing or discovery service | Transitional or optional | Target recommendation | Medium | Discovery is the remote signer, or a network-wide aggregator that adds more data on top. Hosted routing can be done if the ecosystem wants to host a network product, but it is not a core component. |

**Intended owner of Orchestrator selection and failover:** The client SDK, informed by the remote signer or aggregator data. Clients that need more build their own gateway logic.

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
- [ ] Another field: `{DESCRIBE}`
- [ ] Unknown

**Current facts:** The ServiceRegistry holds orchestrator identity and service URI. Discovery endpoints and the remote signer already carry the rest off-chain and are quite versatile, though they need better signing and security.

**Target recommendations:** On-chain does not need much information. Communication can be done off-chain through the discovery endpoints and remote signer. The less on-chain the better from a protocol maintainability perspective. Only put things on-chain if an off-chain solution does not suffice. I am curious to hear what Mike has to say here, since he looked into it.

**Confidence:** Medium

**Basis/source:** Respondent's protocol maintainability view; current ServiceRegistry contents; Mike's investigation to be heard

### 10. Dynamic discovery and selection

Identify the intended owner for each responsibility. Candidate owners include
the on-chain registry, `go-livepeer` gateway, SDK, SDK Service, clearinghouse,
Live Runner control plane, or a separate service.

| Responsibility | Intended owner | Classification | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| Enumerate eligible Orchestrators | On-chain ServiceRegistry (identity and service URI only) | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Obtain current Live Runner capabilities | Orchestrator discovery endpoint, via the remote signer | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Obtain capacity and health | Orchestrator discovery endpoint, via the remote signer; a network-wide aggregator may add more data on top | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Obtain prices or rates | Orchestrator (fixed price per second per GPU type), exposed through the discovery endpoint and remote signer | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Filter incompatible or unavailable supply | Client SDK | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Select an Orchestrator | Client SDK, informed by remote signer or aggregator data | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Retry or fail over | Client SDK; clients needing more build their own gateway logic | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |
| Expose a builder-facing capability catalog | Remote signer, or a network-wide aggregator if the ecosystem hosts one | Target recommendation | Low | First response; derived from the respondent's answers to questions 5 and 8. Many decisions still open. |

**Respondent note:** Hard to say right now, since so many decisions still have to be made. Treat this table as a first response, not a position. Discovery is partly the remote signer, or a hosted aggregator on top if deemed needed based on complexity and the need for a network product, and partly the SDK. Some components are better placed in one of these than the other; the table above is the current best split, not a fixed assignment.

## Section 5: Clearinghouse and payment

### 11. Hosted Pymthouse and `livepeer/clearinghouse`

What is their relationship?

- [ ] Pymthouse deploys `livepeer/clearinghouse`
- [ ] Pymthouse is a fork or derivative of that repository
- [ ] They are separate implementations
- [ ] One is intended to replace the other
- [x] Another relationship: `livepeer/clearinghouse` is an example, not a maintained suite. Combined with updated docs, it shows all the components needed to attach metering, billing, and authentication to a remote signer on Livepeer. Pymthouse is the hosted, community-maintained clearinghouse built on the same remote-signer approach.
- [ ] Unknown

**Classification:** Current fact

**Confidence:** High

**Basis/source:** Respondent's knowledge of the clearinghouse repository's purpose and John's Pymthouse plan

**Person who can verify:** John Mull for Pymthouse

### 12. Clearinghouse direction

Which direction should the architecture process evaluate as the likely target?

- [x] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] Both behind a common clearinghouse contract
- [ ] A new Build Track implementation
- [ ] No clearinghouse in the target architecture
- [ ] Unknown pending requirements and deployment evidence

**Rationale:** The main thing is the remote signer and ensuring people know how to attach metering, billing, and authentication to it. Right now we do not have people running clearinghouses, so there is no need to keep extending a suite without real users of it. Pymthouse is more important if you want to simplify onboarding for go-to-market spikes, hackathons, grants, and similar. The focus should be there: work with John to trim Pymthouse to scope and make it production-ready, while keeping support for people who want to run their own clearinghouse if we get any.

**Unmet requirement requiring a new implementation, if selected:** Not applicable

**Classification:** Target recommendation

**Confidence:** High

**Required owner or follow-up:** John Mull to confirm Pymthouse scope, production readiness, and ownership

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
- [ ] Another scope: `{DESCRIBE}`
- [ ] Unknown; Rich or another named authority must confirm

**Required authority or confirmation:** Rich confirms the payment-path scope. Mike must set up agreed, paid deliverables with John for Pymthouse.

**Wallet-funded path owner and minimum acceptance evidence:** The Python SDK with a funded wallet. Evidence: a paid Live Runner call completed through the SDK.

**Walletless path owner and minimum acceptance evidence:** Pymthouse, owned by John Mull, as an external dependency, but only if Mike does not feel blocked by Pymthouse in hitting his deliverables. He needs to set up agreed deliverables with John, for which John gets paid, or create his own clearinghouse. Evidence: a builder completes a paid Live Runner call through Pymthouse without holding crypto.

After authorization, should both paths use the same builder-facing invocation,
job, result, usage, and charge interfaces?

- [x] Yes
- [ ] No; the required differences are: `{DESCRIBE}`
- [ ] Unknown

For the walletless journey, which evidence is required before “pay without
holding crypto” is satisfied? Mark all that apply.

- [x] One ordinary builder credential
- [x] Self-service credential issuance
- [x] Balance or allowance enforcement
- [x] Successful signer authorization
- [x] A payment ticket attached to the job
- [x] Winning-ticket redemption or fee visible on-chain (note: unclear what is meant. Ticket redemption is probabilistic, so a single job's fee is not necessarily visible on-chain; fees are visible in aggregate once tickets win. If this item means every job must be individually visible on-chain, that is a protocol change and not what I am confirming. I am confirming that the payment path settles on-chain end to end.)
- [x] Usage recorded by the clearinghouse
- [x] Per-job usage and charge receipt
- [x] Understandable insufficient-funds or payment failure
- [x] Another requirement: The full payment path end to end. People pay with Stripe or fiat, a clearinghouse tracks and deducts usage correctly, people get their job done through the SDK, and the fees show up on-chain.
- [ ] Unknown

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Respondent's view; John's Pymthouse plan; current Python SDK and remote-signer behaviour

**Comments or constraints:** The Pymthouse vision is bigger than what the ecosystem might need in its current form to hit Mike's deliverables and gain adoption. Focus is crucial: trim Pymthouse to the Build Track scope rather than adopting the full vision.

Based on the go-to-market, walletless is the more powerful path to onboard more demand. But when working with partners, they might benefit more from better remote-signer integration with their own stack than from a hosted walletless service. Let the demand bets focus the engineering: decide which path gets effort based on which partners are actually being pursued.

## Section 6: Risks and next participants

### 14. Largest unresolved concern

What single unresolved fact, architecture choice, ownership boundary, or
dependency is most likely to prevent clear December requirements?

**Answer:** Two blockers for a December release.

1. John's Pymthouse does not have very clear agreed requirements that need to be hit for the Network Engineering SPE. John also has his own vision and roadmap, with a lot more ideas and features he wants to implement, which can lead to delays on Mike's track. Before starting the work, a very clear agreement and RACI has to be made with John about what Pymthouse will ship to support the network SPE, and how payouts and decision making for this work.

2. Product scope growing too big or too frequently. In the past, go-to-market has shifted too quickly and too much for the network to really build what is needed. There has to be a good agreement with the partners (Livepeer Agent, frameworks, Streamplace, and others) about what will give the most demand growth, which bets will be pursued before December, and what will be delivered for those bets. This is not a demand-generation requirement on the Build Track; it is an input the Build Track needs from the partners and go-to-market owners before its scope can be fixed.

**Classification:** Current fact (unresolved state) with a target recommendation on how to resolve it

**Confidence:** High

**Required owner or follow-up:** Mike and John for the Pymthouse agreement and RACI. Mike with Steph and the partners for the product scope and bets agreement.

### 15. Specialist follow-up

Which targeted 25–30 minute discussion is likely to be required after Workshop
Part 1? Mark all that apply and name the required participants.

- [x] Hosted Pymthouse and `livepeer/clearinghouse` (Steph, Mike, John)
- [x] ServiceRegistry, gateway discovery, and Live Runner registration (Mike, Josh)
- [ ] Agent 2.0 and SDK Service integration
- [x] Identity, signer, payment, and metering (Steph, John, Mike)
- [x] Repository ownership and deployment (Rick, Josh, Mike)
- [ ] No specialist session expected
- [x] Another session: (a) Mike and Rick, 1 hour, to talk things through and do some knowledge challenge. (b) Shane and Mike, since Shane has thought a lot about the product side and is very integrated in the agent space.
- [ ] Unknown

**Required participants:** As listed per session above. Agent 2.0 and SDK Service integration is left unticked because that track is too uncertain for me to say whether a session is needed, not because it is ruled out.

**Rationale:** The Pymthouse and identity/payment sessions close the Pymthouse requirements and RACI gap from question 14. The ServiceRegistry session settles the discovery split from questions 9 and 10. The repository ownership session fixes who owns which repo and deployment before work starts. The Steph and Josh agreements from question 14 are covered inside these sessions.

## Respondent confirmation

Review the entire response before completing this section.

- [x] I reviewed the completed Markdown and it accurately represents my answers. (Disclaimer: answered through an agent-guided interview due to time constraints; each answer was reviewed as it was recorded, but the full file was not independently re-read.)
- [x] The original questions and answer choices were preserved. (Verified by the agent against the template; same disclaimer as above.)
- [x] I distinguished current facts, target recommendations, and unknowns. (Same disclaimer as above.)
- [x] I did not include credentials, tokens, private keys, private contact data,
      or security-sensitive operational details.
- [x] I understand that this response is diagnostic input, not a vote or
      architecture approval.

**Confirmed by:** Rick Staa

**Confirmation date:** 2026-09-07
