# Build Track December 2026 Task Breakdown

**Status:** Draft for review; not an approved delivery commitment\
**Prepared:** 26 September 2026\
**Updated:** 28 September 2026\
**Owner:** Mike Zupper\
**Purpose:** Agree the required work before creating or restructuring delivery issues

The December deliverable must make all seven Build Track outcomes possible
through the shared builder engine and a minimum reference application. This
document breaks that deliverable into proposed tasks, completion evidence, and
dependencies. Mike Zupper owns this Build Track delivery plan. Implementation
assignees, estimates, dates, and detailed choices will follow review of the task
inventory.

The [proposed delivery milestones](#proposed-delivery-milestones) organize all 31 required
tasks into four acceptance gates. The [milestone assignment](#task-to-milestone-mapping)
and [blocking dependencies](#dependencies-that-can-block-a-milestone) are review
proposals, not an approved milestone schedule or a report of current progress.

The [proposed delivery issues](build-track-december-2026-issue-proposal-draft.md)
translate these tasks into 39 reviewable issue candidates, splitting work that
contributes across milestones and preserving a crosswalk back to all 31 source tasks.
This document defines scope; the companion refines issue boundaries and
prerequisites for review before repository issue creation.

The initial Markdown review draft was requested before creating tracker records.
The proposals are now mirrored as draft items in the private
[NE-SPE Build Track sandbox](https://github.com/orgs/Cloud-SPE/projects/13).
Its **Build Track Milestone** custom field groups the drafts under M1–M4.
These IDs and task IDs remain planning references, not repository issue numbers
or approval of the delivery scope. Implementation assignments and dates remain unset.

## Basis and scope

The [architecture and executive summary](self-sovereign-open-builder-stack-draft.md)
provide the delivery shape. The [technical companion](open-builder-architecture-and-sequences.md)
and [capability inventory](console-capability-and-gap-matrix.md) supply integration
questions and evidence to verify. They do not establish that the proposed engine
or required upstream interfaces already exist.

Mike's 26 September planning clarifications define the following baseline for
this draft:

- All seven builder outcomes are required for December.
- Enterprises choose onboarding and authentication. The engine must support
  integration with their chosen access flow through public interfaces; no
  universal self-service, operator-issued-key, OAuth, or login-provider path is
  required. A working standalone example demonstrates access without prescribing
  the enterprise product experience.
- Discovery must reflect capabilities advertised as available by orchestrators.
  The application must not restrict its catalog to a manually selected demo set.
  There is no fixed capability-count acceptance threshold.
- Representative jobs will be chosen later, when execution and reporting are
  ready to validate. Discovering a capability does not prove successful execution
  of that capability.
- The reference application needs only the functionality required to demonstrate
  the seven outcomes. Porting the entire Console is a stretch goal.
- PostgreSQL, additional text/audio/video streaming, and guaranteed hard spending
  limits are stretch goals, outside required December delivery.
- Extra scope may be considered if time permits, after explicit review.

The architecture's other baseline requirements remain: importable packages,
REST/MCP services sharing the same core, embedded and service integration,
SQLite persistence and recovery, payment integration, and documented independent
installation. Small extension examples or test fixtures can demonstrate enterprise
authentication, additional endpoints/tools, and mock commerce without adding a
commercial feature suite to the minimum reference application.

For access, the required deliverable is a trusted integration contract, shared
authorization/ownership enforcement, a usable standalone adapter, and an example
showing that enterprise authentication can replace it without modifying core
source. Enterprises control enrollment, login, credential issuance, and admission
policy. They may map an existing authenticated session into the core's validated
access context without asking the user to obtain an additional engine API key.
The one-credential outcome concerns the builder-facing experience; downstream
payment credentials remain an integration responsibility. A reference access
flow does not commit the project to shipping every identity provider or a complete
self-service account-management product.

The engine reports network usage and network cost. Customer subscriptions,
retail pricing, checkout, invoices, and refunds remain enterprise responsibilities.
Application adoption and demand generation are excluded. This plan covers Build
Track builder-engine delivery led by Mike Zupper and its necessary handoffs.
Upstream components retain their existing maintainers and approval authority;
the plan does not assign their implementation work or imply their agreement.

## Deliverable groups

| Group | Result to deliver |
| --- | --- |
| Foundation | A reusable engine, explicit contracts, and durable SQLite records |
| Access | Enterprise-chosen access integrated with shared authorization and ownership controls |
| Discovery and rates | A current, network-derived capability catalog and understandable rate information |
| Payments | A working authorization/signing integration that keeps crypto handling with the payment operator |
| Execution and results | Supported job modes, usable results, understandable failures, and safe recovery |
| Usage and cost | Job-correlated usage and network-cost reports that preserve uncertainty |
| Interfaces and reuse | Equivalent core behavior through REST/MCP and supported application integration |
| Reference application | A minimum user interface demonstrating all seven outcomes |
| Verification and release | Reproducible evidence, installation guidance, and versioned release artifacts |

## Proposed delivery milestones

Each milestone describes evidence needed to pass a delivery gate. The mapping
assigns each required task exactly one milestone for **full acceptance**.
Implementation, documentation, tests, and examples may begin earlier. Passing a
gate does not imply that work for later milestones has not started, or that a
task is complete before its full definition of done is met.

These are candidate milestones for review. Together they cover the required
December baseline; Milestone 2 alone does not satisfy the entire delivery commitment.

| Milestone | Reviewable result and exit evidence | Full task acceptances | Gate prerequisite |
| --- | --- | --- | --- |
| **M1 — Foundation and integration contracts** | A versioned integration baseline, reviewed core/access/payment contracts, importable engine foundation, and working SQLite migration/restore evidence. Required upstream interfaces have verified source evidence or an explicit, agreed gap disposition. Runnable network integration is proven in M2. | 6 | Source review and the contract agreements described below |
| **M2 — Complete builder journey** | The minimum reference application demonstrates all seven outcomes for selected representative job(s) through one documented access, interface, and payment configuration. A repeatable run connects discovery and expected rate to actual execution, result/failure, usage, and observed network cost. The catalog remains network-derived. | 11, plus required early contributions from M3 tasks | M1 and a working, funded integration with usable accounting evidence |
| **M3 — Reuse and reliability** | The full required execution and integration matrix is demonstrated: immediate/asynchronous/persistent-endpoint behavior, REST/MCP, embedded/service use, enterprise-replaceable authentication, both payment configurations, and failure/accounting/recovery checks. Reference-app functionality and its supported interfaces meet their complete definitions of done. | 11 | M2, the remaining upstream execution/payment support, and the agreed acceptance matrix |
| **M4 — Independent installation and release** | Versioned packages/containers, complete installation and integration guidance, successful clean-environment reproduction, and the assembled acceptance evidence are reviewed together. Known limits and payment/operator prerequisites are explicit. | 3 | M3, release checks, permitted reuse, and the agreed acceptance procedure |

### Work that contributes before full task acceptance

The first complete journey needs working portions of several tasks whose broader
acceptance belongs in M3. These contributions are required evidence for M2, not
new tasks or permission to close the original tasks early.

| Task(s) | Required early contribution | Full acceptance remains |
| --- | --- | --- |
| I1 | REST operations needed for the selected M2 journey call the shared core, enforce access, and expose results and costs. | M3, after all baseline execution modes and shared error behavior are covered |
| J2, J3 | If the selected M2 job uses asynchronous completion or a persistent endpoint, that mode must work for the initial journey before M2 passes. Job selection is not restricted to immediate results. | M3, after complete baseline mode and recovery acceptance |
| R1, R2 | The reference application provides one usable access-to-reporting journey and a dynamic catalog. It may build against evolving interfaces while those interfaces are validated. | M3, when the complete required application behavior and dependencies are proven |
| V2 | Record actual funded execution and correlated usage/cost evidence for the M2 journey. A mocked payment flow does not pass the gate. | M3, after the full acceptance matrix is exercised |
| P4 | Document the funding, credential, configuration, and reporting prerequisites of the payment arrangement used in M2. | M3, after both self-operated and separately operated payment configurations are covered |
| V3 | Run the checks relevant to each implemented feature as it develops, especially access isolation, repeat submission, and accounting deduplication. | M3, after the full failure and recovery set is exercised |
| L1, L2 | Maintain runnable setup instructions, development builds, and automated checks from the foundation onward. Use the same versioned core build for the reuse demonstrations. | M4, with finalized release artifacts and documentation; L3 rechecks the delivered versions |

V1 selects the representative jobs once discovery, execution, and reporting are
usable. That selection defines the full acceptance matrix and the first M2
journey; it does not restrict the catalog to those jobs. Additional baseline modes
are completed in M3. The access flow chosen for a demonstration does not prescribe
how enterprise applications enroll or authenticate their users.

### Task-to-milestone mapping

**Engine** means shared-engine behavior or contracts in this Build Track plan.
**Integration** means work to verify, adapt, or agree upstream interfaces; an
upstream code change still requires its maintainer's agreement and remains in that
repository. **Example** means a reference application or fixture demonstrating
choice and reuse. **Verification/release** means acceptance evidence, guidance,
or delivery tooling. Mike Zupper owns the Build Track delivery plan across these
work types. External component ownership remains with the relevant maintainers.

| Task | Full acceptance milestone | Work kind | Deliverable focus |
| --- | --- | --- | --- |
| F1 | M1 | Integration | Verified source baseline, reusable material, and gaps |
| F2 | M1 | Engine + integration | Shared contracts and supported boundaries |
| F3 | M1 | Engine | Importable core and public integration interfaces |
| F4 | M1 | Engine | SQLite records, migrations, and backup/restore |
| A1 | M1 | Engine | Replaceable authentication and access-policy contract |
| P1 | M1 | Integration | Agreed payment management, authorization, and reporting contracts |
| A2 | M2 | Engine | Working standalone access adapter and ownership controls |
| D1 | M2 | Engine + integration | Dynamic capability discovery and descriptions |
| D2 | M2 | Engine + integration | Network rates, units, source, and assumptions |
| P2 | M2 | Engine + integration | Scoped provisioning and allocation management |
| P3 | M2 | Integration | SDK authorization and remote-signing path |
| J1 | M2 | Engine + integration | Validated submission and immediate execution |
| J4 | M2 | Engine | Owned history and basic input/result access |
| U1 | M2 | Engine + integration | Execution measurements and payment correlation |
| U2 | M2 | Engine + integration | Accounting ingestion and recoverable cost projections |
| U3 | M2 | Engine | Scoped usage/cost reports and integration events |
| V1 | M2 | Verification/release | Representative jobs and acceptance matrix |
| P4 | M3 | Integration | Both payment-operation configurations |
| J2 | M3 | Engine + integration | Asynchronous completion and recovery handles |
| J3 | M3 | Engine + integration | Persistent application endpoint invocation |
| J5 | M3 | Engine + integration | Failures and safe recovery across baseline modes |
| I1 | M3 | Engine | Complete required REST interface |
| I2 | M3 | Engine | MCP interface and equivalent core behavior |
| I3 | M3 | Example + verification/release | Embedded/service reuse and enterprise extension proofs |
| R1 | M3 | Example | Replaceable access flow, live catalog, and rates |
| R2 | M3 | Example | Job-to-result-to-reporting user journey |
| V2 | M3 | Verification/release | Funded journeys across the acceptance matrix |
| V3 | M3 | Verification/release | Isolation, failure, replay, and recovery evidence |
| L1 | M4 | Verification/release | Installation, integration, and operating guidance |
| L2 | M4 | Verification/release | Packages, containers, CI, and release checks |
| L3 | M4 | Verification/release | Independent reproduction and final acceptance evidence |

### Dependencies that can block a milestone

This table describes conditions to resolve, not a claim that they are all blocked
today. Task-level dependencies remain in the inventory below. No task assigned
full acceptance in an earlier milestone depends on full acceptance of a task in
a later milestone. The working contributions needed from tasks in later
milestones are explicit above.

| Dependency or unresolved condition | Acceptance affected | Handling in the plan |
| --- | --- | --- |
| Relevant upstream revisions and required source behavior are not verified. | F1 and M1 | Pin and inspect the components actually used. Review offered private material where relevant; the engine must remain independently buildable. Private-source availability is not a universal gate, and any omitted reuse must have an explicit disposition. |
| Payment provisioning, authorization, reporting, or allocation contracts lack agreement. | P1 and M1 | Resolve the contract or an agreed alternative with the affected maintainer. A reported API push or a proposed adapter is not compatibility evidence. |
| A required payment interface has no usable implementation. | P2, P3, U2 and M2; P4 and M3 for the second configuration | Verify the actual path, or agree and deliver the needed upstream change in its own repository. Keep upstream work distinct from the engine adapter. |
| Discovery lacks usable schemas/rates, or SDK invocation cannot execute the selected journey. | D1, D2, J1, V1 and M2 | Preserve the full advertised catalog, expose missing metadata, and select representative executable jobs later. Resolve required integration gaps; do not fabricate prices or claim support from discovery alone. |
| The test environment lacks funded signing, reachable execution, or retrievable accounting evidence. | The early V2 journey and M2; full V2 and M3 | Establish a reproducible funded environment with explicit prerequisites. The separately operated configuration may be a documented test arrangement; it does not create an ongoing hosted-service commitment. |
| Job/payment references cannot be correlated, or real cost evidence cannot be obtained. | U1–U3 and M2 | Resolve correlation and reporting upstream where necessary. Pending/unmatched states remain visible, but cannot substitute for actual cost evidence on the selected acceptance jobs. |
| Required asynchronous/persistent-endpoint behavior or recovery references are unavailable. | J2, J3, J5, I1, I2 and M3 | Verify selected SDK/runtime support and agree any necessary change. Milestone 2's first journey does not waive these baseline modes. |
| Enterprise authentication cannot replace the default adapter without core changes, or interface/integration modes behave inconsistently. | I3, V3 and M3 | Correct the public integration contract and its implementation. Examples must prove replacement and ownership enforcement without prescribing one enterprise login path. |
| Reuse permissions, release artifacts, clean-install instructions, or the acceptance procedure remain unresolved. | L1–L3 and M4 | Resolve release and evidence requirements for the delivered code, verify the final artifact versions, and record actual acceptance. Publication, organization transfer, and service-operation commitments are separate actions. |

Stretch goals do not block any of these milestones. The required milestones contain no
full Console port, PostgreSQL adapter, additional inference/media streaming, or
guaranteed hard spending limit. Those additions need their own scope and
acceptance review if capacity later permits.

## Required task inventory

The dependencies below identify prerequisites for accepting a task. They are not
a schedule: scaffolding, interface design, examples, and tests can develop together.
Upstream dependencies are described separately after the inventory. Every task in
this section belongs to the proposed required baseline; optional features appear
only in the stretch-goal section.

### Foundation

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| F1 | Verify the integration baseline and reusable source material. | Selected Console, Python SDK, Batteries, and go-livepeer revisions are recorded; relevant source behavior and gaps are rechecked. Any Console reuse has a clear scope. Review the offered Inc implementation when access is available and distinguish access from reuse permission. Unavailable private code is an explicit limitation, never a required build dependency. | Source access for material actually used |
| F2 | Define the minimum shared contracts and supported deployment boundary. | Access context, capability/rate records, jobs/attempts, result references, usage, cost states, and extension boundaries have reviewable definitions. The baseline covers immediate results, asynchronous jobs, and persistent application endpoints. Required upstream contracts and remaining design choices are explicit; no new upstream API is assumed to exist. | F1 |
| F3 | Establish installable core packages and supported integration interfaces. | The core can be imported independently of the reference application. Public interfaces separate core behavior, persistence, network/payment adapters, and enterprise extensions. A minimal import/start check works without PymtHouse, proprietary identity, or the closed-source Inc repository. | F2 |
| F4 | Implement SQLite persistence, migrations, retention, and backup/restore. | Engine-owned access mappings, jobs/attempts, result references, measured usage, and cost projections survive restart. Schema upgrades and restoration are exercised against retained records. Retention behavior is documented and configurable; storage does not duplicate the provider's authoritative ledger. | F3 |

### Access and credentials

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| A1 | Define the replaceable authentication and access-policy integration contract. | Trusted adapters map standalone credentials or enterprise authentication into a validated actor, ownership scope, and permitted operations. REST/MCP, browser trust, and administrative boundaries are documented. Callers cannot assert a trusted identity through unchecked request fields. Enrollment and authentication remain enterprise choices; replacing an adapter requires no core source patches or additional user-facing engine credential. | F2 |
| A2 | Provide a working standalone access adapter and shared ownership enforcement. | The supplied adapter provides usable credential issuance, inspection without secret disclosure, rotation, and revocation. Its example enrollment flow is documented without being mandatory for enterprises. Core ownership and operation checks apply to both this adapter and enterprise-supplied access contexts; invalid or revoked access is rejected according to the documented adapter contract. One actor cannot read or change another actor's jobs, results, or reports. Administrative access is distinct and secrets stay out of normal responses/logs. | A1, F4 |

### Discovery and expected rates

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| D1 | Integrate network-derived capability discovery and descriptions. | SDK discovery produces capability identifiers, available provider information, input descriptions/schemas, and supported execution information where supplied. Advertised additions, changes, and removals are reflected without editing an application catalog. Freshness, missing metadata, and discovery failures are visible. Incomplete metadata does not silently remove an advertised capability or imply verified executability. | F1, F3 |
| D2 | Expose understandable network rates before invocation. | Discovery results include the available rate, exact unit/currency, source, and relevant assumptions. A caller can inspect this information before submission. Missing or stale rates are identified; a rate is not presented as a guaranteed total-job quote or a retail price. | D1 |

### Payment authorization and operation

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| P1 | Agree and verify payment provisioning, authorization, and reporting contracts. | The integration identifies service credentials, allocation mapping, permitted management actions, reporting access, cost units, and correlation references. Available interfaces are distinguished from required upstream changes. Provider maintainers must agree any upstream contract/change needed for acceptance; engine adapters cannot substitute for an absent implementation. | F1, F2 |
| P2 | Implement scoped payment access and allocation management. | The engine or its authorized operator can establish the payment access needed for a builder's requests and read the relevant allocation state. Repeated management commands do not accidentally apply allowance changes twice. Per-application versus per-actor allocation is explicit. Allowance changes are distinguished from signer-wallet funding and from guaranteed spending ceilings. | P1, A2, F4 |
| P3 | Connect the SDK to payment authorization and remote signing. | Supported invocation uses the configured payment credentials and signer. Authorization denial, exhausted allowance, and unavailable signing are distinguishable. Builder-facing clients receive no wallet keys or provider administration credentials. Real funded execution is verified in V2. | P1, F3 |
| P4 | Provide self-operated and hosted payment configurations. | Configuration and setup instructions cover an operator running/funding Batteries and the signer, and an engine using a separately operated payment service. Funding, access, reporting, and operational prerequisites are explicit for each. V2 proves the agreed configurations; a test deployment does not establish an ongoing public hosted service. | P2, P3 |

### Execution, results, and recovery

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| J1 | Implement validated submission and immediate-result execution. | Requests use discovered capability information and validated inputs. Owned job/attempt records are persisted before dispatch, execution uses the Python SDK, and immediate results/failures are retained. Repeated submission references and persistence retries have defined behavior that avoids blindly submitting duplicate work or payment. | F4, A2, D2, P2, P3 |
| J2 | Support asynchronous completion and recoverable job handles. | A job can outlive the original request. The caller can retrieve its status and eventual result/failure using a durable reference. Supported provider recovery handles survive restart; a client disconnect does not discard the job or trigger replacement execution. | J1 |
| J3 | Support persistent application endpoint invocation. | The engine can invoke discovered persistent application endpoints using the agreed input/result contract and retain job, result, and payment references. The contract distinguishes an existing application endpoint from a queued job or a continuous streaming session. | J1 |
| J4 | Provide owned job history and basic input/result access. | A builder can retrieve its jobs, attempts, result references, and understandable failures. The supported input and result-access methods are documented and ownership-checked. Expired or unavailable provider assets are explained. A managed upload service or general media library is not required. | J1 |
| J5 | Implement failure classification and safe recovery across baseline modes. | Validation, access, capacity, execution, payment, and reporting failures are distinguishable. Timeouts, process restarts, failed final saves, and uncertain provider outcomes preserve evidence. Recovery checks existing work before any supported retry; it does not promise generic cancellation, automatic failover, or exactly-once network execution. | J2, J3, J4 |

### Usage and network-cost reporting

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| U1 | Capture execution measurements and payment correlation. | Each job/attempt retains supported usage quantities and the provider references needed to find its payment evidence. Multiple payment records can belong to one job. Unsupported measurements and missing correlation remain explicit rather than being inferred from unrelated identifiers. | J1, P1, F4 |
| U2 | Consume accounting evidence and maintain recoverable cost projections. | Provider observations are matched to owned jobs where evidence permits. Duplicate, late, corrected, and unmatched observations have defined handling. Stable references and replay/checkpoint behavior allow recovery without double application. Missing evidence is pending/unknown, not zero or proof of complete final cost. | U1, P1, P2 |
| U3 | Expose scoped usage/cost reports and integration events. | Builders can inspect job-level usage and resulting observed network cost, plus a basic aggregate report. Records identify units, attribution, and uncertainty. Enterprises can correlate stable IDs and consume a versioned reporting feed with deduplication/replay semantics. A reporting failure does not turn a successful job into an execution failure; network cost, settlement, and retail billing remain distinct. | U2, A2 |

### REST, MCP, and application reuse

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| I1 | Expose the required journey through the REST service. | Documented authenticated APIs cover discovery, rates, submission, status/results, and usage/cost reporting, with appropriate credential/administrative operations. Responses use the shared core's access rules, job states, and errors across all baseline execution modes. | A2, D2, J5, U3 |
| I2 | Expose the same core journey through MCP. | Tools provide discovery, rates, invocation, status/results, and usage/cost access through the configured authentication adapter. REST and MCP enforce equivalent core authorization and semantics even when their access flows differ. Interoperability is demonstrated with an agreed, pinned MCP client and documented access configuration; progress transport is not counted as inference streaming. | A2, D2, J5, U3 |
| I3 | Prove embedding, service consumption, and supported extensions. | Small examples use the same versioned core release candidate by import and through a deployed service; L3 rechecks the final released artifacts. An enterprise authentication example replaces the standalone access path while preserving the same ownership and operation checks, without requiring a separate user-facing engine key. An added endpoint/tool and a minimal mock-commerce/reporting fixture use public interfaces without core source patches or direct ledger/table writes. Normal standalone operation does not require the fixture. | I1, I2 |

### Minimum reference application

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| R1 | Build the example access, live catalog, and rate-viewing experience. | A builder follows one documented example access flow, browses the orchestrator-advertised catalog, inspects capability inputs and available rates, and sees stale/missing metadata. The example's enrollment/login experience is replaceable through the access contract and is not required of enterprise applications. New advertised capabilities appear without adding catalog entries. A generic presentation is sufficient; bespoke screens for every capability and a full onboarding portal are not required. | I1 |
| R2 | Connect job execution, results, history, and cost reporting. | The same application lets a builder supply supported inputs, submit a job, follow status, retrieve its result or understandable failure, and inspect usage/network cost. These actions use the shared engine rather than application-specific execution/payment logic. Representative jobs are selected in V1; a full Console port is unnecessary. | R1, J5, U3 |

### Verification

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| V1 | Select representative jobs and the acceptance matrix. | Once discovery, execution, and reporting can be exercised, choose available capabilities that collectively cover immediate results, asynchronous jobs, and persistent endpoints. Record inputs, expected observations, environments, and pinned component/client versions. Cover all seven outcomes, both interfaces, both application integration modes, and the agreed payment configurations without requiring every possible combination or testing the entire catalog. | D1, J1, U3 |
| V2 | Run the complete funded builder journeys. | Reproducible runs demonstrate all seven outcomes for the selected jobs and acceptance matrix. Evidence connects credential, discovery/rate, request, result/failure, usage, and real network payment observations. The builder handles no crypto on the walletless path; operator funding is documented. Self-operation and separately operated payment access are exercised, with test-only arrangements identified honestly. | V1, P4, I3, R2 |
| V3 | Verify isolation, failure handling, accounting replay, and recovery. | Automated and targeted integration checks cover cross-actor access, revoked credentials, duplicate requests, authorization failures, disconnect/restart, delayed or duplicate cost evidence, and SQLite migration/restore. Assertions check that jobs and payment evidence remain explainable and that recovery does not blindly repeat work. Upstream evidence gaps are reported rather than hidden by mocks. | F4, A2, P2, J5, U3, I1, I2 |

### Documentation and release

| ID | Task and deliverable | Definition of done | Depends on |
| --- | --- | --- | --- |
| L1 | Write installation, integration, and operating guidance. | Version-matched instructions explain example access, discovering capabilities, inspecting rates, running jobs, reading results/costs, and extending the engine. Document how enterprises replace authentication/enrollment while retaining core authorization, including the limits of supplied adapters. Include both integration modes, payment setup/funding prerequisites, configuration, upgrades, backup/restore, recovery, and known limitations. Logs and correlation references support investigation without exposing secrets. | P4, I3, R2, F4 |
| L2 | Prepare versioned packages, containers, and release checks. | Installable packages and runnable service/application artifacts build reproducibly. CI runs relevant tests, lint/type checks, and install/start smoke checks. Release notes, configuration examples, licensing/reuse decisions, and controlled release procedures are present. Repository publication/transfer and ongoing maintenance arrangements are resolved separately before those actions occur. | F3, I1, I2, R2, V3 |
| L3 | Prove independent installation and assemble the acceptance evidence. | A reviewer can reproduce the agreed seven-outcome journey from a clean environment using the released artifacts and instructions, with stated operator/payment prerequisites. The evidence bundle identifies versions, commands, results, limitations, and remaining external dependencies. The designated acceptance authority reviews that evidence against the agreed scope; this draft does not appoint the reviewer or constitute sign-off. | V2, V3, L1, L2 |

## Coverage of the seven outcomes

| Outcome | Primary delivery tasks | Observable acceptance evidence |
| --- | --- | --- |
| 1. Obtain one credential | A1–A2, I3, R1 | A builder follows the application's chosen access flow and can use the journey without obtaining a separate payment credential. The standalone example works, and an enterprise-auth example replaces that flow through public interfaces while preserving authorization. No particular onboarding or credential format is mandatory for every application. |
| 2. Discover capabilities | D1, I1–I2, R1 | The application and interfaces reflect orchestrator advertisements, including catalog changes, without a hard-coded demo list. |
| 3. Understand the expected rate | D2, R1 | Before submitting a selected job, the builder can inspect the available network rate, units, and assumptions. |
| 4. Invoke a capability | P2–P3, J1–J3, I1–I2, R2 | Selected jobs reach the network through the engine and return an immediate result or a recoverable job reference as appropriate. |
| 5. Receive a result or understandable failure | J2–J5, R2 | The builder retrieves a result or an actionable failure/uncertain state, including after relevant disconnect/restart cases. |
| 6. Pay without holding crypto | P1–P4, V2 | A funded operator/provider signs network payments while the builder uses ordinary engine access. An allowance or mock payment alone is insufficient evidence. |
| 7. See usage and resulting charge | U1–U3, R2 | Selected jobs expose supported usage and observed network costs correlated to payment evidence; pending or incomplete evidence is labeled. Customer retail billing remains external. |

V2 and L3 join these into a complete journey. Separate successful component tests
do not by themselves satisfy the seven-outcome deliverable. Uncertainty labels
are required behavior, but cannot replace demonstrating actual network-cost
evidence for the selected acceptance jobs.

## External dependencies and handoffs

These are inputs to Build Track delivery under Mike Zupper's ownership, not
assignments to upstream teams. External handoff contacts and delivery dates can
be added during the later planning pass.

| Dependency | Evidence or agreement needed | Tasks affected |
| --- | --- | --- |
| Python gateway SDK | Discovery/rate/schema behavior, baseline execution-mode support, signing integration, and usable job/payment references at selected revisions; disposition of any gaps | F1, D1–D2, P3, J1–J5, U1 |
| Clearinghouse Batteries/payment provider | Agreed provisioning/read contracts, authorization semantics, cost units, correlation, and accounting replay/completeness limits | P1–P4, U1–U3 |
| go-livepeer signer and Orchestrator/Live Runner | Compatible discovery, signing, execution, and payment-event behavior; usable recovery references where supported | D1, P3, J1–J5, U1–U2 |
| Available network services and funded payment environment | Representative jobs that can actually run, network/chain connectivity, funded signer access, and obtainable accounting evidence | V1–V2, L3 |
| Existing Console and offered Inc implementation | Source review and permission for any selected reuse; shared-contract review where relevant. Private source access is not a runtime or build requirement | F1–F2, I3, R1–R2 |
| SPE and affected-repository review | Disposition of scope, acceptance evidence, and any upstream changes or release/handoff commitments | P1, L2–L3 |

If an upstream handoff cannot supply a required outcome, record the gap and bring
back an integration or scope decision. A mock can help develop the engine but
cannot close funded execution or network-cost acceptance.

## Decisions to resolve as the work is refined

These decisions do not prevent reviewing this inventory. Resolve each before
accepting its dependent delivery work; none requires assigning people or dates
during this first review.

| Decision | What needs to be selected | Related tasks |
| --- | --- | --- |
| Access integration and examples | Trusted adapter/context contract, browser and administrative trust, standalone example, and enterprise-auth acceptance example. Enterprise enrollment and login remain configurable integration choices rather than a universal product decision | A1–A2, I1–I3, R1 |
| Discovery contract | Authoritative schemas, refresh/freshness behavior, and handling of incomplete capability metadata | D1–D2, R1 |
| Payment contract | Per-application/per-actor allocation, supported management/read interfaces, cost correlation, and upstream gap dispositions | P1–P4, U1–U3 |
| Recovery and data retention | Supported status/recovery behavior, input/result access, retention, and treatment of expired provider assets | F4, J2–J5 |
| Acceptance jobs | Representative capabilities and inputs chosen later to exercise the baseline execution modes and reporting | V1 |
| Deployment and service guarantees | Supported installation conditions, minimum performance/failure information, and explicit disposition of requests for service assurance or financial recourse. No SLA, refund promise, or HA guarantee is assumed | F2, J5, V1, L1 |
| Repository and release details | Engine/reference-app locations, permitted code reuse, release procedure, and eventual maintenance/transfer arrangements | F1, F3, L2 |
| Final acceptance procedure | Reviewer/approval authority, independent reproduction procedure, and evidence needed for sign-off | L3 |

## Stretch goals and excluded expansion

None of the following is a prerequisite or dependency for completing the required
task inventory. Adding one requires a separate scope decision and acceptance
criteria after the minimum work is understood.

| Stretch goal | Boundary |
| --- | --- |
| Port the entire Livepeer Console application | Additional screens, account/asset experiences, and product features may follow the minimum reference application. Enterprise commerce remains outside the shared core. |
| PostgreSQL persistence adapter | SQLite remains the required baseline. A PostgreSQL adapter does not by itself add distributed scheduling or high availability. |
| Additional text/audio/video streaming | Incremental text or continuous media needs its own capability, lifecycle, payment, and recovery evidence. Baseline asynchronous jobs and persistent endpoints do not imply this support. |
| Guaranteed hard spending limits | Requires an agreed enforcement/reservation model and proof under concurrent requests and delayed accounting. Ordinary allocations and reporting do not establish a hard ceiling. |

Production retail billing, mandatory proprietary identity/PymtHouse, payment
protocol redesign, a new public hosted-service obligation, application adoption,
and demand generation are outside this delivery baseline. They are not added
implicitly by the Console stretch goal.

## Review and later project setup

The next review should establish whether the required inventory covers the seven
outcomes, whether each task is small and concrete enough to discuss, and whether
any proposed requirement exceeds the minimum architecture. Dependencies and
external gaps should be corrected before this becomes a delivery commitment.

Review the proposed milestone gates, task assignments, and upstream handoffs along
with the task definitions. In particular, confirm that M2 proves a complete
journey while M3 supplies the remaining required coverage, and that demonstration
choices do not become mandatory enterprise product policies.

After sandbox review, agree the repository homes and GitHub/Beads tracking
convention before converting drafts into repository issues and milestones.
Add implementation assignees, estimates, and dates during subsequent planning.
The stable document IDs preserve traceability during conversion; this document
defines the proposed work and acceptance evidence rather than live work status.
