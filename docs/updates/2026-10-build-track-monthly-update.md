# Network Engineering SPE — Build Track Monthly Update: October 2026

October completed M2 and brought M3 to the halfway mark by task count. The shared builder engine is now an open-source package that has run paid jobs on public Livepeer orchestrators and matched each charge to the job that caused it. M2 closed on October 19, three days after its October 16 target, with nothing descoped. In M3, nine of 18 tasks are done and eight more are in open pull requests. The last is the funded seven-outcome run that M3 must deliver, which has not happened yet. Its dry run is due November 13 and the gate is November 20, but M3 can be completed as early as the end of this week, November 6. The December 31 delivery date is unchanged.

**Author:** Mike Zupper · **Reporting period:** October 1–31, 2026

## Where the seven outcomes stand

September's update named seven outcomes for builders. This table shows each one on October 31. M3 work merges to the [`releases/m3`](https://github.com/NE-Build-Track/livepeer-builder-core/tree/2edf903) branch; `main` still holds the M2 release.

| Outcome | Merged | In open pull requests |
| --- | --- | --- |
| 1. Obtain access | API keys with inspection, rotation and revocation; JWT tokens from an enterprise identity provider | None |
| 2. Discover capabilities and supply | A discovery service with on-chain and static orchestrator directories; a live catalog | None |
| 3. Understand a price | Advertised network rates in the catalog | Source, age, and stale or missing markers on every rate ([#77](https://github.com/NE-Build-Track/livepeer-builder-core/pull/77)) |
| 4. Invoke a capability | REST and embedded use; immediate and streamed jobs; repeat-safe commands; paid failover | None |
| 5. Receive a result or actionable failure | Inline results and failure kinds | Distinct payment-failure reasons ([#78](https://github.com/NE-Build-Track/livepeer-builder-core/pull/78)); paged history and documented result access ([#81](https://github.com/NE-Build-Track/livepeer-builder-core/pull/81)) |
| 6. Pay without a crypto wallet | Clearinghouse Batteries allowances and the remote signer | Funded configuration write-up ([Builder Core Console #12](https://github.com/NE-Build-Track/builder-core-console/pull/12)) |
| 7. Inspect usage and cost | Cost per job and by class; reconciliation with Batteries | Cost per app ([#82](https://github.com/NE-Build-Track/livepeer-builder-core/pull/82)). The events feed is held |

Merged means built, tested and on the branch, not proven in the gate. At month end, CI on `releases/m3` passed at `2edf903`, with 1,534 tests at 98% coverage on SQLite and a separate PostgreSQL store suite. Across NE-Build-Track, 74 pull requests merged in October.

## October's work

- **Closed M2.** At the October 16 checkpoint, four of M2's seven tasks were accepted and paid jobs had [succeeded on public orchestrators](https://github.com/NE-Build-Track/livepeer-builder-core/blob/2edf903/docs/references/evidence/2026-10-14-dev-stack-public-orchestrators.md). The contract, payment and package tasks closed on October 19, when [each charge matched its job and reconciliation balanced exactly](https://github.com/NE-Build-Track/livepeer-builder-core/blob/2edf903/docs/references/evidence/2026-10-19-dev-stack-session-log.md) on the tagged `v0.1.0` builds. We showed the work at a demo on October 20 and posted the [M2 update](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3c365a4/docs/updates/2026-10-m2-complete-status-update.md) to the project board, so this is its first report on the forum.

- **Set the M3 plan.** On October 21 we [chose](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3c365a4/docs/decisions/2026-10-21-m3-reference-app-and-scope.md) the Builder Core Console as the reference application, with streamed chat (Qwen) and image generation (FLUX schnell) as the representative jobs. The engine reports wholesale network cost only; retail pricing stays with each application. [Streaming](https://github.com/NE-Build-Track/livepeer-builder-core/pull/28) merged the same day.

- **Built the reference application (ISS-19, ISS-21, ISS-22).** The [Builder Core Console](https://github.com/NE-Build-Track/builder-core-console/pull/1) gained an Operator area for grants, funding, actors and keys, and a Builder area that runs the journey over REST. It was delivered on October 21 and accepted on October 27. An [October 21 paid run](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/35) of two streamed chats and three images cost $0.0092, matching the actor's spent allowance.

- **Made cost reporting hold up under failure (ISS-16, ISS-17).** A running paid job [now reads `pending`](https://github.com/NE-Build-Track/livepeer-builder-core/pull/43), never unpaid. The engine [stores each payment's identifier before asking the signer to sign](https://github.com/NE-Build-Track/livepeer-builder-core/pull/64), so a charge stays attributed to its job even after a crash.

- **Added paid failover.** In [John's change](https://github.com/NE-Build-Track/livepeer-builder-core/pull/61), the engine sends the paid runner request itself and can move a job to another orchestrator when a paid attempt is refused. An [operator setting](https://github.com/NE-Build-Track/livepeer-builder-core/pull/65) caps the paid attempts a job can fail over from, 2 by default, and the operator bears those payments. This answers the failover request made in the forum thread; recourse for a job that fails partway through is not part of the accepted plan. A [live paid failover between two orchestrators](https://github.com/NE-Build-Track/inference-gateway/pull/7) ran on November 1, just after this period, and spend matched exactly.

- **Made commands safe to repeat (ISS-11, ISS-14).** Every command that can move money, create a credential or run paid work [can now be repeated](https://github.com/NE-Build-Track/livepeer-builder-core/pull/76) under the same operation reference without applying twice. [Live checks on Arbitrum One](https://github.com/NE-Build-Track/builder-core-console/blob/ca43baa/docs/references/evidence/2026-10-29-d57-live-check.md) on October 29 passed through the engine (37) and the Builder Core Console's Operator page (14). This settles the retry rules carried from M2.

- **Separated discovery and finished standalone credentials (ISS-09, ISS-08).** [Discovery](https://github.com/NE-Build-Track/livepeer-builder-core/pull/46) now runs as its own service with on-chain and static directories, and the signer only signs. [Keys](https://github.com/NE-Build-Track/livepeer-builder-core/pull/48) can be inspected and rotated, and key events are logged without secrets.

- **Started early on M4's enterprise sign-in (ISS-33).** The engine [accepts JWT access tokens](https://github.com/NE-Build-Track/livepeer-builder-core/pull/50) from an identity provider and has a [read-only auditor credential](https://github.com/NE-Build-Track/livepeer-builder-core/pull/69). The Builder Core Console [signs in through a provider](https://github.com/NE-Build-Track/builder-core-console/pull/7), tested with Keycloak through a paid job.

- **Wrote guides for the remaining work.** [Implementation guides](https://github.com/NE-Build-Track/livepeer-builder-core/pull/74) cover the remaining M3 tasks and every M4 and M5 task. None needs an upstream change.

## In review at month end

Eight M3 tasks are in open pull requests: John's [#77](https://github.com/NE-Build-Track/livepeer-builder-core/pull/77), the stack from [#78](https://github.com/NE-Build-Track/livepeer-builder-core/pull/78) to [#83](https://github.com/NE-Build-Track/livepeer-builder-core/pull/83), and [Builder Core Console #12](https://github.com/NE-Build-Track/builder-core-console/pull/12). On October 30 we ran this work together on a local build against Arbitrum One. [All 41 engine checks passed](https://github.com/NE-Build-Track/livepeer-builder-core/blob/901d90c/docs/references/evidence/2026-10-30-m3-live-suite.md), three of them after fixes to the test runner rather than the engine, covering payment failures, access, secrets, outages, stream restarts and cost-sync replay. Network cost for the day was $0.011. Browser checks found two defects in the Builder Core Console, one fixed in its #12 and one waiting on #77. A rehearsal of the seven-outcome journey also completed, at about $0.00011 per chat and $0.0030 per image, with reconciliation balanced. None of this is the gate, which must run on merged code.

## Working with upstream

- **Batteries and signer.** Josh merged [idempotency keys](https://github.com/livepeer/clearinghouse-batteries/issues/5), [narrower reads](https://github.com/livepeer/clearinghouse-batteries/issues/6) and [attributed usage](https://github.com/livepeer/clearinghouse-batteries/issues/7) in Clearinghouse Batteries on October 6, and [fixed the signer](https://github.com/livepeer/node/issues/1) so it accepts orchestrators whose ticket recipient differs from their node address. Paid jobs on public orchestrators followed on October 14.
- **Python SDK.** The M2 update listed SDK #77 as in review. Josh's [#81](https://github.com/livepeer/livepeer-python-gateway/pull/81) replaced it and merged on October 21.
- **No forks.** By October 28 the engine pinned `livepeer/*` for the SDK, node and Batteries instead of our forks, keeping one adapted copy of the SDK's paid call with a test that fails when upstream changes it. No SDK release on PyPI includes the changes we need, so the engine pins the SDK by commit and can't go to PyPI itself until one does.

## Applications on the engine

- **[ChatLPT](https://github.com/NE-Build-Track/chatlpt-sample-enterprise-app)** embeds the engine and now shows the extra network cost of a failed-over reply.
- **[Inference gateway](https://github.com/NE-Build-Track/inference-gateway)**, new this month, puts OpenAI- and Anthropic-compatible APIs on the engine. Its [October 29 paid check](https://github.com/NE-Build-Track/inference-gateway/pull/6) reconciled 62 paid attempts exactly, on one orchestrator.

## Open items and risks

- **Merge timing.** The stack must merge in order, and the Builder Core Console then re-pins to the result. This is the main risk to the November 6 and 13 checkpoints.
- **Payment latency.** [A partner measured](https://github.com/NE-Build-Track/livepeer-builder-core/issues/89) a 3.2–3.5 second wait before each paid inference reached the GPU pool. Their logs attribute 98% of it to chain RPC calls, and by our reading the node code makes 29 sequential, uncached calls per paid request. [We now record](https://github.com/NE-Build-Track/livepeer-builder-core/pull/90) where each attempt's time goes, but nothing has reduced the wait yet. The fix may need changes in `livepeer/node`. The M3 gate doesn't depend on it; real-time products will.
- **Usable supply.** Discovery leaves out orchestrators with self-signed certificates, because the engine can't call them. [A late-October test](https://github.com/NE-Build-Track/chatlpt-sample-enterprise-app/pull/5) excluded three and left two.
- **Still open from M2.** We still lack a payment reference the caller owns, so a collision between payment identifiers reads as `uncertain`. The forged-manifest and rejected-ticket cases are tested but not yet shown live on the current stack.
- **Held by decision.** The ISS-18 events feed stays held; John has written a [delivery proposal](https://github.com/NE-Build-Track/livepeer-builder-core/issues/86) for it. His [design for media outputs and realtime sessions](https://github.com/NE-Build-Track/livepeer-builder-core/issues/73) (ISS-27) is open for review.

## Next: finish M3 (due November 20)

Our working checkpoints are Builder Core Console areas complete by November 6, a dry run by November 13 and the gate on November 20. The gate is one funded run on merged code, with evidence linking a builder key, live discovery and rate, execution, result, usage and final network-cost class. Spend across all runs is capped at $1. M4 starts November 23. The next monthly update will report the gate result.

The [project board](https://github.com/orgs/Cloud-SPE/projects/13) tracks every task. The [accepted delivery specification](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3c365a4/docs/product-specs/build-track-2026.md) links the architecture, required scope and milestone acceptance criteria through December 31.
