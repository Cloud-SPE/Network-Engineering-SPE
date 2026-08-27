# Build Track Architecture Survey Administration

**Status:** Internal working guide

**Prepared:** 27 August 2026

**Owner:** Mike Zupper

**Execution bead:** `netspe-vun.9`

## Purpose

This document is the survey administrator's guide for collecting and
synthesizing the Build Track architecture pre-work. It is not intended to be
sent to respondents. The respondent-facing package consists of:

- [survey instructions](Build-Track-Architecture-Survey-Instructions.md); and
- [fillable survey template](Build-Track-Architecture-Survey-Template.md).

The survey is diagnostic. It should expose agreements, conflicting
assumptions, missing facts, missing components, and decision-authority gaps
before Workshop Part 1. It is not a vote, approval process, requirements
document, or substitute for architecture review.

## Fixed survey boundaries

The survey and its synthesis must preserve these established boundaries:

- Live Runner is the proposed execution focus.
- The proposed support model is a reusable Live Runner service contract proven
  end to end with at least one representative capability. It does not assume a
  larger named capability list. Rich, Rick, and Josh must all confirm this
  interpretation before it constrains the milestones.
- Batch AI, BYOC, LV2V, and transcoding are proposed execution non-goals.
- Demand generation and application adoption are not Build Track requirements.
- Sample or reference applications may illustrate supported interfaces or
  provide controlled validation, but they create no application-count,
  production-demand, traffic, funding, or ongoing-operation commitment.
- Both wallet-funded and walletless payment journeys are assumed to be in the
  December target based on the upstream outcomes. This is a working assumption
  pending confirmation from Rich, not an accepted scope or ownership decision.
- “Walletless” describes a builder outcome, not a predetermined implementation.
  Hosted Pymthouse, `livepeer/clearinghouse`, both behind a common contract, or
  another justified design remain candidates until the architecture decision.
- The repository covers only the Cloud SPE's portion of the wider Network
  Engineering SPE.

The survey may reveal an objection to a proposed architecture boundary, but a
survey response does not itself change an approved scope decision.

## Respondents

Required initial respondents:

- Mike Zupper;
- Rick Staa; and
- Josh Allmann.

Potential additional respondents:

- John Mull for hosted Pymthouse;
- the Agent 2.0/Storyboard technical owner;
- the SDK Service owner;
- `livepeer/clearinghouse` maintainers; and
- repository or deployment owners identified by Rick or Josh.

Subject-matter experts may establish facts and feasibility. Their responses do
not automatically establish programme approval, Cloud SPE approval, repository
approval, or architecture acceptance.

## Package preparation

Before distribution:

1. Review the instructions and template against the latest scope decisions.
2. Replace `{SURVEY_VERSION}` in both shareable files with the same identifier,
   preferably the commit hash or a date-based version.
3. Confirm that all pre-read links resolve for every respondent.
4. Make one clean copy of the template per respondent.
5. Give each copy a unique filename without changing the questions.
6. Set a response deadline at least two business days before Workshop Part 1.
7. Decide the private return channel and state it in the distribution message.
8. Complete a timed pilot using the same agent-assisted process.

Recommended response filenames:

```text
Build-Track-Architecture-Survey-Response-{Name}-{YYYY-MM-DD}.md
```

Do not ask multiple respondents to edit the same file. Separate files preserve
individual positions and avoid merge conflicts or accidental consensus.

## Suggested distribution message

**Subject:** Pre-work: Build Track outcomes and Live Runner architecture survey

> We are preparing a two-part discussion to translate the Network Engineering
> SPE Build Track outcomes into an end-state architecture and reviewable
> September–December milestones.
>
> Please read the attached survey instructions, make your own copy of the
> survey template, and use an agent to walk through the questions one at a
> time. Review the completed Markdown yourself and return it through the named
> private channel by `{DEADLINE}`. Expected completion time is 10–15 minutes.
>
> The survey is diagnostic, not a vote or approval. “Unknown” is a useful
> answer. Please distinguish current facts from target recommendations and name
> the source or better-positioned owner when possible.

Include the two respondent-facing files and links to:

