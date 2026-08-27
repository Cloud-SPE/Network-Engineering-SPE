# Build Track Architecture Survey Instructions

**Audience:** Survey respondents

**Expected completion time:** 10–15 minutes

**Survey version:** `{SURVEY_VERSION}`

## Why you are receiving this

This survey prepares a focused architecture discussion about the Network
Engineering SPE Build Track and the Cloud SPE's portion of it. The goal is to
identify agreements, conflicting assumptions, missing facts, missing
components, ownership gaps, and decisions that require additional authority
before the architecture workshops.

The survey is diagnostic. It is not a vote, approval, requirements document,
or substitute for architecture review. “Unknown” is a useful answer and is
preferred to guessing.

## What to return

Return one completed copy of the
[survey template](Build-Track-Architecture-Survey-Template.md) through the
private channel named in the invitation. Use this filename:

```text
Build-Track-Architecture-Survey-Response-{Your-Name}-{YYYY-MM-DD}.md
```

Do not edit the administrator's original template. Copy it first, fill in the
respondent information, preserve the original questions and answer choices,
and review the entire completed file before returning it.

## Scope context

Answer based on the intended December 2026 architecture, while clearly
distinguishing it from current implementation facts.

- Live Runner is the proposed execution focus.
- The working support model is a reusable Live Runner service contract proven
  through at least one representative capability, rather than a predetermined
  multi-capability list. Rich, Rick, and Josh must confirm that direction.
- Batch AI, BYOC, LV2V, and transcoding are proposed execution non-goals.
- Demand generation and application adoption are not Build Track requirements.
- Sample or reference applications may demonstrate supported interfaces, but
  they create no application-count, production-demand, traffic, funding, or
  ongoing-operation requirement.
- The working assumption is that both wallet-funded and walletless payment
  journeys are in the December target. Rich's confirmation is still required,
  and the survey asks about scope and ownership rather than treating that
  assumption as approved.
- Walletless payment is an outcome, not a commitment to hosted Pymthouse or any
  other clearinghouse implementation.
- Agent 2.0/Storyboard, SDKs, gateways, identity, ServiceRegistry contracts,
  discovery, clearinghouse and signer services, pricing, errors, metering,
  usage, and charges may still be relevant supporting components.

## How to answer

For each question:

1. Select or write your answer.
2. Classify it as a **current fact**, **target recommendation**, or **unknown**.
3. Give your confidence as **high**, **medium**, or **low**.
4. Name the basis or source when known.
5. Name a better-positioned owner, approver, or follow-up when applicable.

Use these classifications consistently:

| Classification | Meaning |
| --- | --- |
| Current fact | You believe this accurately describes verified code, deployment, ownership, or an accepted decision |
| Target recommendation | You recommend this end state, but it is not yet an accepted decision |
| Unknown | You cannot answer responsibly from available evidence or authority |

Do not convert a preference into a current fact. Technical expertise does not
automatically imply programme, budget, repository, or deployment authority.

## Using an agent as interviewer

You may use an AI agent to walk through the survey one question at a time and
write your answers into the Markdown template. Paste the following prompt into
the agent together with your copy of the template:

```text
Walk me through this Build Track architecture survey one question at a time.

Rules:
- Preserve every original question, answer option, section, and table.
- Do not answer for me, infer my position, or steer me toward an option.
- Explain terminology only when I ask.
- When explaining, distinguish cited source facts from your interpretation.
- Record my selected answer in the existing Markdown answer area.
- For each answer, record whether it is a current fact, target recommendation,
  or unknown; my confidence; the basis or source; and any required owner or
  follow-up.
- Use “Unknown” rather than guessing.
- If my answer combines a fact and recommendation, record them separately.
- Do not add new Build Track requirements or reopen fixed scope decisions.
- Do not include credentials, tokens, private keys, private contact data, or
  security-sensitive operational details.
- Keep the interview within 10–15 minutes. Park lengthy issues as follow-up.
- At the end, show me the complete Markdown and ask me to review and confirm it.
```

The agent is a recorder and explainer, not the respondent. You remain
responsible for every submitted answer. Correct any wording that does not
accurately represent your view before confirming the file.

## Before submitting

Confirm that:

- your name, role, date, and survey version are present;
- every required question is answered or explicitly marked unknown;
- facts and recommendations are distinguishable;
- confidence and basis are included where requested;
- referrals name the relevant person, team, repository, or decision;
- no sensitive information is included;
- the agent did not alter or omit questions; and
- the respondent confirmation at the end is completed by you.

Individual responses will be handled privately unless publication is approved.
A normalized synthesis—not a vote count—will be used to prepare Workshop Part
1.
