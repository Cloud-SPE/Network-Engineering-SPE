# Builder-Layer Proposal Assessment and M2 Handoff

**Date:** 1 October 2026\
**Status:** Review guidance for milestone execution; not an architecture amendment\
**Updated:** 1 October 2026, with ISS-01 and ISS-02 review findings\
**Prepared by:** Assistant, at Mike Zupper's request\
**Proposal author:** Mike Zupper

## Purpose and evidence limits

The [imported proposal](2026-10-01-Builder-Layer-Abstraction-and-Two-Application-Review.md)
turns the accepted architecture into candidate packages, service interfaces, data
contracts and an extraction sequence. Its comparison with a second application
helps reveal assumptions inherited from the first, particularly who pays for
work, where capability mappings come from and whether accounting is available.

This assessment compares the supplied document with the
[accepted specification](../../product-specs/build-track-2026.md),
[architecture](../../design-docs/self-sovereign-open-builder-stack-draft.md),
[technical companion](../../design-docs/open-builder-architecture-and-sequences.md)
and [task acceptance criteria](../../design-docs/build-track-december-2026-issue-proposal-draft.md).
It does not independently inspect the two applications, run their tests, validate
production behavior or confirm fork changes and upstream acceptance. The source
was supplied as a local file; no source Git revision was established. Its checksum
is recorded in the imported document.

The proposal and its two application reviews are dated October 1. M1 remains
complete effective September 30. This is subsequent supporting analysis and an
input to M2; importing it neither backdates work nor reopens M1 approval.

## Useful foundations

- The separation of network execution/accounting from enterprise identity and
  retail billing matches the accepted architecture.
- Package and service integration share a common engine, with replaceable
  discovery, transport, payment, storage and authentication boundaries.
- Jobs, attempts, external operation references and accounting events provide
  concrete starting points for implementation contracts.
- The second-application review exposes limitations of a single application-wide
  payer, a Batteries-only accounting assumption and one descriptor format.
- The extraction sequence proposes incremental changes and tests rather than an
  undifferentiated rewrite. Its individual steps still need scope and milestone review.

## Scope and evidence dispositions

| Proposal area | Assessment | M2 treatment |
| --- | --- | --- |
| Streaming in the first release | The proposal recommends inclusion because one application already uses it. The accepted plan makes additional streaming optional. | Keep the required execution modes distinct from optional streaming. Existing application needs do not add a delivery obligation. |
| PostgreSQL | The package layout and extraction gates include a PostgreSQL store. It remains stretch scope under the accepted plan. | SQLite and its recovery evidence are required. Make any PostgreSQL implementation and tests conditional on separately selected scope. |
| Runner package and application migration | A runner shell, descriptor tooling, GPU probe and migration of an existing enterprise application are additional candidates. | Evaluate reuse, but do not make those deliverables or enterprise adoption prerequisites for December acceptance. |
| Extraction milestone mapping | Full discovery extraction is placed in M2, while SQLite migrations appear in a later service-adapter step. | Preserve M2's accepted core, SQLite and build-check evidence. Review each extraction step against the existing task mapping before scheduling it. |
| BYOC, batch/training and transcoding examples | These illustrate extensibility beyond the selected execution scope. | Retain as examples of possible future adapters, not required implementations or proof of compatibility. |
| Fork-only features and production claims | Exact application revisions, fork URLs/commits, test results and maintainer dispositions are not supplied. | Capture an evidence register before relying on those capabilities. Distinguish author reports, inspected code, runtime tests and upstream agreement. |
| Payment and usage reporting unavailable in one application | Useful evidence of an adapter gap; it does not waive required usage/network-cost outcomes. | Model unavailable/pending evidence honestly and select an acceptance configuration capable of proving the required reporting. |
| Second-review recommendations | The proposal explicitly says these changes have not been applied to its interfaces. | Resolve or defer them by name before freezing the affected contract. Do not implement conflicting versions as if both were settled. |

## Contract questions to resolve

### Trusted access, administration and payment credentials

