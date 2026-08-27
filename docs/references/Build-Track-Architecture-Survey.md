# Build Track Architecture Survey

**Status:** Draft survey instrument

**Prepared:** 26 August 2026

**Owner:** Mike Zupper

**Expected completion time:** 10–15 minutes

**Execution bead:** `netspe-vun.9`

## Survey objective

This survey prepares a focused architecture discussion with Rick Staa, Josh
Allmann, Mike Zupper, and any identified subject-matter experts. It is designed
to reveal agreements, conflicting assumptions, missing facts, missing
components, and decision-authority gaps before the first workshop.

The survey is diagnostic. It is not a vote, approval process, requirements
document, or substitute for architecture review. “Unknown” is a valuable answer
and should be selected instead of guessing.

## Suggested distribution message

**Subject:** Pre-work: Build Track outcomes and Live Runner architecture survey

> We are preparing a two-part discussion to translate the Network Engineering
> SPE Build Track outcomes into an end-state architecture and reviewable
> September–December milestones. Please complete this 10–15 minute survey before
> the stated deadline.
>
> The proposed execution focus is Live Runner. The full builder experience also
> crosses Agent 2.0, SDK or gateway interfaces, identity, discovery,
> ServiceRegistry behavior, clearinghouse and signer services, pricing, errors,
> metering, usage, and charges.
>
> Responses are inputs to the workshop, not binding votes. Select “Unknown” when
> a fact, target design, or approval boundary is unclear. The synthesis will
> identify disagreements and questions without attributing consensus where none
> exists.

Include links to:

