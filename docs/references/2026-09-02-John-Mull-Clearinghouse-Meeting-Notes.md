# 2 September 2026 John Mull Clearinghouse Meeting Notes

**Meeting:** Build Track clearinghouse architecture and roadmap discussion

**Participants:** Mike Zupper and John Mull, Elite Encoder

**Duration:** Approximately three hours

**Prepared:** 2 September 2026

**Status:** Initial reported findings; follow-up evidence required

**Execution bead:** `netspe-vun.19`

**Discussion guide:** [John Mull Clearinghouse Roadmap Discussion Guide](John-Mull-Clearinghouse-Roadmap-Discussion-Guide.md)

## Purpose and method

This record captures Mike Zupper's contemporaneous summary of a three-hour
discussion with John Mull. It is not a verbatim transcript, independent code
review, accepted architecture, or selection of Pymthouse or
`livepeer/clearinghouse`. Statements are classified below so reported current
facts are not confused with assessments, recommendations, or unverified
expectations.

The meeting established that another session and supporting artifacts are
needed. Later repository inspection, deployment evidence, corrections from
John, and accepted decision records take precedence over this summary.

## Executive summary

The reviewed `livepeer/clearinghouse` repository is not currently a usable
Build Track baseline. It reportedly requires substantial modernization and
integration work, has no usable new-builder login path, and depends on an
outdated `go-livepeer` remote-signer integration. The surrounding architecture
combines or leaves unclear identity, API policy, discovery, invocation,
payment, metering, and charge responsibilities without a defined capability
contract.

Some pieces exist outside the clearinghouse repository:

- remote signer exposes `/discover-orchestrators`, including capability and
  basic capacity information;
- the Python gateway SDK can use remote-signer discovery and invoke a remote
  capability directly at an Orchestrator; and
- Pymthouse reportedly meters credit usage and applies a markup.

These pieces do not yet establish the complete builder journey. Storyboard
capabilities are reported as unavailable through the clearinghouse path and
tied to BYOC work, while the proposed target focuses on Live Runner and excludes
BYOC execution. Neither Pymthouse nor `livepeer/clearinghouse` was selected.

## Reported findings

| ID | Finding | Classification | Verification needed |
| --- | --- | --- | --- |
| J1 | `livepeer/clearinghouse` requires substantial work before it is usable | John/Mike assessment | Decompose gaps by component, owner, and reproducible acceptance evidence |
| J2 | A new builder cannot currently create a login | Reported current fact | Identify deployment, attempted flow, failure point, and whether API or administrative provisioning works |
| J3 | The `go-livepeer` remote-signer integration is outdated | Reported current fact | Record required and deployed revisions, incompatible endpoints or schemas, and upstream status |
| J4 | The repository path requires Auth0, OpenMeter, Kafka, and Kong integration work | Reported current gap | Separate missing implementation from configuration, deployment, documentation, and testing gaps |
| J5 | The architecture is overly complicated and not clearly defined | Assessment | Produce a component-responsibility and sequence diagram for the target journey |
| J6 | The required capability set and authoritative capability model are undefined | Reported architecture gap | Confirm capability identifiers, versions, source of truth, supported set, and owner |
| J7 | Work developed for Storyboard is not available through the clearinghouse path and is tied to BYOC | Reported current gap | Inventory concrete capabilities, adapters, execution paths, and possible Live Runner reuse |
| J8 | There is no complete builder-facing way to identify available network capabilities | Reported current gap | Compare the remote-signer API with the required catalog behavior |
| J9 | There is no capability UI, but remote signer exposes `/discover-orchestrators` | Reported current fact | Capture a sanitized response and decide whether a human UI is actually required |
| J10 | `/discover-orchestrators` includes basic capacity data | Reported current fact | Define fields, units, freshness, source, accuracy, health semantics, and failure behavior |
| J11 | The Python SDK can invoke a remote capability directly against an Orchestrator after looking up Orchestrators through remote signer | Reported current fact | Reproduce a call and capture selection, authorization, payment, error, and result behavior |
| J12 | Walletless payment is considered basic clearinghouse behavior for either Pymthouse or `livepeer/clearinghouse` | Requirement interpretation | Confirm with Rich and the architecture authorities; keep it implementation-neutral |
| J13 | Both candidate deployments require Stripe, Auth0, OpenMeter, and Kong setup for the described walletless experience | Reported implementation constraint | Determine whether each named product is mandatory, replaceable, optional, or merely a current deployment choice |
| J14 | Pymthouse meters credit usage and adds a markup fee | Reported Pymthouse behavior | Obtain a sanitized event, calculation, balance change, and builder-visible record |
| J15 | `livepeer/clearinghouse` is expected to provide comparable usage behavior, but it has not been tested | Unverified expectation | Treat as unknown until an end-to-end test or code evidence establishes it |

