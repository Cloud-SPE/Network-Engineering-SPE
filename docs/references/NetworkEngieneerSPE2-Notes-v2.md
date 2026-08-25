# Pre-Proposal: Network Engineering SPE II

Proposed by: Rich O'Grady, Ecosystem Director, Livepeer Foundation.

---

## Abstract

The Network Engineering SPE funds the work that makes the Livepeer network easier to participate in: builders, orchestrators, delegators and, if 2.0 lands as planned, validators. Round one proved the SPE’s value as a funding mechanism. It also showed that one pool with one technical reviewer and no clear outcomes can lack direction. So round two keeps the mission and changes the shape: four tracks, one named owner on each, one outcome per track to hit by the end of the year, and the capital sitting with those owners rather than held centrally.

**Request:** $230,000 USD-equivalent in LPT, 1 Sep to 31 Dec 2026

**Preceded by:** the Network Engineering SPE pilot, 15 May to 30 Aug 2026, $95,000

**Feedback session**: https://docs.google.com/document/d/1DgU8ovr2qCwJ8-xkbxajfb53UNh_ghQZRl-SGhf_LDg/edit?tab=t.d47gkljqyzrr

---

## Mission

The mission of the SPE is to make the Livepeer network easy to participate in: to build on, operate, validate and delegate for all participants.

It focuses on the key actors within the Livepeer network: Builders (including developers, agents and gateways), Orchestrators (also referred to as Operators), Delegators and, with the upcoming 2.0 vote, Validators.

To achieve this mission, the SPE will aim to unify key engineering leaders around one vision, and empower them with capital, talent and programs. By working with the community, the SPE will give these leaders a clear mandate to remain accountable to, while providing operational support with mechanisms that can fund critical engineering work quickly.

The SPE will divide the work to be done into four tracks. These tracks guide the SPE focused on four personas, each with their own outcome, a single owner responsible and a set of milestones to achieve it. These owners can be funded by the SPE or receive a salary from another core organisation (e.g. the Livepeer Foundation or Livepeer Inc).

The capital from the SPE is deployed to fund the work to complete these milestones through a variety of mechanisms (RFPs, grants, bounties, fixed contracts). After discussing this in a recent feedback session, the SPE will use a variety of funding mechanisms to ensure that we find the person for the right task at the right cost.

---

## Rationale

### What’s changed from the pilot SPE

This Network Engineering SPE will be structured differently to the pilot.

The pilot SPE structure was focused on three directional priorities with a combined pot for RFPs and grants (direct or retroactive). This model had a great deal of flexibility baked in. However, it (a) lacked concrete outcomes or goals that were clearly set at the beginning; (b) had a review bottleneck with the Technical Director; and (c) did not have strong enough accountability. See the full retro here.

This SPE is structured differently. It splits the work into four tracks each around a core ecosystem stakeholder: Builder, Orchestrator, Delegator, and, still to be decided and shaped, Validator. Each track then gets one owner, one outcome by the end of the year, and a budget that owner is allocated.

The owner is on the hook for the outcome. It can route the funding allocated to other contributors to complete the work.

### Four new tracks to focus work

The four tracks are places where our claim to be an open network still falls down in practice:

| **Track** | **Owner** | **Outcome by 31 Dec** |
| --- | --- | --- |
| **Easy to build**
Builder | Mike Zupper | The Livepeer Agent plus four further demand sources are onboarded and putting real, attributable traffic through the network via the clearinghouse, supported by a credits programme (separate SPE). A developer, client or agent can make a first successful call and settle payment without a wallet, without setup and without contacting an Operator. |
| **Easy to operate**
Orchestrator | Josh Allman | 50 orchestrators have advertised and served capabilities through Live Runner, with enough observability to understand failures. Livepeer has a network substrate that connects demand to supply end to end, where new capabilities can be introduced without building a new integration stack each time, and every capability is discoverable with clear pricing by an application. |
| **Easy to delegate**
Delegator | Elliott Conway | Make self-custody delegation clearer, safer, and easier to use, with a staking experience that is competitive with leading alternatives. This primarily means improving conversion between stages of the delegation journey and ultimately increasing delegation volume, provided that upstream interest in delegation does not decline. |
| **Easy to validate***
Validator | Shane Burgett | TBD on Livepeer 2.0.

