# Rick Build Track Survey Discussion Agenda

**Status:** Draft facilitator agenda

**Meeting date:** 8 September 2026

**Meeting time:** 8:30 a.m. America/New_York (EDT)

**Planned duration:** 60 minutes

**Agenda blocks:** 15 minutes, 30 minutes, and 15 minutes

**Participants:** Mike Zupper and Rick Staa

**Execution bead:** `netspe-vun.9`

**Related Doug follow-up:** `netspe-vun.18`

## Meeting objective

Turn the survey findings into a concrete, technically feasible hypothesis for
what the Build Track will deliver by 31 December 2026. Resolve what Rick can
resolve as the Network Engineering SPE technical gate, identify questions that
require Josh or another repository owner, and isolate outcome questions that
must be decided by Rich, Doug, or the participating SPEs.

The meeting should end with named deliverable candidates, repositories,
owners, external dependencies, acceptance evidence, and decision authorities.
It should not treat Rick's survey response as programme approval or assign the
Cloud SPE work owned by another participant.

## Proposed December outcome statement

Ask Rick to accept, reject, or rewrite this statement before discussing a
feature list:

> By 31 December 2026, the Build Track will provide an independently
> reproducible paid Live Runner journey through a supported builder interface.
> A builder can discover eligible supply and pricing, invoke a requirements-
> selected capability, receive a result or understandable failure, complete
> each confirmed payment path, and reconcile usage and charges. The
> implementation, repositories, operational owners, external dependencies, and
> acceptance evidence are explicitly named.

Follow with:

1. Which parts are wrong, incomplete, or outside the Build Track?
2. Which subset is assigned to the Cloud SPE?
3. Is the December target production-ready, a production-oriented reference
   implementation, or a validated prototype?

## Important unconfirmed hypothesis: Doug's self-sovereign Agent

Rich relayed that Doug is leaning heavily toward a self-sovereign, wallet-based
setup and suggested examining x402 or another easy on-chain payment approach.
Doug has not yet clarified the intended product or architecture.

Mike's current hypothesis is that Doug may be distinguishing the Livepeer Inc
Agent 2.0/Storyboard product from an open-source agent experience that an
individual can operate independently of Livepeer Inc. That is a reasonable
question to test, but it is not an accepted interpretation of Doug's words.

The phrase “self-sovereign Agent” could mean materially different things:

| Possible meaning | Architecture implication | Required clarification |
| --- | --- | --- |
| A self-hostable distribution of the current Agent 2.0/Storyboard product | Storyboard or a fork becomes a Build Track artifact | Does Doug intend the current product code, and can it operate without Livepeer Inc services? |
| A new open-source reference agent over canonical Livepeer interfaces | The agent demonstrates the platform but is not its authoritative contract | Is a reference agent a December deliverable or only a validation aid? |
| Self-sovereign network primitives that any agent can use | SDK, discovery, payment, and Live Runner interfaces are the deliverable; applications remain external | Does “Agent” describe the user of the platform rather than a product to build? |
| A self-sovereign wallet and payment experience | Easy on-chain payment is the emphasis; no new agent application is implied | Is x402 an example, preferred direction, or required compatibility target? |
| A combination of the above | Scope may span product, platform, deployment, and payment work | Which elements are mandatory, optional, or owned outside the Cloud SPE? |

Do not leave the meeting describing Storyboard as both outside the target
architecture and the basis of a required self-sovereign product. Record what
Rick knows, what he recommends, and what only Doug can answer.

## Required pre-read

