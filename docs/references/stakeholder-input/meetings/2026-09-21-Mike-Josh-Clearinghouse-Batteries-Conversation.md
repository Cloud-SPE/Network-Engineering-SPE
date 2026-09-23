# Mike–Josh Clearinghouse Batteries Conversation

**Conversation date:** 21 September 2026\
**Recorded:** 22 September 2026\
**Participants:** Mike Zupper (`Mike Zoop`) and Josh Allmann (`j0sh`, speaking about Livepeer Inc's direction)\
**Status:** Participant-supplied conversation and evidence-qualified synthesis; not an approved architecture or verified implementation baseline\
**Execution bead:** `netspe-vun.26`

## Provenance and limits

Mike supplied the conversation below and requested its preservation. Message
text, speaker labels, timestamps, spelling, and mentions are retained; Markdown
blockquotes and headings are editorial formatting. Times are as supplied; the
source timezone, channel, message permalinks, and completeness of the surrounding
thread are not established. Rick and Mehrdad are mentioned, but no statements
from them are included.

The repository Josh linked is
[`livepeer/clearinghouse-batteries`](https://github.com/livepeer/clearinghouse-batteries).
This capture does not inspect its code, commit, license, deployment, or current
behavior. Technical statements below are attributed to this conversation and
must be verified against a named revision before becoming an implementation
baseline. Josh's stated Inc commitment and offer of hosting are preserved as
statements, not converted into a funded delivery agreement or service guarantee.

This is distinct from the earlier
[Payments Clearinghouse Notion proposal capture](../../source-material/2026-09-21-Josh-Payments-Clearinghouse-Reference.md).
The relationship among that proposal, `clearinghouse-batteries`,
`livepeer/clearinghouse`, and Pymthouse is not established by this conversation.

## Findings and their status

| Finding | Evidence and classification |
| --- | --- |
| Inc direction | At 11:13 AM Josh calls the repository WIP intended for Agent billing. At 7:16 PM he states that Inc is committed to building on it and supporting it for the foreseeable future. **Stated commitment**, with no release date, support terms, or deployed revision supplied. |
| Packaging | Josh describes a batteries-included clearinghouse plus the `go-livepeer` remote signer, reducing the number of components an operator must assemble and monitor. At 8:30 PM he describes reasonable self-containment as the goal. **Reported design and work in progress**, not verified deployment evidence. |
| Payment boundary | Josh describes basic accounting, limits, and network-payment facilitation as the clearinghouse's scope. He explicitly avoids ownership of application user databases, application auth, usage tracking, and the complete application stack. **Stated design intent**; this does not mean the clearinghouse has no credential or authorization functionality. |
| Credential choice | Josh says an application can issue and register a credential with the clearinghouse, or the clearinghouse can create one. **Reported capability**; a universal credential across all services is not promised. |
| Network cost versus customer billing | Josh says ticket expected value (EV) is tracked; winning-ticket settlement aggregates value and should not drive user-level accounting. Network-payment events can support correlation and reconciliation, while application billing may differ from network cost. **Reported accounting model**, not a verified reconciliation algorithm or a guarantee of exact per-job on-chain settlement. |
| Discovery and prices | Josh says discovery already exists in the remote signer, including prices and rates, and can be exposed by the clearinghouse. He suggests a more user-friendly console experience. **Reported capability and UI suggestion**, not an accepted expansion of the payment core. |
| Hosted access | Josh offers to stand up something to support the builder experience and pressure-test ecosystem needs. **Offer requiring a concrete agreement** about coverage, operator, funding, access, support, and dates. It is not a commitment to deliver all seven outcomes as one complete product. |
| Intended users | Josh argues that operating payment infrastructure is niche and that most application builders should be able to delegate it to a signer service. Mike emphasizes both ready access and optional self-operation with documentation and tooling. **Stakeholder positions**; the emphasis and responsibility split remain to be reconciled. |
| Ecosystem comparison | Mike states an intention to work with John in October and compare Pymthouse with BlueClaw and Flipsuite needs. Josh invites those requirements and offers to align. **Mike's stated plan and Josh's collaboration offer**; John and those projects do not make commitments in this excerpt. |

## Implications for the seven builder outcomes

| Outcome | What the conversation establishes | What remains open |
| --- | --- | --- |
| 1. Obtain one credential | Josh agrees with the proposed coverage and describes application-issued/registered or clearinghouse-created credentials. | Issuer and onboarding experience for the supported builder journey; cross-component authorization contract. |
| 2. Discover what the network can do | Josh says the remote signer provides discovery and the clearinghouse can expose it. | Verified discovery behavior, catalog contract, supported capabilities, and builder-facing presentation. |
| 3. Understand expected price or rate | Josh says signer discovery includes prices and rates. | Units, validity, completeness, markup, and how network rates map to the builder's expected charge. |
| 4. Invoke through a standard interface | Mike asks whether this is the Python SDK. | Josh does not explicitly confirm that assignment in the supplied exchange; interface and owner remain unconfirmed. |
| 5. Receive a result or understandable failure | Mike also suggests the Python SDK for this outcome. | No explicit confirmation or error contract is supplied. |
| 6. Pay without holding crypto | Josh agrees that the clearinghouse addresses this outcome. | Reproducible onboarding, funding, authorization, limits, and end-to-end payment evidence. |
| 7. See usage and resulting charge | Josh agrees with partial coverage: network-payment records and EV-based accounting can help correlate app usage and reconcile cost. | Application usage semantics, customer billing, markup, receipts, and correlation evidence across the complete journey. |

## Architecture relevance

This exchange supports evaluating `clearinghouse-batteries` as a candidate for
the payment/accounting core in Mike's proposal. It does not select that
repository or establish that Inc and Elite Encoder will adopt one common core.

A coherent, independently deployable builder stack can compose separate
components; it need not make the clearinghouse own the entire application data
model. Josh's signer-discovery claim can be evaluated as an integration surface
while preserving Mike's selected payment/accounting core boundary. The main
unresolved distinction is the complete builder experience versus the narrower
role of a payment-infrastructure operator.

Mike's statement that the outcomes reflect the Network Engineering SPE and
Doug's self-sovereign direction is preserved as his explanation, not independent
proof of formal approval. Existing scope and approval boundaries still apply;
BlueClaw and Flipsuite needs are architecture inputs, not new Cloud SPE adoption
or application-delivery obligations. Work state and follow-up evidence belong
in `netspe-vun.10`, `netspe-vun.11`, and `netspe-vun.19`.

## Supplied conversation

### j0sh — 11:13 AM

> This is what the agent will be using for billing - WIP
> https://github.com/livepeer/clearinghouse-batteries
>
> It's a "batteries included" version of the clearinghouse so anyone who is interested in operating payment infrastructure can start with just this and the go-livepeer remote signer, rather than having to assemble and monitor half a dozen components.
>
> Still some work to do yet but that's the gist of it.
>
> @Mike Zoop @Rick (OOO) @Mehrdad
> fwiw, I believe that "operating payments infrastructure" is always going to be a relatively niche activity so it probably should not be a primary focus of the builder track, although we can certainly work to make that more accessible for folks who are truly interested in contributing that way.
>
> Smooth network access for builders, including ready access to payment methods, is more important rather than expecting folks to DIY payments on top of building their own Livepeer-powered apps.

### Mike Zoop — 12:03 PM

> I will take a look at this. John and I are going to work this part of the build track in October

### Mike Zoop — 7:16 PM

> is this the approach that Inc is moving towards?

### j0sh — 7:16 PM

> yes - we are committed to building on top of it and supporting it for the foreseeable future.

### Mike Zoop — 7:23 PM

> I plan to compare this against what pymnthouse does and other gateways like BlueClaw and Flipsuite need.  Hopefully they align and share similar patterns

### j0sh — 7:30 PM

> Let me know what BlueClaw and Flipsuite might need, I think we can figure out how to align needs.
>
> FWIW, for general apps like those, it might be nice to not have to worry about network payments infrastructure. The goal is to do only what is needed to facilitate network payments (basic accounting, limits, etc) and step out of the way. The clearinghouse is not trying to own the whole stack, your user database, auth, usage tracking, etc; those are app-level concerns, not network-payment concerns.

### Mike Zoop — 7:49 PM

> The "Outcomes" needed by the build track are
>
> 1. Obtain one credential.
> 2. Discover what the network can do.
> 3. Understand the expected price or rate.
> 4. Invoke a capability through a standard interface.
> 5. Receive a result or understandable failure.
> 6. Pay without holding crypto.
> 7. See their usage and resulting charge.
>
> I see the clearinghouse-batteries would solve 1,6 and partially 7? would you agree?

### j0sh — 7:56 PM

> Correct.
>
> Although the "credential" is also up to you.
>
> It can be a credential that you issue and register with the clearinghouse, or the clearinghouse can create one for you.
>
> Also #7 "see their usage" is also going to be quite app-specific and I'm trying to avoid the clearinghouse grow tentacles around other parts of app logic because what gets charged for a certain app might not always apply 1:1 to network payments. The clearinghouse's only job is to facilitate network payments. But you should be able to correlate app usage to network payment events.
>
> Eg, usage tracking / observability is a huge part of the agent and they are doing that on their own, as they should. Clearinghouse data can certainly be helpful as a matter of reconcilation though.
> But you can certainly look at clearinghouse data and say "this user made a text-to-image call against that orchestrator at &lt;timestamp&gt; and that cost $0.05"
>
> whether that $0.05 network cost gets mapped 1:1 to how the user is billed is ultimately up to the app

### Mike Zoop — 8:00 PM

> "Network Payments"  means "how many probabilistic micro payment tickets sent to an orchestrator for the given job"  NOT the acutal fees paid for the work, corredt?

### j0sh — 8:03 PM

> It does work out to actual fees at the end, roughly - since each ticket has an EV and we track that.
>
> When work "settles" via a winning ticket it's a higher face value that blends many tickets. But that settlement doesn't / shouldn't impact user-level accounting

### Mike Zoop — 8:04 PM

> so where does 2,3,4,5 come into play? is that app specific too?
>
> i assume 4,5 are Python SDK?

### j0sh — 8:08 PM

> (2) can be provided by the clearinghouse too as a discovery service; it's already built into the remote signer. That of course also has (3) prices and rates etc as part of that.
>
> But for something a little more user-friendly I think you might want something more akin to the livepeer console UI concept that was floating around a while ago ... that link does not seem to be working anymore tho, so not sure what happened to it.
>
> That can also be the mechanism from which users obtain a credential, etc.

### Mike Zoop — 8:10 PM

> is it accurate to say that Inc will NOT be providing those features in a unified solution?

### Mike Zoop — 8:13 PM

> yeah these one-off PoC sites are probably not what is needed for the build track outomes. There will need to be something that does the entire 1-7 in a unified software stack. Something that can be hosted by individuals or enterprises can use but provide a paid wrapper around it (BlueClaw/Flipsuite or even Livepeer inc)

### j0sh — 8:16 PM

> We actually can. Inc is mostly looking to support the agent but I'm happy to stand up something for this, so you can focus on a good builder experience without having to fiddle around with network payments.
>
> It'd also be a good pressure test to make sure this can work with whatever else the ecosystem needs.
>
> Although TBH I'm not sure what your end goal is. Is it to provide documentation, etc help people run their own payments infrastructure?
>
> Or is the idea more to have pre-existing service that builders can depend on, eg, get an API key and go?

### Mike Zoop — 8:18 PM

> These are not my goals. they are the goals of this Network Engineering SPE. Based on Doug's idea of "Self Sovereign" software stack.
> part of that means running infrastructure to hide the details of the Livepeer payments complexities from app builders.
> But also providing the documenation and tooling to make running the payment infra easy (if they builder so chooses)

### j0sh — 8:20 PM

> As far as network payments goes goes, we do not want to impose a singular data model from the clearinghouse for their entire app.
>
> Most folks building apps will have their own way of doing things. The more that things become a monolithic all-in-one architecture just to support Livepeer, the harder that becomes to reconcile.
> And again, "operating network payments" is going to be a pretty niche activity overall.
>
> Projects integrating Livepeer would be much better off just delegating that to a signer service. So I think it's important to make that distinction when considering the different roles within the overall builder experience

### j0sh — 8:30 PM

> That being said though, I think the clearinghouse + signer can be reasonably self contained for the purpose, or at least that is the goal.
