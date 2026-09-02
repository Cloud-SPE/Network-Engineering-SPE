# Build Track Architecture Survey Response

**Expected completion time:** 10–15 minutes

**Survey version:** `Unknown`

**Respondent:** `Shane`

**Role:** `Validation Owner`

**Date completed:** `2026-09-01`

Read the [survey instructions](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/main/docs/references/Build-Track-Architecture-Survey-Instructions.md)
before beginning. Preserve the original questions and answer choices. Replace
the answer placeholders, mark unanswerable items as **Unknown**, and review the
completed file yourself before returning it.

## Section 1: Respondent context and authority

### 1. Role and relevant authority

Briefly describe your role:

**Answer:** Helping build Livepeer 2.0 by owning validation, which touches all
aspects of the protocol. Also building with the SDK, Agent 2.0, and related
components.

Mark every area where you can provide authoritative facts, architectural
direction, repository approval, or programme approval:

- [ ] Build Track outcome or milestone authority
- [ ] Cloud SPE scope authority
- [x] `go-livepeer` architecture
- [ ] `go-livepeer` merge or release approval
- [ ] Live Runner architecture
- [ ] Live Runner merge or release approval
- [x] Agent 2.0/Storyboard
- [x] SDK Service
- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [x] ServiceRegistry contracts
- [ ] Deployment or operations
- [ ] Other: None

**Classification:** Target recommendation

**Confidence:** High

**Basis/source:** Written role description

### 2. Missing decision makers

Who else must participate or approve before the end-state architecture can be
accepted? Name the person, team, repository, and decision where possible.

**Answer:** The DAO

**Classification:** Unknown

**Confidence:** Unknown

**Basis/source:** Unknown

**Required owner or follow-up:** The DAO

## Section 2: Outcomes and scope

### 3. Live Runner execution focus

Should the September–December target architecture use Live Runner as its
execution focus?

- [ ] Yes
- [ ] No
- [ ] Yes, with constraints
- [x] Unknown

**Constraints or explanation:** Unknown

**Classification:** Unknown

**Confidence:** Unknown

**Basis/source:** Unknown

What should “supported Live Runner service types” mean for December acceptance?

- [x] A reusable Live Runner service contract proven through at least one
      representative capability
- [x] A prescribed minimum set of named capabilities
- [ ] One fixed capability without a general extensibility commitment
- [x] Another support model: A reusable architectural contract together with a
      prescribed minimum capability set accessible to agent builders
- [ ] Unknown

The working assumption is the reusable-contract option. It requires
confirmation from Rich on outcome intent and from Rick and Josh on architecture
and delivery feasibility before it becomes an accepted requirement.

**Representative capability or selection owner:** Unknown