## Current component path described in the meeting

The reported path is:

```text
Builder
  -> Python gateway SDK
  -> remote signer /discover-orchestrators
  -> selected Orchestrator
  -> remote capability

Walletless authorization and accounting
  -> identity and API policy
  -> clearinghouse or Pymthouse
  -> remote signer
  -> payment ticket/network payment
  -> usage meter
  -> credit deduction plus optional markup
```

This is a current-state sketch, not an accepted target. It does not yet show a
stable identity joining discovery, invocation, execution, payment, usage, and
charge, nor does it identify the authoritative component for price, selection,
failure normalization, or a per-job receipt.

## Mapping to the seven builder outcomes

| Builder outcome | Status after initial meeting | Evidence or gap |
| --- | --- | --- |
| Obtain one credential | Blocked or unverified | No usable new-builder login was reported for `livepeer/clearinghouse`; Pymthouse issuance was not captured |
| Discover what the network can do | Partial | `/discover-orchestrators` reports capabilities and basic capacity, but no canonical builder catalog, schema, UI decision, or freshness contract was established |
| Understand expected price or rate | Unverified | Credit markup was discussed, but the authoritative pre-invocation rate, units, validity, and quote-to-charge relationship were not captured |
| Invoke through a standard interface | Partial | Python SDK can reportedly invoke an Orchestrator directly; target interface, Live Runner conformance, selection, retry, and failover remain unresolved |
| Receive a result or understandable failure | Unverified | No result contract or cross-component error and payment-state behavior was captured |
| Pay without holding crypto | Partial for Pymthouse; unverified for `livepeer/clearinghouse` | Pymthouse behavior was described; the repository path requires setup and testing |
| See usage and resulting charge | Partial for Pymthouse; unverified for `livepeer/clearinghouse` | Credit usage and markup were reported, but per-job receipt and network-payment reconciliation were not shown |

## Architecture implications

### Clearinghouse responsibility must be bounded

The missing capability UI or catalog should not automatically become a
clearinghouse responsibility. The target architecture must separately assign:

- identity and credential lifecycle;
- balance and payment authorization;
- capability discovery and catalog projection;
- Orchestrator selection, retry, and failover;
- invocation and result or failure behavior;
- usage metering and markup; and
- per-job charge and network-payment evidence.

The clearinghouse should own only the responsibilities deliberately assigned to
its implementation-neutral contract.

### Named services are not yet requirements

Stripe, Auth0, OpenMeter, Kafka, and Kong describe reported implementation and
deployment dependencies. The Build Track requirement should first name the
function each performs. A specific vendor or product becomes mandatory only
through an accepted architecture decision that considers replaceability,
self-hostability, operations, cost, and failure behavior.

### BYOC coupling requires a disposition

The reported Storyboard work is tied to BYOC, while BYOC is a proposed execution
non-goal. The follow-up must identify whether individual capability declarations,
runners, adapters, or interfaces can conform to Live Runner without restoring
BYOC as a Build Track deliverable.

### A missing UI is not automatically a failed outcome

The builder outcome requires discoverability, not necessarily a human-facing
capability UI. The architecture decision must identify the user and purpose of
any UI and decide whether a machine-readable API plus supported SDK is
sufficient for December acceptance.

## Decisions not made

The initial meeting did not:

- establish the code relationship between Pymthouse and
  `livepeer/clearinghouse`;
