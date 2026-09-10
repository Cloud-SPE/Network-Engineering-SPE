# 21 August 2026 Build Track Alignment Transcript Extract

**Meeting:** 2.0 Alignment <> Network Engineering SPE

**Source date:** 21 August 2026

**Prepared:** 2 September 2026

**Status:** Historical evidence; not an approved decision record

**Related bead:** `netspe-vun.18`

## Scope and provenance

This document is an editorially normalized, timestamped extract of a user-
supplied meeting transcript. It preserves the portions relevant to the Cloud
SPE's participation in the Network Engineering SPE Build Track. The original
meeting continued for approximately 63 minutes and also covered the Operate,
Delegate, Validate, Explorer, protocol, subgraph, and programme-coordination
work. Those unrelated portions are not reproduced here.

The excerpts remove repetition and filler and normalize sentence boundaries
while preserving the recorded position of each speaker. They are evidence for
analysis, not exact quotations for attribution. Consult the complete source
transcript or recording before quoting a participant. Transcription artifacts
remain possible:

- “Mike Zoop” is retained as transcribed and is understood to refer to Mike
  Zupper;
- “Live Pier,” “Live Pure,” and similar forms refer to Livepeer; and
- “payment house” is retained rather than silently changing it to Pymthouse.

Use the recording or complete source transcript to resolve any disputed phrase
or nuance. Statements in a discussion are not automatically accepted
decisions. Later scope confirmations and approved decision records take
precedence.

## Participants represented in the source

- Doug Petkanics
- Rich O'Grady
- Josh Allmann, invited but not present for the quoted Build discussion
- Rick Staa, invited but not present for the quoted Build discussion
- Elliott Conway
- Mike Zupper, transcribed as Mike Zoop
- Mehrdad Sadeghi

## Build Track transcript

### 00:01:09 — open-source Agent and self-sovereign access

> **Doug Petkanics:** On the Build Track, I wanted to highlight—again, this is a
> very 2.0-centric view. I think Livepeer Agent is being developed. It is a
> network gateway, basically an access point to use the network directly through
> agentic interfaces. People can build anything they want on top of it. When the
> go-to-market team is trying to validate demand, they have to make opinionated
> and commercial decisions and actions. They have to market certain use cases
> and maybe bundle payments or credits. I think this group—the Build Track—can
> focus on making sure that the core open-source Livepeer Agent software can be
> run self-sovereign.

### 00:02:22 — local deployment, payment choices, and demand boundary

> **Doug Petkanics:** It can be deployed locally instead of just hosted. It can
> be funded with a wallet or connect through a clearinghouse, and just make sure
> it maintains that open-access Livepeer network building block that allows
> anything to be built on top. That means documenting and ensuring that the
> developer experience is good, completing the development of payment house to
> support initial product validation and some of the payment abstraction, and
> focusing on the core development there. I disagree a little bit with the
> document that frames it as having demand-generation goals in terms of
> generating different entities building demand-generation businesses on top of
> the network. I do not know if an engineering-focused Build Track is also
> responsible for generating demand and attracting entities to build on top.

### 00:03:27 — infrastructure scope rather than demand generation

> **Rich O'Grady:** It is not about building new solutions or new
> demand-generating entities. It is purely about serving what is already there.
>
> **Mike Zoop:** I think you need to strike all that demand-generation language
> out of it entirely. If it is literally self-sovereign software—make sure that
> the core network stack runs self-hosted, you run your own wallet, and you can
> integrate to a clearinghouse—that is very different messaging from what I was
> reading in the original track.
>
> **Doug Petkanics:** Yeah.

### 00:04:33 — terminology remains unresolved

> **Mike Zoop:** Those two statements make it much more clear to me what Build
> actually means.
>
> **Rich O'Grady:** Do you think Build is actually the wrong word?
>
> **Doug Petkanics:** You can call it network product if you want.
>
> **Mike Zoop:** Do not call it that. That is definitely loaded right now.
>
> **Doug Petkanics:** A lot of loaded terms here. Maybe we do not spend the time
> on terminology now and come back to it.

### 00:05:13 — clearinghouse ambiguity and separate go-to-market ownership

> **Elliott Conway:** Is the top-level goal to illustrate the open-access way for
> people to connect with the network? It seems like the payment clearinghouse
> and Agent have two different goals in mind: one to generate usage, the other
> to illustrate good connective tissue for other people to build on top of the
> open network.
>
> **Doug Petkanics:** There is a go-to-market team trying to generate demand.
> They are thinking about their own SPE proposal to do demand generation and
> marketing. They are talking to users, sharing learnings, and doing demos, and
> that is outside this track. I agree there is ambiguity as to whether payment
> house exists just for commercial support for go-to-market to generate demand,
> or whether it is a core network component that makes the self-sovereign way of
> using this easier.

### 00:06:41 — an open-access front door

> **Doug Petkanics:** There is product work to do to define that. Ultimately, we
> want to market Livepeer as awesome at media generation, editing, and inference
> through agentic-first tools. You can use Livepeer Agent or build on Livepeer
> Agent directly to do whatever you want. There has to be a project-centric,
> open-access gateway. It cannot just start by swiping a credit card with a
> commercial company focused on one use case. That cannot be the front door of
> Livepeer, even if the demand-generation effort finds that it generates demand.
>
> **Rich O'Grady:** This is infrastructure which enables demand.
>
> **Doug Petkanics:** I like that.