**Required named capability list, if any:** A generative-media capability
(exact capability unknown); the `openai:audio-transcriptions` media-processing
capability implemented by
[audio-diarized-transcription-runner](https://github.com/moatus/audio-diarized-transcription-runner);
and a general inference LLM capability. This set is intended to cover
generative media, media processing, and general inference needs for agent
builders.

**Do all supported capabilities have to satisfy the complete confirmed builder journey?** Yes

**Confirmation or follow-up required from Rich, Rick, and Josh:** Unknown

### 4. Proposed execution non-goals

For each path, enter **Exclude**, **Include**, or **Unknown**. Identify required
compatibility or migration work even when execution is excluded.

| Execution path | Your answer | Classification | Confidence | Constraint, basis, or follow-up |
| --- | --- | --- | --- | --- |
| Batch AI | Unknown | Unknown | Unknown | Requires architecture brainstorming; the current execution paths and surrounding components are fragmented and need a clearer, cohesive structure. |
| BYOC | Unknown | Unknown | Unknown | Requires architecture brainstorming; the current execution paths and surrounding components are fragmented and need a clearer, cohesive structure. |
| LV2V | Unknown | Unknown | Unknown | Requires architecture brainstorming; the current execution paths and surrounding components are fragmented and need a clearer, cohesive structure. |
| Transcoding | Unknown | Unknown | Unknown | Requires architecture brainstorming; the current execution paths and surrounding components are fragmented and need a clearer, cohesive structure. |

### 5. Seven builder outcomes

For each outcome, name the component that should be authoritative in the
intended architecture. Use **Unknown** rather than guessing.

| Builder outcome | Intended authoritative component | Classification | Confidence | Basis or required follow-up |
| --- | --- | --- | --- | --- |
| Obtain one credential | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| Discover what the network can do | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| Understand the expected price or rate | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| Invoke a capability through a standard interface | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| Receive a result or understandable failure | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| Pay without holding crypto | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |
| See usage and resulting charge | Unknown | Unknown | Unknown | Important to agent-tooling builders and a current pain point; respondent is not sufficiently familiar with the protocol architecture to assign ownership. Brainstorming required. |

## Section 3: Builder-facing components

### 6. Primary builder-facing interface

What should an independent builder call in the target architecture?

- [ ] Agent 2.0/Storyboard
- [x] A supported SDK
- [x] A hosted gateway API
- [ ] A direct `go-livepeer` gateway API
- [ ] Multiple supported interfaces over one common platform contract
- [ ] Another interface: None
- [ ] Unknown

**Rationale or constraints:** A supported SDK should provide a self-hostable,
customizable builder experience, while a hosted gateway API should provide
quick endpoint access.

**Classification:** Target recommendation

**Confidence:** Unknown

**Basis/source:** Respondent's experience building agent tooling

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

**Answer:** Livepeer should build and own the core platform software and
interfaces. Agent 2.0 should primarily wrap Livepeer around popular software
that builders already use, making those capabilities immediately accessible
through Livepeer. Roboflow is one example of this integration model, with
Diffusion Studio and other popular software as possible future integrations.

**Classification:** Target recommendation

**Confidence:** Unknown

**Basis/source:** Respondent's experience building Livepeer integrations with
agent tooling

**Required owner or follow-up:** Unknown

### 8. SDK Service and gateway roles

Classify each component as **Permanent**, **Transitional**, **Replace**, **Not
in target**, or **Unknown**.

| Component | Classification in target | Current fact, target recommendation, or unknown | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| SDK Service in `simple-infra` | Unknown | Unknown | Unknown | Respondent is not fully familiar with this component; brainstorm its target role. |
| Python gateway SDK | Unknown | Unknown | Unknown | Respondent is not fully familiar with this component; brainstorm its target role. |
| `go-livepeer` gateway | Unknown | Unknown | Unknown | Respondent is not fully familiar with this component; brainstorm its target role. |
| Hosted routing or discovery service | Replace | Target recommendation | Unknown | Replace the current service as part of a redesigned discovery architecture. |

**Intended owner of Orchestrator selection and failover:** Unknown

## Section 4: ServiceRegistry and discovery

### 9. On-chain ServiceRegistry role

What should be represented on-chain in the target architecture? Mark all that
apply, then distinguish current facts from target recommendations.

- [x] Orchestrator identity or address
- [x] Service URI
- [x] Live Runner capability identifiers
- [x] Capability versions
- [x] Hardware information
- [x] Capacity
- [x] Health
- [ ] Prices or rates
- [ ] None of these
- [ ] Another field: None
- [ ] Unknown

**Current facts:** Unknown

**Target recommendations:** Keep the selected fields above on-chain. A free,
Foundation-operated off-chain discovery API should provide prices or rates,
Capability API, capability category, and agent-facing usage guidance. Lean
toward unified pricing for equivalent capabilities until the marketplace
matures. The usage-guidance field should provide the special instructions and
metadata agents need to understand how to use a capability.

**Confidence:** Unknown

**Basis/source:** Respondent's architecture recommendation

### 10. Dynamic discovery and selection

Identify the intended owner for each responsibility. Candidate owners include
the on-chain registry, `go-livepeer` gateway, SDK, SDK Service, clearinghouse,
Live Runner control plane, or a separate service.

| Responsibility | Intended owner | Classification | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| Enumerate eligible Orchestrators | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Initially unify and nurture the market through a Foundation-hosted service. |
| Obtain current Live Runner capabilities | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Initially unify and nurture the market through a Foundation-hosted service. |
| Obtain capacity and health | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Initially unify and nurture the market through a Foundation-hosted service. |
| Obtain prices or rates | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Initially use unified pricing for equivalent capabilities. |
| Filter incompatible or unavailable supply | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Prioritize capability quality and a consistent builder experience. |
| Select an Orchestrator | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Prioritize capability quality and a consistent builder experience. |
| Retry or fail over | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Prioritize capability quality and a consistent builder experience. |
| Expose a builder-facing capability catalog | Free Foundation-hosted discovery and routing service | Target recommendation | Unknown | Present a unified builder experience. |

The Foundation-hosted service should initially prioritize capability quality
over Orchestrator competition. As the market matures, progressively open
discovery, selection, and pricing into a more competitive marketplace.

## Section 5: Clearinghouse and payment

### 11. Hosted Pymthouse and `livepeer/clearinghouse`

What is their relationship?

- [ ] Pymthouse deploys `livepeer/clearinghouse`
- [ ] Pymthouse is a fork or derivative of that repository
- [ ] They are separate implementations
- [ ] One is intended to replace the other
- [ ] Another relationship: None
- [x] Unknown

**Classification:** Unknown

**Confidence:** Unknown

**Basis/source:** Unknown

**Person who can verify:** Unknown

### 12. Clearinghouse direction

Which direction should the architecture process evaluate as the likely target?

- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] Both behind a common clearinghouse contract
- [ ] A new Build Track implementation
- [ ] No clearinghouse in the target architecture
- [x] Unknown pending requirements and deployment evidence

