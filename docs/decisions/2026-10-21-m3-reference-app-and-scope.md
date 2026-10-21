# M3 Reference Application, Jobs and Scope

**Status:** Accepted\
**Effective:** 21 October 2026\
**Recorded:** 21 October 2026\
**Delivery owner and decision recorder:** Mike Zupper

## Context and evidence

M2 closed on 19 October. M3, the complete builder journey, is due 20 November 2026. Its gate is
one minimum-app journey that demonstrates all seven outcomes with funded execution and correlated
network-cost evidence ([epic #20](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/20)).
On 21 October Mike reviewed the 18 M3 tasks (ISS-08 to ISS-25) against the state of
`livepeer-builder-core` and made the decisions below in the internal planning conversation.

Two demo applications already use the engine: John's enterprise desk (REST) and ChatLPT
(embedded). The [builder console](https://github.com/NE-Build-Track/builder-core-mgmt-ui), scaffolded
on 20 October, reads one builder stack through the engine's REST API and is read-only.

## Decision

1. **The reference application is the builder console.** It gains two areas beside its read-only
   pages: Operator actions (admin key: grants, funding, actors, key issue, inspection, rotation and
   revocation, allocation status) and Builder (actor key: the seven outcomes over REST). The
   enterprise desk is not used for M3. ChatLPT stays the embedded showcase. The console's own
   decisions D15–D20 record the design: key sign-in held server-side, fill in → review → result for
   every write, the REST request and response shown on every action, one generic job form fed by
   the live catalog, and output views chosen by content type.
2. **The representative jobs (ISS-19) are chat (Qwen, streamed) and image (FLUX schnell).** Both are
   immediate jobs, so no M4 work moves into M3: async jobs (ISS-26) and persistent endpoints
   (ISS-27) stay in M4. The gate runs on merged code, so streamed chat depends on the builder-core
   streaming pull request being merged into `releases/m3`.
3. **Ownership.** John owns the engine work in M3 (ISS-08, ISS-09, the final idempotency rules and
   capability input descriptions). Mike builds the console's Operator actions and Builder areas with
   an AI coding agent, under his review.
4. **The integration events feed in ISS-18 is held.** It is revisited once the rest of M3 is under
   way, if there is room. Until then the engine's `/v1/events` stays defined but unimplemented.
5. **The funded environment (ISS-13) is the console's stack**: builder-core's engine, Batteries and
   the node signer at pinned commits, plus the console. It is the M3 dev stack until a deployment on
   real infrastructure exists.
6. **Wholesale is the engine's only cost.** Wholesale (network cost) is what the Livepeer network
   charged for a job: tickets paid to orchestrators, in USD and in the orchestrator's own unit,
   reported by the engine from Batteries accounting. Retail (app price) is what an application
   charges its own users, in the unit it chooses; the application sets and records it, and the
   engine never computes or stores it. How rates are presented beyond that is each application's
   choice. Builder-core documents both terms side by side, and the console shows wholesale only.
7. **ISS-09 reads "a static catalog" as the offerings, not the orchestrators.** The orchestrator set
   is a configured list by choice (public orchestrators' certificates are pinned one by one);
   what each listed orchestrator offers is read live. Automatic orchestrator discovery remains a
   stretch goal.
8. **The funded seven-outcome run (ISS-25)** is run by the agent with Mike watching, after a dry run,
   on merged code, with the builder key issued through the console, the operator funding step shown
   explicitly, and costs followed to their final class. Spend across dry runs and the final run is
   capped at $1, with the expected cost stated before each paid run.

## Alternatives and consequences

- **Enterprise desk or ChatLPT as the reference app.** The desk was declined. ChatLPT is embedded,
  so it would leave ISS-20 without a REST consumer, and its catalog is one fixed chat app. A new
  application was considered and declined in favour of extending the console, which already holds
  the stack, the typed engine client and the catalog.
- **A job that needs async or persistent endpoints.** Declined: it would pull ISS-26 or ISS-27 into
  M3.
- **Consequence for ISS-18:** its feed criterion is not met in M3 unless the hold is lifted.
- **Consequence for ISS-09:** a new orchestrator still needs a configuration change; this is stated
  in the task rather than treated as a gap.
- **Consequence for the console:** its v1 decisions D1 and D7 are revised and D13 is superseded.

## Review and change history

- 21 October 2026: recorded from Mike's decisions in the internal planning conversation.
- 21 October 2026: decision 5 clarified by Mike: the M3 dev stack is the console's stack, not a
  separate builder-core dev stack.
