# Network Engineering SPE — Build Track: M2 complete

M2, Foundation and integration contracts, was completed on October 19, three days after its
October 16 target, with nothing descoped. The shared builder engine now exists as one open-source
package, its contracts for access, jobs, payments and cost are written and tested, and it has run
paid jobs on public Livepeer orchestrators with every charge matched to the job that caused it.
We showed the work in an M2 wrap demo on October 20. M3, a complete builder journey, is due
November 20, and the December 31 delivery date is unchanged.

**Author:** Mike Zupper · **Reporting period:** October 1–19, 2026

## What M2 delivered

- **One engine, two ways to use it.** [livepeer-builder-core](https://github.com/NE-Build-Track/livepeer-builder-core)
  is a Python package an application can import, or run as a REST service. It handles who may run
  jobs and spend which allocation, finds and pays a runner, records every attempt, and attributes
  each network charge to its job. It stores its records in SQLite or PostgreSQL. It is tagged
  `v0.1.0`.
- **Contracts for the seven builder outcomes.** Access, discovery and rates, jobs and attempts,
  results, measured usage and cost states are documented with tests, including the cases where a
  job is paid for and then fails.
- **Builds and checks.** Versioned development builds, with tests, lint, type and install checks
  on every change.
- **A reproducible baseline.** The engine pins tested revisions of the node remote signer,
  Clearinghouse Batteries and the Python gateway SDK. Forks of each live in the
  [NE-Build-Track](https://github.com/NE-Build-Track) organization, tagged `build-track/v0.1.0`.
  The signer, Batteries and engine deploy to Railway.

## Proven on the network

- **October 14:** paid jobs succeeded on public orchestrators, after a signer fix we requested.
- **October 19:** on the tagged builds, each charge was matched to its job and reconciliation
  balanced exactly, with nothing unattributed.

## Working with upstream

- **livepeer/node #1:** the signer rejected orchestrators whose ticket recipient differs from their
  node address. Josh fixed it; the fix ships in node v1.0.2.
- **Python SDK #77:** the SDK reports each payment session it signs, so an application can see what
  every call cost, failed calls included. In review; the engine pins our fork until it merges.
- **Python SDK #74:** on review, we changed how charges are matched, using the session's ManifestID
  instead of reading the signer's private state.
- **livepeer/node #2:** orchestrators with self-signed certificates are handled by pinning their
  certificates in our stack.

## Demo applications

Two applications already build on the engine and were shown at the M2 wrap demo:

- **[Enterprise desk](https://github.com/NE-Build-Track/enterprise-ui)** (John): a Next.js app on
  the engine's REST API, with per-actor keys, operator funding and per-actor reconciliation.
- **[ChatLPT](https://github.com/NE-Build-Track/chatlpt-sample-enterprise-app)** (Mike): a chat app
  that embeds the engine, runs Qwen3.8-27B and FLUX schnell on Livepeer orchestrators, and shows
  retail price beside network cost for every reply.

## Next: M3, complete builder journey (due November 20)

The M3 gate is one application journey that demonstrates all seven outcomes with funded execution
and network-cost evidence. Already in progress: streaming results through the engine, built and in
review, and the two demo applications as reference-app candidates. Carried from M2 by agreement:
final retry semantics for repeated commands, the upstream merge of SDK #77, a payment reference the
caller owns, and two attribution cases tested but not yet shown live.

The [accepted delivery specification](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/main/docs/product-specs/build-track-2026.md)
links the architecture, required scope and milestone acceptance criteria through December 31.