*Proposed: an independent, reproducible measurement service that anyone can run and duplicate, producing evidence of self-dealing and fee manipulation.* |

*We do not yet know whether validation means a full validator set with on-chain scoring, or existing participants carrying an extra responsibility. Those need very different programmes and very different funding, so we are holding the budget and naming no owner until we know more.

### How funds reach contributors

For this SPE, owners will pick the mechanism per task. Different mechanisms can be used dependent on whether the work is defined, a contributor has been identified or the price of work still needs to be determined.

This decision emerged out of the roadmap session call form August 11th, where community members suggested that there was no need to over-index on one or two mechanisms.

The suggested mechanisms that could be used are:

| **Mechanism** | **When an owner reaches for it** | Funding Amount |
| --- | --- | --- |
| **RFP** | Scope is clear but the right contributor is neither in the network nor known to us. Longer window than last round, distributed beyond the forum | $5,000 to $30,000 |
| **Direct grant** | Scope is clear and the builder is obvious. Paid against milestones. Moved the most capital last round | Up to $20,000 |
| **Retroactive grant** | Work has already shipped against a problem the community named publicly first | Up to $10,000 |
| **Scoping grant** | The work cannot be specified yet, and specifying it is the deliverable. New this round | Up to $5,000 |
| **Bounty** | Small and self-contained, worth opening to anyone. Spendable directly by a committee member, no application path. Five of round one's seven retro grants were bounties and they reached builders no portal had | $500 to $2,000. |
| **Fixed contract** | Sustained ownership of a surface over 2-4 months, with milestones set by the track owner. | $5,000 to $40,000 |

### What this SPE isn't

- **Not funding the agent framework.** The Livepeer agent will be funded separately from across Inc, the Foundation and the treasury.
- **Not a demand generation or credits fund.** Go-to-market and end-user product work will sit within anothe SPE proposal coming soon.
- **Not protocol design.** 2.0 is designed and voted elsewhere. This funds getting the people already here across to it.
- **Not an open-ended pool.** Every disbursement needs a verified definition of done.

---

## SPE Governance Structure

### Roles & responsibilities

| **Role** | **Who** | **Responsibilities** | **Paid by SPE** |
| --- | --- | --- | --- |
| **Committee** | Rick Staa, Josh Allmann, Elliott Conway, plus Orchestrator | Sets each track's outcome, defines and reviews milestones, signs off and merges code, decides allocations brought by another member | Two of four, as track owners |
| **Track owner** | One committee member per track | Presents three to five milestones, allocates the track budget, picks the mechanism per task, brings in contributors to do the work | $20,000 each, where not already paid by Inc or the Foundation |
| **Foundation Operations** | Rich O'Grady, Ben Perez, Mehrdad Sadeghi, Jalaj Jain | Programme management, bringing in new contributors, treasury and payment operations, monthly reporting, final sign-off on release of funds. Buys in independent review per task so payouts do not queue behind one calendar | No, though bought-in review is paid from the bounty pot |

### Committee operations

- **Voting -** When a member brings an allocation, a sign-off or a scope change forward, the other three decide it on a simple majority and the member bringing it does not vote. Where a committee member is absent, a Foundation Operations team member will step in so a decision is never held up by a diary. The Foundation Operations team also holds the final gate on payment and releases funds only once the definition of done is verified.
- **Code review** - review is a named committee responsibility: every contribution funded by this SPE will aim to get an approve or reject with reasons within the month.
- **Conflicts of interest -** Several committee members run something that touches the network commercially, and excluding them would cost us more than the conflict does. We will therefore introduce that a track owner may direct no more than 50% of their own track allocation to themselves or to an entity they control. It will also be disclosed on the forum when it happens, with the member recused and Foundation Operations releasing the funds. Any contributors paid by the Foundation or Livepeer Inc will not receive further compensation from the SPE.

