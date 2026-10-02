# simple-infra on the Builder Engine

**Status:** Draft for review\
**Updated:** 1 October 2026\
**Extends:** *Review against a second application* in the [builder-layer proposal](../references/analysis/2026-10-01-Builder-Layer-Abstraction-and-Two-Application-Review.md), with the [proposal extensions](builder-layer-proposal-extensions.md)

The proposal reviews the `livepeer/simple-infra` SDK service as its second
application. This draft shows how that service would adopt the engine: it keeps
its legacy routes as its own facade, and replaces its Live Runner internals
class by class with `BuilderEngine.from_settings(...)` and the proposal's
protocols, in imported mode. The engine reuses no simple-infra source. This
draft cites files and functions only; it is for Inc to review.

No Cloud SPE decision record accepts this plan.

## Corrections to the proposal's description

Reviewed against `livepeer/simple-infra` `main` at `4ec364f`.

| Proposal's description | Finding |
| --- | --- |
| Training jobs run outside Live Runner | Training runs as Live Runner offerings through `/inference` |
| Global and per-capability caps refuse with 503 before dispatch | The global cap applies only after the Live Runner attempt; the per-capability limiter waits up to 240 s, fails as 502, and is unset in production |
| Discovery reads URLs plus a remote registry | The URL list is live; the registry client is off |
| Finished async jobs are mirrored to durable storage | Yes, to a host-volume file store, not object storage |
| Each caller's bearer is forwarded to a hosted signer | Yes: PymtHouse composite keys (`app_*_pmth_*`, `key_routing.py`) go to the PymtHouse signer, not Batteries |

Two defects are filed for Inc:
[simple-infra#268](https://github.com/livepeer/simple-infra/issues/268) (pinned
requests return 500) and
[simple-infra#269](https://github.com/livepeer/simple-infra/issues/269)
(`SDK_JOB_STORE` missing from the Pulumi template).

## Class-level replacement

Each row replaces one simple-infra module with the facade argument or protocol
the proposal defines.

| simple-infra today | `BuilderEngine` part | Notes |
| --- | --- | --- |
| `key_routing.classify_key`, `signer_decision` | `authenticator=` (`Authenticator`) | A pattern authenticator in the service's facade, producing `ActorContext` |
| `_effective_signer` | `payments=` (`PaymentProvider.credential(actor)`, gap 1) | `BatteriesProvider` with a per-actor `lpg_` key. PymtHouse composite keys stay on the legacy path until the service moves to Batteries keys |
| `_discover_lr_orchs` over a URL list | `discovery_source=` (`DiscoverySource`) | The URL-list source the proposal lists as missing, polled rather than read per request |
| Live Runner offering table (`lr_offerings.py`) | `discovery.resolve_app` with a configuration-table resolver (gap 3) | Plus `allowed_orchestrators` on `JobRequest` |
| `lr_select.pick_bases`, `provider_selection.MeritSelector` | `selection=` (`SelectionPolicy`) | Over the SDK's runner selection, with a pool size ([livepeer-python-gateway#70](https://github.com/livepeer/livepeer-python-gateway/issues/70)) |
| `_dispatch_lr_v2` → `call_runner` | `transport=` (`SdkRunnerTransport`) | Unchanged call path |
| In-memory job and idempotency maps, file job store | `store=` (`SqliteStore`) | Join-and-return idempotency (gap 4); jobs durable before dispatch |
| Pass-through `data.usage` | `jobs.report_usage`, or a `UsageMeter` | Usage keeps its source |
| Global semaphore, per-capability limiter | Engine admission (gap 6) | Bounds every Live Runner dispatch, 503 before it |

## Route map

The legacy routes stay as simple-infra's facade. Each becomes one service call.

| Legacy route | Service call |
| --- | --- |
| `POST /inference` | `jobs.run` |
| `POST /inference/submit` | `jobs.submit` |
| `GET /inference/jobs/{job_id}` | `jobs.get`, `jobs.result` |
| `POST /inference/stream` | `jobs.run` with progress events; heartbeats are progress, not output |
| `GET /capabilities`, `GET /lr/offerings` | `discovery.offerings` |
| `/enrich`, `/replan`, `/llm/chat`, `/upload`, `/files/{name}` | Product routes that call the engine for dispatch |

## Order

Adoption follows the proposal's extraction steps. Each step ends with
simple-infra's golden routing suite, route inventory and environment-plumbing
tests unchanged unless the step changes them on purpose. Each change is a
simple-infra pull request; every new setting goes into the `agent-infra`
template.

1. **Preconditions.** Inc reviews this plan; the two defects are fixed, so the
   golden fixtures stop encoding the 500.
2. **Contracts and discovery** (proposal steps 1 and 2). Import the core; wire
   the authenticator, discovery source and resolver.
3. **Execution** (step 3). Transport, selection, `SqliteStore` and engine
   admission replace the dispatch path.
4. **Cost and events** (step 4). Engine-paid jobs use a Batteries key, so the
   cost feed and event feed apply.
