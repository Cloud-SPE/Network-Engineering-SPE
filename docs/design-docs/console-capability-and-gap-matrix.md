# Required App Capabilities, Current Providers, and Gaps

**Status:** Draft capability inventory for Mike's proposal; not approved implementation scope\
**Prepared:** 23 September 2026\
**Evidence consolidation:** 24 September 2026\
**Owner:** Mike Zupper\
**Design:** [Self-sovereign open builder stack](self-sovereign-open-builder-stack-draft.md)\
**Decision status:** Pending architecture and scope review; no accepted decision

## Selected product profile

Mike's latest direction is a noncommercial open stack with commerce implemented
externally through supported package interfaces or service APIs/events. This inventory still describes the larger
existing Console surface. Section D is now **external extension scope**, not
features to recreate in the open core. Earlier full-parity assumptions are
superseded by the linked design.

Core acceptance centers on access, discovery, rates, invocation, results,
network payment, cost evidence and independent operation. Device login (A6) and enhanced upload/media storage (B8) remain experience
choices to disposition. A Console-informed sample is selected; its exact browser
feature set (B5) still needs definition. Basic result access remains core. Customer invoicing and
retail charges are external; the standalone app shows network cost.

## How to read this inventory

The target app must provide a coherent builder experience without requiring
PymtHouse. “Target app” now means the new backend repository and sample enterprise
application. Console is the behavior/code reference, not the required host.
Rows below inventory existing behavior, not an instruction to recreate all of
Console inside core. SSO belongs to the enterprise/example; standalone access
is a pending policy decision. Mock commerce demonstrates extension points;
working Stripe checkout and production commerce are excluded.

**Existing** means implementation found in the inspected source, not production
verification. **Partial** means useful code exists but the target requirement
is incomplete. **External contract** means Console calls an upstream service;
the upstream implementation was not inspected. **Gap** means the reviewed
components do not establish the required independent behavior.

Source baseline: Mike's 22 September Console/Batteries engineering research,
selectively preserved here on 24 September. This document now contains the useful source map, behavior
qualifications and integration findings; no external research folder is needed.
The original seven documents and 25 duplicated diagram sets were not imported.
Their proposed replacement architecture and delivery choices are superseded by
the primary design, not adopted as source facts.

Console `009a703d7b6434bab905902375f562e5980728af` and Batteries
`6b75564247dd6dc20b2690a103445e9a9b392223` remain the inspected local revisions
as of 24 September. Source paths below were verified in those Git objects;
execution/payment callback and authorization/funding details were spot-checked.
This is source evidence, not a fresh complete audit, latest-upstream claim or
runtime parity test. Supporting earlier spot checks used go-livepeer
`e8dcf7a34744d5cb6b65ba43c0d9160a3975ccc6` and Python Gateway
`44df06157fcdb864e37d971e8caba86b2a7dc92e`; neither was fully audited for parity.

Console tests were not run for the original research or this preservation pass.
The original research reported a Batteries `make check` pass, but no retained
execution log is supplied here; it is not acceptance evidence. No funded network
jobs or production-service validation were performed. Recheck the source map and
relevant behavior when selecting different revisions, without rewriting this
snapshot as if it described the newer code.

Current providers named below:

- **Console:** `livepeer/console`; application backend, browser UI and MCP.
- **Batteries:** `livepeer/clearinghouse-batteries`; payment authorization and accounting.
- **go-livepeer:** `livepeer/go-livepeer`; remote signer and Orchestrator roles.
- **Python SDK:** `livepeer/livepeer-python-gateway`; client-side discovery, payment and execution code.
- **PymtHouse:** hosted contracts plus `@pymthouse/builder-sdk` and
  `@pymthouse/gateway-web`; no inspected source repository is assigned to its
  private services. It is not synonymous with Batteries or `livepeer/clearinghouse`.

## A. Accounts and access