**Rationale:** The respondent is not sufficiently familiar with the
clearinghouse implementations to select one. Evaluate an ecosystem-native
option such as `livepeer/clearinghouse` or a new Build Track implementation.
Users should pay in stablecoins. Also evaluate whether DeFi automation could
handle settlement directly, potentially reducing or eliminating the
traditional clearinghouse role.

**Unmet requirement requiring a new implementation, if selected:** Not
applicable; requirements and deployment evidence are not yet established.

**Classification:** Unknown for the implementation selection; target
recommendations are recorded in the rationale.

**Confidence:** Unknown

**Required owner or follow-up:** Architecture process and Livepeer 2.0
tokenomics owners

### 13. Payment-path scope and walletless definition of done

The working assumption is that both wallet-funded and walletless payment
journeys are in the December target, pending confirmation from Rich. This does
not assume that the Cloud SPE implements every part of both journeys or that
hosted Pymthouse is the selected walletless implementation.

Which payment-path scope should the architecture and milestone process use?
Select one.

- [ ] Both journeys are required Build Track acceptance paths
- [ ] Both are required in the target architecture, but one or more paths are
      external dependencies or compatibility obligations rather than Cloud SPE
      deliverables
- [ ] Walletless is required; wallet-funded compatibility is not a Build Track
      acceptance path
- [ ] Another scope: None
- [x] Unknown; Rich or another named authority must confirm

**Required authority or confirmation:** Unknown

**Wallet-funded path owner and minimum acceptance evidence:** The wallet-funded
journey should use a straightforward, direct DeFi path without an intermediary.
Specific owner and minimum acceptance evidence are unknown.

**Walletless path owner and minimum acceptance evidence:** The walletless
journey should be owned by a centralized service provider such as Cloud SPE or
another clearinghouse. Specific owner and minimum acceptance evidence are
unknown.

After authorization, should both paths use the same builder-facing invocation,
job, result, usage, and charge interfaces?

- [ ] Yes
- [ ] No; the required differences are: Unknown
- [x] Unknown

For the walletless journey, which evidence is required before “pay without
holding crypto” is satisfied? Mark all that apply.

- [ ] One ordinary builder credential
- [ ] Self-service credential issuance
- [ ] Balance or allowance enforcement
- [ ] Successful signer authorization
- [ ] A payment ticket attached to the job
- [ ] Winning-ticket redemption or fee visible on-chain
- [ ] Usage recorded by the clearinghouse
- [ ] Per-job usage and charge receipt
- [ ] Understandable insufficient-funds or payment failure
- [ ] Another requirement: None
- [x] Unknown

**Classification:** Unknown

**Confidence:** Unknown

**Basis/source:** Respondent's target-direction input; final payment scope and
acceptance evidence remain unknown.

**Comments or constraints:** Users should pay in stablecoins. Wallet-funded
calls should have a direct DeFi path; walletless calls should use a centralized
provider.

## Section 6: Risks and next participants

### 14. Largest unresolved concern

What single unresolved fact, architecture choice, ownership boundary, or
dependency is most likely to prevent clear December requirements?

**Answer:** The actual Livepeer 2.0 tokenomics described by the forthcoming
litepaper. The respondent has not seen the litepaper and cannot determine what
will ultimately work. The tokenomics are likely to have the largest impact
across payment, clearinghouse, DeFi, pricing, and other architecture paths.

**Classification:** Unknown

**Confidence:** Unknown

**Required owner or follow-up:** Review the Livepeer 2.0 litepaper and obtain
direction from its authors or responsible approvers.

### 15. Specialist follow-up

Which targeted 25–30 minute discussion is likely to be required after Workshop
Part 1? Mark all that apply and name the required participants.

- [ ] Hosted Pymthouse and `livepeer/clearinghouse`
- [x] ServiceRegistry, gateway discovery, and Live Runner registration
- [x] Agent 2.0 and SDK Service integration
- [ ] Identity, signer, payment, and metering
- [ ] Repository ownership and deployment
- [ ] No specialist session expected
- [x] Another session: Livepeer 2.0 tokenomics
- [ ] Unknown

**Required participants:** Unknown

**Rationale:** Resolve the registry/discovery/registration architecture,
clarify the boundary between core services and Agent 2.0 integrations, and
understand the tokenomics constraints that may affect all architecture paths.

## Respondent confirmation

Review the entire response before completing this section.

- [x] I reviewed the completed Markdown and it accurately represents my answers.
- [x] The original questions and answer choices were preserved.
- [x] I distinguished current facts, target recommendations, and unknowns.
- [x] I did not include credentials, tokens, private keys, private contact data,
      or security-sensitive operational details.
- [x] I understand that this response is diagnostic input, not a vote or
      architecture approval.

**Confirmed by:** Shane

**Confirmation date:** 2026-09-01
