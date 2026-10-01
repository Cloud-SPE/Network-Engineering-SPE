# Network Engineering SPE — Build Track Monthly Update: September 2026

September completed the Build Track’s architecture and planning milestone. We brought together stakeholder input, assessed existing Livepeer software, and finalized the architecture and delivery plan for a shared builder engine. The intended benefit is straightforward: application teams can reuse common functions for access, discovery, execution, results and network-cost reporting while retaining control of their products. The architecture and milestones were accepted effective September 30 following stakeholder review. Source assessment and planning are complete; runtime integration verification is ahead. The next milestone targets foundations and integration contracts by October 16, with final delivery planned for December 31.

**Author:** Mike Zupper · **Reporting period:** September 1–30, 2026

## What builders will gain

Today, a team building on Livepeer needs to connect several components to discover capabilities, understand prices, submit work, retrieve results and account for network costs. The Build Track will bring these common functions into a reusable open-source engine. Teams will be able to embed its packages in their applications or run it as a service, with an HTTP API and a Model Context Protocol (MCP) interface for agent tools.

The engine and reference application will support seven outcomes for builders:

1. Obtain access with an appropriate credential.
2. Discover available network capabilities and usable supply.
3. Understand a price, estimate or bounded rate before execution.
4. Invoke a capability through a stable interface.
5. Receive a result or an actionable failure.
6. Pay for network work without managing a crypto wallet.
7. Inspect usage and the resulting network cost.

An enterprise could use the engine with its own login system, application interface and billing service. A smaller team could start from the reference application. Both should be able to add features through supported interfaces without rewriting the shared core. The reference application will demonstrate that complete builder journey and the extension points needed for different products.

The engine will integrate existing network components, including the Python gateway SDK, remote signer, Clearinghouse Batteries and Orchestrator/Live Runner execution. The [architecture and executive summary](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3b622ee/docs/design-docs/self-sovereign-open-builder-stack-draft.md) explain the components and their responsibilities.

## September’s work

- **Consolidated stakeholder requirements.** Survey responses and discussions with Network Engineering SPE participants and Livepeer Inc informed the design. Conversations with Rick, Doug, John and Josh clarified technical direction, payment paths, enterprise needs and ownership. The September 24 NE-SPE and Inc Agent team meeting established conceptual alignment around the shared builder foundation.

- **Assessed existing software and reuse opportunities.** We reviewed source evidence for the SDK, signer, Batteries and Console prototype, and mapped existing capabilities and integration gaps. Console serves as reference material. We also identified Inc’s private `livepeer/simple-infra` implementation as a potential source of reusable work, subject to access, inspection and permission. The [capability inventory](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3b622ee/docs/design-docs/console-capability-and-gap-matrix.md) distinguishes inspected behavior from integration still to be verified.

- **Defined the architecture and delivery boundaries.** The design separates enterprise applications, the shared engine, and network/payment components. It supports embedded and service deployment, with self-operated or separately operated payment infrastructure. Mike Zupper owns Build Track delivery; existing maintainers retain responsibility for their upstream components. Network usage and costs remain separate from enterprise retail billing.

- **Prepared the stakeholder review package.** We produced and refined the executive summary, component and sequence diagrams, source inventory, and acceptance requirements. The package explains both the builder experience and how enterprise features can be added without changing core components.

- **Established the delivery plan and public tracking.** The plan contains six September planning tasks and 39 implementation tasks across five milestones. It defines dependencies and evidence needed for completion, with a minimum reference application and all seven builder outcomes required. PostgreSQL, additional streaming, hard spending guarantees and a full Console port remain stretch goals. The [public GitHub project](https://github.com/orgs/Cloud-SPE/projects/13) makes the milestones and progress visible to the ecosystem.

## Review outcome

The architecture and executive summary were circulated for review from September 27–30. The milestone plan was sent to the NE-SPE committee on September 28. All parties approved the plans and architecture, establishing the delivery baseline effective September 30.

M1—defining and approving the shared builder architecture—is complete. The [approval record](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3b622ee/docs/decisions/2026-09-30-build-track-architecture-and-milestones.md) documents the review basis. Remaining implementation decisions and late feedback will be considered during delivery, with any changes to scope or dates made explicit.

## Next: foundations and integration contracts

M2 runs from October 1–16, with an October 1 kickoff to determine which tasks start first. Its planned work covers confirming which existing software we can reuse, agreeing how access and payments will work across components, and establishing the engine’s foundation with reliable data storage and a repeatable process for building the software.

Runtime integration remains to be verified. Key dependencies include compatible upstream interfaces, permitted source reuse and a funded environment for later execution and accounting tests. Those dependencies will be resolved as their delivery tasks require. The next milestone update is planned for the October 16 checkpoint.

The [accepted delivery specification](https://github.com/Cloud-SPE/Network-Engineering-SPE/blob/3b622ee/docs/product-specs/build-track-2026.md) links the full architecture, required scope and milestone acceptance criteria through December 31.
