# Build Track Architecture Survey Response

**Expected completion time:** 10–15 minutes

**Survey version:** `{SURVEY_VERSION}`

**Respondent:** `{YOUR NAME}`

**Role:** `{YOUR ROLE}`

**Date completed:** `{YYYY-MM-DD}`

Read the [survey instructions](Build-Track-Architecture-Survey-Instructions.md)
before beginning. Preserve the original questions and answer choices. Replace
the answer placeholders, mark unanswerable items as **Unknown**, and review the
completed file yourself before returning it.

## Section 1: Respondent context and authority

### 1. Role and relevant authority

Briefly describe your role:

**Answer:** `{ENTER ANSWER}`

Mark every area where you can provide authoritative facts, architectural
direction, repository approval, or programme approval:

- [ ] Build Track outcome or milestone authority
- [ ] Cloud SPE scope authority
- [ ] `go-livepeer` architecture
- [ ] `go-livepeer` merge or release approval
- [ ] Live Runner architecture
- [ ] Live Runner merge or release approval
- [ ] Agent 2.0/Storyboard
- [ ] SDK Service
- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] ServiceRegistry contracts
- [ ] Deployment or operations
- [ ] Other: `{DESCRIBE}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

### 2. Missing decision makers

Who else must participate or approve before the end-state architecture can be
accepted? Name the person, team, repository, and decision where possible.

**Answer:** `{ENTER ANSWER OR UNKNOWN}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

**Required owner or follow-up:** `{ENTER ANSWER OR NONE}`

## Section 2: Outcomes and scope

### 3. Live Runner execution focus

Should the September–December target architecture use Live Runner as its
execution focus?

- [ ] Yes
- [ ] No
- [ ] Yes, with constraints
- [ ] Unknown

**Constraints or explanation:** `{ENTER ANSWER OR NONE}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

What should “supported Live Runner service types” mean for December acceptance?

- [ ] A reusable Live Runner service contract proven through at least one
      representative capability
- [ ] A prescribed minimum set of named capabilities
- [ ] One fixed capability without a general extensibility commitment
- [ ] Another support model: `{DESCRIBE}`
- [ ] Unknown

The working assumption is the reusable-contract option. It requires
confirmation from Rich on outcome intent and from Rick and Josh on architecture
and delivery feasibility before it becomes an accepted requirement.

**Representative capability or selection owner:** `{ENTER ANSWER OR UNKNOWN}`

**Required named capability list, if any:** `{ENTER ANSWER OR NONE}`

**Do all supported capabilities have to satisfy the complete confirmed builder journey?** `{YES | NO, EXPLAIN | UNKNOWN}`

**Confirmation or follow-up required from Rich, Rick, and Josh:** `{ENTER ANSWER OR UNKNOWN}`

### 4. Proposed execution non-goals

For each path, enter **Exclude**, **Include**, or **Unknown**. Identify required
compatibility or migration work even when execution is excluded.

| Execution path | Your answer | Classification | Confidence | Constraint, basis, or follow-up |
| --- | --- | --- | --- | --- |
| Batch AI |  |  |  |  |
| BYOC |  |  |  |  |
| LV2V |  |  |  |  |
| Transcoding |  |  |  |  |

### 5. Seven builder outcomes

For each outcome, name the component that should be authoritative in the
intended architecture. Use **Unknown** rather than guessing.

| Builder outcome | Intended authoritative component | Classification | Confidence | Basis or required follow-up |
| --- | --- | --- | --- | --- |
| Obtain one credential |  |  |  |  |
| Discover what the network can do |  |  |  |  |
| Understand the expected price or rate |  |  |  |  |
| Invoke a capability through a standard interface |  |  |  |  |
| Receive a result or understandable failure |  |  |  |  |
| Pay without holding crypto |  |  |  |  |
| See usage and resulting charge |  |  |  |  |

## Section 3: Builder-facing components

### 6. Primary builder-facing interface

What should an independent builder call in the target architecture?

- [ ] Agent 2.0/Storyboard
- [ ] A supported SDK
- [ ] A hosted gateway API
- [ ] A direct `go-livepeer` gateway API
- [ ] Multiple supported interfaces over one common platform contract
- [ ] Another interface: `{DESCRIBE}`
- [ ] Unknown

**Rationale or constraints:** `{ENTER ANSWER OR UNKNOWN}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

### 7. Agent 2.0 role

What should Agent 2.0/Storyboard be by December?

- [ ] The canonical builder-facing interface
- [ ] A reference integration over canonical platform APIs
- [ ] One sample or reference application
- [ ] A transitional implementation
- [ ] Outside the Build Track architecture
- [ ] Unknown

For capability catalog, price estimate, invocation, error normalization,
credential handling, job tracking, usage, and cost reporting, identify what
should remain in Agent 2.0 and what should move to canonical services.

