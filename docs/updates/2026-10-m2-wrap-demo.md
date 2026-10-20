# M2 wrap demo — 20 October 2026

The slide deck for the M2 wrap demo: what milestone 2 delivered, where the builder engine fits in
the existing Livepeer stack, and two live demos of applications built on it.

**Presenters:** Mike Zupper and John (Elite Encoder) · **Date:** 20 October 2026 ·
**Milestone:** M2, Foundation and integration contracts, completed 19 October 2026 (target
16 October).

- **Deck (to present or export as PowerPoint or PDF):**
  [M2 Wrap Demo](https://claude.ai/artifact/8UhvGuWbweMWxubdLWUTJ8). Private until shared from its
  Share menu.
- **PowerPoint:** [2026-10-m2-wrap-demo.pptx](2026-10-m2-wrap-demo.pptx), the same nine slides with
  speaker notes, using fonts every Office install has (Arial, Calibri, Courier New).
- **Source:** [2026-10-m2-wrap-demo-deck/](2026-10-m2-wrap-demo-deck/deck.json), the deck index and
  one HTML file per slide, as published on 20 October.

## Slides

| # | Slide | What it says |
| --- | --- | --- |
| 1 | Cover | M2 wrap: foundation and integration contracts. Closed 19 October; builder core v0.1.0. |
| 2 | Seven things every builder must be able to do | The seven outcomes from the accepted baseline. M2 built the engine for all seven; M3 proves them in one funded journey. |
| 3 | One engine any app can build on | Builder core lets an app run paid AI jobs on Livepeer and know what every job cost: who can run what, run and pay, what it cost. Used embedded or as a REST service. |
| 4 | Where builder core fits | Diagram: apps on top (enterprise desk over REST, ChatLPT embedded, your app), builder core in the middle, the existing Livepeer stack below (Batteries, remote signer, Python SDK, orchestrators), and the usage feed builder core reads back. |
| 5 | What we found, filed and fixed | livepeer/node #1 fixed (in v1.0.2); Python SDK #77 in review; livepeer/node #2 worked around with certificate pinning; SDK #74 changed on review to use the session's ManifestID. |
| 6 | Repos and GitHub orgs | NE-Build-Track (builder core, enterprise desk, ChatLPT; forks of node, Batteries and the SDK tagged `build-track/v0.1.0`) and livepeer upstream; link to [GitHub Project 13](https://github.com/orgs/Cloud-SPE/projects/13). |
| 7 | Complete builder journey (M3 by 20 November) | The M3 gate; work already moving (streaming through the engine, reference apps, network cost read from the engine); items carried from M2. |
| 8 | Questions | |
| 9 | Demos | John's enterprise desk over REST and Mike's ChatLPT embedded. |

## Demo run sheet

**John, enterprise desk (REST),
[NE-Build-Track/enterprise-ui](https://github.com/NE-Build-Track/enterprise-ui):**

1. Sign in with the admin key and open Operator.
2. Provision an actor from the grant and issue its key (shown once).
3. Sign in as that actor and run one paid job from an offering.
4. Show its cost class and the actor's reconciliation (Batteries spent = delivered + failed after
   payment + uncertain). Optional: the ISS-04 page, which runs the M2 payment checks live.

**Mike, ChatLPT (embedded),
[NE-Build-Track/chatlpt-sample-enterprise-app](https://github.com/NE-Build-Track/chatlpt-sample-enterprise-app):**

1. Sign in, ask a question, and let the reply stream.
2. Point at the line under the reply: tokens, retail at Alibaba's Qwen list price, and the network
   cost, which goes from pending to filled in from the engine.
3. Ask it to draw something: the model calls the image tool and the engine pays an orchestrator
   running FLUX schnell.
4. Open Usage in the profile menu, then the admin page: retail against network spend per user, and
   the margin.

Streaming comes from builder-core work for M3 that is in review, not from the M2 tag; say so during
the demo.
