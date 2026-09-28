# Build Track December 2026 Proposed Delivery Issues

**Status:** Review proposal; mirrored as draft items in the public GitHub project\
**Prepared:** 27 September 2026\
**Updated:** 28 September 2026\
**Owner:** Mike Zupper\
**Basis:** [Task breakdown and proposed milestones](build-track-december-2026-task-breakdown-draft.md)

This document translates the 31 source tasks into **39 proposed issues**, each
with one milestone, a proposed implementation home, acceptance criteria, and
explicit prerequisites. The extra issue boundaries separate first-journey work
from broader coverage, documentation, and release completion; they do not add
new December scope.

These are review IDs, not GitHub or Beads issue numbers. Mike Zupper owns this
Build Track delivery plan and its proposed delivery issues. Implementation
assignees, estimates, dates, and live work status remain unassigned. Upstream
components retain their existing maintainers. The milestone plan and issue proposal
remain subject to review and the applicable scope approvals.

The public [NE-SPE Build Track project](https://github.com/orgs/Cloud-SPE/projects/13)
uses a **Build Track Milestone** custom field for M1–M4. This supports project-only
drafts while repository homes and the later tracking convention remain under review.

## Scope and reading guide

The [source scope](build-track-december-2026-task-breakdown-draft.md#basis-and-scope) and its
[stretch-goal boundary](build-track-december-2026-task-breakdown-draft.md#stretch-goals-and-excluded-expansion)
govern this proposal. All seven outcomes are required. Discovery displays
orchestrator-advertised capabilities; representative execution jobs are selected
later. Enterprises choose onboarding and authentication through supported
integration interfaces. A reference access flow is an example, not a mandatory
enterprise policy.

The reference application remains the minimum needed for the journey.
A complete Console port, PostgreSQL, additional text/audio/video streaming, and
hard spending guarantees are outside the required issue set. Retail commerce,
application adoption, and demand generation are also outside it.

Each issue's title states its deliverable. Its acceptance bullets define the
evidence needed to close that issue, and its source links preserve the broader
task contract. **A source task is complete only after all issues mapped to it are
accepted.** A successful early slice does not close the remaining coverage.

“Depends on” lists full issue-acceptance prerequisites, not restrictions on when
design or implementation may begin. External references identify the interface
or agreement needed; their evidence requirement is determined by the particular
issue. Source review can record a runtime gap, whereas a funded execution issue
cannot pass with that gap unresolved.

## Proposed milestones

Counts below use the default placement, before representative job selection.
They differ from the source plan's counts of whole tasks because several tasks
have been split into independently reviewable results.

| Milestone | Proposed issues | Acceptance gate |
| --- | --- | --- |
| [M1: Foundation and integration contracts](#m1-foundation-and-integration-contracts) | 7 | Source baseline, shared/access/payment contracts, importable core, SQLite evidence, and development build checks are reviewable. |
| [M2: Complete builder journey](#m2-complete-builder-journey) | 18 | One minimum-app journey demonstrates all seven outcomes with funded execution and correlated network-cost evidence. |
| [M3: Reuse and reliability](#m3-reuse-and-reliability) | 11 | Remaining required execution modes, REST/MCP and embedded/service coverage, enterprise auth replacement, both payment configurations, and failure/recovery evidence are complete. |
| [M4: Independent installation and release](#m4-independent-installation-and-release) | 3 | Final artifacts, documentation, clean-environment reproduction, and acceptance evidence are reviewed together. |

A milestone passes when its assigned issues and gate evidence are accepted.
Milestone 2 does not replace the required Milestone 3 coverage.

### Representative jobs can change placement without changing scope

ISS-19 selects the jobs after the core execution and reporting path is usable.
If the first selected job needs asynchronous execution, advance ISS-26 from M3
to M2. If it needs a persistent endpoint, advance ISS-27 instead, or both if the
first journey requires both. ISS-20 then depends on the applicable advanced
issue(s). Each issue still has exactly one milestone.

These are explicit conditional prerequisites, not permission to accept the
first journey while its execution support is unfinished. No capability or job
has been selected by this proposal. Once chosen, update the placement and
dependency before accepting M2; the remaining required modes still complete
by M3.

## Proposed implementation homes

| Home | Proposed location | Boundary |
| --- | --- | --- |
| ENGINE | New builder-engine repository; name and organization pending | Shared packages, adapters, REST/MCP services, tests, integration examples, and release tooling. |
| APP | Proposed `examples/reference-app` area in ENGINE; separate repository remains a review option | Minimum reference application and its own interface checks. This does not assign migration of the existing Console repository. |
| PLAN | This repository's Build Track planning documents, owned by Mike Zupper | Source evidence, agreement records, acceptance-matrix decisions, and final scope/evidence sign-off. Link implementation artifacts from their repositories. |

These are placement proposals, not repository-creation actions. If APP moves to
its own repository, its issues and CI/artifact links move with it; the shared
core remains independently releasable. An issue touching a companion artifact
names a primary home and links the companion work rather than claiming that
this coordination repository contains service implementation.

## External handoffs and conditional upstream changes

This table is separate from the 39 Build Track delivery issues. The interface need
may be satisfied by verified existing behavior. An upstream implementation issue
is needed only if verification reveals a gap and the affected maintainer agrees
the change. No external owner, date, or delivery commitment is assigned here.

| Ref | Interface or handoff | Evidence needed for the consuming issue | Where any upstream change belongs |
| --- | --- | --- | --- |
| H1 | Python gateway SDK | Selected-revision discovery/rates, required invocation modes, signing behavior, and usable execution/payment references; explicit disposition of gaps | `livepeer/livepeer-python-gateway` |
| H2 | Payment-core management, authorization, and accounting | Agreed provisioning/read interfaces, scoped access, repeat-command behavior, cost units, correlation, and replay/completeness limits, with an implementation usable for acceptance | `livepeer/clearinghouse-batteries` or the agreed provider's repository |
| H3 | Remote signer and Orchestrator/Live Runner | Compatible discovery, signing, execution, recovery references, and payment-event behavior at selected revisions | `livepeer/go-livepeer` and the relevant runner repository if a gap is located there |
| H4 | Funded acceptance environment | Reachable representative capabilities, funded signing, scoped credentials, and obtainable accounting evidence for the configurations under test | Named test/operator arrangement during later planning; no standing public-service obligation |
| H5 | Source access and permitted reuse | Access and permission for material actually reused; disposition of unavailable private material; independent buildability | Existing Console/Inc source owners for their material; ENGINE for the delivered code |
| H6 | Scope and final acceptance | Agreed acceptance procedure and actual SPE/affected-owner dispositions where needed; evidence tied to the delivered revision | Existing authorities and their decision records; Build Track consequences linked from PLAN |

Build Track integration work remains in ENGINE: inspect an interface, build its adapter,
and prove compatibility. A missing upstream feature remains a visible dependency;
a mock or an adapter declaration does not satisfy funded-job or cost-reporting
acceptance. Any later upstream issue should link back to its consuming Build Track issue.

## M1: Foundation and integration contracts

### ISS-01: Verify the integration baseline and reusable source material

**Milestone:** M1 · **Home:** PLAN · **Source:** [F1](build-track-december-2026-task-breakdown-draft.md#foundation)\
**Depends on:** None · **External:** H1, H2, H3, H5

Acceptance:

- Record selected Console, Python SDK, Batteries, and go-livepeer revisions and recheck the behavior required by the task breakdown; distinguish source evidence from runtime proof.
- Record reusable material, permissions, compatibility gaps, and their dispositions. Review offered private source if available and relevant; the engine remains independently buildable without it.

### ISS-02: Define the shared engine contracts and supported boundaries

**Milestone:** M1 · **Home:** ENGINE · **Source:** [F2](build-track-december-2026-task-breakdown-draft.md#foundation)\
**Depends on:** ISS-01 · **External:** None

Acceptance:

- Document access context, capabilities/rates, jobs/attempts, results, measured usage, cost states, and extension boundaries with examples sufficient to implement and test them.
- Cover immediate, asynchronous, and persistent-endpoint execution; identify upstream contracts and explicitly dispose of deployment, performance, and recovery assumptions. New APIs, HA, financial recourse, and extra streaming are not assumed.

### ISS-03: Define replaceable authentication and access-policy interfaces

**Milestone:** M1 · **Home:** ENGINE · **Source:** [A1](build-track-december-2026-task-breakdown-draft.md#access-and-credentials)\
**Depends on:** ISS-02 · **External:** None

Acceptance:

- Define how trusted standalone and enterprise adapters produce validated actor identity, ownership scope, and permitted operations across imported and service modes.
- Document browser and administrator trust boundaries and credential-lifecycle responsibilities. Enterprises can choose enrollment and authentication without core patches or an additional user-facing engine key; unchecked request fields cannot establish identity.

### ISS-04: Agree payment provisioning, authorization, and reporting contracts

**Milestone:** M1 · **Home:** PLAN · **Source:** [P1](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation)\
**Depends on:** ISS-01, ISS-02 · **External:** H2, H3

Acceptance:

- Record credential/allocation mapping, permitted management operations, reporting access, units, stable references, and repeat-command semantics.
- For each required interface, record available implementation evidence or an agreed gap disposition from the affected maintainer. Link any proposed upstream change to its owning repository; contract agreement does not count as implemented compatibility.

### ISS-05: Establish installable core packages and public extension interfaces

**Milestone:** M1 · **Home:** ENGINE · **Source:** [F3](build-track-december-2026-task-breakdown-draft.md#foundation)\
**Depends on:** ISS-02 · **External:** None

Acceptance:

- The shared core imports and starts independently of the reference application, proprietary identity, PymtHouse, and private Inc source.
- Document supported interfaces for persistence, execution/payment adapters, and enterprise extension. Provide an import/start smoke check using a versioned development build.

### ISS-06: Implement SQLite records, migrations, retention, and backup/restore

**Milestone:** M1 · **Home:** ENGINE · **Source:** [F4](build-track-december-2026-task-breakdown-draft.md#foundation)\
**Depends on:** ISS-05 · **External:** None

Acceptance:

- Persist the required engine-owned access mappings, jobs/attempts, result references, measured usage, and cost projections behind the defined storage interface.
- Exercise restart, schema migration, and restore with representative records; document configurable retention. Preserve the provider ledger as the network-accounting authority.

### ISS-07: Add development builds and continuous checks

**Milestone:** M1 · **Home:** ENGINE · **Source:** [L2](build-track-december-2026-task-breakdown-draft.md#documentation-and-release)\
**Depends on:** ISS-05 · **External:** None

Acceptance:

- Produce versioned development packages and establish automated test, lint/type, and install/start checks for the components available at this milestone.
- Provide the build/test framework that later service and application components extend. Final service/application artifacts and release readiness remain ISS-38.

## M2: Complete builder journey

### ISS-08: Provide standalone credentials and shared ownership controls

**Milestone:** M2 · **Home:** ENGINE · **Source:** [A2](build-track-december-2026-task-breakdown-draft.md#access-and-credentials)\
**Depends on:** ISS-03, ISS-06 · **External:** None

Acceptance:

- A self-contained adapter supports credential issuance, inspection without secret disclosure, rotation, and revocation using one documented example access flow.
- Enforce operation and ownership checks for validated access contexts; reject invalid/revoked access according to the adapter contract. Separate administrative access and keep secrets out of normal logs/responses. Enterprise enrollment remains replaceable.

### ISS-09: Integrate dynamic capability discovery

**Milestone:** M2 · **Home:** ENGINE · **Source:** [D1](build-track-december-2026-task-breakdown-draft.md#discovery-and-expected-rates)\
**Depends on:** ISS-01, ISS-05 · **External:** H1, H3

Acceptance:

- Expose SDK-derived capability identifiers, provider information, inputs/schemas, and execution information where available.
- Reflect additions, changes, and removals without editing a static catalog. Expose freshness, incomplete metadata, and discovery failure; advertised capabilities remain visible without implying verified execution support.

### ISS-10: Expose network rates and pricing assumptions

**Milestone:** M2 · **Home:** ENGINE · **Source:** [D2](build-track-december-2026-task-breakdown-draft.md#discovery-and-expected-rates)\
**Depends on:** ISS-09 · **External:** H1, H3

Acceptance:

- Before invocation, callers can inspect available rates with exact units/currency, source, and relevant assumptions.
- Missing or stale rates are explicit. A network rate is not represented as an immutable total-job quote or an enterprise retail price.

### ISS-11: Integrate scoped allocation provisioning and management

**Milestone:** M2 · **Home:** ENGINE · **Source:** [P2](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation)\
**Depends on:** ISS-04, ISS-06, ISS-08 · **External:** H2

Acceptance:

- Using the agreed provider contract, establish the payment access needed for requests and retrieve the relevant allocation state under scoped administrative authorization.
- Repeated management commands do not double-apply allowance changes. Record the selected allocation mapping and distinguish allowance changes from signer funding and hard spending guarantees. Missing provider implementation must be resolved through H2.

### ISS-12: Connect SDK payment authorization and remote signing

**Milestone:** M2 · **Home:** ENGINE · **Source:** [P3](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation)\
**Depends on:** ISS-04, ISS-05 · **External:** H1, H2, H3

Acceptance:

- SDK invocation uses configured payment credentials and remote signing; authorization denial, exhausted allowance, and unavailable signing are distinguishable.
- Builder-facing clients receive no wallet keys or provider administration credentials. Integration checks exercise the agreed interfaces; funded execution proof is ISS-25.

### ISS-13: Prepare the first funded payment configuration

**Milestone:** M2 · **Home:** ENGINE · **Source:** [P4](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation)\
**Depends on:** ISS-11, ISS-12 · **External:** H4

Acceptance:

- One reproducible payment configuration has documented endpoints, scoped credentials, allocation setup, signer funding, and accounting-access prerequisites.
- A funded test environment is available for the first journey, with responsibility for each external prerequisite explicit. Actual job/payment evidence is captured in ISS-25; the second configuration remains ISS-31.

### ISS-14: Implement durable submission and immediate execution

**Milestone:** M2 · **Home:** ENGINE · **Source:** [J1](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery)\
**Depends on:** ISS-06, ISS-08, ISS-10, ISS-11, ISS-12 · **External:** H1, H3

Acceptance:

- Validate discovered capability inputs, persist owned job/attempt identity before dispatch, invoke through the SDK, and retain immediate results or failures.
- Define repeat-submission references and persistence retry behavior so they do not blindly repeat execution or payment. Asynchronous and persistent-endpoint completion have separate issues.

### ISS-15: Expose owned job history and basic results

**Milestone:** M2 · **Home:** ENGINE · **Source:** [J4](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery)\
**Depends on:** ISS-14 · **External:** None

Acceptance:

- Builders can retrieve their jobs, attempts, result references, and understandable failures with ownership enforcement.
- Document supported input/result-access methods and explain expired or unavailable provider assets. No managed upload service or general media library is required.

### ISS-16: Capture usage and correlate jobs with payment evidence

**Milestone:** M2 · **Home:** ENGINE · **Source:** [U1](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting)\
**Depends on:** ISS-04, ISS-06, ISS-14 · **External:** H1, H2, H3

Acceptance:

- Retain supported execution measurements and the exact provider references needed to correlate each job/attempt with payment observations, including multiple observations per job.
- Unknown quantities and missing references stay explicit; unrelated request, session, job, and manifest identifiers are not treated as interchangeable.

### ISS-17: Maintain replayable network-cost projections

**Milestone:** M2 · **Home:** ENGINE · **Source:** [U2](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting)\
**Depends on:** ISS-04, ISS-11, ISS-16 · **External:** H2, H3

Acceptance:

- Consume provider accounting observations, match them where evidence permits, and handle duplicates, late data, corrections, and unmatched observations.
- Stable references and checkpoint/replay behavior support recovery without double application. Pending or missing evidence is never silently zero or proof of final completeness.

### ISS-18: Expose scoped usage, cost reports, and integration events

**Milestone:** M2 · **Home:** ENGINE · **Source:** [U3](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting)\
**Depends on:** ISS-08, ISS-17 · **External:** None

Acceptance:

- Expose job-level usage/observed network cost and a basic aggregate report with units, attribution, and uncertainty; provide stable IDs and a versioned feed with replay/deduplication semantics.
- Reporting failures preserve successful execution state. Network cost, settlement, and retail billing remain distinguishable.

### ISS-19: Select representative jobs and the acceptance matrix

**Milestone:** M2 · **Home:** PLAN · **Source:** [V1](build-track-december-2026-task-breakdown-draft.md#verification)\
**Depends on:** ISS-09, ISS-14, ISS-18 · **External:** H4

Acceptance:

- Choose available jobs after discovery, execution, and reporting are usable; record inputs, expected observations, pinned versions, and the initial seven-outcome journey.
- Define coverage of immediate/asynchronous/persistent endpoints, REST/MCP, embedded/service use, enterprise-auth replacement, and both payment configurations. Avoid a full catalog test requirement. If the first job needs ISS-26 or ISS-27, advance that prerequisite into M2 before accepting the journey.

### ISS-20: Expose REST operations for the first complete journey

**Milestone:** M2 · **Home:** ENGINE · **Source:** [I1](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse)\
**Depends on:** ISS-08, ISS-10, ISS-15, ISS-18, ISS-19 · **External:** None

**Conditional prerequisites:** ISS-26, ISS-27 only when required by the first job selected in ISS-19; advance the applicable issue into M2 as described above.

Acceptance:

- Document and exercise authenticated discovery, rate lookup, submission, status/results, and usage/cost operations for the selected first journey, using the shared core and its access rules.
- Include necessary credential/admin operations under appropriate authorization. If the selected job needs asynchronous or persistent-endpoint support, its advanced prerequisite must be accepted first. Complete baseline REST coverage remains ISS-29.

### ISS-21: Build the reference application's access and live catalog

**Milestone:** M2 · **Home:** APP · **Source:** [R1](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application)\
**Depends on:** ISS-20 · **External:** None

Acceptance:

- Provide one documented example access flow and display the orchestrator-advertised catalog, capability inputs, available rates, and stale/missing metadata.
- Advertised catalog changes require no hand-maintained entries. Use supported access interfaces, with no full onboarding portal or bespoke screen per capability. Demonstrating replacement of the app's access flow remains ISS-33.

### ISS-22: Connect the reference application's first execution and reporting journey

**Milestone:** M2 · **Home:** APP · **Source:** [R2](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application)\
**Depends on:** ISS-20, ISS-21 · **External:** None

Acceptance:

- A builder can supply supported inputs, submit the selected job, follow its state, access its result or understandable failure, and inspect job history and usage/cost through the shared engine.
- The app contains no separate network execution/payment implementation. Full baseline application coverage remains ISS-34; a complete Console port is excluded.

### ISS-23: Verify access, repeat-command, and accounting behavior for the first journey

**Milestone:** M2 · **Home:** ENGINE · **Source:** [V3](build-track-december-2026-task-breakdown-draft.md#verification)\
**Depends on:** ISS-08, ISS-11, ISS-14, ISS-17, ISS-20 · **External:** None

Acceptance:

- Retain automated checks for cross-actor access, revoked credentials, duplicate submission/management commands, authorization denial, and delayed/duplicate cost observations.
- Assert that jobs and costs remain explainable and retries do not blindly repeat work. Identify which cases use fixtures; funded-path evidence must come from ISS-25. Broader recovery coverage remains ISS-35.

### ISS-24: Write the first runnable installation and journey guide

**Milestone:** M2 · **Home:** ENGINE · **Source:** [L1](build-track-december-2026-task-breakdown-draft.md#documentation-and-release)\
**Depends on:** ISS-07, ISS-13, ISS-22 · **External:** None

Acceptance:

- Version-matched steps take a reviewer from the development artifacts and stated payment prerequisites through access, discovery, rates, submission, results, and reporting.
- Include the reference-app entry point, sample commands/inputs, and known limitations without secrets. Complete integration and operating guidance remains ISS-37.

### ISS-25: Prove the first funded seven-outcome journey

**Milestone:** M2 · **Home:** ENGINE · **Source:** [V2](build-track-december-2026-task-breakdown-draft.md#verification)\
**Depends on:** ISS-13, ISS-19, ISS-22, ISS-23, ISS-24 · **External:** H4

Acceptance:

- Run the selected journey and retain reproducible evidence connecting the builder credential, live discovery/rate, execution, result/failure, usage, and actual network-payment cost observations.
- The builder handles no crypto; operator funding and all external prerequisites are explicit. Mocks, allowance creation alone, or pending-cost labels alone do not pass this gate. The remaining configuration matrix is ISS-36.

## M3: Reuse and reliability

### ISS-26: Support asynchronous jobs and durable recovery handles

**Milestone:** M3 · **Home:** ENGINE · **Source:** [J2](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery)\
**Depends on:** ISS-14, ISS-15, ISS-19 · **External:** H1, H3

Acceptance:

- A job outlives its original request and exposes durable status and eventual result/failure using the supported provider handle.
- Disconnect and restart preserve identity and recovery references without submitting replacement execution. Default milestone is M3; ISS-19 advances this whole issue to M2 if needed for the first selected journey.

### ISS-27: Support persistent application endpoint invocation

**Milestone:** M3 · **Home:** ENGINE · **Source:** [J3](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery)\
**Depends on:** ISS-14, ISS-19 · **External:** H1, H3

Acceptance:

- Invoke supported discovered persistent endpoints using the agreed inputs/results contract and preserve owned job, result, and payment references.
- Demonstrate a representative endpoint and distinguish it from queued completion and continuous streaming. Default milestone is M3; ISS-19 advances this whole issue to M2 if needed for the first selected journey.

### ISS-28: Complete failure classification and recovery across baseline modes

**Milestone:** M3 · **Home:** ENGINE · **Source:** [J5](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery)\
**Depends on:** ISS-15, ISS-26, ISS-27 · **External:** H1, H3

Acceptance:

- Distinguish validation, access, capacity, execution, payment, and reporting failures across the baseline modes; preserve evidence for timeout, restart, uncertain outcome, and failed final save.
- Recovery checks existing work before supported retries and does not infer success from payment alone. Generic cancellation, automatic failover, and exactly-once execution are not promised.

### ISS-29: Complete REST coverage across the required execution modes

**Milestone:** M3 · **Home:** ENGINE · **Source:** [I1](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse)\
**Depends on:** ISS-18, ISS-20, ISS-28 · **External:** None

Acceptance:

- Extend and verify the initial REST contract for all required modes, durable status/results, shared errors, and ownership rules.
- Run contract checks showing that all REST operations use shared behavior and preserve initial journey compatibility. This closes the remaining I1 scope after ISS-20.

### ISS-30: Expose the same authorized journey through MCP

**Milestone:** M3 · **Home:** ENGINE · **Source:** [I2](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse)\
**Depends on:** ISS-29 · **External:** None

Acceptance:

- Provide discovery, rates, invocation, status/results, and usage/cost tools using the configured authentication adapter and the same core authorization/semantics as REST.
- Verify interoperability with the pinned client and access configuration chosen in ISS-19. No universal OAuth/API-key path is imposed on enterprises; MCP progress is not treated as inference streaming.

### ISS-31: Complete both payment-operation configurations

**Milestone:** M3 · **Home:** ENGINE · **Source:** [P4](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation)\
**Depends on:** ISS-13 · **External:** H2, H3, H4

Acceptance:

- Add and verify the payment-operation configuration not covered by ISS-13 so both self-operated and separately operated payment access have usable setup, funding, credentials, and reporting prerequisites.
- Document the actual test/operator arrangement and its limits. Do not imply an ongoing public service; full funded evidence for both configurations is ISS-36.

### ISS-32: Prove package embedding, service consumption, and enterprise extensions

**Milestone:** M3 · **Home:** ENGINE · **Source:** [I3](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse)\
**Depends on:** ISS-07, ISS-29, ISS-30 · **External:** None

Acceptance:

- Use one versioned core candidate in embedded and service examples. Replace standalone authentication with an enterprise adapter while preserving ownership checks and avoiding an extra user-facing engine key.
- Demonstrate an additional endpoint/tool and minimal mock-commerce/reporting integration through public interfaces, including repeat/event handling, without core patches or direct table/ledger writes. Standalone use remains independent of the fixture.

### ISS-33: Demonstrate replacement of the reference application's access flow

**Milestone:** M3 · **Home:** APP · **Source:** [R1](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application)\
**Depends on:** ISS-21, ISS-32 · **External:** None

Acceptance:

- Connect the reference app to the alternative enterprise-auth example using the supported access contract, without changing shared core source or requiring its default enrollment flow.
- Verify catalog/rate access and isolation under that configuration. One reference login remains an example, not a required enterprise policy or a mandate to implement every identity provider.

### ISS-34: Complete reference-app coverage of baseline execution and reporting

**Milestone:** M3 · **Home:** APP · **Source:** [R2](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application)\
**Depends on:** ISS-22, ISS-28, ISS-29 · **External:** None

Acceptance:

- Exercise the minimal app with the selected immediate, asynchronous, and persistent-endpoint jobs, including durable status, results/history, understandable failures, and correlated usage/cost.
- Handle missing metadata, unavailable results, and pending/uncertain costs visibly. Continue using the shared engine; extra Console screens and product features remain stretch scope.

### ISS-35: Verify full isolation, recovery, and accounting replay behavior

**Milestone:** M3 · **Home:** ENGINE · **Source:** [V3](build-track-december-2026-task-breakdown-draft.md#verification)\
**Depends on:** ISS-06, ISS-23, ISS-28, ISS-29, ISS-30, ISS-31, ISS-32 · **External:** H1, H2, H3

Acceptance:

- Extend early checks across required interfaces and auth configurations, restart/disconnect, uncertain final saves, late/unmatched/corrected cost observations, and replay without double application.
- Exercise SQLite migration/restore with integrated records and supported recovery handles. Clearly separate injected failures from observed upstream behavior and record unresolved external evidence limits.

### ISS-36: Prove funded journeys across the complete acceptance matrix

**Milestone:** M3 · **Home:** ENGINE · **Source:** [V2](build-track-december-2026-task-breakdown-draft.md#verification)\
**Depends on:** ISS-19, ISS-25, ISS-31, ISS-32, ISS-33, ISS-34, ISS-35 · **External:** H4

Acceptance:

- Complete the matrix selected in ISS-19, demonstrating all seven outcomes across required modes and integration/payment configurations with pinned versions and real payment observations.
- Retain reproducible commands, results, and correlation evidence with explicit limitations. No exhaustive catalog or Cartesian-product test obligation is introduced; final artifacts are rechecked in ISS-39.

## M4: Independent installation and release

### ISS-37: Complete installation, extension, and operating documentation

**Milestone:** M4 · **Home:** ENGINE · **Source:** [L1](build-track-december-2026-task-breakdown-draft.md#documentation-and-release)\
**Depends on:** ISS-24, ISS-31, ISS-32, ISS-33, ISS-34, ISS-35 · **External:** None

Acceptance:

- Finalize version-matched guidance for both integration/payment modes, enterprise auth replacement, jobs/reporting, configuration, upgrades, retention, backup/restore, and recovery.
- Link reference-app instructions and supported interface examples; explain secrets, funding prerequisites, logs/correlation, and limitations. Documentation must match the actual release candidate and remain usable without its authors present.

### ISS-38: Prepare final release artifacts and controlled release procedures

**Milestone:** M4 · **Home:** ENGINE · **Source:** [L2](build-track-december-2026-task-breakdown-draft.md#documentation-and-release)\
**Depends on:** ISS-07, ISS-29, ISS-30, ISS-34, ISS-35, ISS-37 · **External:** H5

Acceptance:

- Build versioned packages and service/application containers, with relevant tests, lint/type checks, and install/start checks passing for the delivered components. Link any companion APP build artifacts.
- Provide release notes, configuration examples, documented reuse/license decisions, and controlled release procedures. Public publication, organization transfer, and ongoing service operation are separate authorized actions.

### ISS-39: Prove independent installation and record final acceptance

**Milestone:** M4 · **Home:** PLAN · **Source:** [L3](build-track-december-2026-task-breakdown-draft.md#documentation-and-release)\
**Depends on:** ISS-36, ISS-37, ISS-38 · **External:** H6

Acceptance:

- A reviewer reproduces the agreed seven-outcome journey from a clean environment using the delivered artifact versions and instructions, including the required configuration/reuse evidence and explicit payment prerequisites.
- Link the exact versions, commands, results, known limits, and remaining external dependencies to the acceptance record. Obtain the applicable scope/evidence sign-off; this proposed issue does not constitute approval.

## Source-task coverage

This crosswalk is the completion rule for the original 31 tasks. It also makes
scope review possible without treating every split issue as a new requirement.
The source plan remains the scope reference; issue prerequisites refine its
broader task-level ordering so the first journey can be reviewed independently.

| Source task | Proposed issue(s) | Full source-task acceptance |
| --- | --- | --- |
| [F1](build-track-december-2026-task-breakdown-draft.md#foundation) | ISS-01 | M1 |
| [F2](build-track-december-2026-task-breakdown-draft.md#foundation) | ISS-02 | M1 |
| [F3](build-track-december-2026-task-breakdown-draft.md#foundation) | ISS-05 | M1 |
| [F4](build-track-december-2026-task-breakdown-draft.md#foundation) | ISS-06 | M1 |
| [A1](build-track-december-2026-task-breakdown-draft.md#access-and-credentials) | ISS-03 | M1 |
| [A2](build-track-december-2026-task-breakdown-draft.md#access-and-credentials) | ISS-08 | M2 |
| [D1](build-track-december-2026-task-breakdown-draft.md#discovery-and-expected-rates) | ISS-09 | M2 |
| [D2](build-track-december-2026-task-breakdown-draft.md#discovery-and-expected-rates) | ISS-10 | M2 |
| [P1](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation) | ISS-04 | M1 |
| [P2](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation) | ISS-11 | M2 |
| [P3](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation) | ISS-12 | M2 |
| [P4](build-track-december-2026-task-breakdown-draft.md#payment-authorization-and-operation) | ISS-13, ISS-31 | M3 |
| [J1](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery) | ISS-14 | M2 |
| [J2](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery) | ISS-26 | M3 by default; M2 if advanced for the first journey |
| [J3](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery) | ISS-27 | M3 by default; M2 if advanced for the first journey |
| [J4](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery) | ISS-15 | M2 |
| [J5](build-track-december-2026-task-breakdown-draft.md#execution-results-and-recovery) | ISS-28 | M3 |
| [U1](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting) | ISS-16 | M2 |
| [U2](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting) | ISS-17 | M2 |
| [U3](build-track-december-2026-task-breakdown-draft.md#usage-and-network-cost-reporting) | ISS-18 | M2 |
| [I1](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse) | ISS-20, ISS-29 | M3 |
| [I2](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse) | ISS-30 | M3 |
| [I3](build-track-december-2026-task-breakdown-draft.md#rest-mcp-and-application-reuse) | ISS-32 | M3 |
| [R1](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application) | ISS-21, ISS-33 | M3 |
| [R2](build-track-december-2026-task-breakdown-draft.md#minimum-reference-application) | ISS-22, ISS-34 | M3 |
| [V1](build-track-december-2026-task-breakdown-draft.md#verification) | ISS-19 | M2 |
| [V2](build-track-december-2026-task-breakdown-draft.md#verification) | ISS-25, ISS-36 | M3 |
| [V3](build-track-december-2026-task-breakdown-draft.md#verification) | ISS-23, ISS-35 | M3 |
| [L1](build-track-december-2026-task-breakdown-draft.md#documentation-and-release) | ISS-24, ISS-37 | M4 |
| [L2](build-track-december-2026-task-breakdown-draft.md#documentation-and-release) | ISS-07, ISS-38 | M4 |
| [L3](build-track-december-2026-task-breakdown-draft.md#documentation-and-release) | ISS-39 | M4 |

## Review and conversion

The useful review now is of issue boundaries, milestone exit evidence, and
repository placement. Check whether an issue can be accepted on its own evidence,
whether anything required by the source task is missing, and whether an example
has inadvertently become an enterprise product requirement. Review the conditional
execution-mode prerequisites when representative jobs are selected.

After proposal review, agree repository homes and the GitHub/Beads tracking
convention before converting drafts into repository issues. Add implementation
assignees, estimates, and dates during subsequent planning. Translate these review
IDs into actual issue links, keep upstream handoffs separate, and preserve the
source-task crosswalk. Existing architecture and SPE scope approvals must be
recorded rather than inferred from approval of issue formatting.

The project contains 39 project-only draft items; repository issues and Beads
delivery records have not been created for this proposal. The captured auth
discussion remains reference material; this proposal follows Mike's explicit
enterprise-choice clarification and does not adopt an upstream JWT design or a
compulsory onboarding path.
