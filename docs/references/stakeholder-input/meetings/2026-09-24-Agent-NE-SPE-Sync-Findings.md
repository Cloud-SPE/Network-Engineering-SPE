# Agent–Network Engineering SPE Sync Findings

**Meeting date:** 24 September 2026**Prepared:** 25 September 2026**Status:** Conceptual alignment evidence; not an accepted architecture or delivery contract**Participants represented:** Mike Zupper, Rich O'Grady, Steph Alinsug, Rick Staa, Emran Mahbub, Qiang Han, peace node, and a phone participant addressed as Josh

## Source and limits

This synthesis uses the [Mike-supplied transcript](09-24-2026-Livepeer-Inc-Agent-Team-NE-SPE-sync-meeting.txt).
Automated transcription contains errors in names and technical terms; the phone
speaker is identified as Josh from the dialogue. Reported implementation and
source-access offers are not independently verified. Mike's subsequent repository
identification below is dated separately from the meeting.

## Conceptual alignment

| Discussion | Evidence | Implication |
| --- | --- | --- |
| Common capability descriptions, prices and invocation | Peace restates these common patterns at 14:59–16:09; Josh supports the wholesale/retail distinction at 20:10–21:41 | The shared foundation should support different products; exact schemas and the common subset still need agreement. |
| Reusable software versus a hosted commercial product | Emran proposes a router-like API at 31:25; Mike explains reusable packages/services at 33:28, and Emran acknowledges the distinction at 34:37 | The builder engine supplies common behavior; enterprises own their public products and retail business models. |
| SDK-backed HTTP and MCP interfaces | Qiang asks about SDK placement at 38:28–39:52; Mike describes the two interfaces at 41:07–42:27 | The proposed shared layer reuses network primitives through the SDK. Interface contracts are not finalized in the meeting. |
| Concrete source handoff | Qiang offers capability-schema work and the private SDK REST wrapper at 48:44–51:52; Rich recaps access at 53:48 and 1:00:19 | Review the existing implementation before fixing shared contracts. An access offer does not establish delivery, reuse permission or a public release. |
| Inc product independence | Rich's opening and Rick at 52:52–53:48 emphasize avoiding delays to Inc's product work | Convergence should minimize duplication without making Inc wait for the shared engine or committing it to a migration date. |

## Payment operation and Console clarification

At 35:28–46:24, Mike describes both self-operated payment infrastructure and a
hosted walletless route. Josh asks who runs and pays for the service. Mike raises
Inc and possibly Cloud SPE operation as options; no funded operator or ongoing
support commitment is assigned.

At 54:50–55:52, Inc participants state that their current Agent effort uses
Batteries and distinguish it from the earlier PymtHouse-dependent Console
prototype. This corrects the assumption made during the discussion, but is not
code or deployment verification. At 57:39–59:22, Console is discussed as a useful
reference experience. Retrofitting it versus building a new example remains a
separate implementation choice.

## Review outcome

At 1:00:19, architecture circulation and stakeholder review are the next step.
The call records support for the concept and specific source offers; it does not
finalize interface contracts, funding, long-term maintenance, upstream work,
Inc adoption, final milestones or SPE acceptance.

The [current proposal](../../../design-docs/self-sovereign-open-builder-stack-draft.md)
incorporates the direction and Mike's later refinements. It proposes an engine
and reference application that demonstrate enterprise extensions without core
changes, while retaining separate software and service-operation responsibilities.

## Subsequent clarification: 25 September

Mike identified `livepeer/simple-infra` as Qiang's currently closed-source Inc
repository and said Qiang will provide him access. Access and inspection remain
pending. The schema and SDK wrapper discussed in the meeting are candidates for
review there, not inspected implementation evidence. Permission to redistribute
code in the open-source engine must be established separately; the delivered
engine must build and run independently of the private repository.
