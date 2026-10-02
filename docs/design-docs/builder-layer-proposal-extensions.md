# Builder-Layer Proposal Extensions

**Status:** Draft for review\
**Updated:** 1 October 2026\
**Extends:** [Livepeer Builder Layer: Abstraction Design and Two-Application Review](../references/analysis/2026-10-01-Builder-Layer-Abstraction-and-Two-Application-Review.md) (the proposal), with its [assessment](../references/analysis/2026-10-01-Builder-Layer-Proposal-Assessment.md)

This draft adds what the proposal leaves to enterprise integration: access for
REST and MCP callers, payment credential custody, provisioning through
Clearinghouse Batteries, and delivery of network cost to the enterprise
application. Each section names the proposal section it extends. Names,
routes, tools and contracts not listed here stay as proposed.

No Cloud SPE decision record accepts this contract yet.

## Access

Extends the proposal's `Authenticator` protocol, the `ActorContext` contract and
gap 1 (who pays).

Authentication runs in `livepeer_builder_service`, above the engine core. The
core receives only `ActorContext`. An application that imports the engine
supplies its own context, as the proposal already allows.

| Authenticator | Use | Caller credential |
| --- | --- | --- |
| `KeyAuthenticator` (proposed) | Standalone service | Operator-issued API key |
| `OidcAuthenticator` (added) | Enterprise service | Access token from a configured trusted issuer, normally the enterprise app's authentication server |