Job methods accept an `ActorContext`, but cost queries, event reads, key issuance
and provider administration do not show the same authorization boundary. Define
whether these methods are trusted internal interfaces or require an explicit
validated context. Apply application/actor isolation consistently in imported,
HTTP and MCP modes; UUID knowledge alone must not grant access.

The second review proposes obtaining signer credentials from the actor. The
current actor attributes are copied into jobs and events. Keep raw payment
secrets out of those copied attributes: define a separate credential resolver or
protected reference, its scope and its lifecycle. Resolve the difference between
application identity, payment authority and permission to administer allocations.

### Idempotency, failover and recovery

The first contract raises `OperationExists`; the second review proposes joining
and returning an existing job. Select one behavior, including simultaneous
requests, changed payloads under the same key, retention expiry and restart.
Define atomic persistence and the recovery state when the process loses contact
after dispatch but before recording whether payment or execution occurred.

The `payment_sent` boolean and the proposal's at-most-once claim need evidence at
the chosen SDK revision. Absence of confirmed payment does not by itself prove
that work never ran. Keep unknown outcomes distinct from safe-to-retry failures.
Storing jobs makes recovery possible; it does not alone guarantee that in-flight
work survives restart or that retry cannot duplicate execution or payment.

### Cost correlation, units and usage provenance

Verify how job IDs, attempts, manifests, sessions, credentials and cost events
relate at selected revisions. Do not assume a manifest ID is globally unique or
that every job or attempt has a one-to-one mapping. Include provider/deployment
scope and multi-attempt cases where needed. Reconcile the claim that paid work
is bound to one runner with the discussion of jobs having several paid attempts.

Define the meaning and units of reported amounts, separating network expected
value, settlement and enterprise charges. For application-reported usage, retain
its source and trust level; do not silently equate a caller's report with engine
or runner measurement. If evidence is unavailable, report that state explicitly.

### Events, retention and extension behavior

A promise to replay from zero needs reconciliation with configurable retention.
Define expired-cursor behavior, replay limits and how consumers resynchronize.
A durable engine feed cannot restore events that an upstream producer never sent.

The proposal forbids callbacks during a job but also supports application-provided
usage meters and selection policies. Clarify whether the prohibition concerns
commercial orchestration only, and specify the extension lifecycle and trust
boundary in both embedded and service modes.

### Execution modes and source claims

Verify that SDK session reservation supplies the persistent-application behavior
required by the accepted baseline. Do not treat session reservation, persistent
endpoints, progress events and streaming output as interchangeable.

The second-application section says it supplies evidence for two previously
missing baseline requirements, then lists asynchronous jobs and idempotency.
The earlier missing pair was asynchronous jobs and persistent sessions. Correct
that statement in a future proposal revision; persistent-endpoint evidence is
still outstanding in this document. Claims that applications run these paths in
production remain unverified by this assessment.

## ISS-01 and ISS-02 review findings

