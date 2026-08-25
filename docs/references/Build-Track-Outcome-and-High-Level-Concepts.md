# Build Track: Outcome and High-Level Concepts

**Status:** Working draft
**Date:** 24 August 2026
**Track:** Easy to Build — Builder
**Track owner:** Mike Zupper
**Source:** [Network Engineering SPE II notes](NetworkEngieneerSPE2-Notes-v2.md)

## Intended outcome

By 31 December 2026:

> The Livepeer Agent and four additional demand sources are generating real, attributable traffic through the Livepeer network using the clearinghouse. A developer, application, or agent can make a successful call and pay for network services without managing a crypto wallet, configuring network infrastructure, or contacting an operator.

The Build Track is successful when Livepeer can be consumed as a practical developer platform—not merely when individual components have shipped.

## Builder promise

A builder should be able to:

1. Obtain one credential.
2. Discover what the network can do.
3. Understand the expected price or rate.
4. Invoke a capability through a standard interface.
5. Receive a result or understandable failure.
6. Pay without holding crypto.
7. See their usage and resulting charge.

The complexity of orchestrators, runners, discovery, payment tickets, and settlement should remain behind the builder-facing interface.

## High-level concepts

### 1. Self-service participation

A new builder should not require assistance from a Livepeer contributor or operator. Account creation and SDK installation are reasonable; manual operator selection, signer configuration, wallet funding, and private infrastructure knowledge are not.

### 2. Standard builder interface

Builders need a stable way to discover and invoke network capabilities. Adding a new capability should not require creating another authentication, discovery, payment, and metering stack.

### 3. Discoverable supply

Applications should be able to determine:

- what capabilities are available;
- whether usable supply exists;
- the relevant price or rate; and
- how to invoke the capability.

The builder-facing catalog should reflect real network supply rather than a disconnected static list.

### 4. Walletless payment

Builders should interact with ordinary credentials, credits, balances, and usage records. The clearinghouse should translate that experience into Livepeer network payments without exposing crypto mechanics to the builder.

### 5. Cost transparency

Before execution, the builder should receive the most honest available cost statement:

- a fixed price;
- an estimate or bounded estimate; or
- a usage rate and maximum spend.

After execution, the builder should be able to see actual metered usage and the resulting charge.

### 6. Consistent experience across capabilities

Different capabilities may use different execution and billing models, but those differences should not require the builder to learn an entirely new integration stack.

The common concepts—identity, discovery, invocation, payment, usage, and errors—should remain consistent.

### 7. Attributable demand

Network traffic must be attributable to a specific demand source and capability. This allows the programme to distinguish genuine adoption from internal tests, demos, retries, or unattributed network activity.

### 8. Proven adoption

The Livepeer Agent serves as the reference integration, but the outcome requires more than one internally controlled client. Four additional demand sources demonstrate that the builder experience is reusable outside its original implementation.

### 9. Verifiable success

The outcome should be demonstrated through observable facts:

- an independent builder completes a first call;
- no wallet or operator coordination is required;
- payment and usage are visible;
- traffic passes through the clearinghouse;
- the Agent and four additional sources produce attributable usage; and
- documentation describes the system that is actually deployed.

## Responsibility boundary

The Build Track owns the demand-side experience:

- builder identity;
- capability discovery;
- standard invocation;
- walletless payment;
- usage and cost visibility;
- SDKs and documentation;
- integration support; and
- demand attribution.

It depends on the Operate Track for healthy, discoverable capability supply and on the separate credits and demand programmes for funding and recruiting external users.

## Out of scope

The Build Track does not primarily fund:

- development of the Livepeer Agent framework;
- general demand generation or marketing;
- the credits programme itself;
- Livepeer protocol design;
- operator tooling unrelated to the builder journey; or
- broad feature development without a direct connection to the outcome.

## Core principle

> The Build Track is not complete when the infrastructure exists. It is complete when independent builders can use that infrastructure successfully, pay through it, understand what happened, and return with real demand.

## Open questions

### 1. Why are "demand sources" part of the Build Track outcome?

The outcome requires the Livepeer Agent plus four additional demand sources to be putting real, attributable traffic through the clearinghouse. Yet the SPE notes state that this SPE is *not* a demand generation or credits fund, and that go-to-market and end-user product work sit in a separate SPE. The "what must be true" list also holds the Build Track to "demand side programme has funded 2-3 core demand bets", which the Build Track does not own.

This leaves the Build Track accountable for an adoption result whose funding, recruitment, and timing sit elsewhere. Two readings are possible:

- **Platform reading.** The Build Track owns the builder-facing surface (identity, discovery, invocation, walletless payment, usage, SDK, docs). The demand sources are the *proof* that the surface works, recruited and funded by the demand/credits SPE.
- **Programme reading.** The Build Track itself selects, builds or onboards the five demand sources as reference integrations, using its contributor budget.

These need different milestones and a different use of the $50,000. Proposed phrasing for Rich and the committee:

> "The outcome names five demand sources, but demand generation and credits are explicitly out of scope for this SPE. Is the Build Track responsible for the builder platform being *ready and proven* by five integrations, or for *delivering* those five integrations? If the former, who owns recruiting and funding the four external sources and by when? If the latter, should the demand-side bets line be removed from the Build Track's 'what must be true'?"

A related definition is needed regardless: what counts as a demand source (deployed application, unique credential, external organisation, minimum job or fee threshold), and what makes its traffic "attributable".

### 2. What is the current state of the builder path?

The concepts above read as if starting from a blank slate, but several repositories already cover parts of the journey. Before milestones are set, the track needs a baseline of what each provides today, what is deployed, and what gaps remain:

| Repository | Presumed role in the builder journey | Questions |
| --- | --- | --- |
| [livepeer/storyboard](https://github.com/livepeer/storyboard) (the Livepeer Agent) | Reference client and first demand source | Does it call the network today, and through which path? Is it integrated with the clearinghouse? Who owns its integration timeline, given the agent framework is funded outside this SPE? |
| [livepeer/go-livepeer](https://github.com/livepeer/go-livepeer) | Core node: gateway, orchestrator, ticket broker payments | Which capabilities are invokable through a gateway today? Where does capability discovery and pricing currently live, and is there a service registry contract or only per-capability behaviour? |
| [livepeer/livepeer-python-gateway](https://github.com/livepeer/livepeer-python-gateway) | Gateway or SDK surface that builders would call | Is this the intended standard builder interface, or an interim one? What is its deployment status and how far is it from the "one credential, discover, price, invoke" promise? |
| [livepeer/clearinghouse](https://github.com/livepeer/clearinghouse) | Walletless auth, credits, metering and settlement | What works end to end today: account creation, credit balance, per-job metering, on-chain settlement through the ticket broker? What is the attribution model (per credential, per source, per capability)? Who is funding and maintaining it? |

Specific questions:

- Which of these components are deployed and reachable by someone outside the project today, and which exist only in a repository?
- Is there a working end-to-end call today (credential → discover → invoke → result → charge) for any capability, even manually? If so, what are the manual steps that self-service must remove?
- Are there other repositories or services on this path that are not listed above (docs, SDKs, registry, dashboards)?
- Where does the boundary sit between the Build Track, the Operate Track (Live Runner, service registry), and Livepeer Inc's payments work on the clearinghouse?
- What usage and fee data can be produced today that would count as acceptance evidence in December?

The answers determine the baseline milestone and how much of the $50,000 goes to closing gaps versus integration and documentation.