---

## Timeline & Milestones

Each track will have their own milestones, which will be tracked and reported on concurrently by their respective owners.

### SPE Timeline

**1st September - Track Milestones Finalised** - each Track Owner has finalised their respective milestones (see below).

**8th September - Operating Cadence Established** - weekly committee meeting running and payment operations set up.

**29th September - First Monthly Update Published - p**ublished on the forum, covering work funded and delivered per track, funds committed and disbursed, code merges and every committee decision with its rationale.

**20th December - Retro Completed -**  Each track assessed against its outcome, total spend against budget, and a recommendation per track: continue, change owner, or stop. Community session held alongside it.

### Milestones

Each track has an outcome to achieve by the end of the year (see above). They then have a series of facts that need to be true to know whether they have achieved their outcome:

| **Track** | What Must Be True | **Checked by** |
| --- | --- | --- |
| **Easy to build**
Builder | • First call works without a wallet or setup
• Clients can discover, price, pay for and invoke services through standard interfaces
• Payments and metering work across supported service types without bespoke integration
• You can see what a job costs, before and after you run it
• Docs and SDK match what's actually deployed
• Demand side programme has funded 2-3 core demand bets | Fees on-chain through the ticket broker. A timed first call by someone outside the project |
| **Easy to operate**
Orchestrator | • Live Runner covers the operator path end to end
• There is a canonical contract for capabilities, hardware, pricing and service discovery
• Operators can determine why a job failed, including failures outside the operator's control
• A capability can be validated before deployment
• There is a credible path from today's network architecture to 2.0 | Count of orchestrators serving a capability. Failed job diagnosed by the operator, not by us |
| **Easy to delegate**
Delegator | • Delegation journey conversion is measurable against a clear baseline
• Users can confidently discover and compare Orchestrators using meaningful, trustworthy information
• Rewards, fees, risks and unbonding conditions are clear before commitmen
• Delegating, switching and exiting are understandable, reliable and low-friction
• Delegators can clearly understand their position and earnings after delegating | Explorer surfaces shipped against the scored backlog. Every lockup shown before commitment |
| **Easy to validate***
Validator | *Proposed:
• The runner and signer emit the events the measurement depends on
• Two parties running the same service against the same data get the same answer
• Evidence of self-dealing or fee manipulation is published
• A client can check their own job ran
• The output is usable by delegators and gateways, not only by validators* | TBD |

**Note: In the coming days, formal milestones will be formed around each track. The aim is to publish these in time for the final proposal.**

---

## Budget Breakdown

**$230,000 USD-equivalent in LPT** for one four-month cycle, sized on the **30-day moving average** LPT price at approval.

### Budget Overview

| **Line** | **Allocation** | **What it funds** |
| --- | --- | --- |
| Track owner, Validate | $20,000 | Accountable ownership and delivery of the Validate outcome. Expected roughly 10-15 hours per week, including meetings |
| Track owner, Delegate | $20,000 | Accountable ownership and delivery of the Delegate outcome. Expected roughly 10-15 hours per week, including meetings |
| Build track, contributors | $50,000 | SDK, payment clearinghouse, service registry and schema contract, discovery, docs and capability templates, metering and spend transparency |
| Operate track, contributors | $50,000 | Operator tooling, diagnostics and real job state, Live Runner developer experience, capability supply, migration tooling and the 2.0 upgrade path |
| Delegate track, contributors | $20,000 | Explorer delegator experience, lockup transparency, staking guidance, subgraph engineering including audit remediation, and research into what 2.0 changes for delegators |
| Validate track, contributors | $20,000 | Provisional, released only if the track activates |
| Bounties, grants and research | $30,000 | Cross-track work no single track owns: a bounty pot spendable directly under a per-item cap, scoping grants, retroactive grants, and bought-in review |
| Buffer | $20,000 | Held against LPT price movement, so a falling price is not a pay cut mid-milestone |
| **Total** | **$230,000** |  |

