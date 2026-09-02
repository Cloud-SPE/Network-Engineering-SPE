# Doug Build Track Feedback Discussion Guide

**Status:** Draft facilitator guide

**Prepared:** 2 September 2026

**Duration:** 60 minutes

**Agenda blocks:** 15 minutes, 30 minutes, and 15 minutes

**Facilitator:** Mike Zupper

**Execution bead:** `netspe-vun.18`

## Meeting objective

Confirm what remains valid from Doug Petkanics's 21 August Build Track vision,
identify what has changed, and translate the remaining strategic language into
architecture, scope, ownership, evidence, and decision-authority inputs. This
meeting gathers authoritative context; it does not by itself approve the Cloud
SPE milestones or wider Network Engineering SPE architecture.

## Required pre-read

- [21 August transcript extract](2026-08-21-Build-Track-Alignment-Transcript-Extract.md)
- [Seven builder outcomes](Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise)
- [Current-state component diagram](Build-Track-Repo-Traceability.md#component-diagram)
- [Draft September–December milestones](../design-docs/cloud-spe-september-december-2026-milestones-draft.md)
- [Josh's survey response](Build-Track-Architecture-Survey-Response-Josh-2026-08-31.md)

## Starting evidence, not assumed decisions

| August statement | Current treatment |
| --- | --- |
| Build provides open-source, self-sovereign infrastructure | Directional intent requiring testable acceptance boundaries |
| Build enables demand but does not generate it | Resolved scope: no application-adoption, traffic, or demand-generation requirement |
| Open-source Agent is the network gateway/front door | Historical position requiring confirmation against the newer platform-contract direction |
| Builders may fund a gateway wallet or use a clearinghouse | Working assumption that both paths are in play; ownership and acceptance remain unresolved |
| Complete “payment house” | Candidate work, not an accepted Pymthouse or `livepeer/clearinghouse` selection |
| Build and Operate are different but work together | Directional boundary; discovery, routing, registration, pricing, and metrics still need owners |
| ServiceRegistry should address manual discovery | Problem statement only; no accepted on-chain data model |
| Agent could expose hundreds of models | Product vision, not an application count or December capability commitment |

## Block 1 — confirm intent and changes since 21 August

**Duration:** 15 minutes

### Objective

Establish which August statements remain current before discussing components.

### Priority questions

1. Does the August definition still stand: Build delivers open-source,
   self-sovereign infrastructure and has no demand-generation or application-
   adoption responsibility?
2. What does “self-sovereign” require in observable terms? Which mandatory
   components must be open source, locally deployable, and independently
   operable?
3. Are optional Foundation-, Cloud-, or commercial-hosted conveniences
   compatible with that definition, and what must remain usable without them?
4. Since August, has the intended front door changed from the open-source Agent
   product to supported SDK/API surfaces over a canonical platform contract?
5. Which August assumptions have changed because of the litepaper, Live Runner
   work, repository evolution, or later discussions with Rich, Rick, and Josh?

### Exit evidence

- current intent separated from superseded August language;
- a testable self-sovereignty direction; and
- any disagreement with the resolved demand/adoption exclusion recorded as an
  escalation rather than silently reopened.

## Block 2 — resolve architecture implications

**Duration:** 30 minutes

### Agent and builder-facing contract

1. Is Agent 2.0 the canonical gateway, a supported client, a reference
   integration, a source of reusable runners/adapters, or outside the target?
2. Which Agent-originated artifacts should survive independently of the Agent
   product, and what must be decoupled from product-specific infrastructure?
3. Should SDKs and hosted APIs expose one capability-agnostic platform contract?

### Live Runner and capability scope

4. Is Live Runner the intended September–December execution focus?
5. Should December prove a reusable contract with one representative
   capability, require a named capability set, or deliver another scope?
6. Does every capability called “supported” have to satisfy the complete
   credential, discovery, price, invocation, result/failure, payment, usage,
   and charge journey?

### Payment and clearinghouse

7. Are wallet-funded and walletless journeys both required acceptance paths,
   or is either an externally owned compatibility obligation?
8. When Doug said “complete payment house,” did that mean John's hosted
   Pymthouse, a self-hostable implementation, an implementation-neutral
   clearinghouse contract, or simply a working walletless outcome?
9. Should both paths converge after authorization on the same invocation, job,
   result, error, usage, and charge interfaces?

### Build and Operate boundary

10. Which track and repository own Live Runner registration, Orchestrator and
    gateway enumeration, capability discovery, selection, retry, failover,
    current pricing, capacity, health, and builder-facing catalog projection?
11. What must be durable in the on-chain ServiceRegistry, and what must remain
    dynamic? What self-sovereignty property justifies each on-chain field?
12. Where does the Cloud SPE's delivery responsibility end, and which named
    external owner accepts each handoff?

### Exit evidence

- a preferred architecture direction or explicit alternatives;
- unresolved factual questions assigned to specialists;
- no application-count or demand obligation introduced through capability
  language; and
- Pymthouse kept distinct from the generic walletless requirement until the
  John Mull evidence review is complete.

## Block 3 — milestone and authority confirmation

**Duration:** 15 minutes

### Priority questions

1. Do the seven builder outcomes accurately express the intended open-access
   experience? Which is missing, overstated, or externally owned?
2. Does the proposed four-milestone arc reflect the desired sequencing from
   architecture and ownership through an independently reproducible journey?
3. What exact evidence must Milestone 1 produce before implementation and
   funding commitments are responsible?
4. Which statements are Doug's strategic guidance, which are stable litepaper
   intent, and which can Doug authorize as decisions?
5. Which decisions require Rich, Rick, Josh, John Mull, Network Engineering
   SPE, Cloud SPE, DAO, repository owners, or deployment owners?
6. Is any amount from the previously discussed 30,000 combined fund allocated
   to Build or Cloud SPE work? If so, who controls it and for which outcomes?
7. For every unresolved item, who owns the answer and by what date?

## Decision-capture table

| Topic | Statement | Classification | Authority | Evidence/source | Owner and date |
| --- | --- | --- | --- | --- | --- |
| Demand/adoption boundary |  |  |  |  |  |
| Self-sovereignty definition |  |  |  |  |  |
| Agent role |  |  |  |  |  |
| Live Runner focus |  |  |  |  |  |
| Capability support model |  |  |  |  |  |
| Payment-path scope |  |  |  |  |  |
| Clearinghouse requirement |  |  |  |  |  |
| Build/Operate boundary |  |  |  |  |  |
| ServiceRegistry boundary |  |  |  |  |  |
| Milestone arc |  |  |  |  |  |
| Budget |  |  |  |  |  |

Use only these classifications:

- **confirmed fact** — verified current behavior or historical statement;
- **working assumption** — temporarily usable with an owner and review date;
- **target recommendation** — preferred direction without approval;
- **accepted decision** — approved by a named authority;
- **unknown** — evidence or authority is missing; or
- **out of Cloud SPE scope** — relevant context owned elsewhere.

## Parking lot

Do not consume the one-hour discussion with implementation detail unless it
changes the architecture. Park:

- credential expiry, rotation, and revocation mechanics;
- quote units, validity windows, and reconciliation formulas;
- retry, timeout, cancellation, and idempotency details;
- balance reservation, top-up, refund, and correction mechanics;
- per-job receipt field definitions;
- deployment topology and exact repository revisions for the John Mull session;
  and
- detailed budget estimates before owners and scope are confirmed.

## Required meeting output

Within one business day, produce a dated record that:

- links each conclusion to the transcript, current evidence, or Doug's new
  statement;
- separates historical fact, current recommendation, decision, and unknown;
- identifies changes since 21 August;
- names the authority for every accepted decision;
- records owners and dates for all follow-ups;
- feeds relevant evidence into `netspe-vun.9` and `netspe-vun.12`; and
- does not treat Doug's feedback alone as joint SPE approval.
