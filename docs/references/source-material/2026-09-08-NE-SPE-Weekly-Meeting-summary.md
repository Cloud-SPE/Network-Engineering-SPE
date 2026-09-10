# Network Engineering SPE Weekly Meeting Summary

**Status:** Automated source summary retained as working evidence; not an
approved decision record or Cloud SPE task tracker

**Meeting date:** 8 September 2026

**People represented in updates or discussion:** Mehrdad Sadeghi, Mike Zupper,
Josh Allmann, Elliott Conway, Shane, Rich O'Grady, and Doug Petkanics

The action-item checkboxes below are preserved from the supplied source
summary. Cloud SPE work state and ownership remain authoritative in Beads.

## Action Items

- [ ]  Josh and Mike to share their calendars with Mehrdad to enable coordination scheduling
- [ ]  Rich to discuss foundation node vote with Ben and decide on abstain vs. not voting by Friday
- [ ]  Elliot to drop a note to Rick and coordinate offline on subgraph ownership and scope
- [ ]  Add Shane to the Thursday alignment meeting on agent stack and canonical decisions
- [ ]  Doug to share a preview version of the light paper as soon as possible
- [ ]  Doug to connect Shane with Emrin (Inc. team) for tokenomics simulation collaboration to avoid duplicated work
- [ ]  Subgraph ownership discussion to be deferred until Rick returns (approx. 3 weeks)
- [ ]  Mike to publish build track architectural thesis / straw man with crystallized deliverables for the next meeting
- [ ]  Mike to align with John, Rick, and Rich on a simplified clearinghouse software plan and how it differs from Payment House
- [ ]  Mike to finalize September funding milestones for the build track
- [ ]  Discuss Shane's agent-forward repo strategy as a group in 1–2 weeks once more context is available
- [ ]  Shane's repo approach to be discussed offline (incremental migration vs. greenfield)
- [ ]  Mehrdad to finalize and add their weekly commitment async after the call

---

### Doug's Participation & Light Paper Framing

- Doug was invited to join mid-call to address alignment questions; Shane raised concern about not wanting all decisions to route through Doug or create indefinite open invites
- Group aligned that Doug is a key stakeholder but not a de facto leader of the SPE
- Shane emphasized the light paper should be treated as a **starting point and one person's vision**, not the final word — the SPE's job is to bring what can realistically be built and what the community needs
- Rich agreed: Doug's near-term presence is to help resolve misinterpretation after the light paper is published, not to gate decisions
- Doug confirmed he is happy to advise and give clarity on tracks that serve the 2.0 direction; noted potential confusion where tracks serve alternate demand-gen paths

### Weekly Status Updates

- **Mehrdad:** 5 of 7 SPE members have shared calendars; Josh and Mike still to share  ; Mehrdad is formally taking over running this call and monthly updates from Rich going forward
- **Mike:** Gathered survey feedback from Shane, Josh, and Rick; working on concept compilation and architectural thesis to be published soon; open questions remain on lifecycle agent discussion with Doug and X402 payments
- **Josh:** Mixed green/yellow status across milestones; some items slipped during the week but overall feeling confident in the track
- **Elliot:** Milestone 1 mapped as tickets; milestone 3 tickets created but need organizing into a project board; Raid Guild started with ~50% of contributors ready; bounties going public soon; subgraph scope still unclear
- **Shane:** Completed an agent-forward repository strategy and shared it in chat; this is the main focus until the light paper is published
- **Rich:** Governance vote is progressing toward quorum; only "no" votes have come from Navigara's nodes; MIA voter (Varese) typically appears last minute

### Governance Vote Update

- Quorum is close but not yet confirmed; question raised about whether the foundation node should abstain or simply not vote
- Consensus leaned toward **not voting** being preferable to abstaining, to let orchestrators speak for themselves, unless abstaining is needed to reach the 33% threshold
- Rich to follow up with Ben and make a call by Friday

### Tensions Discussed

- **Subgraph ownership:** Elliot raised uncertainty about who owns subgraph work and 2.0 upgrade coordination  ; discussion concluded Rick is the only person with full context, the subgraph is a large standalone project, and it primarily affects the Explorer track  ; agreed to **defer to Rick's return in ~3 weeks**
- **Milestone 3 budget:** Elliot recommended adding **$3K to milestone 3** to cover security bug remediation and dependency/security scan recommendations; group agreed it is reasonable

### Q&A with Doug: Self-Sovereign Agent, X402 & Build Track Scope

- **Build track 7 outcomes** (get credential, find capabilities, find pricing, send work, get results, see cost, wallet/non-wallet) are clear to Doug
- **Livepeer Agent MCP** is envisioned as an open-source gateway targeting agentic media creation; the commercial version (hosted, credit-card abstracted) builds on top of this open-source base
- Shane confirmed that Steph and Peace are moving toward a **fully open stack** for the agent, with the foundation running MCP server infrastructure
- **Clearinghouse vs. Payment House:** Strong consensus that the build track needs a **simplified clearinghouse** (token for API calls, capability discovery, pricing, job submission, cost reporting) — not the full Payment House stack (Kafka, OpenMeter, Kong, Auth0)
- If the agent team builds around the simplified remote-signer-based clearinghouse, the group is in good shape; building toward Payment House would be a problem
- **X402 payments:** Doug clarified he is not championing X402 as a core build track requirement; notes that unlimited node operator set size could weaken probabilistic micropayment security, but prefers to keep PMs under a slightly less secure guarantee for now rather than committing to X402
- **Build track scope:** Doug framed it as making raw capabilities available (public good / open playground) while opinionated commercial demand-gen efforts like Agent drive demand separately; the toolbox must exist and be documented but does not need its own scaled go-to-market yet

### Light Paper Timeline & Shane's Validation Modeling

- Doug is targeting light paper draft release **within the next two days**; the admissions mechanism section is the remaining sticking point
- Shane's validation track work will begin with **quantitative modeling of mechanisms and parameters** under ideal conditions, then stress-test with real-world chaos factors
- Doug will connect Shane with **Emrin (Inc. team)** who is preparing simulation environments, to ensure collaboration rather than duplication

### Shane's Agent-Forward Repo Strategy

- Shane proposed an agent-forward repo approach where the repo self-verifies key scenes and generates a verifiability report on PRs touching major areas
- Only Mike had reviewed the proposal by the time of the meeting
- Mike noted the proposal is **greenfield in concept** and does not address how existing repos (Go-Livepeer, Explorer, Storyboard, Payment House, etc.) would migrate
- Josh emphasized the need for alignment on *what* and *why* before any PR-level process matters, as review and merge alignment is the expensive part
- Group agreed to **defer full discussion 1–2 weeks** to allow everyone to review and to have more clarity on direction first

### Meeting Format Discussion

- Mehrdad proposed containing future meetings to **one hour** and moving more to async
- Mike and Rich pushed back: during the current discovery phase, longer open-forum discussions are necessary and often involve enough people that offline conversation is harder to schedule
- Compromise: if a conversation becomes a pure 1-on-1, others should feel empowered to suggest taking it offline; otherwise, longer meetings are acceptable for now
