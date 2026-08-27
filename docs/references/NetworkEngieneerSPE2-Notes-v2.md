# Pre-Proposal: Network Engineering SPE II

**Status:** Working draft

**Source:** Normalized from five screenshots of the Notion pre-proposal captured on 25 August 2026

**Proposed by:** Rich O'Grady, Ecosystem Director, Livepeer Foundation

> **Scope resolution recorded 26 August 2026:** This file preserves the
> upstream working draft as captured. Its application-adoption and live-demand
> language is not a current Build Track requirement. The confirmed scope
> excludes demand generation, application adoption, application counts,
> production-traffic targets, and live-demand evidence. See decision
> `netspe-vun.7` and the
> [current milestone draft](../design-docs/cloud-spe-september-december-2026-milestones-draft.md#application-adoption-exclusion).

---

## Abstract

The Network Engineering SPE funds the work that makes the Livepeer network easier to participate in: builders, orchestrators, delegators and, if 2.0 lands as planned, validators. Round one proved the SPE's value as a funding mechanism. It also showed that one pool with one technical reviewer and no clear outcomes can lack direction. So round two keeps the mission and changes the shape: four tracks, one named owner on each, one outcome per track to hit by the end of the year, and the capital sitting with those owners rather than held centrally.

**Request:** $230,000 USD-equivalent in LPT, 1 Sep to 31 Dec 2026

**Preceded by:** the Network Engineering SPE pilot, 15 May to 30 Aug 2026, $95,000

**Feedback session:** [Network Engineering Priorities — 2026/08/11 07:56 PDT — Notes](https://docs.google.com/document/d/1DgU8ovr2qCwJ8-xkbxajfb53UNh_ghQZRl-SGhf_LDg/edit?tab=t.d47gkljqyzrr)

---

## Mission

The mission of the SPE is to make the Livepeer network easy to participate in: to build on, operate, validate and delegate for all participants.

It focuses on the key actors within the Livepeer network: Builders (including developers, agents and gateways), Orchestrators (also referred to as Operators), Delegators and, with the upcoming 2.0 vote, Validators.

To achieve this mission, the SPE will aim to unify key engineering leaders around one vision and empower them with capital, talent and programs. By working with the community, the SPE will give these leaders a clear mandate for which they remain accountable, while providing operational support with mechanisms that can fund critical engineering work quickly.

The SPE will divide the work into four tracks focused on four personas, each with its own outcome, a single responsible owner and a set of milestones to achieve it. These owners can be funded by the SPE or receive a salary from another core organisation (e.g. the Livepeer Foundation or Livepeer Inc).

The capital from the SPE is deployed to fund the work to complete these milestones through a variety of mechanisms (RFPs, grants, bounties, fixed contracts). After discussing this in a recent feedback session, the SPE will use a variety of funding mechanisms to ensure that we find the person for the right task at the right cost.

---

## Rationale

### What's changed from the pilot SPE

This Network Engineering SPE will be structured differently from the pilot.

The pilot SPE structure was focused on three directional priorities with a combined pot for RFPs and grants (direct or retroactive). This model had a great deal of flexibility baked in. However, it (a) lacked concrete outcomes or goals that were clearly set at the beginning; (b) had a review bottleneck with the Technical Director; and (c) did not have strong enough accountability. See the full retro here.

This SPE is structured differently. It splits the work into four tracks each around a core ecosystem stakeholder: Builder, Orchestrator, Delegator and Validator. Each track then gets one owner, one outcome by the end of the year, and a budget that owner is allocated.

The owner is on the hook for the outcome. They can route the allocated funding to other contributors to complete the work.

### Four new tracks to focus work

The four tracks are places where our claim to be an open network still falls down in practice:

| **Track** | **Owner** | **Outcome by 31 Dec** |
| --- | --- | --- |
| **Easy to build**<br>Builder | Mike Zupper | A developer can go from a clean machine to a working, paid call on the Livepeer stack using only the published documentation, without contacting an Operator. Both payment paths work: funding from a wallet by default, and pymthouse for anyone who does not want to hold one. The Livepeer Agent and at least two further applications are sending live demand through the network rather than test traffic. |
| **Easy to operate**<br>Orchestrator | Josh Allmann | 50 orchestrators have advertised and served capabilities through Live Runner, with enough observability to understand failures. Livepeer has a network substrate that connects demand to supply end to end, where new capabilities can be introduced without building a new integration stack each time, and every capability is discoverable with clear pricing by an application. |
| **Easy to delegate**<br>Delegator | Elliott Conway | Make self-custody delegation clearer, safer, and easier to use, with a staking experience that is competitive with leading alternatives. This primarily means improving conversion between stages of the delegation journey and ultimately increasing delegation volume, provided that upstream interest in delegation does not decline. |
| **Easy to validate***<br>Validator | Shane Burgett | Self-dealing and gaming Livepeer tokenomics are expensive and untenable, with the network protected from token exploitation through a combination of economic levers, network data, and social consensus. Lead testing of methods to further validate work on the network, protecting users from dishonest or low-quality operators. |

*We do not yet know whether validation means a full validator set with on-chain scoring, or existing participants carrying an extra responsibility. The shape of this track is therefore subject to change depending on how it evolves.*

### How funds reach contributors

For this SPE, owners will pick the mechanism per task. Different mechanisms can be used depending on whether the work is defined, a contributor has been identified or the price of work still needs to be determined.

This decision emerged out of the roadmap session call from August 11th, where community members suggested that there was no need to over-index on one or two mechanisms.

The suggested mechanisms that could be used are:

| **Mechanism** | **When an owner reaches for it** | **Funding amount** |
| --- | --- | --- |
| **RFP** | Scope is clear but the right contributor is neither in the network nor known to us. | $5,000 to $30,000 |
| **Direct grant** | Scope is clear and the builder is obvious. Paid against milestones. Moved the most capital last round. | Up to $20,000 |
| **Retroactive grant** | Work has already shipped against a problem the community named publicly first. | Up to $10,000 |
| **Scoping grant** | The work cannot be specified yet, and specifying it is the deliverable. New this round. | Up to $5,000 |
| **Bounty** | Small and self-contained, worth opening to anyone. Spendable directly by a committee member, no application path. | $500 to $2,000 |
| **Fixed contract** | Sustained ownership of a surface over 2–4 months, with milestones set by the track owner. | $5,000 to $40,000 |

### What this SPE isn't

- **Not funding the agent framework.** The Livepeer Agent will be funded separately from across Inc, the Foundation and the treasury.
- **Not a demand generation or credits fund.** Go-to-market and end-user product work will sit within another SPE proposal coming soon.
- **Not protocol design.** 2.0 is designed and voted elsewhere. This funds getting the people already here across to it.
- **Not an open-ended pool.** Every disbursement needs a verified definition of done.

---

## SPE Governance Structure

### Roles and responsibilities

| **Role** | **Who** | **Responsibilities** | **Paid by SPE** |
| --- | --- | --- | --- |
| **Chairperson** | Rick Staa | Accountable for making sure every contribution funded by this SPE is reviewed and either merged or rejected with reasons. Rules on architectural decisions that cross track boundaries where owners cannot agree. | No, the Foundation |
| **Committee** | Rick Staa (Chair), Josh Allmann, Elliott Conway, Mike Zupper, Shane Burgett | Sets each track's outcome, defines and reviews milestones, signs off and merges code, decides allocations brought by another member. | Two of four, as track owners |
| **Track owner** | Josh Allmann, Elliott Conway, Mike Zupper, Shane Burgett | Presents three to five milestones, allocates the track budget, picks the mechanism per task, brings in contributors to do the work. | $20,000 each, where not already paid by Inc or the Foundation |
| **Foundation Operations** | Rich O'Grady, Ben Perez, Mehrdad Sadeghi | Programme management, bringing in new contributors, treasury and payment operations, monthly reporting, final sign-off on release of funds. Buys in independent review per task so payouts do not queue behind one calendar. | No, though bought-in review is paid from the bounty pot |

### Committee operations

- **Voting —** When a member brings an allocation, a sign-off or a scope change forward, there is a simple majority vote. Where a committee member is absent, a Foundation Operations team member will step in so a decision is never held up by a diary. The Foundation Operations team also holds the final gate on payment and releases funds only once the definition of done is verified.
- **Code review —** Review is a named committee responsibility: every contribution funded by this SPE will aim to receive an approval or rejection, with reasons, within the month.
- **Conflicts of interest —** Several committee members run something that touches the network commercially, and excluding them would cost us more than the conflict does. We will therefore introduce that a track owner may direct no more than 50% of their own track allocation to themselves or to an entity they control. It will also be disclosed on the forum when it happens, with the member recused and Foundation Operations releasing the funds. Any contributors paid by the Foundation or Livepeer Inc will not receive further compensation from the SPE.

---

## Timeline and Milestones

Each track will have its own milestones, which will be tracked and reported on concurrently by its owner.

### SPE Timeline

**1st September — Track Milestones Finalised** — each Track Owner has finalised their respective milestones (see below).

**8th September — Operating Cadence Established** — weekly committee meeting running and payment operations set up.

**29th September — First Monthly Update Published** — published on the forum, covering work funded and delivered per track, funds committed and disbursed, code merges and every committee decision with its rationale.

**20th December — Retro Completed** — each track assessed against its outcome, total spend against budget, and a recommendation per track: continue, change owner, or stop. Community session held alongside it.

### Milestones

Each track has an outcome to achieve by the end of the year (see above). They then have a series of facts that need to be true to know whether they have achieved their outcome:

| **Track** | **Milestones** | **Checked by** |
| --- | --- | --- |
| **Easy to build**<br>Builder | • First call works without a wallet or setup<br>• Clients can discover, price, pay for and invoke services through standard interfaces<br>• Payments and metering work across supported service types without bespoke integration<br>• You can see what a job costs, before and after you run it<br>• Docs and SDK match what's actually deployed | Fees on-chain through the ticket broker. A timed first call by someone outside the project. |
| **Easy to operate**<br>Orchestrator | • Live Runner covers the operator path end to end<br>• There is a canonical contract for capabilities, hardware, pricing and service discovery<br>• Operators can determine why a job failed, including failures outside the operator's control<br>• A capability can be validated before deployment<br>• There is a credible path from today's network architecture to 2.0 | Count of orchestrators serving a capability. Failed job diagnosed by the operator, not by us. |
| **Easy to delegate**<br>Delegator | • Delegation journey conversion is measurable against a clear baseline<br>• Users can confidently discover and compare Orchestrators using meaningful, trustworthy information<br>• Rewards, fees, risks and unbonding conditions are clear before commitment<br>• Delegating, switching and exiting are understandable, reliable and low-friction<br>• Delegators can clearly understand their position and earnings after delegating | Explorer surfaces shipped against the scored backlog. Every lockup shown before commitment. |
| **Easy to validate***<br>Validator | • LPT is protected from exploitation: self-dealing and tokenomics gaming<br>• Gaming is an expensive endeavor with little reward<br>• Token exploitation is visible in network data, and the community has the evidence it needs to act<br>• Real testing has begun on the long-term challenge: validating the work itself, protecting users from false data and low-quality work | Cost-of-attack analysis published, recomputable by anyone from on-chain parameters: known gaming strategies have negative expected return. A self-dealing attempt run by us loses money. First work-validation test results published. |

**Note:** In the coming days, formal milestones will be formed around each track. The aim is to publish these in time for the final proposal.

---

## Budget Breakdown

**$230,000 USD-equivalent in LPT** for one four-month cycle, sized on the **30-day moving average** LPT price at approval.

### Budget Overview

| **Line** | **Allocation** | **What it funds** |
| --- | --- | --- |
| Track owner, Validate | $20,000 | Accountable ownership and delivery of the Validate outcome. ~15 hours/week, 4 months. |
| Track owner, Delegate | $20,000 | Accountable ownership and delivery of the Delegate outcome. ~15 hours/week, 4 months. |
| Track owner, Build | $20,000 | Accountable ownership and delivery of the Build outcome. ~15 hours/week, 4 months. |
| Build track, contributors | $50,000 | SDK, payment clearinghouse, service registry and schema contract, discovery, docs and capability templates, metering and spend transparency. |
| Operate track, contributors | $30,000 | Operator tooling, diagnostics and real job state, Live Runner developer experience, capability supply, migration tooling and the 2.0 upgrade path. |
| Delegate track, contributors | $20,000 | Explorer delegator experience, lockup transparency, staking guidance, subgraph engineering including audit remediation, and research into what 2.0 changes for delegators. |
| Validate track, contributors | $30,000 | Provisional, released only if the track activates. |
| Bounties, grants and research | $30,000 | Cross-track work no single track owns: a bounty pot spendable directly under a per-item cap, scoping grants, retroactive grants, and bought-in review. |
| Buffer | $20,000 | Held against LPT price movement, so a falling price is not a pay cut mid-milestone. |
| **Total shown in source** | **$230,000** | |

> **Snapshot note:** The allocations shown in the screenshot add up to $240,000, while the request and displayed total are both $230,000. This repository preserves those values as part of the upstream working draft; resolving its arithmetic remains outside the Cloud SPE work tracked here.

### Budget Notes

- Reallocation between tracks is possible at the end of each month with a published decision.
- A Track Owner works inside their allocation and brings anything larger to the committee.
- A Track Owner may direct no more than 50% of their own track allocation to themselves or to an entity they control.
- No contributors funded by Livepeer Inc or the Livepeer Foundation will receive further funding from the SPE.
- The three Track Owners for Validate, Delegate and Build will be compensated a $5,000 per month fixed contract. Payments can be withheld for extreme neglect of their role.
- Payouts in LPT at a 7-day average at the point of payment.
- We will manage the treasury position on receipt rather than sitting on $230,000 of LPT for four months, so contributors get what they were promised whatever the price does.
- Anything unspent carries to the next round, or goes back to the treasury if there isn't one. Incomplete work at 31 December gets a short remediation window first.

---

## Transparency and Accountability

- Monthly written updates on the forum: work funded and delivered per track, milestones signed off and missed, funds committed and disbursed against allocation, and every committee decision with its rationale.
- A public per-track financial record of allocation, commitment and disbursement, updated monthly rather than reconciled at the end.
- Every conflict disclosed at the point of the decision, with the recusal published.
- Every self-allocation by a committee member published against the 50% cap.
- A closing retro and community session before 20th December.

---

## Key Terms

- **Track.** A body of work built around one core ecosystem stakeholder, with one owner and one outcome.
- **Foundation Operations.** The Foundation team running programme management, payments and reporting, and holding the final gate on releasing funds.
- **Builder.** Anyone building on the network: developers, agents and gateways putting work through it.
- **Orchestrator.** An operator running hardware that serves jobs on the network, also referred to as an operator.
- **Delegator.** Someone staking LPT to an orchestrator and earning a share of their rewards and fees.
- **Validator.** Under 2.0, a participant that independently checks and scores what the network did. Whether that is a new role or an existing one carrying an extra responsibility is not yet decided.
- **Payment clearinghouse.** The auth and billing layer that lets a client pay for network work without using a crypto wallet.
- **Live Runner.** The runtime an orchestrator deploys to serve capabilities on the network.
- **Capability.** A specific job type an orchestrator advertises and can be paid to run.
- **Passthrough.** Serving a capability by routing it to a third-party provider rather than running it on your own hardware.
- **Service registry.** The single place capabilities, hardware and pricing are advertised so a gateway can discover and price them.
- **Subgraph.** The indexed on-chain data that feeds the Explorer, console and dashboards. Not real-time, and not used for orchestration.
- **Explorer.** The public interface where delegators and orchestrators stake, vote and see network activity.

---

## CTA: Please Give Feedback and Ideas

We want to ensure that we are funding community initiatives.

Much of what is included above is based on the feedback of the community within the roadmap session from August 11th.

Related source pages shown in the screenshots:

- Network Engineering SPE Milestones
- Validate Track: Proposed Direction