| ID | Required capability | What provides it today | Gap for the independent app |
| --- | --- | --- | --- |
| A1 | Sign in and maintain a stable user identity | **Existing:** Console identity records and Auth0 browser login | Enterprise/example supplies login; map validated subjects into opaque core actors. Core must not require Auth0 or customer profiles. |
| A2 | Approve, disable and administer user access | **Existing:** Console admission gates, admin permissions and audit records | Separate core access controls from enterprise admission policy; remove PymtHouse account/token assumptions. |
| A3 | Provision the user's payment account and spending allocation | **Partial:** Console binds users to a PymtHouse account; Batteries creates grants/allocations through CLI | Define service/actor-to-allocation mapping and authenticated, retry-safe provisioning. Per-customer allocations are not mandated; grants are not user identities. |
| A4 | Issue, list, rotate and revoke developer API credentials | **Partial/external:** Console key UI delegates to PymtHouse; Batteries has allocation-key CLI operations | Implement owner-scoped credential APIs and rotation behavior; distinguish platform access from payment authorization. |
| A5 | Authenticate MCP/API clients using access tokens and refresh | **Partial/external:** Console OAuth/PKCE flow exists; access-token minting and issuer/JWKS depend on PymtHouse | Define standalone access and enterprise auth adapters. API-key baseline and example OAuth are recommendations; no mandatory provider issuer. Existing routes alone are insufficient. |
| A6 | Approve device/CLI login | **External contract:** Console forwards device approval to PymtHouse | Optional example behavior to disposition; do not require a new device authorization server by default. |

## B. Discovery, execution, and results

| ID | Required capability | What provides it today | Gap for the independent app |
| --- | --- | --- | --- |
| B1 | Discover available capabilities and eligible providers | **Existing/partial:** go-livepeer signer discovery; Python SDK discovery; Console MCP normalization | Remove PymtHouse signer-session lookup dependency; define shared discovery records and freshness. Wire the browser catalog to live data. |
| B2 | Show capability inputs, supported modes and schemas | **Partial:** Console MCP uses discovery plus local catalog/schema hints | Establish authoritative schema/version sources and validate the selected capability end to end. Static hints do not prove current provider support. |
| B3 | Show an expected price or rate before invocation | **Partial:** signer publishes rates; Console MCP and Python SDK expose price metadata | Normalize exact units and source; display network-rate assumptions; enterprise applies any customer markup. Representative discovery prices are not binding job quotes. |
| B4 | Invoke through a supported programmatic interface | **Existing/partial:** Console MCP dispatches using PymtHouse gateway SDK; Python SDK has Live Runner/payment code | Replace mandatory gateway SDK dependency with a verified execution adapter; prove required progress, payment callbacks and session behavior. A generic public run-submission API is not established by Console's history API. |
| B5 | Invoke from the browser if the app exposes a playground | **Partial:** Console has playground UI/fixtures and a separate live MCP path | Connect browser inputs to the real discovery/execution path; reuse backend behavior rather than implementing a second execution path. |
| B6 | Track progress and retain job history and results | **Existing:** Console durable runs, events, results and payment manifests | Preserve behavior with the independent execution adapter; define background execution where jobs outlive requests. Batteries does not execute jobs. |
| B7 | Explain failures and recover uncertain outcomes | **Partial:** Console failure records and limited read-only provider recovery; SDK error handling | Prove failure classification and supported recovery for the selected capability; schedule recovery as needed. Cancellation, generic retries and exactly-once execution are not established. |
| B8 | Access result assets and provide inputs | **Partial:** Console stores asset URLs, ownership metadata and signed references; upload-named MCP tools request public URLs | Document the public-URL baseline. Upload storage and durable media retention need separate implementation if promised; metadata is not a media archive. |

## C. Network payments and cost evidence

