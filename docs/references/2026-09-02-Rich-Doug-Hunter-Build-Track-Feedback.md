# Rich, Doug, and Hunter Build Track Feedback

**Status:** Stakeholder input; not an accepted scope or architecture decision

**Recorded:** 2 September 2026

**Recorder:** Mike Zupper

**Related bead:** `netspe-vun.9`

## Purpose and provenance

This note preserves additional Build Track input relayed by Rich O'Grady after
he collected feedback from Doug Petkanics and Hunter Hillman. Hunter's direct
comment was supplied as a screenshot named `ne-spe-hunter-comment.png`.

The relay and screenshot are evidence of stakeholder concerns. They do not by
themselves amend the seven builder outcomes, select a payment mechanism, create
a service-level agreement, or constitute joint Network Engineering SPE and
Cloud SPE approval.

## Feedback received

### Doug feedback relayed by Rich

Doug is leaning more heavily toward a self-sovereign, wallet-based setup and
suggested examining approaches such as x402 or other easy on-chain payment
mechanisms. Rich characterized this as a slightly different direction.

### Hunter feedback

Hunter supported the direction and named ownership, then asked that “easy to
build” account for uptime, failover, expected performance, and recourse after a
failure. His concrete example was a three-hour job that fails after two and a
half hours, leaving the buyer without an account manager, a result, or clarity
about the money already spent. He described that situation as a showstopper.

Hunter also said a companion go-to-market SPE would be valuable. That comment
is consistent with the accepted boundary that the Build Track enables demand
but does not own demand generation or application adoption.

## Interpretation

### 1. Self-sovereign payment may be the architectural centre of gravity

The current planning assumption says both wallet-funded and walletless journeys
are in play, pending confirmation. Doug's new emphasis does not yet remove the
walletless outcome, but it may change the relationship between the paths:

- an easy wallet-controlled, on-chain path may be the canonical
  self-sovereign baseline;
- a clearinghouse-backed walletless path may be an optional or hosted
  convenience over the same invocation contract; or
- both may remain required, co-equal acceptance paths.

x402 is therefore a candidate to evaluate, not a selected technology or
approved requirement. “Easy on-chain payment” must also be translated into an
observable builder experience rather than inferred from a protocol name.

This direction creates a visible tension with the current outcome that a
builder can pay without holding crypto. The tension must be resolved by the
appropriate authority; neither outcome should be silently removed or demoted.

### 2. Service assurance is not explicit in the seven outcomes

Hunter's concern spans several existing outcomes but adds an important buyer
decision and protection dimension:

| Existing outcome | Assurance question introduced by the feedback |
| --- | --- |
| Discover what the network can do | Can the builder see relevant availability, capacity, health, or historical performance information? |
| Understand the expected price or rate | Can the builder understand financial exposure before starting a long-running job? |
| Invoke through a standard interface | Does the contract support the job state, timeout, cancellation, retry, and failover behavior needed for the supported workload? |
| Receive a result or understandable failure | Does the failure identify what happened, whether retry or failover is possible, and whether partial work exists? |
| See usage and resulting charge | Does the builder know what was charged after a failed or partial job and what correction, credit, refund, or dispute path is available? |

The high-level requirement should not prematurely promise a conventional SLA,
automatic refund, centralized account manager, or protocol-enforced remedy.
The architecture discussion must first distinguish:

- declared performance from observed performance;
- an estimate from a contractual commitment;
- automatic retry or failover from financial recourse;
- protocol-enforced behavior from gateway, clearinghouse, operator, or
  commercial support responsibilities; and
- a Build Track acceptance requirement from an Operate Track or hosted-service
  dependency.

## Directional decisions to obtain

### Self-sovereign payment

1. Is an easy wallet-controlled payment path the canonical Build Track path,
   with walletless access treated as a secondary hosted convenience, or are
   both required and co-equal?
2. Does “self-sovereign” require a builder to operate without centralized
   identity, custody, metering, or payment services? Which dependencies may be
   optional?
3. Was x402 offered as an example to investigate, a preferred direction, or a
   required compatibility target?
4. Which builder-visible properties define “easy on-chain payment” for
   acceptance purposes?
5. Does the outcome “pay without holding crypto” remain a mandatory Build
   Track outcome? If so, who owns it and how must it interoperate with the
   self-sovereign path?
6. Must wallet-funded and walletless paths converge on the same capability,
   invocation, result, failure, usage, and charge contract?

### Expected performance and recourse

1. Which performance information must be available before invocation for each
   supported capability: uptime, capacity, expected completion time, latency,
   throughput, success rate, or another measure?
2. Is the information a provider declaration, a gateway estimate, an observed
   network metric, or a commitment? Who publishes and validates it?
3. Which component owns retry, rerouting, failover, checkpointing, or recovery
   for a long-running Live Runner job?
4. What must happen when a job fails after consuming substantial time or
   resources: no charge, partial charge, automatic credit, refund, dispute,
   operator penalty, or another defined response?
5. What evidence connects the invocation, execution progress, failure, usage,
   network payment, and resulting charge?
6. Which forms of recourse are protocol-level, Build Track, Operate Track,
   clearinghouse, gateway operator, or commercial-service responsibilities?
7. What is the smallest service-assurance behavior that must be demonstrated by
   31 December 2026, and what may be explicitly deferred?

## Planning impact

### Survey

Do not change the survey instrument in the middle of response collection.
Treat this note as late stakeholder input to `netspe-vun.9` and compare future
responses against it. The payment-path question already exposes the relevant
directional choice. The performance and recourse concern should be presented
in the architecture workshops because it crosses outcome, component, and track
boundaries and cannot be answered as a simple preference poll.

### Workshop Part 1

Use Part 1 to determine whether service assurance is part of the builder
promise, which high-level behaviors are required, and which architecture
component or external track must own each behavior. Also resolve whether the
self-sovereign path changes the payment architecture alternatives.

### Workshop Part 2

If service assurance is confirmed, use Part 2 to establish high-level contract
and acceptance boundaries for performance information, failure state, retry or
failover ownership, payment state, and recourse. Defer detailed thresholds and
mechanics to named follow-up work unless they alter the architecture.

### Milestones and normative outcome documents

Do not amend milestone acceptance or the seven builder outcomes solely from
this feedback. Once authorities resolve the directional questions, the likely
normative change is to make the builder's expected service behavior and failed-
job financial state explicit, while retaining implementation-neutral wording.

## Required follow-up evidence

- Rich confirms whether his relay is a request for investigation or an intended
  change to the Build Track outcome.
- Doug states the priority and required status of the wallet-controlled and
  walletless paths, and clarifies the status of x402.
- Hunter identifies the minimum performance and recourse information a builder
  needs before accepting the risk of a long-running job.
- Rick and Josh assess architecture and repository feasibility.
- The Network Engineering SPE and Cloud SPE approve any resulting outcome or
  milestone change through the documented decision process.