- [Rick's survey response](Build-Track-Architecture-Survey-Response-Rick-Staa-2026-09-07.md)
- [Josh's survey response](Build-Track-Architecture-Survey-Response-Josh-2026-08-31.md)
- [Shane's survey response](Build-Track-Architecture-Survey-Response-Shane-2026-09-01.md)
- [Rich, Doug, and Hunter feedback](2026-09-02-Rich-Doug-Hunter-Build-Track-Feedback.md)
- [Current repository traceability](Build-Track-Repo-Traceability.md)
- [Draft September–December milestones](../design-docs/cloud-spe-september-december-2026-milestones-draft.md)

## Known alignment before the meeting

Treat these as survey alignment or working direction, not accepted decisions:

- Live Runner is the proposed execution focus.
- Agent 2.0/Storyboard should not be an authoritative platform component.
- No prescribed application, adoption, traffic, or demand-generation target is
  required.
- No prescribed minimum capability count is currently supported.
- Every capability called supported should complete the confirmed builder
  journey.
- Durable Orchestrator identity and service URI belong on-chain; dynamic
  capability, capacity, health, and price data should remain off-chain.
- Wallet-funded and walletless paths are both contemplated, with some work
  potentially owned as an external dependency.
- Both paths should converge after authorization on a consistent invocation,
  result, failure, usage, and charge experience.

## Known disagreements and uncertainties

| Topic | Rick's survey direction | Other evidence or open issue |
| --- | --- | --- |
| Primary interface | Python SDK, but Rick also marked the answer unknown pending go-to-market | Clarify whether the SDK is selected or provisional |
| `go-livepeer` gateway | Deprecated; clients add gateway logic if needed | Josh describes it or a Live Runner control plane as permanent |
| Orchestrator selection and failover | Client SDK | Josh assigns this to a shared gateway or control plane |
| Hosted discovery | Remote signer or optional aggregator | Exact authoritative source, operator, security, and self-sovereign boundary are unknown |
| Live Runner repository | Rick reports Josh wants a combined Live Runner and SDK repository | Approval, ownership, scope, and delivery timing are not established |
| Capability acceptance | Requirements-driven selection informed by externally supplied builder research | Josh proposes a reusable contract proven with one representative capability; the positions may be compatible but are not yet reconciled |
| Clearinghouse | Rick recommends a production-scoped Pymthouse | John must verify implementation status, scope, ownership, and roadmap; Josh recommends contract and evidence before selection |
| Payment priority | Rick supports both paths and would prioritize from partner needs | Rich must confirm scope; Doug's self-sovereign and x402 direction remains unclear |
| Performance and recourse | Selection and failover may sit in the SDK | Hunter's expected-performance, late-failure, charge, and recourse concern remains unanswered |

## Block 1 — define the December result

**Duration:** 15 minutes

### Objective

Replace broad phrases such as “support Live Runner” and “improve the SDK” with
an outcome and a finite set of identifiable artifacts.

### Questions

1. What tangible artifacts or deployed behaviors must exist on 31 December?
2. Does the outcome statement above accurately define success?
3. Is architecture and requirements work itself a final deliverable, or must
   the December acceptance include a deployed end-to-end journey?
4. Does one requirements-selected representative capability prove the reusable
   contract without becoming a demand or adoption obligation?
5. Can the common contract be defined before external product research selects
   the representative capability?
6. Which deliverables belong to the wider Build Track, and which are assigned
   specifically to the Cloud SPE?
7. Which non-goals need explicit confirmation: Agent product development,
   application adoption, traffic, batch AI, BYOC, LV2V, or transcoding?

### Exit evidence

- a corrected one-paragraph December outcome;
- an initial list of tangible deliverables;
- the Cloud SPE boundary separated from wider Build Track work; and
- any remaining outcome-authority question assigned to Rich or Doug.

## Block 2 — resolve the architecture direction

**Duration:** 30 minutes

### Self-sovereign Agent and Storyboard

1. What does Rick understand Doug to mean by a “self-sovereign Agent”?
2. Does Rick have evidence that Doug wants an open-source, independently
   runnable version of the Livepeer Inc Agent 2.0/Storyboard product?
3. Is the current Storyboard code actually a viable starting point, or does
   “self-sovereign” instead imply canonical SDK, discovery, Live Runner, and
   payment primitives that any agent can use?
4. Which dependencies currently prevent an individual from operating the
   relevant experience independently of Livepeer Inc?
5. Should December include a self-hostable reference agent, or should a sample
   agent remain only acceptance evidence over the platform contract?
6. Which of these questions can Rick answer technically, and which must be
   taken directly to Doug?

### SDK, gateway, and Live Runner

1. Rick selected both a supported SDK and “Unknown” as the primary interface.
   Is the SDK the intended target subject to product confirmation, or is the
   interface choice wholly unresolved?
2. When Rick says the `go-livepeer` gateway is deprecated, does that mean the
   current gateway mode or every form of shared gateway/control-plane logic?
3. How should the direct-SDK architecture be reconciled with Josh's permanent
   gateway or Live Runner control-plane recommendation?
4. Is Josh's proposed combined Live Runner and SDK repository approved or only
   an idea? What would it own, and who would maintain and release it?
5. Where should capability declarations, job lifecycle, error normalization,
   Orchestrator selection, retry, and failover live?

### Discovery, pricing, and service assurance

Ask Rick to correct this candidate flow:

```text
On-chain ServiceRegistry
        ↓ durable identity and service URI
Orchestrator discovery endpoints
        ↓ capabilities, capacity, health, and price
Remote signer or optional aggregator
        ↓ network view
Supported SDK
        ↓ selection, payment, retry, and failover
Orchestrator / Live Runner
```

1. Is the remote signer a payment component, a discovery aggregator, or both?
2. Who operates each required service, and can the self-sovereign path function
   without Foundation or Livepeer Inc infrastructure?
3. If selection and failover live in each SDK, how will different clients
   provide consistent policy and failure behavior?
4. Is one fixed price per second per GPU type sufficient for all supported Live
   Runner workloads?
5. Which discovery-data signing and security improvements are required?
6. Where must uptime, capacity, expected completion behavior, and historical or
   declared performance be exposed?
7. Who owns retry, failover, payment-state reporting, and recourse when a long-
   running job fails late?

### Payment and clearinghouse

1. Are wallet-funded and walletless journeys both December requirements, with
   one or both potentially external to the Cloud SPE?
2. How does Doug's self-sovereign direction affect the priority of the paths?
3. Does x402 fit the existing remote-signer and probabilistic-ticket model, or
   does it imply a separate path? Treat this as a question, not an assumption.
4. Is Pymthouse the likely target, or must John's evidence review finish before
   selection?
5. If Pymthouse is late or does not meet the agreed scope, what happens to Build
   Track and Cloud SPE acceptance?
6. Confirm that evidence means end-to-end on-chain settlement, not a winning-
   ticket transaction for every individual job.

### Exit evidence

- one preferred architecture or explicitly bounded alternatives;
- the self-sovereign Agent hypothesis classified as supported, rejected, or
  requiring Doug;
- the Rick/Josh disagreement stated in terms they can decide together;
- clearinghouse and payment decisions separated from unresolved evidence; and
- repository and operational owners named wherever possible.

## Block 3 — define deliverables, evidence, and escalation

**Duration:** 15 minutes

### Candidate deliverables for Rick to correct

| Candidate December deliverable | Decision required |
| --- | --- |
| Approved target architecture and ownership map | Which components, repositories, owners, deployments, and external handoffs are authoritative? |
| Supported Live Runner builder interface | Is this a released Python SDK, a common contract exposed by multiple interfaces, a shared control plane, or another artifact? |
| Requirements-selected capability proof | Does one representative capability have to demonstrate the complete journey, and who supplies selection requirements? |
| Self-sovereign builder or agent path | Is the deliverable an independently operable agent product, an open-source reference agent, or only self-hostable network primitives and wallet payment? |
| Confirmed payment journeys | Which paths are required, who owns each, and what is the fallback if Pymthouse is unavailable? |
| Discovery, selection, and service-assurance behavior | Where do current supply, price, capacity, performance, retry, failover, and recourse live? |
| Documentation and independent evidence | What release, deployment, clean-environment test, payment evidence, and known-limitations record prove completion? |

### Deliverable capture table

Complete one row for every candidate retained:

| Deliverable | Repository or service | Accountable owner | Cloud SPE portion | External dependency | Required deployment state | Acceptance evidence | Approver | Decision date | Dependency failure plan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Authority classification

For every conclusion, record whether it is:

- technical direction Rick can authorize;
- a recommendation requiring Josh or another repository owner;
- an outcome or payment-scope decision requiring Rich;
- strategic intent requiring Doug;
- a Pymthouse dependency requiring John;
- a Cloud SPE scope commitment requiring Mike and Cloud SPE approval;
- a joint Network Engineering SPE and Cloud SPE decision; or
- an unresolved question with a named owner and date.

### Exit evidence

- a deliverable matrix with no unnamed owner or dependency;
- acceptance stated as observable evidence, not “work on” language;
- questions for Doug, Josh, John, Rich, Hunter, or product owners isolated into
  targeted follow-ups; and
- a clear statement of what must be decided before the draft milestones can be
  approved.

## If time becomes constrained

Prioritize these questions:

1. What exactly can the Build Track point to on 31 December and say it
   delivered?
2. Does “self-sovereign Agent” mean an independently operable agent product or
   self-hostable network and payment primitives that agents can use?
3. Is discovery, Orchestrator selection, and failover owned by each client SDK
   or by a shared gateway or Live Runner control plane?
4. Which payment paths are required, and what happens to acceptance if
   Pymthouse is not delivered?

## Required meeting record

When the transcript is available, produce a dated evidence note that:

- preserves Rick's statements with timestamps where possible;
- separates verified current facts, recommendations, decisions, and unknowns;
- records the exact authority asserted for each decision;
- updates the three-response synthesis without treating agreement as a vote;
- identifies every change needed to the draft milestone deliverables;
- creates or updates Beads dependencies for named follow-up work; and
- does not treat the self-sovereign Agent hypothesis as Doug's position until
  Doug confirms it.