| ID | Required capability | What provides it today | Gap for the independent app |
| --- | --- | --- | --- |
| C1 | Authorize network payments without exposing a wallet to the builder | **Existing components:** Batteries key/allocation policy and go-livepeer remote signer; client SDK requests payments | Connect account provisioning, credential delivery and SDK signing into a supported app flow. Signer escrow funding remains an operator responsibility. |
| C2 | Allocate budget and view spendable balance | **Existing/partial:** Batteries grant/allocation ledger and CLI; Console calls PymtHouse for account balance/access status | Add authenticated control/read APIs and owner mapping. Creating a grant does not fund signer escrow. |
| C3 | Record network fees and prevent duplicate accounting | **Existing:** go-livepeer signed-ticket events; Batteries transactional ingestion, deduplication and ledger | Pin event compatibility and expose evidence to the app. Existing authorization does not reserve future cost or guarantee a hard spending cap. |
| C4 | Attribute network cost to the correct job/attempt | **Partial:** Console has run/manifest lineage through PymtHouse; Batteries has payment-session/event evidence | Define and verify cross-repository correlation; expose missing references and aggregation. Do not assume run, request, manifest and signer-state IDs are interchangeable. |
| C5 | Show account usage, per-job costs and daily/capability summaries | **External/partial:** Console presentation calls PymtHouse usage APIs; Batteries offers operator reports | Build owner-scoped reporting/projections from execution and network-accounting evidence. Preserve pending, unmatched, late and corrected states. |
| C6 | Reconcile recorded usage with network settlement | **Existing/partial:** Batteries optional on-chain listener and session-level attribution | Expose appropriate operator evidence and uncertainty. Winning-ticket settlement is not an exact one-to-one job receipt. |

## D. Commercial features currently consumed by Console

These describe the commercial features consumed by the existing Console. The
example may mock these flows; real implementations belong to enterprises. They
are explicitly excluded from the selected open-core product and can be supplied
by external applications. Sponsoring an allocation does not implement these
features; this product no longer claims full commercial parity.

| ID | External feature | What provides it today | Gap for the independent app |
| --- | --- | --- | --- |
| D1 | Product plans, subscription entitlements and periodic allowances | **External contract:** Console billing adapters/UI call PymtHouse | Independent billing catalog and entitlement lifecycle; explicit bridge from entitlement to network budget. |
| D2 | Checkout and payment-method management | **External contract:** Console requests hosted payment flows from PymtHouse | Commercial payment-provider integration, account linkage and deduplicated payment events. Batteries has no checkout. |
| D3 | Subscription changes, cancellation, resumption and history | **External contract:** PymtHouse through Console adapters | Replacement subscription operations, timing rules and local entitlement reconciliation. |
| D4 | Invoices and invoice history | **External contract:** Console retrieves PymtHouse billing records/links | Independent invoice retrieval/issuance through the selected billing provider; preserve historical source records. |
| D5 | Customer credit balance, top-ups and associated billing records | **External contract:** PymtHouse wallet/top-up APIs | Commercial customer-credit authority plus payment/funding integration. This is separate from signer escrow and Batteries allocations. |
| D6 | USD display, customer pricing and markup | **External/partial:** Console consumes upstream USD cost and billing data; Batteries records ETH/wei | Exchange-rate evidence, rounding and pricing policy. Keep network cost distinct from the customer's bill. |

Refunds and chargebacks require explicit treatment in the replacement commercial
integration, but the reviewed Console contracts do not establish complete
existing refund/chargeback behavior. Do not label these as verified parity.

## E. Deployment and reuse requirements

| ID | Required capability | What provides it today | Gap for the independent app |
| --- | --- | --- | --- |
| E1 | Independently deploy the full supported app | **Partial:** individual repository configuration and deployment code | Version-pinned installation covering identity, app database, Batteries, signer, SDK/worker and optional example identity integration. Commerce is not required. No PymtHouse credentials, issuer or required packages. |
| E2 | Operate and recover the combined system | **Partial:** Console recovery script; Batteries health and ledger/chain tooling | Scheduled recovery, lag/quarantine monitoring, backups/restores and cross-component operational guidance. |
| E3 | Swap payment providers without rewriting app features | **Gap:** current Console integrations use PymtHouse-specific contracts | Provider-neutral account/payment/report interfaces plus a working independent implementation. PymtHouse can be optional. |
| E4 | Let other applications use the same payment core | **Partial:** Batteries and signer exist separately from Console | Generic supported payment APIs and documented integration; no required adoption of Console's user or job schema. |
| E5 | Demonstrate builder-controlled wallet-funded access | **Partial:** signer and SDK payment components | Separate deployment and acceptance proof. Sponsored access alone does not prove the independently funded journey. |