**Reviewed:** 1 October 2026 by John (`eliteprox`), against source at the revisions
below. These are source findings, not runtime proof. They answer the contract
questions above for ISS-01 ([#7](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/7))
and ISS-02 ([#8](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/8)).
Access detail belongs to ISS-03 and payment contracts to ISS-04; this section
records only the boundaries those tasks start from.

### Evidence register

| Component | Revision | Finding that affects the proposal |
| --- | --- | --- |
| Python gateway SDK | [`44df061`](https://github.com/livepeer/livepeer-python-gateway/commit/44df06157fcdb864e37d971e8caba86b2a7dc92e) | [`RunnerSelectionCursor`](https://github.com/livepeer/livepeer-python-gateway/blob/44df06157fcdb864e37d971e8caba86b2a7dc92e/src/livepeer_gateway/selection.py#L159-L227) already fails over across runners, but only within the [first orchestrator batch](https://github.com/livepeer/livepeer-python-gateway/blob/44df06157fcdb864e37d971e8caba86b2a7dc92e/src/livepeer_gateway/discovery.py#L203-L229) that returns any. It has no pool-size setting, ranking, capacity-versus-other distinction or per-attempt payment record. Multipart, `payment_sent` and the stream manifest id are not on `main` |
| Python gateway SDK | [`44df061`](https://github.com/livepeer/livepeer-python-gateway/commit/44df06157fcdb864e37d971e8caba86b2a7dc92e) | Runner modes (`single-shot`, `persistent`) and payment types by price unit (`fixed`, `live`, `lv2v`) are [already defined](https://github.com/livepeer/livepeer-python-gateway/blob/44df06157fcdb864e37d971e8caba86b2a7dc92e/src/livepeer_gateway/live_runner.py#L44-L54) |
| go-livepeer | [`773734d9`](https://github.com/livepeer/go-livepeer/commit/773734d91e068a6ad9f870d16af97a27abea6216) | The remote signer [authorizes through a webhook](https://github.com/livepeer/go-livepeer/blob/773734d91e068a6ad9f870d16af97a27abea6216/server/remote_signer.go#L311-L361) and uses the same [payment types](https://github.com/livepeer/go-livepeer/blob/773734d91e068a6ad9f870d16af97a27abea6216/server/remote_signer.go#L35-L37). Since [go-livepeer#4095](https://github.com/livepeer/go-livepeer/pull/4095), discovery adds `price_usd` to runner prices and each [`create_signed_ticket` event](https://github.com/livepeer/go-livepeer/blob/773734d91e068a6ad9f870d16af97a27abea6216/server/remote_signer.go#L740-L785) carries `computed_fee_usd`, `payer_address` and the caller's `manifest_id`, including a session's first prepay. Events are best-effort: they are dropped when the signer's Kafka queue is full |
| Clearinghouse Batteries | [`9cf68d6`](https://github.com/livepeer/clearinghouse-batteries/commit/9cf68d6b97ec263911ddfb383f0df66492c1417e) | A management HTTP API exists on `main` ([`a2ed175`](https://github.com/livepeer/clearinghouse-batteries/commit/a2ed17529deba702437a68b709fe4ac4cdc20ef0)). Batteries answers the signer webhook with [402 at zero balance](https://github.com/livepeer/clearinghouse-batteries/blob/9cf68d6b97ec263911ddfb383f0df66492c1417e/internal/store/auth.go#L151-L152) and [debits allocations by the signer's `computed_fee_usd`](https://github.com/livepeer/clearinghouse-batteries/blob/9cf68d6b97ec263911ddfb383f0df66492c1417e/internal/store/ingest.go#L100-L126). It keeps `manifest_id` only in the raw event and does not expose it. The `/v1/cost/events` read API is fork-only |
| simple-infra (second application) | [`4ec364f`](https://github.com/livepeer/simple-infra/commit/4ec364fe5e51e6fa6771481a8f39cc571b180330) | Matches the proposal except for the training path, admission caps, limiter, registry and job store. It pays through PymtHouse composite keys, not Batteries. Its SDK is a fork, [`4dbcee69`](https://github.com/livepeer/livepeer-python-gateway/commit/4dbcee69a46b7dddc60c7c4b2eaf4666166c99e4) |
| Console | [`009a703`](https://github.com/livepeer/console/commit/009a703d7b6434bab905902375f562e5980728af) | Reference for authorization patterns only. Console, Batteries and PymtHouse carry no license, so no code is copied from them |

### Recommended resolutions

**Trusted access, administration and payment credentials.** Authentication
sits above the engine core: the service package runs it, with configurable
trusted issuers, and an importing application supplies its own. The core
receives only `ActorContext`. Cost, event, key and provider-administration
methods take that context and check scope, like job methods. A separate
credential resolver returns a reference resolved at call time, never copied
into actor attributes, jobs or events. Detail: ISS-03.

**Idempotency, failover and recovery.** Adopt the proposal's gap 4:
join-and-return replaces `OperationExists`. Release the operation reference on a
pre-dispatch decline; refuse a changed payload under the same reference with 409;
allow one dispatch for simultaneous duplicates; expire with configurable
retention. Write job and attempt rows before dispatch, and mark payment sent with
an unknown outcome as `uncertain`, never retried. Build failover on the SDK's
runner selection and add a maximum pool size and capacity classification there,
so a capacity refusal moves to the next candidate. Do not rely on `payment_sent`
until it is upstream.

**Cost correlation, units and usage provenance.** Reported cost is network cost
in USD, priced per ticket by the remote signer; retail pricing stays with the
enterprise application. The proposal's cost feed (`cost_events`,
`manifest_cost`) remains the usage source, and the engine delivers cost and
usage to the enterprise application through its event feed. Key cost by
provider deployment and `manifest_id`, and sum a job's attempts, since a capacity
refusal after a session prepay produces several paid attempts. Keep the four
statuses `none`, `pending`, `observed` and `corrected`. Batteries and the remote
signer are the planned payment path, so missing cost is `pending`; the proposal's
gap 2 `unavailable` status is not needed. Usage keeps its source (`meter`,
`runner_reported`, `app_reported`). Provisioning and reporting contracts: ISS-04.

**Events, retention and extension behavior.** Replace replay from zero with a
retention window; an expired cursor returns 410 and the consumer resynchronizes
from job and cost listings. "No callbacks" means no commercial orchestration
during a job. Usage meters and selection policies are pure functions over the
request and reply.

**Capabilities.** A capability is data, not a class. Its descriptor uses the
runner mode and price unit gateway core already defines, and resolution is a
protocol with descriptor and configuration-table implementations plus
`allowed_orchestrators` (gap 3). Offering rates can carry the signer's
`price_usd` from discovery. BYOC (gap 5) is excluded.

### Upstream work

These changes would remove engine workarounds. None blocks M2.

- Batteries: the cost read API behind the cost feed, merged from the Enterprise
  App's fork into `main`; caller idempotency; per-allocation balance reads; and
  attributed usage.
- go-livepeer: reliable delivery of the signer's payment events, which are
  dropped today when its Kafka queue is full.
- Python gateway SDK: runner-selection pool size, capacity classification and
  a per-attempt payment record, and the fork-only fields upstreamed.
- simple-infra: two defects handed to Inc, a pinned-request 500 and a job-store
  setting missing from its Pulumi template.

## Relationship to M1 and M2

| Milestone/task | Repository issue | Relationship |
| --- | --- | --- |
| M1 / ISS-41 — Assess software and reuse | [#2](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/2) | Subsequent two-application evidence and reuse hypotheses; not new September completion evidence |
| M1 / ISS-42 — Define architecture | [#3](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/3) | Elaborates accepted package/service and component boundaries without superseding them |
| M1 / ISS-43 — Ownership, extensions and acceptance | [#4](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/4) | Supplies enterprise-extension examples and highlights optional scope |
| M2 / ISS-01 — Verify integration baseline | [#7](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/7) | Pin application and fork evidence, permissions, SDK/payment behavior and gaps |
| M2 / ISS-02 — Shared engine contracts | [#8](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/8) | Review models, protocols, recovery, correlation, events and scope before adoption |
| M2 / ISS-03 — Access interfaces | [#9](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/9) | Resolve trusted contexts, scoped reads/administration and credential handling |
| M2 / ISS-04 — Payment contracts | [#10](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/10) | Verify provisioning, payment authority, reporting units/references and upstream gap dispositions |

ISS-05–ISS-07 can use the selected package, storage and testing ideas after the
contracts are reviewed. Their accepted criteria remain unchanged.

## Suggested review handoff for John and Mike

Use the proposal as a concrete input to ISS-01–ISS-04. For each interface or
behavior, record the proposal section, source revision, available evidence,
accepted-scope fit, decision, owner and consuming task. Separate what can be
implemented now from what needs upstream agreement or additional investigation.
The immediate result should be reviewed contracts and reproducible evidence,
not acceptance of the entire extraction plan or a claim of runtime parity.

This document recommends that handoff; it does not create new assignments,
change dates or authorize upstream modifications.
