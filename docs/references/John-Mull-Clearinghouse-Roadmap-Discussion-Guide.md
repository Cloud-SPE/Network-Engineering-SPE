# John Mull Clearinghouse Roadmap Discussion Guide

**Status:** Draft facilitator guide

**Prepared:** 2 September 2026

**Duration:** 60 minutes

**Agenda blocks:** 15 minutes, 30 minutes, and 15 minutes

**Facilitator:** Mike Zupper

**Execution bead:** `netspe-vun.19`

## Meeting objective

Establish authoritative facts about Elite Encoder's hosted Pymthouse system,
its code and deployment, its relationship to `livepeer/clearinghouse`, and
John Mull's intended roadmap. Evaluate those facts against the Build Track's
implementation-neutral clearinghouse requirements without selecting a target
implementation or assigning work outside the Cloud SPE's authority.

## Desired outcome

The meeting should leave the architecture process able to distinguish:

- what Pymthouse is and what is deployed now;
- what `livepeer/clearinghouse` is and whether it shares code or contracts;
- what works end to end versus what is planned, demo-only, manual, or unknown;
- which requirements either implementation can satisfy;
- which gaps require engineering, operations, funding, or another owner;
- what John and Elite Encoder are willing and able to maintain; and
- which decisions still require Rich, Rick, Josh, Network Engineering SPE, or
  Cloud SPE authority.

This is a fact-finding and roadmap meeting. It is not a procurement decision,
implementation selection, security review, or architecture approval.

## Required pre-read