### Budget Notes

- A Track Owner works inside their allocation and brings anything larger to the committee. Reallocation between tracks is possible at the end of each month with a published decision.
- A Track Owner may direct no more than 50% of their own track allocation to themselves or to an entity they control.
- No contributors funded by Livepeer Inc or the Livepeer Foundation will receive further funding from the SPE.
- The two Track Owners for Validate and Build will be compensated a $5,000 per month fixed contract. This will be withheld if duties have not been performed.
- Payouts in LPT at a 7-day average at the point of payment. We will manage the treasury position on receipt rather than sitting on $250,000 of LPT for four months, so contributors get what they were promised whatever the price does.
- Anything unspent carries to the next round, or goes back to the treasury if there isn't one. Incomplete work at 31 December gets a short remediation window first.

---

## Transparency and Accountability

- Monthly written updates on the forum:  work funded and delivered per track, milestones signed off and missed, funds committed and disbursed against allocation, and every committee decision with its rationale.
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

## CTA: Please Give Feedback & Ideas

We want to ensure that we are funding community initiatives

Much of what is included above is based on the feedback of the community within the roadmap session from August 11th.

Network Engineering SPE Milestones

| **Track** | **Owner** | **Outcome by 31 Dec** |
| --- | --- | --- |
| **Easy to build**
Builder | Mike Zupper | The Livepeer Agent plus four further demand sources are onboarded and putting real, attributable traffic through the network via the clearinghouse, supported by a credits programme (separate SPE). A developer, client or agent can make a first successful call and settle payment without a wallet, without setup and without contacting an Operator. |
| **Easy to operate**
Orchestrator | Josh Allman | 50 orchestrators have advertised and served capabilities through Live Runner, with enough observability to understand failures. Livepeer has a network substrate that connects demand to supply end to end, where new capabilities can be introduced without building a new integration stack each time, and every capability is discoverable with clear pricing by an application. |
| **Easy to delegate**
Delegator | Elliott Conway | Make self-custody delegation clearer, safer, and easier to use, with a staking experience that is competitive with leading alternatives. This primarily means improving conversion between stages of the delegation journey and ultimately increasing delegation volume, provided that upstream interest in delegation does not decline. |
| **Easy to validate***
Validator | Shane Burgett | TBD on Livepeer 2.0.

*Proposed: an independent, reproducible measurement service that anyone can run and duplicate, producing evidence of self-dealing and fee manipulation.* |
*We do not yet know whether validation means a full validator set with on-chain scoring, or existing participants carrying an extra responsibility. Those need very different programmes and very different funding, so we are holding the budget and naming no owner until we know more.

### How funds reach contributors

For this SPE, owners will pick the mechanism per task. Different mechanisms can be used dependent on whether the work is defined, a contributor has been identified or the price of work still needs to be determined.

This decision emerged out of the roadmap session call form August 11th, where community members suggested that there was no need to over-index on one or two mechanisms.

The suggested mechanisms that could be used are:
| **Mechanism** | **When an owner reaches for it** | Funding Amount |
| --- | --- | --- |
| **RFP** | Scope is clear but the right contributor is neither in the network nor known to us. Longer window than last round, distributed beyond the forum | $5,000 to $30,000 |
| **Direct grant** | Scope is clear and the builder is obvious. Paid against milestones. Moved the most capital last round | Up to $20,000 |
| **Retroactive grant** | Work has already shipped against a problem the community named publicly first | Up to $10,000 |
| **Scoping grant** | The work cannot be specified yet, and specifying it is the deliverable. New this round | Up to $5,000 |
| **Bounty** | Small and self-contained, worth opening to anyone. Spendable directly by a committee member, no application path. Five of round one's seven retro grants were bounties and they reached builders no portal had | $500 to $2,000. |
| **Fixed contract** | Sustained ownership of a surface over 2-4 months, with milestones set by the track owner. | $5,000 to $40,000 |