`OidcAuthenticator` verifies `iss` against the configured trusted issuers, then
`aud`, `exp`, `nbf` and the [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)
resource against that issuer's JWKS, and maps `sub` to an opaque `actor_id`. The
service publishes [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728)
protected-resource metadata, and the issuer publishes
[RFC 8414](https://www.rfc-editor.org/rfc/rfc8414) metadata with PKCE `S256`
for public clients. MCP clients therefore register with the MCP URL and a
browser login. The access token stops at the service; it is never forwarded to
the signer or to Batteries.

Optional provider modes (device authorization, audience token exchange, HTTP
Basic, CIMD client metadata) belong to ISS-03.

**Payment credential custody (gap 1).** `PaymentProvider.credential` takes the
actor and returns a reference to a Batteries `lpg_` allocation key, which the
transport resolves at call time. `LivepeerSettings.signer_credential` stays the
default. In enterprise mode the key is a vault secret on the enterprise app's
authentication server, named by `sub`. The key is never copied into
`ActorContext.attributes`, jobs or events, and the client never receives it.

## REST and MCP

Extends *Service and HTTP interfaces*. The proposal's REST and MCP tables are
adopted as written, with these changes.

| Change | Reason |
| --- | --- |
| `GET /v1/offerings/{app}/runners` becomes `GET /v1/offerings/runners?app=` | App names contain a slash (`live-video-to-video/scope`). A path segment splits them, and an encoded `%2F` is decoded by many proxies before routing |
| `NetworkRate` records its source and carries `price_usd` when the signer supplies it | Since [go-livepeer#4095](https://github.com/livepeer/go-livepeer/pull/4095) ([`bd645a0`](https://github.com/livepeer/go-livepeer/commit/bd645a09266833fb859053445d9ac85846330756), in v0.9.3) the signer's discovery adds `price_usd` to each runner price. It is absent when the signer has no USD rate |
| `run_job` sends MCP `notifications/progress` while a job runs | Matches the second application's SSE heartbeats. Progress is not streamed output and not proof of success |
| Protected-resource metadata is served beside the routes | Required by `OidcAuthenticator` |

Upload and asset tools stay enterprise routes mounted beside the core ones, as
the proposal describes. Persistent media remains with the reserved `sessions`
interface.

## PaymentProvider and upstream interfaces

Extends *The extension protocols* (`PaymentProvider`) and *Upstream interfaces
the layer wraps*.

The Batteries management HTTP API is on `main`
([`a2ed175`](https://github.com/livepeer/clearinghouse-batteries/commit/a2ed17529deba702437a68b709fe4ac4cdc20ef0),
service credentials in
[`9cf68d6`](https://github.com/livepeer/clearinghouse-batteries/commit/9cf68d6b97ec263911ddfb383f0df66492c1417e)).
It is integral to this design: `BatteriesProvider.provision`, `fund` and `revoke`
use it, and the CLI is only an operator alternative.

| Method | Batteries `main` | Note |
| --- | --- | --- |
| `provision` | `POST /v1/allocations`, then `POST /v1/api-keys` | The one-time `lpg_` key goes straight to the vault |
| `fund` | `POST /v1/allocations/{id}/fund` | Not caller-idempotent: each call posts a new ledger entry |
| `revoke` | `POST /v1/allocations/{id}/revoke` | Safe to repeat |
| `allowance` | `GET /v1/ledger/report`, row `allocation_available` | `GET /v1/allocations/{id}` returns cumulative `allocated_units`, not the balance |

- **Retry safety.** Until Batteries accepts a caller idempotency key, the
  provider runs create, key and fund as separate steps. It journals each step in
  the engine store and reconciles before any retry.
- **Least privilege.** The engine holds one `management` credential without
  `grants.*` permissions. Creating and funding grants stays an operator action.
- **Allowance at signing.** The signer calls its authorization webhook during
  `GenerateLivePayment`, and Batteries answers 402 when the allocation is
  exhausted. The allowance is a hard cap. Retail balances stay with the
  enterprise app.
- **Hosted operator (Mode B).** The operator runs Batteries and the signer; the
  engine holds `lpg_` keys under a grant the operator provides.

Batteries `serve` flags this design uses: `--enable-auth-webhook`,
`--enable-management-api` (a port different from the webhook's), `--creds-file`
for the `management` and `webhook` credentials, and `--enable-accounting`. Both
HTTP listeners stay on loopback unless a TLS proxy fronts them.

## Cost feed

Extends *Cost and allowance* and *Events*.

The proposal's cost feed remains the usage source: `PaymentProvider.cost_events`
and `manifest_cost`, folded into `JobCost` with the statuses `none`, `pending`,
`observed` and `corrected`. Gap 2's `unavailable` status is not needed, because
Batteries and the remote signer are the payment path.

- **Source.** The signer's `create_signed_ticket` event carries the caller's
  `manifest_id` and the USD fee (`computed_fee_usd`, go-livepeer#4095).
  Batteries debits allocations by that fee. The read API the feed uses
  (`/v1/cost/events`, `/v1/cost/manifests/{id}`) exists only on the Enterprise
  App's Batteries fork, so merging it into Batteries `main` is an upstream ask.
- **Delivery to the enterprise app.** The engine ships cost and usage to the
  enterprise app through its own event feed: `cost.observed`, `cost.corrected`
  and `usage.reported` on `GET /v1/events`, or `EventFeed.after` when imported.
  The app keeps an event-fed copy and applies retail pricing and billing there.
- **Several paid attempts.** A capacity refusal after a session prepay leaves
  more than one paid attempt, so a job's cost sums its attempts' manifests.

## Second application

Extends *Review against a second application*. The
[simple-infra adoption plan](simple-infra-builder-migration.md) maps each of
its Live Runner modules to a `BuilderEngine` argument or protocol, keeps its
legacy routes as its own facade, and follows the proposal's extraction steps.

## Decisions

- Authentication sits above the engine core. `OidcAuthenticator` with trusted
  issuers is added beside `KeyAuthenticator`.
- The payment credential is a reference to a vault-held `lpg_` allocation key,
  never an actor attribute.
- The proposal's routes and tools are adopted, with app names as a query
  parameter and `price_usd` on rates.
- Provisioning uses the Batteries management API.
- The cost feed is the usage source, and the engine delivers cost to the
  enterprise app through its event feed.

## Work this design implies

`netspe-cz5.2` to `netspe-cz5.4` cover protected-resource metadata, token
verification and the standalone key adapter. `netspe-cz5.6` is the vault
resolver, and `netspe-cz5.16` is the `BatteriesProvider` client of the
management API. The Batteries asks (caller idempotency, a per-allocation
balance read, attributed usage) are `netspe-scr.12` to `netspe-scr.14`.