- [Repository traceability and current gaps](Build-Track-Repo-Traceability.md)
- [Seven builder outcomes](Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise)
- [Josh's clearinghouse recommendations](Build-Track-Architecture-Survey-Response-Josh-2026-08-31.md#section-5-clearinghouse-and-payment)
- [21 August Build Track transcript extract](2026-08-21-Build-Track-Alignment-Transcript-Extract.md)
- [Draft September–December milestones](../design-docs/cloud-spe-september-december-2026-milestones-draft.md)

Ask John to bring non-sensitive references to the relevant repositories,
branches or releases, deployed version identifiers, public API documentation,
architecture diagrams, and roadmap artifacts. Do not request credentials,
private keys, signer secrets, customer data, or security-sensitive deployment
details for the repository record.

## Working terminology

- **Pymthouse** means Elite Encoder's hosted system until its code lineage is
  verified.
- **`livepeer/clearinghouse`** means the reviewed GitHub repository and does not
  automatically mean the hosted Pymthouse deployment.
- **Clearinghouse contract** means the implementation-neutral credential,
  authorization, balance, signer, usage, and charge behavior required by the
  builder journey.
- **Walletless** is a builder outcome, not a product name or implementation
  selection.
- **Production evidence** means evidence of deployed technical behavior. It is
  not a demand-generation, traffic-volume, or application-adoption target.

## Known facts and unresolved claims

| Topic | Current planning record | What John can clarify |
| --- | --- | --- |
| Pymthouse codebase | Not reviewed or verified | Repository, history, license, branch, revision, and release process |
| Relationship to `livepeer/clearinghouse` | Unknown | Same deployment, upstream, fork, derivative, alternative, shared contract, or unrelated |
| Hosted deployment | Existence reported; exact revision and topology unknown | Deployed components and version evidence without sensitive details |
| `go-livepeer` dependency | Reviewed repo pins a Pymthouse-labeled signer build | Actual branch/revision, required patches, and upstream status |
| Identity and credential | Multiple credential and webhook modes exist in reviewed code | What Pymthouse issues and accepts in production |
| Balance enforcement | Reviewed code contains demo-fixed and manual paths | Actual ledger, funding, enforcement, and correction behavior |
| Usage and charge | Aggregate usage exists in reviewed code | Job correlation, billable units, rates, receipts, and reconciliation |
| Agent integration | A recorded JWT mismatch blocked the reviewed path | Current blocker status and whether the integration remains relevant |
| Live Runner | Remote signer support exists in parts of the current stack | Supported Live Runner path, versions, limitations, and evidence |
| Roadmap and ownership | Not documented in this repository | Planned work, capacity, funding, maintainers, and operational commitment |

## Block 1 — verify system identity and current deployment

**Duration:** 15 minutes

### Repository and lineage

1. Is “Pymthouse” the correct product and project name?
2. Which exact repository or repositories contain its source? Which are public,
   private, archived, or deployment-only?
3. What is the relationship to `livepeer/clearinghouse`: same code, upstream,
   fork, derivative, alternative implementation, shared contract, or none?
4. Which branch, tag, release, or commit is deployed today?
5. What changes exist only in the deployed Pymthouse version and are not in
   `livepeer/clearinghouse` or upstream `go-livepeer`?
6. What license and contribution model apply, and can required changes be
   upstreamed?

### Deployment and ownership

7. Which high-level components are deployed: identity, Builder API, balance
   ledger, remote signer, discovery, event pipeline, metering, and settlement?
8. Who owns the code, merge approval, release, deployment, signer operations,
   incident response, and user support?
9. Is the deployed system production, pilot, demonstration, dormant, or
   partially operated? What non-sensitive evidence supports that status?

### Exit evidence

- a verified code and deployment identity;
- a precise relationship to `livepeer/clearinghouse` or a named verifier who
  can establish it;
- current owner and operator assignments; and
- every unverified statement classified as unknown rather than inferred.

## Block 2 — evaluate contract coverage and roadmap

**Duration:** 30 minutes

### Credential and account journey

1. How does a new builder obtain one ordinary credential without contacting an
   Operator or receiving a manually provisioned secret?
2. Which credential formats are accepted, and where are issuance, exchange,
   scope, expiry, rotation, revocation, and tenant isolation enforced?
3. Can Pymthouse be self-hosted? If so, what external identity or account
   dependencies remain mandatory?

### Balance and authorization

4. How is an account funded or granted an allowance? Which funding paths are
   live, manual, planned, or deliberately out of scope?
5. Is the balance checked and reserved before authorization? What happens on
   exhaustion, cancellation, partial execution, duplicate requests, refunds,
   and corrections?
6. Which policy component authorizes the remote signer, and which stable
   identity follows the request into the payment event?

### Network payment and Live Runner

7. Which `go-livepeer` remote-signer endpoints and protocol version does
   Pymthouse require? Are the required changes upstream?
8. Does the deployed path support a current Live Runner capability end to end?
   Which capability, gateway, Orchestrator, runner, and version provide the
   reproducible evidence?
9. Does authorization produce a payment ticket attached to the same job? What
   evidence shows redemption or network fees without requiring access to
   sensitive infrastructure?
10. Can wallet-funded and Pymthouse-backed calls converge after authorization
    on the same invocation, job, result, failure, usage, and charge interfaces?

### Metering, price, and receipt

11. Which identifier joins credential, request, gateway, Orchestrator, Live
    Runner execution, signed ticket, usage event, and charge?
12. What usage units, rate or quote, currency, markup, and network fee are
    recorded? Which values are authoritative?
13. Can a builder retrieve a per-job usage-and-charge receipt, or only aggregate
    usage and balance information?
14. Can an understandable failure say whether authorization, execution,
    metering, or payment occurred and whether retry is safe?

### Roadmap and Build Track fit

15. When Doug referred to “completing payment house,” what work did John
    understand that to include?
16. What is already committed on John's roadmap through December 2026, and what
    is merely proposed or dependent on funding, protocol work, or another team?
17. Which gaps can Elite Encoder own, by when, and with what repository and
    operational commitment?
18. Would John support a common clearinghouse contract implemented by
    Pymthouse, `livepeer/clearinghouse`, or both? What prevents that approach?
19. Does any known unmet requirement justify a new implementation rather than
    extending an existing one?

### Exit evidence

- a requirements-to-current-behavior matrix;
- a reproducible or explicitly unavailable Live Runner payment path;
- named current gaps and roadmap items;
- a statement of Elite Encoder's intended ownership and capacity; and
- implementation alternatives preserved for the architecture authority.

## Block 3 — confirm evidence, owners, and follow-ups

**Duration:** 15 minutes

### Priority confirmations

1. Which statements from the meeting are verified current facts, John's target
   recommendations, roadmap commitments, or unknowns?
2. Which public artifacts can support the facts: repository links, revisions,
   API documentation, diagrams, release records, tests, or sanitized call
   evidence?
3. Which questions require a `livepeer/clearinghouse` maintainer, deployment
   owner, identity owner, signer owner, `go-livepeer` maintainer, or Josh/Rick?
4. Which scope and funding decisions require Rich, Network Engineering SPE, or
   Cloud SPE approval?
5. What is the owner and decision date for every unresolved item?

## System identity capture

| Item | Verified answer | Evidence | Owner/verifier | Follow-up date |
| --- | --- | --- | --- | --- |
| Correct system name |  |  |  |  |
| Source repository |  |  |  |  |
| Relationship to `livepeer/clearinghouse` |  |  |  |  |
| Deployed revision |  |  |  |  |
| Required `go-livepeer` revision |  |  |  |  |
| Code owner and merge gate |  |  |  |  |
| Release/deployment owner |  |  |  |  |
| Operational/support owner |  |  |  |  |
| License and contribution path |  |  |  |  |

## Builder-contract coverage

| Required behavior | Works now | Planned | Missing or disputed | Evidence | Owner |
| --- | --- | --- | --- | --- | --- |
| Self-service credential |  |  |  |  |  |
| Real balance/allowance enforcement |  |  |  |  |  |
| Expected price or rate |  |  |  |  |  |
| Live Runner authorization |  |  |  |  |  |
| Signed payment ticket |  |  |  |  |  |
| Understandable payment failure |  |  |  |  |  |
| Stable end-to-end job identity |  |  |  |  |  |
| Usage metering |  |  |  |  |  |
| Network-payment evidence |  |  |  |  |  |
| Per-job usage-and-charge receipt |  |  |  |  |  |
| Self-hosted deployment |  |  |  |  |  |
| Common interface with wallet-funded path |  |  |  |  |  |

## Roadmap capture

| Roadmap item | Current state | Intended outcome | Repository/owner | Dependency | Target date | Commitment level |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Use only these commitment levels:

- **committed** — accepted by the delivery owner with a target date;
- **proposed** — desired but not accepted or funded;
- **dependent** — conditional on a named external prerequisite;
- **exploratory** — research or evaluation only; or
- **not planned** — explicitly outside the current roadmap.

## Decision and follow-up log

| Finding | Classification | Decision authority | Required evidence or action | Owner | Date |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

John can establish Pymthouse implementation facts and state his roadmap and
commitments. Unless separately authorized, his response does not approve Build
Track scope, Cloud SPE ownership, budget, the target clearinghouse, or the final
architecture.

## Parking lot

Defer details that do not change architecture:

- exact identity-provider configuration;
- private deployment topology, secrets, and key custody procedures;
- field-by-field API or event schemas;
- precise pricing formulas and plan catalog entries;
- operational runbook detail;
- individual implementation tasks and pull-request estimates; and
- application counts, traffic volume, or demand-generation targets.

## Required meeting output

Within one business day, produce a dated record that:

- corrects the Pymthouse system and repository map;
- cites public or sanitized evidence for current behavior;
- separates current facts, recommendations, commitments, and unknowns;
- maps Pymthouse and `livepeer/clearinghouse` against the same requirements;
- records ownership, dependencies, capacity, and target dates;
- assigns every factual gap to a verifier;
- feeds relevant findings into `netspe-vun.9` and `netspe-vun.12`; and
- leaves implementation selection to the named architecture and SPE authorities.