## Current implementation homes

| Proposed home | Selected responsibility | Boundary |
| --- | --- | --- |
| New backend repository | Shared core packages, REST/MCP services, access context, B1–B4/B6–B7, C4–C5, persistence and provider adapters | Console behavior extracted/redesigned; no mandatory PymtHouse or commerce |
| Sample enterprise app | Login/admission experience, browser journey, added tools/endpoints and mocked D1–D6 scenarios as selected | Import core or call deployed service; real commerce is enterprise work |
| Console | Existing behavior and reusable code evidence | Its migration is not an automatic delivery assignment |
| Python SDK | Discovery/rates and execution/payment integration | Verify Console baseline compatibility; worker process topology remains open |
| Batteries | Authorization, allocations and network ledger; proposed scoped management/reporting surfaces | Upstream changes require maintainer agreement; no customer/retail model |
| go-livepeer | Signer, event production and current Orchestrator/Runner integration | Consume existing primitives; verify evidence and raise gaps upstream |
| New repo tooling | Installable packages, containers, tests, CI and controlled release workflows | Mike interim owner; future Livepeer org transfer, no publication authorized here |

## Execution baseline and additional scope

Mike requires Console's current execution behavior. At the pinned Console
revision, `lib/mcp/mcp-server.ts`, `lib/mcp/run-capability.ts` and
`lib/mcp/gateway.ts` show single-shot invocation, queue completion/recoverable
handles and persistent application endpoint support. Its HTTP MCP adapter sends
progress notifications; this does not establish continuous inference streaming.
The new Python SDK path must prove representative runtime parity. Additional
incremental text and continuous live audio/video scope is explicitly undecided
and does not block the baseline.

Persistence minimum: SQLite with a defined interface for engine records,
migrations and recovery. PostgreSQL is a target. Enterprise stores integrate
through supported persistence adapters, stable IDs and events, not arbitrary
shared-schema assumptions. Neither database choice establishes HA guarantees.

## Definition of a complete replacement

A selected core feature is complete only when its replacement behavior is
implemented and verified in the supported deployment. Section D is external
extension scope and is not part of core completion. A screen, adapter interface, database
table or command-line primitive alone does not complete the user journey.