### What this SPE isn't

- **Not funding the agent framework.** The Livepeer agent will be funded separately from across Inc, the Foundation and the treasury.
- **Not a demand generation or credits fund.** Go-to-market and end-user product work will sit within anothe SPE proposal coming soon.
- **Not protocol design.** 2.0 is designed and voted elsewhere. This funds getting the people already here across to it.
- **Not an open-ended pool.** Every disbursement needs a verified definition of done.

---

## SPE Governance Structure

### Roles & responsibilities

| **Role** | **Who** | **Responsibilities** | **Paid by SPE** |
| --- | --- | --- | --- |
| **Committee** | Rick Staa, Josh Allmann, Elliott Conway, plus Orchestrator | Sets each track's outcome, defines and reviews milestones, signs off and merges code, decides allocations brought by another member | Two of four, as track owners |
| **Track owner** | One committee member per track | Presents three to five milestones, allocates the track budget, picks the mechanism per task, brings in contributors to do the work | $20,000 each, where not already paid by Inc or the Foundation |
| **Foundation Operations** | Rich O'Grady, Ben Perez, Mehrdad Sadeghi, Jalaj Jain | Programme management, bringing in new contributors, treasury and payment operations, monthly reporting, final sign-off on release of funds. Buys in independent review per task so payouts do not queue behind one calendar | No, though bought-in review is paid from the bounty pot |

### Committee operations

- **Voting -** When a member brings an allocation, a sign-off or a scope change forward, the other three decide it on a simple majority and the member bringing it does not vote. Where a committee member is absent, a Foundation Operations team member will step in so a decision is never held up by a diary. The Foundation Operations team also holds the final gate on payment and releases funds only once the definition of done is verified.
- **Code review** - review is a named committee responsibility: every contribution funded by this SPE will aim to get an approve or reject with reasons within the month.
- **Conflicts of interest -** Several committee members run something that touches the network commercially, and excluding them would cost us more than the conflict does. We will therefore introduce that a track owner may direct no more than 50% of their own track allocation to themselves or to an entity they control. It will also be disclosed on the forum when it happens, with the member recused and Foundation Operations releasing the funds. Any contributors paid by the Foundation or Livepeer Inc will not receive further compensation from the SPE.

---

## Timeline & Milestones

Each track will have their own milestones, which will be tracked and reported on concurrently by their respective owners.

### SPE Timeline

**1st September - Track Milestones Finalised** - each Track Owner has finalised their respective milestones (see below).

**8th September - Operating Cadence Established** - weekly committee meeting running and payment operations set up.

**29th September - First Monthly Update Published - p**ublished on the forum, covering work funded and delivered per track, funds committed and disbursed, code merges and every committee decision with its rationale.

**20th December - Retro Completed -**  Each track assessed against its outcome, total spend against budget, and a recommendation per track: continue, change owner, or stop. Community session held alongside it.

### Milestones

Each track has an outcome to achieve by the end of the year (see above). They then have a series of facts that need to be true to know whether they have achieved their outcome:

| **Track** | What Must Be True | **Checked by** |
| --- | --- | --- |
| **Easy to build**
Builder | • First call works without a wallet or setup
• Clients can discover, price, pay for and invoke services through standard interfaces
• Payments and metering work across supported service types without bespoke integration
• You can see what a job costs, before and after you run it
• Docs and SDK match what's actually deployed
• Demand side programme has funded 2-3 core demand bets | Fees on-chain through the ticket broker. A timed first call by someone outside the project |
| **Easy to operate**
Orchestrator | • Live Runner covers the operator path end to end
• There is a canonical contract for capabilities, hardware, pricing and service discovery
• Operators can determine why a job failed, including failures outside the operator's control
• A capability can be validated before deployment
• There is a credible path from today's network architecture to 2.0 | Count of orchestrators serving a capability. Failed job diagnosed by the operator, not by us |
| **Easy to delegate**
Delegator | • Delegation journey conversion is measurable against a clear baseline
• Users can confidently discover and compare Orchestrators using meaningful, trustworthy information
• Rewards, fees, risks and unbonding conditions are clear before commitmen
• Delegating, switching and exiting are understandable, reliable and low-friction
• Delegators can clearly understand their position and earnings after delegating | Explorer surfaces shipped against the scored backlog. Every lockup shown before commitment |
| **Easy to validate***
Validator | *Proposed:
• The runner and signer emit the events the measurement depends on
• Two parties running the same service against the same data get the same answer
• Evidence of self-dealing or fee manipulation is published
• A client can check their own job ran
• The output is usable by delegators and gateways, not only by validators* | TBD |

**Note: In the coming days, formal milestones will be formed around each track. The aim is to publish these in time for the final proposal.**

---

## Budget Breakdown

**$230,000 USD-equivalent in LPT** for one four-month cycle, sized on the **30-day moving average** LPT price at approval.

### Budget Overview
| **Line** | **Allocation** | **What it funds** |
| --- | --- | --- |
| Track owner, Validate | $20,000 | Accountable ownership and delivery of the Validate outcome. Expected roughly 10-15 hours per week, including meetings |
| Track owner, Delegate | $20,000 | Accountable ownership and delivery of the Delegate outcome. Expected roughly 10-15 hours per week, including meetings |
| Build track, contributors | $50,000 | SDK, payment clearinghouse, service registry and schema contract, discovery, docs and capability templates, metering and spend transparency |
| Operate track, contributors | $50,000 | Operator tooling, diagnostics and real job state, Live Runner developer experience, capability supply, migration tooling and the 2.0 upgrade path |
| Delegate track, contributors | $20,000 | Explorer delegator experience, lockup transparency, staking guidance, subgraph engineering including audit remediation, and research into what 2.0 changes for delegators |
| Validate track, contributors | $20,000 | Provisional, released only if the track activates |
| Bounties, grants and research | $30,000 | Cross-track work no single track owns: a bounty pot spendable directly under a per-item cap, scoping grants, retroactive grants, and bought-in review |
| Buffer | $20,000 | Held against LPT price movement, so a falling price is not a pay cut mid-milestone |
| **Total** | **$230,000** |  |

### Budget Notes

- A Track Owner works inside their allocation and brings anything larger to the committee. Reallocation between tracks is possible at the end of each month with a published decision.
- A Track Owner may direct no more than 50% of their own track allocation to themselves or to an entity they control.
- No contributors funded by Livepeer Inc or the Livepeer Foundation will receive further funding from the SPE.
- The two Track Owners for Validate and Build will be compensated a $5,000 per month fixed contract. This will be withheld if duties have not been performed.
- Payouts in LPT at a 7-day average at the point of payment. We will manage the treasury position on receipt rather than sitting on $250,000 of LPT for four months, so contributors get what they were promised whatever the price does.
- Anything unspent carries to the next round, or goes back to the treasury if there isn't one. Incomplete work at 31 December gets a short remediation window first.

---

## Transparency and Accountability

- Monthly written updates on the forum:  work funded and delivered per track, milestones signed off and missed, funds committed and disbursed against allocation, and every committee decision with its rationale.
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

## CTA: Please Give Feedback & Ideas

We want to ensure that we are funding community initiatives

Much of what is included above is based on the feedback of the community within the roadmap session from August 11th.
