# John–Josh Authentication and API Key Discussion

**Recorded:** 26 September 2026\
**Conversation date:** Not independently established; supplied messages say “Yesterday,” suggesting 25 September relative to this capture\
**Participants:** John of Elite Encoder (`eliteproxy`), Josh (`j0sh`), and Mike Zupper (`Mike Zoop`)\
**Status:** User-supplied conversation and separately attributed assistant assessment; reference only, not an accepted design or scope change

## Provenance and use

Mike supplied this exchange while asking for an off-record opinion separate from
the specification work. He subsequently requested its capture in Markdown for
reference and a return to project planning. That instruction authorizes this
reference capture; it does not promote the discussion or the assistant's opinion
into a requirement.

The supplied message text, speaker labels, relative dates, and displayed times
are preserved below, with Markdown formatting added for readability. The source
timezone, channel, message permalinks, absolute conversation date, and completeness
of the surrounding thread are not established. The filename and catalog date
refer to this capture, not a verified event date.

Statements about Batteries, the signer, SDK behavior, and the newly pushed admin
API are participant reports. No named Batteries/go-livepeer/SDK implementation
revision or runtime evidence was checked for this capture. Josh's final message
reports a push but does not identify a commit or establish API stability.

The linked design commit is
[`eliteprox/Network-Engineering-SPE@c76b09249787ae4812c2a732b258dfb861743e78`](https://github.com/eliteprox/Network-Engineering-SPE/commit/c76b09249787ae4812c2a732b258dfb861743e78).
The assistant reviewed its authorization and provisioning drafts and the
standards linked below when forming the assessment. These are design proposals
and standards, not proof of deployed behavior or upstream acceptance.

## Discussion findings

| Topic | What the exchange records | Qualification |
| --- | --- | --- |
| Provisioning API | Josh initially reports CLI provisioning and an unpushed optional HTTP API; his final message says he has pushed work with further auth changes pending. | Reported work in progress; exact API, revision, permissions, and behavior require inspection. |
| Enterprise-issued JWTs | John proposes a trusted JWKS URL per grant, an allocation claim, and session binding through issuer/subject instead of API-key identity. | Proposal for delegated payment authorization, not a selected implementation. |
| Grant/allocation model | Josh explains grants as originating in community/customer budgets, allocations as subdivisions for different uses, and multiple API keys per allocation for rotation/revocation. | Explains intended business semantics; does not make grants or allocations application-user records or prove strict spending ceilings. |
| OAuth experience | John wants clients to connect by URL and log in through the enterprise authorization server without manually copying payment API keys. | Client-facing product requirement he advocates; it does not by itself require JWT validation in Batteries. |
| Working accommodation | John agrees to retain generated allocation keys server-side while preserving OAuth at the gateway/MCP boundary. Josh expects application-mediated signing requests to be common. | Direction reached in the conversation, not verified implementation or SPE approval. |
| Direct signer access | John argues for the option of clients calling the signer directly with enterprise-issued credentials. | A distinct proposed access model with different delegation and security requirements. |
| Overloaded identity terms | Mike observes that “user” is overloaded; Josh clarifies his use of “customer.” | Application identity, gateway identity, budget ownership, and payment authorization need separate meanings. |

## Assistant assessment recorded with the conversation

This section summarizes the assistant's response to Mike. It is analysis, not a
statement by John or Josh and not a decision for the planning document.

The assistant favored retaining payment credentials behind the gateway for the
gateway-mediated flow. Enterprise OAuth can authenticate a caller to the gateway,
which checks application permissions and uses an appropriately scoped allocation
credential for signing. A third, separate boundary governs administration of
grants, allocations, and credentials. A coherent builder experience does not
require the same credential at all three boundaries.

The assessment recognized John's concern about protecting stored allocation keys:
an allocation identifier and a spending credential have different consequences
if disclosed. It also recognized the convenience of URL-and-login onboarding.
Neither concern establishes that downstream API keys break OAuth. Josh's suggested
client API-key access is a separate user experience, not a necessary consequence
of API keys inside Batteries.

The [authorization draft at the linked commit](https://github.com/eliteprox/Network-Engineering-SPE/blob/c76b09249787ae4812c2a732b258dfb861743e78/docs/design-docs/enterprise-authorization-server.md)
already distinguishes caller credentials, allocation keys, and signer webhook
credentials, with caller tokens ending at the gateway. Its separate choice of
one wholesale allocation per enterprise is not implied by that authentication
separation and is not adopted here.

The assistant qualified several technical statements:

- OAuth does not require JWT access tokens; tokens can be opaque or carry signed
  authorization information. See [RFC 6749, section 1.4](https://www.rfc-editor.org/rfc/rfc6749.html#section-1.4).
- The standard MCP browser authorization flow uses authorization code with PKCE;
  OAuth device authorization is a separate flow. MCP tokens must be intended for
  the MCP resource. See the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).
- Public clients cannot reliably protect an embedded application secret. This is
  distinct from presenting a user's credential; there is no blanket prohibition
  on a public application using a user-held API key. See [OAuth client types](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.1).
- Claude Code documents both OAuth and custom authorization headers. This does
  not establish identical support or onboarding across all MCP clients. See
  [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp).

Direct client-to-signer access could justify a separate design for short-lived,
scoped payment tokens. The assistant identified issuer/audience trust, grant and
allocation binding, rotation, revocation, and session lifetime as necessary parts
of evaluating such a design. A JWKS URL alone does not define the full trust
relationship; see [JWT validation guidance](https://www.rfc-editor.org/rfc/rfc8725.html#section-3.8).

Specific unresolved concerns in John's proposal include whether refreshed tokens
remain authorized for the same allocation, whether issuer/subject matching alone
would be insufficient, how token expiry interacts with payment-session lifetime,
what `expiry: 0` means in the signer callback, and why a key-set URL should be
unique across grants. These are review questions, not findings of an implemented
vulnerability.

The assistant's recommendation was to retain enterprise login at the gateway,
use scoped payment credentials downstream, and define management permissions
explicitly; reconsider JWT payment delegation when a concrete direct-access
requirement calls for it. No architecture, task acceptance criterion, or December
scope was changed on the basis of this opinion.

## Supplied conversation

### eliteproxy — Yesterday at 3:33 PM

> It's a good place for it so everybody is on the same price oracle. PymtHouse did this inside the event collector behind kafka to avoid changes to go-livepeer, but this is much better to have it integrated into the signer and events
> One parallel point I want to confirm - the provisioning of grants by api-key on the clearinghouse, is that only a CLI interface right now?

### j0sh — Yesterday at 3:36 PM

> yes, there's also an optional HTTP API that I haven't pushed yet
> btw let me know if you prefer to generate your own keys then give those to the clearinghouse, rather than getting keys from clearinghouse. Should be easy to do it either way.

### eliteproxy — Yesterday at 4:33 PM

> Good topic, this is where I've spent most of my time analyzing the codebase today.
>
> I'd like the enterprise app to issue its own credentials, with Batteries only verifying them.
>
> Proposal:
> The operator sets one JWKS URL per grant (a new nullable grants.jwks_url, unique across grants).
> On the first authorize call of a stream, clearinghouse-batteries verifies the JWT, requires the allocation claim to belong to that grant, runs the usual balance check, and pins the allocation to the payment session. The session id is returned as auth_id.
> Later calls in the stream look up the allocation through auth_id, the same way Kafka debits already do. A rotated token only has to match the session's issuer and sub. The balance check runs on every call as it does today, and expiry stays 0.
>
> I checked go-livepeer, the signer forwards the header without reading it and only requires auth_id to stay the same, so rotating tokens work fine. The Python SDK needs a header refresh for live sessions, which I'd take on.
>
> The main change on your side is that payment_sessions would bind to issuer plus sub where it currently requires api_key_id. Does this direction work for you?
> This design assumes each "enterprise client application" will have a single grant. Each app is likely to operate it's own authorization server (issuer)
>
> Let me know if I overlooked any other functional purpose associated with grants. This could be a separate relational table instead of modifying grants directly, was just leaning toward minimal change

### eliteproxy — Yesterday at 4:46 PM

> The grant funding flow from the batteries admin API would be as follows:
>
> The operator funds the grant, as above.
> The enterprise app (admin) calls POST /v1/grants/{grant_id}/allocations and keeps the returned allocation_id.
> The enterprise app stores allocation_id in its own db, next to the grant and the gateway that will spend it. Batteries does not store which user paid.
> The issuer puts that allocation_id in the token:
>
> ```json
> {
>   "aud": "<batteries --jwt-audience>",
>   "sub": "<gateway identity>",
>   "allocation_id": "<id from the create response>",
>   "exp": "<short>"
> }
> ```
>
> The gateway sends it as Authorization: Bearer on each signer request. The signer forwards the header. Batteries loads that allocation, verifies the token with that grant's jwks_url, checks the balance, and returns auth_id.

### eliteproxy — Yesterday at 4:56 PM

> We can set aside the admin api/external auth for later if preferred. I drafted technical design docs for the entire solution based on api-key auth here https://github.com/eliteprox/Network-Engineering-SPE/commit/c76b09249787ae4812c2a732b258dfb861743e78

### j0sh — Yesterday at 5:22 PM

> We can explore that as we get further along. I'm a little hesitant to impose "JWT everything" right now

### eliteproxy — Yesterday at 5:23 PM

> Fully agree, I'm also scoping what this looks like keep the AS within the gateway server for now

### j0sh — Yesterday at 5:24 PM

> The underlying flow does not change massively for the app anyway; you're just sending your customer's key instead of minting a JWT for them

### Mike Zoop — Yesterday at 5:26 PM

> Yeah I don’t think we need any JWT stuff right now … the concept of “user” is overloaded in this context.

### eliteproxy — Yesterday at 5:26 PM

> Once we have an admin http server for clearinghouse-batteries, then the administrative function of crediting payments to users becomes more clear.
>
> JWT has two primary advantages:
> Allows each enterprise to bring their own auth, without leaving gaps between protected resources
> The token can be validated cryptographically and hold additional user info like the allocation_id so the systems can communicate better

### j0sh — Yesterday at 5:27 PM

> Yeah sorry that was my being imprecise. The flow for the app doesn't change and used "customer" when we're talking about the end-user.... edited the comment

### eliteproxy — Yesterday at 5:28 PM

> A shared secret between the clearinghouse-batteries and the enterprise app/gateway would also be sufficient. My understanding is that is what api-key currently is, however, I am confused by the fact that each allocation has it's own api-key, can you explain the business logic for that? Why not associate api-key with the grant? grants<->allocations is a one to many relationship, are these designed to represent "accounts"?

### eliteproxy — Yesterday at 5:30 PM

> Then the enterprise app would need to store the customer's api-key, though

### j0sh — Yesterday at 5:35 PM

> Another way to think is in terms of
>
> Grant == customer (this was originally designed for community grants)
>
> Allocation ==  a subset of a grant. So customers can partition off their usage, set limits etc. Maybe CI is limited to $10 per day, production has $100, etc.
>
> Then they can issue multiple API keys against each allocation. Since you need to be able to rotate gracefully, revoke, etc.

### j0sh — Yesterday at 5:35 PM

> If not the API key you'd be storing the allocation ID. So not a huge difference either way.

### eliteproxy — Yesterday at 5:37 PM

> ah, thank you for the context. That clarifies several open questions 🙂

### eliteproxy — Yesterday at 5:38 PM

> That makes sense now, the enterprise app can store and append the allocation_id after authentication. I was thinking too narrowly

### eliteproxy — Yesterday at 5:51 PM

> Alright, looks like we'll have to store the api-key from clearinghouse-batteries, as it is the only way to authenticate with the signer + clearinghouse without a trusted JWKS issuer in the clearinghouse db.
>
> Alternatively, the user can hold the api-key and use it for for signer/gateway authentication for job requests, but that becomes a confidential secret with no expiry and breaks OAuth login flow for MCP clients (which is a primary target consumer)
>
> We can accept this for now as a known constraint without affecting the product surface, but I still stand by my professional recommendation
> I'll stick it in the Gateway/MCP authorization server for now as a user-scoped vault secret so we can keep OAuth client support. The AS already holds credentials so it should be safe there

### j0sh — Yesterday at 5:56 PM

> How does it break the OAuth login flow? It's not like MCP clients are actually calling the signer directly?
>
> It seems the only real difference is when you check validity: either before starting the job (before calling the signer), or somewhat mid-job from a signer callback (JWKS)
> BTW you could also just give customers the generated API key and they use that with MCP, pretty straightforward.

### eliteproxy — Yesterday at 6:12 PM

> MCP Clients (like Claude) default to OAuth public device authentication flow. This is what allows the user to "just plug in an MCP url" without an api-key. The desktop client initiates OAuth device login with enterprise app's authorization server, allowing user to login at the website in lieu of creating and setting a specific api-key. This is quite standard across other productionized MCP servers.
>
> As an example, the setup instructions for a user become very different. For example:
>
> Standard OAuth public device login flow
>
> ```bash
> claude mcp add --transport http livepeer-mcp https://gateway.example/mcp
> ```
>
> API key auth:
>
> ```bash
> claude mcp add --transport http livepeer-mcp https://gateway.example/mcp \
>   --header "Authorization: Bearer ${GATEWAY_API_KEY}"
> ```
>
> In desktop, all you need for OAuth is the MCP URL and it's very simple. api-key auth requires more fields to fill out. Enforcing api-key auth on the client also restricts the types of workflows that can interact with the signer (technically from an RFC perspective, an api-key cannot be used from a public application surface (like a cookie or web session)

### eliteproxy — Yesterday at 6:14 PM

> imho, the client app actually should be able to send signing requests directly, the MCP and/or gateway server can use the same auth without proxying. Otherwise, requests would need to be proxied server-side by the enterprise application (or the confidental api-key is used on the client)

### j0sh — Yesterday at 6:20 PM

> Otherwise, requests would need to be proxied server-side by the enterprise application
>
> I think this is usually going to be the case

### eliteproxy — Yesterday at 6:23 PM

> In this case, we can keep the OAuth public login flow and preserve the product surface. I'll find a place to store the api-keys that are generated. Lmk once you have a draft admin http server for clearinghouse and we should be unblocked to build

### j0sh — Yesterday at 7:03 PM

> Just pushed, still have a buch of more stuff WIP including a system to configure auth so there will be more changes coming, buuuut Codex is down for me, so I think that means I'm done for the day 🙃

### eliteproxy — Yesterday at 7:05 PM

> Thanks, have a great weekend! Excited to kick off the build track sprint next week