For each inventory row, implementation review must identify exact
source calls, replacement contract, implementation repository, owner, remaining
work and acceptance evidence. The source review does not establish estimates or
external delivery commitments. The design's
[acceptance requirements](self-sovereign-open-builder-stack-draft.md#delivery-and-acceptance)
define integration, parity and cutover gates.

Hard spending ceilings, immutable total-job quotes, provably complete final
fees, production HA/SLAs and generic cancellation are additional guarantees to
decide explicitly. They must not be mistaken for features already supplied by
the inspected stack.

## Preserved source evidence

Links use immutable commit IDs rather than a moving branch or local Desktop
paths. They establish where to reproduce the source review, not guarantees about
a deployed service. Row IDs refer to the inventory above.

| Repository | Pinned source | Evidence supported |
| --- | --- | --- |
| Console | [package.json](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/package.json) | Framework and gateway dependencies; package presence does not establish SDK parity |
| Console | [lib/mcp/mcp-server.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/mcp/mcp-server.ts) | B1–B4/B8/C5: complete MCP tool inventory and invocation/progress interface |
| Console | [lib/mcp/discovery.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/mcp/discovery.ts) | B1–B3: aggregation and representative rate metadata, not immutable quotes |
| Console | [lib/mcp/gateway.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/mcp/gateway.ts) | B4: gateway SDK boundary and signer-refresh retry |
| Console | [lib/runs/execute.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/runs/execute.ts) | B4/B6/B7/C4: persist-before-dispatch, awaited payment callbacks, outcomes |
| Console | [lib/runs/store.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/runs/store.ts) | B6/C4: owned runs, events, payment lineage and recovery records |
| Console | [lib/runs/reconcile.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/runs/reconcile.ts) | B7: bounded provider-status recovery, not new inference dispatch |
| Console | [lib/runs/manifest-billing.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/runs/manifest-billing.ts) | C4/C5: matching owned manifests to cumulative billing observations |
| Console | [lib/console/manifest-usage.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/console/manifest-usage.ts) | C4/C5: external bearer-scoped usage contract |
| Console | [lib/console/session-user.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/console/session-user.ts) | A1–A3: browser identity, admission and external-account dependencies |
| Console | [lib/mcp/jwt.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/mcp/jwt.ts) | A5: provider issuer/JWKS and account binding |
| Console | [app/token/route.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/app/token/route.ts) | A5: code/refresh flow and external access-token exchange |
| Console | [lib/console/pymthouse-billing-bff.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/lib/console/pymthouse-billing-bff.ts) | D1–D6: external commerce requests, not provider internals |
| Console | [app/api/assets/[id]/route.ts](https://github.com/livepeer/console/blob/009a703d7b6434bab905902375f562e5980728af/app/api/assets/%5Bid%5D/route.ts) | B8: owned/signed asset access and controlled provider fetching |
| Batteries | [internal/app/server.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/app/server.go) | C1/E1: service/listener surface and startup |
| Batteries | [internal/app/cli.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/app/cli.go) | A3/A4/C2: actual operator command surface |
| Batteries | [internal/app/presentation.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/app/presentation.go) | C5: report fields actually exposed versus stored evidence |
| Batteries | [internal/auth/http.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/auth/http.go) | C1: outer webhook credential and transport/decision response distinction |
| Batteries | [internal/store/auth.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/store/auth.go) | C1/C2: nested credential, session binding and balance policy |
| Batteries | [internal/store/manage.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/store/manage.go) | C2: grant/allocation/key lifecycle and fresh funding operation IDs |
| Batteries | [internal/store/ingest.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/store/ingest.go) | C3/C4: validation, deduplication, quarantine and accounting |
| Batteries | [internal/kafka/listener.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/kafka/listener.go) | C3/E2: consumer checkpoint/offset behavior |
| Batteries | [internal/store/settlements.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/store/settlements.go) | C6: settlement attribution and compensation |
| Batteries | [internal/chain/listener.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/chain/listener.go) | C6/E2: chain observations and reorg handling |
| Batteries | [internal/store/store.go](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/internal/store/store.go) | C2/E2: exact ledger operations and SQLite configuration |
| Batteries | [migrations/001_initial.sql](https://github.com/livepeer/clearinghouse-batteries/blob/6b75564247dd6dc20b2690a103445e9a9b392223/migrations/001_initial.sql) | C2–C6: domain schema, monetary records and constraints |

### Console MCP behavior inventory

The pinned `mcp-server.ts` above registers these 13 tools. This is a behavior
inventory, not a decision to put every tool in the new core. Discovery/execution
and usage evidence belong to the shared journey; application asset-library and
identity presentation need an explicit core/example disposition.

| Tool(s) | Pinned behavior and qualification |
| --- | --- |
| `list_capabilities` | Signer discovery aggregated by app; not an immutable offer |
| `describe_capability` | Discovery plus local endpoint/schema hints; no guarantee of live capacity |
| `get_pricing` | Available rate metadata; not a binding total-job quote |
| `run_capability` | Exact capability/inputs; single-shot or persistent endpoint; queued results/progress |
| `upload`, `upload_image`, `create_upload_url` | Public-HTTPS-URL instructions/unavailable response; no implemented upload/storage service |
| `get_recent_assets`, `search_assets` | Owned asset-reference retrieval, not a permanent media archive |
| `forget_assets` | Hides library records; does not delete provider files or run history |
| `get_cost_report`, `me_usage` | Provider-backed current UTC-day spend/usage; not generic per-job history |
| `me` | Principal/account/app identity; response labels Console access unknown although transport enforces admission |

Browser catalog/playground fixtures are distinct from the live MCP execution
path. The run-list/detail API does not establish a general REST submission API.
A browser file chooser does not establish an upload service. Newsletter
subscriptions and Console admission grants are unrelated to paid subscriptions
and Batteries monetary grants, respectively.

### Console execution and reporting behavior to preserve or disposition

- Persist owned run identity before dispatch. Failure to persist the running
  transition prevents dispatch. Persistence retries must not repeat inference.
- Retain the gateway request ID and awaited payment-manifest callbacks across
  execution. The SDK adapter has a signer-refresh retry; this is not evidence
  that arbitrary inference failures can be retried safely.
- Record progress and provider recovery handles separately from terminal results.
  Client notification failure does not imply failed execution. A failed final
  save can accompany a real result; report persistence uncertainty honestly.
- Recovery is bounded, read-only inspection of supported public `queue.fal.run`
  status/result handles. It neither submits replacement work nor infers success
  from payment records. Its one-shot script does not prove a deployed scheduler.
- Join billing by exact owned manifest identifiers, including multiple manifests
  per run. Cumulative observations are projections, not new financial postings.
  Missing fees remain pending/unmatched; billing refresh failure must not change
  a successful execution into a failed one.
- Asset references represent provider URLs/metadata with controlled access.
  Provider retention and media availability are external. A `cancelled` status
  enum does not establish a generic cancellation API.

These are compatibility questions for the Python SDK integration. They do not
mandate carrying Console's Next.js runtime, Auth0, queue provider, separate
worker topology or full application schema into the new engine.

### Batteries integration details

- The signer webhook uses an outer `Livepeer-Clearinghouse-Token`; the gateway
  credential is nested in the body's `headers.Authorization`. Neither is an
  enterprise customer login. Normal policy responses use HTTP 200 with a JSON
  decision status; invalid outer token, malformed request and internal failure
  use transport errors. Adapters must inspect the decision, not just HTTP status.
- Allocation keys are returned once and stored hashed. At this snapshot they
  do not have their own expiry field; grant/allocation windows and revocation
  affect authorization. Short-lived per-attempt managed keys were a research
  proposal, not existing functionality or a selected design requirement.
- Sessions bind signer state to allocation/key and execution-related fields.
  Positive-balance authorization is not a reservation. Funding operations create
  fresh posting IDs; blindly retrying a CLI funding call does not provide
  caller-idempotent provisioning over HTTP.
- Reports differ from stored records. Usage CLI output includes event/transport
  identity, status/error, fee and timestamps but omits several stored request,
  session and quantity dimensions. Balance comes from ledger reporting, not the
  original allocated amount. Operator CLI reports are not an owner-scoped,
  paginated user reporting API.
- Duplicate event handling and accounting checkpoints do not prove all signer
  events were published. Quarantine retains evidence without making an applied
  fee; transport progress must not be presented as financial completeness.
- Settlement attribution is session-level and may be matched, unmatched or
  ambiguous. Chain compensation does not erase delivered off-chain usage.
  Revocation prevents future authorized use while valid delayed charges remain.
- SQLite/local broker operations require consistent backup and recovery.
  Readiness is not accounting-lag monitoring; local locks do not establish
  distributed HA. Public management/report APIs and hard ceilings are gaps,
  not capabilities supplied by the existence of SQLite or Kafka.

The research's proposed per-run credential scheme, exact new HTTP routes,
Batteries outbox, PostgreSQL dispatch queue and production migration plan were
not imported as requirements. Contracts and runtime evidence still require
validation; additional streaming remains an open scope decision. Acceptance
should cover targeted failure and replay scenarios, as described in the
[primary design](self-sovereign-open-builder-stack-draft.md#delivery-and-acceptance).