### 00:07:38 — Build and Operate are coupled but distinct

> **Rich O'Grady:** The question is whether to collapse a lot of the Build and
> Operate tracks into one and say it is all network infrastructure.
>
> **Doug Petkanics:** I think they are different. They work together, but they
> are different.

### 00:08:31 — wallet-funded and walletless use

> **Mike Zoop:** If you go to the Livepeer Agent GitHub, it is a place where you
> can download the software, configure it, run it, find defects, and contribute.
> This is the open-source version. You do not need a credit card. You can host it
> yourself and run it yourself. If you want to use a wallet, set up a crypto
> wallet. If you do not want a crypto wallet, payment house is a clearinghouse:
> sign up for an API key, connect the open-source software to it, and you do not
> need to deal with wallets. You can run both; you can run payment house and the
> software.
>
> **Doug Petkanics:** Exactly.

### 00:09:15 — Operate Track responsibilities

> **Doug Petkanics:** Payment house is off to the side if you do not want to deal
> with crypto wallets and funding Livepeer gateways. Everything else from the
> Agent is open-source software. Operate is about software for node operators:
> helping them adapt to new Live Runner capabilities, API pass-through jobs,
> deterministic compute jobs, adding services, pricing dynamically, and having
> metrics and transparency so nodes know which services are making money and in
> demand and in what volumes.

### 00:10:20 — ServiceRegistry concern was raised, not decided

> **Mike Zoop:** If people have to go to Discord to register a node or find
> gateways, this becomes almost impossible. I think the ServiceRegistry has to
> be put on-chain and let nodes look this stuff up dynamically. Orchestrators
> need to see where gateways are and offer the supply and features they need.
> There is service registration for Orchestrators advertising capabilities, but
> how do Orchestrators find gateways that need capabilities? Both sides need to
> be addressed.
>
> **Doug Petkanics:** Good call out.

### 00:11:32 — Agent breadth remained a vision, not a milestone

> **Doug Petkanics:** Operator is not useful because there is not diverse demand
> coming in all the time. Presumably Agent unlocks more of that diverse demand
> across hundreds of models, so the ideas in Operator are iterated to expose all
> this stuff. Josh is not here; we can take this offline. I think we agree on the
> themes.

## Later requirement and authority context

Doug left at approximately 00:27:58. The following statements therefore
describe how the remaining participants interpreted the next steps; they are
not statements by Doug.

### 00:28:57 — litepaper authorship and conceptual status

> **Rich O'Grady:** It is important because it is all coming from Doug. The
> litepaper will be singly authored by him, so what he just discussed is largely
> what is going to be in the litepaper.
>
> **Mike Zoop:** From a conversation with Doug, a forum post, or even a
> litepaper, you are still at the level of ideas and concepts. There is a lot
> that has to happen before actual requirements can be built and delivered with
> specificity.

### 00:32:46 — avoid premature commitments

> **Rich O'Grady:** I do not want us to commit to anything we are going to go
> back on. We have to balance timing and commit to milestones broad enough to
> say enough without hanging ourselves on specific details that will hurt us
> later.

### 00:40:01 — Build was expected to produce artifacts

> **Mike Zoop:** Operate and Build will produce more software, node updates, and
> software documentation. The other tracks may produce more research and
> planning initially.
>
> **Rich O'Grady:** Doing the research and ensuring we are building the right
> thing is shipping. I would rather have an instrumental interface that works
> than build a large amount that is not adopted.

### 00:43:55 — requirements require a source vision

> **Rich O'Grady:** Your role is to get clear on the milestones and report for
> milestone one: here are the requirements.
>
> **Mike Zoop:** Requirements cannot be manufactured. They have to be driven by
> a vision. If Doug's vision is vague and unclear, requirements will be vague
> and unclear.
>
> **Rich O'Grady:** I mean speaking with Doug, Josh, and Rick. Your role is to
> scratch beneath the conceptual surface and get to the real requirements.

### 00:47:25 — first milestone arc requested

> **Rich O'Grady:** The priority is to get the pre-proposal out. Ideally there
> would be a first draft of milestones. It does not need to be perfect; there
> needs to be an arc from milestone one to three or four.

### 00:52:27 — combined funding was not a Build allocation

> **Rich O'Grady:** There will be a separate protocol-focused 2.0 SPE and an
> Agent SPE or iteration that sits on top. We can reallocate budget and dip into
> the 30,000 combined fund.

## Evidence interpretation

The transcript supports these historical statements:

- Build enables demand but does not own demand generation.
- Doug's August vision placed the open-source Agent at the center of the
  self-sovereign builder experience.
- Both wallet-funded and clearinghouse-backed access were contemplated.
- The role of payment house as commercial support versus core infrastructure
  was explicitly unresolved.
- Build and Operate were intended to be distinct but coupled.
- ServiceRegistry problems were raised, but no on-chain schema was approved.
- The 30,000 combined fund was not established as a Cloud SPE or Build budget.

The transcript does not approve the current Live Runner focus, select a
clearinghouse implementation, define the seven builder outcomes, approve a
capability count, assign repositories, or establish final milestone acceptance.
