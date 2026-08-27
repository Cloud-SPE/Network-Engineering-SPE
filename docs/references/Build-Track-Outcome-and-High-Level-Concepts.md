# Build Track: Outcome and High-Level Concepts

**Status:** Revised working draft
**Date:** 27 August 2026
**Track:** Easy to Build — Builder
**Track owner:** Mike Zupper
**Source:** [Network Engineering SPE II notes](NetworkEngieneerSPE2-Notes-v2.md)

> **Scope correction:** Demand generation, application adoption, application
> counts, production-traffic targets, and live-demand evidence are not Build
> Track requirements. Decision `netspe-vun.7` supersedes the adoption language
> in earlier drafts. Sample or reference applications may demonstrate an
> interface, but they are documentation or controlled validation aids only.

## Intended outcome

By 31 December 2026:

> A developer, application, or agent can make a successful paid call through
> the supported Livepeer builder interface without managing crypto mechanics,
> configuring network infrastructure, or contacting an Operator.

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

### 7. Verifiable success

The outcome should be demonstrated through observable facts:

- an independent builder completes a first call;
- no wallet or operator coordination is required;
- payment and usage are visible;
- traffic passes through the clearinghouse;
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
- correlation of an invocation with its usage, network payment, and resulting
  charge.

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

> The Build Track is not complete when the infrastructure exists. It is
> complete when an independent builder can use that infrastructure
> successfully, pay through it, and understand the result and resulting charge.

## Open questions

### 1. What is the current state of the builder path?

The concepts above read as if starting from a blank slate, but several repositories already cover parts of the journey. Before milestones are set, the track needs a baseline of what each provides today, what is deployed, and what gaps remain:

| Repository | Presumed role in the builder journey | Questions |
| --- | --- | --- |
| [livepeer/storyboard](https://github.com/livepeer/storyboard) (the Livepeer Agent) | Possible reference integration and builder-facing client | Does it call the network today, through which path, and against which supported interfaces? Which parts are reusable platform behavior versus Agent-specific behavior? |
| [livepeer/go-livepeer](https://github.com/livepeer/go-livepeer) | Core node: gateway, orchestrator, ticket broker payments | Which capabilities are invokable through a gateway today? Where does capability discovery and pricing currently live, and is there a service registry contract or only per-capability behaviour? |
| [livepeer/livepeer-python-gateway](https://github.com/livepeer/livepeer-python-gateway) | Gateway or SDK surface that builders would call | Is this the intended standard builder interface, or an interim one? What is its deployment status and how far is it from the "one credential, discover, price, invoke" promise? |
| [livepeer/clearinghouse](https://github.com/livepeer/clearinghouse) | Walletless auth, credits, metering and settlement | What works end to end today: account creation, credit balance, per-job metering, on-chain settlement through the ticket broker? What is the correlation model across credential, job, capability, usage, and charge? Who is funding and maintaining it? |

Specific questions:

- Which of these components are deployed and reachable by someone outside the project today, and which exist only in a repository?
- Is there a working end-to-end call today (credential → discover → invoke → result → charge) for any capability, even manually? If so, what are the manual steps that self-service must remove?
- Are there other repositories or services on this path that are not listed above (docs, SDKs, registry, dashboards)?
- Where does the boundary sit between the Build Track, the Operate Track (Live Runner, service registry), and Livepeer Inc's payments work on the clearinghouse?
- What usage and fee data can be produced today that would count as acceptance evidence in December?

The answers determine the baseline milestone and how much of the $50,000 goes to closing gaps versus integration and documentation.
