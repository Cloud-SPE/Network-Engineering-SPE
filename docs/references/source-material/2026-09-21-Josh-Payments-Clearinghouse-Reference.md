# Josh Payments Clearinghouse Proposal: Reference Capture

**Captured and reviewed:** 21 September 2026\
**Status:** External proposal and historical evidence; not an accepted Cloud SPE design\
**Author and sharing provenance:** Mike Zupper identifies Josh Allmann as the author and Rick Staa as the person who shared the document. Mike describes it as material concerning Livepeer Inc's clearinghouse plans. The supplied export does not independently establish authorship, approval, or a current Inc delivery commitment.\
**Source title:** Payments Clearinghouse\
**Original publication and last substantive revision dates:** Unknown\
**Execution bead:** `netspe-vun.23`

## Preserved source and limitations

- [Original Notion page](https://app.notion.com/p/livepeer/Payments-Clearinghouse-25e0a3485687817394d0c3442ffca622).
- [Unmodified nine-page PDF supplied by Mike](2026-09-21-Josh-Payments-Clearinghouse-Notion.pdf), originally named `Josh-Payments Clearinghouse _ Notion-09212026.pdf`.
- PDF metadata records creation on 21 September 2026 at 08:18:10 EDT. This is an export date, not evidence of when the proposal was authored or approved.
- SHA-256: `9de71502b584f5f7781835407d0ef00ab2346ba69954e87a8695be1230213dfc`.

All nine pages were text-extracted and visually inspected. The final page is
visibly clipped after the USD billing-service estimate, at the start of another
bullet. The capture therefore does not establish the complete ending of the
Notion document. The live URL was not accessible through the available web
reader; no comparison with the live revision was possible. Missing content has
not been reconstructed.

The proposal identifies itself as Part 1 of the Livepeer: Weir proposal. Its
present-tense software and network claims are claims made by that source, not
verified descriptions of September 2026 deployments. No repository, commit,
deployed configuration, implementation status, or external approval was verified
for this capture. Reverify those facts before using them for an architecture
decision or delivery acceptance.

## What the source proposes

| Topic | Source proposal or argument | PDF pages |
| --- | --- | --- |
| Payment proxy | A clearinghouse signs probabilistic micropayment tickets for gateways, maintains customer balances, and settles with customers in fiat or through allocated credits. Gateway-to-orchestrator payments continue using the existing PM mechanism and ETH settlement. | 1, 4-5 |
| Motivation | Reduce cryptocurrency and PM integration burdens, dependence on full-service gateway providers, payment-key exposure to untrusted media, and difficulty accounting for grant-funded usage. | 2-3 |
| Remote payment signer | Add a `go-livepeer` signer mode and RPCs for tickets and supporting signatures such as `OrchestratorRequest`. Keep payment keys separate from media processing; gateways continue submitting work and tickets to orchestrators. | 4 |
| Minimal signer versus clearinghouse | The signer initially needs basic signing behavior. Customer bookkeeping and balance management can be added by clearinghouse implementations. Remote signing is optional in the proposed rollout. | 4 |
| Local gateways | A locally operated gateway can obtain signed tickets using an API key and/or service URL, allowing payment abstraction without outsourcing media processing. | 4 |
| Grants foundation | A proposed Grants Clearinghouse SPE would provide usage credits, account tracking, and transparency reports, and could form a base for specialized clearinghouses. This is an external proposal, not assigned Cloud SPE work. | 5 |
| Specialized providers | Providers could support fiat, other cryptocurrencies, x402, or other payment arrangements above the network payment mechanism. These are examples, not selected integrations. | 5 |
| Optional on-chain differentiation | Customer and end-user identifiers might be added to tickets for reporting and verification. The source describes this as an optional extension, not a prerequisite for remote signing. | 6 |
| Intended effect | Lower the barrier to independent gateways and specialized payment providers while improving separation of payment keys from media handling. | 6-7 |

## Risks and estimates recorded by the source

The proposal discusses provider concentration and outages, and suggests defined
RPCs and possibly advance ticket batches as mitigations (pages 7-8). Switching a
provider URL is presented as a possibility, not demonstrated portability of
balances, credentials, or customer history.

It explicitly separates payment processing from the quality of completed work.
Refunds or credits for poor execution can leave the clearinghouse bearing an
already-paid network cost; a possible community-funded reinsurance pool is an
idea, not an accepted obligation (page 8). The proposal also states that the
clearinghouse does not itself solve orchestrator self-dealing and discusses
gateway quality monitoring and transparency reports (pages 8-9).

The legible estimates on page 9 are one month for signer implementation and
associated testing/documentation; one month for a grants SPE proposal/design
followed by three months to build and launch; and three months for a USD billing
service using the grants service as a base. The USD service is proposed to be
operated by a legal entity rather than an SPE. These are undated source
estimates, not current commitments or the Cloud SPE's October-December schedule.
The remaining timeline content is clipped.

## Relevance to the Cloud SPE architecture proposal

This source provides an input to the clearinghouse boundary question raised in
the [John Mull findings](../stakeholder-input/meetings/2026-09-02-John-Mull-Clearinghouse-Meeting-Notes.md)
and the [Doug alignment findings](../stakeholder-input/meetings/2026-09-09-Doug-Agent-GTM-Build-Track-Alignment-Meeting-Findings.md).
Its narrow payment-service boundary needs to be reconciled with the broader
discovery, invocation, and usage responsibilities shown in the
[emerging builder architecture](../analysis/2026-09-09-Build-Track-Emerging-Architecture.md).

Mike's direction on 21 September is to propose one reusable open-source
clearinghouse core that Livepeer Inc, Elite Encoder's Pymthouse, and independent
open-source deployments could build on or retrofit into. The initial proposal
may differ from existing products, and the October-December work may need to
reshape its integration boundaries. This is Mike's proposed design direction;
the source does not establish agreement to adopt one shared implementation.

The architectural implication is to distinguish shared engine behavior,
provider-specific integrations, and the wider builder journey. The exact core
boundary, source repository, maintainers, license, compatibility contracts,
migration effort, and operator commitments remain to be proposed and reviewed.
Interoperability should have reproducible evidence; adoption by Inc or Elite
Encoder cannot be promised on their behalf.

Mike intends to propose dispositions for all remaining architecture and outcome
decisions, present the complete proposal to the Network Engineering SPE, and
then finalize Cloud SPE milestones for 1 October through 31 December 2026.
This replaces waiting for full preliminary consensus as the planning approach;
it does not replace the relevant owners' decision authority or the required SPE
approvals. Execution state, dependencies, and GitHub Project preparation belong
in Beads, not in this reference. Demand generation and application adoption
remain outside the Cloud SPE Build Track scope.
