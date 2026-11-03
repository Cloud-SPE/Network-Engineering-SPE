# Events Feed Moves to M4

**Status:** Accepted\
**Effective:** 2 November 2026\
**Recorded:** 2 November 2026\
**Delivery owner and decision recorder:** Mike Zupper

## Context and evidence

ISS-18 ([#31](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/31)) has two parts: the
usage and cost reports, and a versioned integration events feed. The
[M3 scope decision of 21 October](2026-10-21-m3-reference-app-and-scope.md) (item 4) held the feed,
to be revisited if M3 had room, and left ISS-18 open as partial until the hold was lifted.

On 2 November the cost reports were complete on builder-core `releases/m3` at `1514212`:
- costs per job, attributed to attempts, with units;
- the cost summary per class and per app and class (builder-core D60,
  [#82](https://github.com/NE-Build-Track/livepeer-builder-core/pull/82));
- network rates with their source and age (D62);
- tests showing that a reporting failure leaves a succeeded job unchanged.

Building the feed in M3 was weighed against the calendar: the ISS-25 dry run is due by 13 November and
the gate is 20 November. The feed would change the engine's job and cost write paths shortly before the
gate. It would also need a new migration, so the console, ChatLPT and inference-gateway would each need
another re-pin, and the final ISS-25 run would move to a later pin. Nothing in M3 uses the feed.

## Decision

1. **ISS-18 is closed for M3** on the cost reports. Its closing comment records the evidence.
2. **The events feed moves to M4 as ISS-46**
   ([#51](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/51)). Its acceptance is the
   feed half of ISS-18's criteria, unchanged. It is a delivery task under the M4 summary
   ([#39](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/39)), which now lists 12 tasks.
3. **John's delivery design**
   ([builder-core#86](https://github.com/NE-Build-Track/livepeer-builder-core/issues/86)) carries
   over to ISS-46. Whether M4 delivers the pull feed only or also push delivery is decided when the
   ISS-46 implementation guide is locked
   ([builder-core#92](https://github.com/NE-Build-Track/livepeer-builder-core/pull/92)).

This supersedes item 4 of the 21 October decision and its consequence for ISS-18.

## Alternatives and consequences

- **Lift the hold and build the feed in M3.** Declined, for the schedule and pin reasons above.
- **Keep ISS-18 open as partial into M4.** Declined. It would leave a met M3 task open across two
  milestones, with its remaining part tracked only as a comment.
- **Consequence for M4:** the milestone gains one engine task. ISS-26, ISS-29 and ISS-32 each have a
  row that waits for the feed, and now depend on ISS-46.
- **Consequence for builder-core:** `GET /v1/events` still answers 501 naming ISS-18, and its docs still
  call the feed held. They are updated in a later builder-core change.

## Review and change history

- 2 November 2026: recorded from Mike's decision in the internal planning conversation.
- 3 November 2026: ISS-18 closed, and the ISS-46 implementation guide merged on builder-core
  `releases/m3` ([builder-core#92](https://github.com/NE-Build-Track/livepeer-builder-core/pull/92)).