- [the architecture-alignment process](Build-Track-Architecture-Alignment-Process.md);
- [the current-state diagram](Build-Track-Repo-Traceability.md#component-diagram);
- [the seven builder outcomes](Build-Track-Outcome-and-High-Level-Concepts.md#builder-promise);
  and
- [the draft milestone proposal](../design-docs/cloud-spe-september-december-2026-milestones-draft.md).

Use a separate scheduling poll. Combining architecture and availability makes
the survey harder to complete within 10–15 minutes and complicates synthesis.

## Collection rules

- Accept only one reviewed response file per respondent.
- Preserve the respondent's wording; do not silently normalize it during
  collection.
- Record the survey version and return date.
- Ask the respondent to resolve blank required fields or confirm that they are
  intentionally unknown.
- Do not treat an agent-generated answer as the respondent's position unless
  the respondent has explicitly reviewed and confirmed the final file.
- Do not collect credentials, tokens, private keys, private contact data,
  security-sensitive operational details, or confidential repository data.
- Store raw responses privately unless each respondent approves publication.
- Commit only a sanitized synthesis or explicitly approved response files to
  this public repository.

## Response tracking

Work status belongs in Beads. Use `netspe-vun.9` for distribution, collection,
synthesis, missing responses, and handoff to Workshop Part 1. Do not maintain a
competing Markdown checklist of live response status.

The response set is sufficient when the required respondents have answered or
their absence and its impact are explicitly recorded in Beads.

## Synthesis method

For every question, separate the response into current fact, target
recommendation, unknown, and authority. Classify the combined result as:

| Result | Interpretation | Workshop Part 1 treatment |
| --- | --- | --- |
| Aligned fact | Respondents agree and an authoritative source is available | Confirm briefly and cite the source |
| Aligned preference | Respondents prefer the same target but it is not approved | Present as a proposal requiring authority |
| Divergent architecture | Respondents select materially different target designs | Prepare alternatives and allocate discussion time |
| Factual uncertainty | Respondents disagree about current code, deployment, or ownership | Assign verification or specialist follow-up |
| Authority gap | No respondent can approve the required decision | Identify and invite or escalate to the authority |
| Low-confidence area | Most confidence responses are low or unknown | Prioritize evidence and avoid treating it as settled |

Do not report plurality as consensus. Preserve meaningful minority objections.
Give greater evidentiary weight to an answer from the verified owner of a
repository or deployment, but do not treat technical ownership as programme
approval.

## Survey synthesis template

### Response coverage

| Invited role | Response received | Authority represented | Important limitation |
| --- | --- | --- | --- |
| Build Track/Cloud SPE |  |  |  |
| Foundation technical gate |  |  |  |
| Livepeer Inc/Live Runner architecture |  |  |  |
| Clearinghouse specialist |  |  |  |
| Agent 2.0 specialist |  |  |  |

### Agreements and disagreements

| Topic | Current fact | Preferred target | Confidence | Disagreement or unknown | Part 1 treatment |
| --- | --- | --- | --- | --- | --- |
| Live Runner scope |  |  |  |  |  |
| Live Runner capability support model |  |  |  |  |  |
| Builder-facing interface |  |  |  |  |  |
| Agent 2.0 role |  |  |  |  |  |
| Gateway and SDK Service |  |  |  |  |  |
| On-chain ServiceRegistry |  |  |  |  |  |
| Runtime discovery |  |  |  |  |  |
| Clearinghouse relationship |  |  |  |  |  |
| Clearinghouse direction |  |  |  |  |  |
| Payment-path scope and walletless definition of done |  |  |  |  |  |

### Outcome ownership

| Builder outcome | Candidate authoritative component | Conflicting answer | Missing owner | Part 1 question |
| --- | --- | --- | --- | --- |
| One credential |  |  |  |  |
| Discover |  |  |  |  |
| Price |  |  |  |  |
| Invoke |  |  |  |  |
| Result or failure |  |  |  |  |
| Walletless payment |  |  |  |  |
| Usage and charge |  |  |  |  |

### Decisions and follow-ups

| Finding | Classification | Required owner or authority | Workshop treatment or specialist session |
| --- | --- | --- | --- |
|  |  |  |  |

## Completion evidence

Survey administration is ready for Workshop Part 1 when:

- required respondents have answered or their absence is documented;
- every response identifies the survey version and respondent confirmation;
- responses are preserved privately and a sanitized synthesis is available;
- facts, recommendations, unknowns, confidence, and decision authority are
  separated;
- all seven builder outcomes are represented;
- the highest-impact disagreements are selected for Workshop Part 1;
- missing specialists or approvers are named;
- the synthesis preserves the demand-generation and application-adoption
  exclusion; and
- the synthesis is distributed with the final Workshop Part 1 agenda.