- select either clearinghouse candidate;
- approve a new clearinghouse implementation;
- define the target component architecture;
- approve Auth0, OpenMeter, Kafka, Kong, or Stripe as mandatory technologies;
- establish a required capability set;
- make BYOC part of the target scope;
- assign Cloud SPE implementation or operational ownership;
- approve a budget or delivery date; or
- demonstrate complete acceptance of either payment path.

## Follow-up questions for John

### System identity and deployment

1. Where is the Pymthouse source, and how is it related to
   `livepeer/clearinghouse`?
2. Which Pymthouse and `go-livepeer` revisions are deployed?
3. Which changes or configuration exist only in the hosted deployment?
4. Who owns code, merge approval, release, deployment, signer operations,
   support, and incident response?

### Builder account and walletless path

5. Does “cannot create a login” mean no public UI, no public API, broken Auth0
   configuration, or no supported self-service lifecycle?
6. Can an administrator provision a working account and credential today?
7. How are credits funded, checked, reserved, exhausted, refunded, and
   corrected?
8. Which components require Stripe, Auth0, OpenMeter, Kafka, and Kong? Which are
   replaceable or optional?
9. Can the full Pymthouse walletless path be reproduced without exposing
   sensitive infrastructure?

### Capability discovery and invocation

10. What exact capability, capacity, health, price, and payment fields are
    returned by `/discover-orchestrators`?
11. Where do those values originate, how fresh are they, and which component is
    authoritative?
12. Why does remote signer own discovery today, and is that intended to remain?
13. Which component filters, selects, retries, and fails over among
    Orchestrators?
14. Can the Python SDK path invoke a current Live Runner capability, or only
    BYOC or other legacy execution paths?
15. Which Storyboard capability artifacts are reusable under the Live Runner
    contract?

### Usage, charges, and network payment

16. Which identifier joins the builder, request, Orchestrator, execution,
    payment ticket, meter event, credit deduction, markup, and receipt?
17. What are Pymthouse's credit units, pricing source, markup calculation, and
    failure or partial-job charging rules?
18. Can a builder retrieve a per-job charge record and reconcile it with
    network-payment evidence?
19. What exact evidence would prove the same behavior in
    `livepeer/clearinghouse`?

### Roadmap and commitment

20. What does John recommend: repair `livepeer/clearinghouse`, upstream
    Pymthouse, operate both behind a common contract, or pursue another path?
21. Which work is committed, proposed, dependent, exploratory, or not planned?
22. What can Elite Encoder own through December, and what requires another
    team, funding source, or repository gate?
23. Which gaps must be resolved before John would consider either path ready for
    a new builder?

## Evidence requested before or during the follow-up

- Pymthouse source repository and deployed commit or release.
- Relationship map between Pymthouse and `livepeer/clearinghouse`.
- Required and deployed `go-livepeer` remote-signer revisions.
- Sanitized `/discover-orchestrators` response.
- Reproduction notes for the failed or unavailable login flow.
- Sanitized successful Pymthouse credential-to-call trace.
- Sanitized Pymthouse usage event, credit deduction, and markup calculation.
- Example per-job usage-and-charge record, if one exists.
- Functional dependency map for Stripe, Auth0, OpenMeter, Kafka, and Kong.
- Roadmap with repository, owner, dependency, target date, and commitment level.

## Recommended follow-up structure

Use another focused 60-minute session rather than continuing an unbounded
architecture discussion:

- **15 minutes:** verify repositories, revisions, deployment, and ownership;
- **30 minutes:** walk one Pymthouse call and one
  `livepeer/clearinghouse` attempt against the seven outcomes; and
- **15 minutes:** confirm roadmap commitments, missing authorities, owners, and
  follow-up dates.

Questions that cannot be answered with current evidence should be assigned to a
named verifier rather than extended into another speculative discussion.

## Decision authority

John can establish Pymthouse facts and state Elite Encoder's recommendations,
capacity, and commitments. Rich must confirm outcome and payment-path scope.
Rick and Josh must confirm cross-repository, `go-livepeer`, Live Runner, and
Operate-boundary implications. Network Engineering SPE and Cloud SPE approval
remain required before these findings constrain the final milestone plan.