- [the architecture-alignment process](Build-Track-Architecture-Alignment-Process.md);
- [the current-state diagram and traceability report](Build-Track-Repo-Traceability.md#component-diagram);
- [the seven-outcome working draft](Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise); and
- [the draft milestone proposal](../design-docs/cloud-spe-september-december-2026-milestones-draft.md).

## Respondents

Required initial respondents:

- Mike Zupper;
- Rick Staa; and
- Josh Allmann.

Potential additional respondents:

- John Mull (Elite Encoder) Pymthouse;
- the Agent 2.0/Storyboard technical owner;
- the SDK Service owner;
- `livepeer/clearinghouse` maintainers; and
- other repository or deployment owners identified by Rick or Josh.

Responses from subject-matter experts establish facts and feasibility. They do
not automatically establish programme or Cloud SPE approval.

## Survey instructions

- Answer based on the intended December architecture, not only current code.
- Use comments to distinguish what exists from what you recommend.
- Select “Unknown” where repository state, deployment state, ownership, or
  intent has not been verified.
- Name another person when they are better positioned to answer.
- Do not spend more than 10–15 minutes. Complex issues belong in the workshops
  or a targeted specialist session.

## Section 1: respondent context and authority

### 1. Role and relevant authority

**Response type:** Short text plus multi-select

Provide your role and select the areas where you can provide authoritative
facts, architectural direction, repository approval, or programme approval:

- Build Track outcome or milestone authority;
- Cloud SPE scope authority;
- `go-livepeer` architecture;
- `go-livepeer` merge or release approval;
- Live Runner architecture;
- Live Runner merge or release approval;
- Agent 2.0/Storyboard;
- SDK Service;
- hosted Pymthouse;
- `livepeer/clearinghouse`;
- ServiceRegistry contracts;
- deployment or operations; or
- other, with explanation.

### 2. Missing decision makers

**Response type:** Short text

Who must participate or approve before the end-state architecture can be
accepted? Name the person, team, repository, and decision where possible.

## Section 2: outcomes and scope

### 3. Live Runner execution focus

**Response type:** Single select plus optional comment

Should the September–December target architecture use Live Runner as its
execution focus?

- Yes;
- no;
- yes, with stated constraints; or
- unknown.

### 4. Proposed execution non-goals

**Response type:** One choice per row

For each path, select **exclude**, **include**, or **unknown**:

| Execution path | Proposed treatment |
| --- | --- |
| Batch AI | Exclude from target scope |
| BYOC | Exclude from target scope |
| LV2V | Exclude from target scope |
| Transcoding | Exclude from target scope |

Use the comment field to identify any required compatibility or migration work
that remains relevant even when execution is excluded.

### 5. Seven builder outcomes

**Response type:** Matrix with short text and confidence

For each outcome, name the component you believe should be authoritative in the
end-state architecture. “Unknown” is acceptable.

| Builder outcome | Intended authoritative component | Confidence: high, medium, or low |
| --- | --- | --- |
| Obtain one credential |  |  |
| Discover what the network can do |  |  |
| Understand the expected price or rate |  |  |
| Invoke a capability through a standard interface |  |  |
| Receive a result or understandable failure |  |  |
| Pay without holding crypto |  |  |
| See usage and resulting charge |  |  |

## Section 3: builder-facing components

### 6. Primary builder-facing interface

**Response type:** Single select plus comment

What should an independent builder call in the target architecture?

- Agent 2.0/Storyboard;
- a supported SDK;
- a hosted gateway API;
- a direct `go-livepeer` gateway API;
- multiple supported interfaces over one common platform contract;
- another interface; or
- unknown.

### 7. Agent 2.0 role

**Response type:** Single select plus comment

What should Agent 2.0/Storyboard be by December?

- the canonical builder-facing interface;
- a reference integration over canonical platform APIs;
- one application among multiple applications;
- a transitional implementation;
- outside the Build Track architecture; or
- unknown.

Identify which current Agent responsibilities should remain in the Agent and
which should move to canonical services: capability catalog, price estimate,
invocation, error normalization, credential handling, job tracking, usage, and
cost reporting.

### 8. SDK Service and gateway roles

**Response type:** One choice per row plus comment

Classify each component as **permanent**, **transitional**, **replace**, **not in
target**, or **unknown**:

| Component | Classification |
| --- | --- |
| SDK Service in `simple-infra` |  |
| Python gateway SDK |  |
| `go-livepeer` gateway |  |
| Hosted routing or discovery service |  |

Name the component that should own Orchestrator selection and failover.

## Section 4: ServiceRegistry and discovery

### 9. On-chain ServiceRegistry role

**Response type:** Multi-select plus comment

What should be represented on-chain in the target architecture?

- Orchestrator identity or address;
- service URI;
- Live Runner capability identifiers;
- capability versions;
- hardware information;
- capacity;
- health;
- prices or rates;
- none of these;
- another field; or
- unknown.

Mark which selected fields are current facts and which are target-design
recommendations.

### 10. Dynamic discovery and selection

**Response type:** One component per responsibility

Identify the intended owner for each responsibility:

| Responsibility | Intended owner |
| --- | --- |
| Enumerate eligible Orchestrators |  |
| Obtain current Live Runner capabilities |  |
| Obtain capacity and health |  |
| Obtain prices or rates |  |
| Filter incompatible or unavailable supply |  |
| Select an Orchestrator |  |
| Retry or fail over |  |
| Expose a builder-facing capability catalog |  |

Candidate owners include the on-chain registry, `go-livepeer` gateway, SDK,
SDK Service, clearinghouse, Live Runner control plane, or a separate service.

## Section 5: clearinghouse and payment

### 11. Hosted Pymthouse and `livepeer/clearinghouse`

**Response type:** Single select, confidence, and referral

What is their relationship?

- Pymthouse deploys `livepeer/clearinghouse`;
- Pymthouse is a fork or derivative of that repository;
- they are separate implementations;
- one is intended to replace the other;
- another relationship; or
- unknown.

State the basis for the answer and name the person who can verify it.

### 12. Clearinghouse direction

**Response type:** Single select plus rationale

Which direction should the architecture process evaluate as the likely target?

- hosted Pymthouse;
- `livepeer/clearinghouse`;
- both behind a common clearinghouse contract;
- a new Build Track implementation;
- no clearinghouse in the target architecture; or
- unknown pending requirements and deployment evidence.

If selecting a new implementation, identify the requirement that cannot be met
by either existing option.

### 13. Walletless payment definition of done

**Response type:** Multi-select plus comment

Which evidence is required before “pay without holding crypto” is satisfied?

- one ordinary builder credential;
- self-service credential issuance;
- balance or allowance enforcement;
- successful signer authorization;
- a payment ticket attached to the job;
- winning-ticket redemption or fee visible on-chain;
- usage recorded by the clearinghouse;
- per-job usage and charge receipt;
- understandable insufficient-funds or payment failure;
- another requirement; or
- unknown.

## Section 6: risks and next participants

### 14. Largest unresolved concern

**Response type:** Short text

What single unresolved fact, architecture choice, ownership boundary, or
dependency is most likely to prevent clear December requirements?

### 15. Specialist follow-up

**Response type:** Multi-select plus referral

Which targeted 25–30 minute discussion is likely to be required after Part 1?

- hosted Pymthouse and `livepeer/clearinghouse`;
- ServiceRegistry, gateway discovery, and Live Runner registration;
- Agent 2.0 and SDK Service integration;
- identity, signer, payment, and metering;
- repository ownership and deployment;
- no specialist session expected;
- another session; or
- unknown.

Name the required participants for every selected session.

## Survey administration

Use a form tool for structured collection and preserve an export or normalized
summary in the repository after responses are received. Do not store private
contact details, credentials, access tokens, or sensitive operational data in
this repository.

Use a separate scheduling poll for availability. Combining architecture and
availability questions makes the survey harder to complete within 10–15
minutes and complicates synthesis.

## Synthesis method

For each question, classify results as:

| Result | Interpretation | Part 1 treatment |
| --- | --- | --- |
| Aligned fact | Respondents agree and an authoritative source is available | Confirm briefly and cite the source |
| Aligned preference | Respondents prefer the same target but it is not approved | Present as a proposal requiring authority |
| Divergent architecture | Respondents select materially different target designs | Allocate discussion time and prepare alternatives |
| Factual uncertainty | Respondents disagree about current code, deployment, or ownership | Assign verification or specialist follow-up |
| Authority gap | No respondent can approve the required decision | Identify and invite or escalate to the authority |
| Low-confidence area | Most confidence responses are low or unknown | Avoid treating it as settled; prioritize evidence |

Do not report plurality as consensus. Preserve meaningful minority objections
and distinguish responses based on verified ownership from general preference.

## Survey synthesis template

### Response coverage

| Invited role | Response received | Authority represented | Important limitation |
| --- | --- | --- | --- |
| Build Track/Cloud SPE |  |  |  |
| Foundation technical gate |  |  |  |
| Livepeer Inc/Live Runner architecture |  |  |  |
| Clearinghouse specialist |  |  |  |
| Agent 2.0 specialist |  |  |  |

### Agreements and disagreements

| Topic | Current fact | Preferred target | Confidence | Disagreement or unknown | Part 1 action |
| --- | --- | --- | --- | --- | --- |
| Live Runner scope |  |  |  |  |  |
| Builder-facing interface |  |  |  |  |  |
| Agent 2.0 role |  |  |  |  |  |
| Gateway and SDK Service |  |  |  |  |  |
| On-chain ServiceRegistry |  |  |  |  |  |
| Runtime discovery |  |  |  |  |  |
| Clearinghouse relationship |  |  |  |  |  |
| Clearinghouse direction |  |  |  |  |  |
| Walletless definition of done |  |  |  |  |  |

### Outcome ownership

| Builder outcome | Candidate authoritative component | Conflicting answer | Missing owner | Part 1 question |
| --- | --- | --- | --- | --- |
| One credential |  |  |  |  |
| Discover |  |  |  |  |
| Price |  |  |  |  |
| Invoke |  |  |  |  |
| Result or failure |  |  |  |  |
| Walletless payment |  |  |  |  |
| Usage and charge |  |  |  |  |

## Completion evidence

The survey work is ready for Part 1 when:

- required respondents have answered or their absence is documented;
- responses are exported or normalized safely;
- facts, preferences, unknowns, and decision authority are separated;
- the seven outcomes are represented in the synthesis;
- the highest-impact disagreements are selected for Part 1;
- missing specialists are named; and
- the synthesis is distributed with the final Part 1 agenda.