**Answer:** `{ENTER ANSWER OR UNKNOWN}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

**Required owner or follow-up:** `{ENTER ANSWER OR NONE}`

### 8. SDK Service and gateway roles

Classify each component as **Permanent**, **Transitional**, **Replace**, **Not
in target**, or **Unknown**.

| Component | Classification in target | Current fact, target recommendation, or unknown | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| SDK Service in `simple-infra` |  |  |  |  |
| Python gateway SDK |  |  |  |  |
| `go-livepeer` gateway |  |  |  |  |
| Hosted routing or discovery service |  |  |  |  |

**Intended owner of Orchestrator selection and failover:** `{ENTER ANSWER OR UNKNOWN}`

## Section 4: ServiceRegistry and discovery

### 9. On-chain ServiceRegistry role

What should be represented on-chain in the target architecture? Mark all that
apply, then distinguish current facts from target recommendations.

- [ ] Orchestrator identity or address
- [ ] Service URI
- [ ] Live Runner capability identifiers
- [ ] Capability versions
- [ ] Hardware information
- [ ] Capacity
- [ ] Health
- [ ] Prices or rates
- [ ] None of these
- [ ] Another field: `{DESCRIBE}`
- [ ] Unknown

**Current facts:** `{ENTER ANSWER OR UNKNOWN}`

**Target recommendations:** `{ENTER ANSWER OR UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

### 10. Dynamic discovery and selection

Identify the intended owner for each responsibility. Candidate owners include
the on-chain registry, `go-livepeer` gateway, SDK, SDK Service, clearinghouse,
Live Runner control plane, or a separate service.

| Responsibility | Intended owner | Classification | Confidence | Basis or follow-up |
| --- | --- | --- | --- | --- |
| Enumerate eligible Orchestrators |  |  |  |  |
| Obtain current Live Runner capabilities |  |  |  |  |
| Obtain capacity and health |  |  |  |  |
| Obtain prices or rates |  |  |  |  |
| Filter incompatible or unavailable supply |  |  |  |  |
| Select an Orchestrator |  |  |  |  |
| Retry or fail over |  |  |  |  |
| Expose a builder-facing capability catalog |  |  |  |  |

## Section 5: Clearinghouse and payment

### 11. Hosted Pymthouse and `livepeer/clearinghouse`

What is their relationship?

- [ ] Pymthouse deploys `livepeer/clearinghouse`
- [ ] Pymthouse is a fork or derivative of that repository
- [ ] They are separate implementations
- [ ] One is intended to replace the other
- [ ] Another relationship: `{DESCRIBE}`
- [ ] Unknown

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

**Person who can verify:** `{ENTER ANSWER OR UNKNOWN}`

### 12. Clearinghouse direction

Which direction should the architecture process evaluate as the likely target?

- [ ] Hosted Pymthouse
- [ ] `livepeer/clearinghouse`
- [ ] Both behind a common clearinghouse contract
- [ ] A new Build Track implementation
- [ ] No clearinghouse in the target architecture
- [ ] Unknown pending requirements and deployment evidence

**Rationale:** `{ENTER ANSWER OR UNKNOWN}`

**Unmet requirement requiring a new implementation, if selected:** `{ENTER ANSWER OR NOT APPLICABLE}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Required owner or follow-up:** `{ENTER ANSWER OR NONE}`

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
- [ ] Another scope: `{DESCRIBE}`
- [ ] Unknown; Rich or another named authority must confirm

**Required authority or confirmation:** `{ENTER ANSWER OR UNKNOWN}`

**Wallet-funded path owner and minimum acceptance evidence:** `{ENTER ANSWER OR UNKNOWN}`

**Walletless path owner and minimum acceptance evidence:** `{ENTER ANSWER OR UNKNOWN}`

After authorization, should both paths use the same builder-facing invocation,
job, result, usage, and charge interfaces?

- [ ] Yes
- [ ] No; the required differences are: `{DESCRIBE}`
- [ ] Unknown

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
- [ ] Another requirement: `{DESCRIBE}`
- [ ] Unknown

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Basis/source:** `{ENTER SOURCE OR UNKNOWN}`

**Comments or constraints:** `{ENTER ANSWER OR NONE}`

## Section 6: Risks and next participants

### 14. Largest unresolved concern

What single unresolved fact, architecture choice, ownership boundary, or
dependency is most likely to prevent clear December requirements?

**Answer:** `{ENTER ANSWER OR UNKNOWN}`

**Classification:** `{CURRENT FACT | TARGET RECOMMENDATION | UNKNOWN}`

**Confidence:** `{HIGH | MEDIUM | LOW}`

**Required owner or follow-up:** `{ENTER ANSWER OR NONE}`

### 15. Specialist follow-up

Which targeted 25–30 minute discussion is likely to be required after Workshop
Part 1? Mark all that apply and name the required participants.

- [ ] Hosted Pymthouse and `livepeer/clearinghouse`
- [ ] ServiceRegistry, gateway discovery, and Live Runner registration
- [ ] Agent 2.0 and SDK Service integration
- [ ] Identity, signer, payment, and metering
- [ ] Repository ownership and deployment
- [ ] No specialist session expected
- [ ] Another session: `{DESCRIBE}`
- [ ] Unknown

**Required participants:** `{ENTER ANSWER OR UNKNOWN}`

**Rationale:** `{ENTER ANSWER OR NONE}`

## Respondent confirmation

Review the entire response before completing this section.

- [ ] I reviewed the completed Markdown and it accurately represents my answers.
- [ ] The original questions and answer choices were preserved.
- [ ] I distinguished current facts, target recommendations, and unknowns.
- [ ] I did not include credentials, tokens, private keys, private contact data,
      or security-sensitive operational details.
- [ ] I understand that this response is diagnostic input, not a vote or
      architecture approval.

**Confirmed by:** `{YOUR NAME}`

**Confirmation date:** `{YYYY-MM-DD}`
