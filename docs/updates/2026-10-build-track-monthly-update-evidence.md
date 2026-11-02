# October 2026 Build Track update: evidence ledger

Working record behind the [draft update](2026-10-build-track-monthly-update.md). It is not part
of what gets posted. Data pulled from GitHub on 2 November 2026 (Project 13, every NE-Build-Track
repository, all branches, and the upstream `livepeer/*` repositories). Reporting period: 1–31 October 2026.

**Publication state:** published to [Project 13](https://github.com/orgs/Cloud-SPE/projects/13/views/4?pane=info&statusUpdateId=307941) on 2 November 2026 (On track, start 2026-10-01, target 2026-11-20), from commit `567597c`. Not yet posted to the Livepeer forum.

## GitHub status update settings

| Field | Value | Basis |
| --- | --- | --- |
| Status | On track | M3 is at 9 of 18 tasks with 12 of 32 days elapsed. The named risk is merge timing, not missing work |
| Start date | 2026-10-01 | Reporting period start, as in earlier status updates |
| Target date | 2026-11-20 | M3 gate |

**Early completion:** "as early as the end of this week, November 6" in the opening paragraph is Mike's forecast, stated on 2 November. No ticket or decision record carries that date. The plan's dates are unchanged: dry run by 13 November, gate on 20 November, so the status update's target stays 2026-11-20. Finishing by 6 November needs #77 and the #78 → #83 stack merged, Builder Core Console #12 re-pinned and merged, and the funded run passed on merged code.

## Board snapshot

| Milestone | Target | Tasks | Done | In progress | Planned |
| --- | --- | --- | --- | --- | --- |
| M1 | 30 Sep | 6 | 6 | 0 | 0 |
| M2 | 16 Oct (closed 19 Oct) | 7 | 7 | 0 | 0 |
| M3 | 20 Nov | 18 | 9 | 9 | 0 |
| M4 | 18 Dec | 11 | 0 | 1 (ISS-33) | 10 |
| M5 | 31 Dec | 3 | 0 | 0 | 3 |
| **Total** | | **45** | **22** | **10** | **13** |

Three builder-core issues are also on the board: #33 and #45 (Done), and #89 (Planned, M3).

## M2 and the 16 October checkpoint

The September post said the next update was planned for the 16 October checkpoint. No post went to the forum.
The M2 update went only to Project 13, on 20 October. The forum's only Build Track post is #15, of 1 October.

| Task | Accepted or closed | State at 16 Oct |
| --- | --- | --- |
| ISS-01 Baseline | 12 Oct | Accepted |
| ISS-03 Access | 13 Oct | Accepted |
| ISS-06 SQLite records | 13 Oct | Accepted |
| ISS-07 Builds and CI | 13 Oct | Accepted |
| ISS-02 Engine contracts | 19 Oct | Open |
| ISS-04 Payments | 19 Oct | Open |
| ISS-05 Core packages | 19 Oct | Open |

Paid runs: [12 Oct, first funded run on the new baseline](https://github.com/NE-Build-Track/livepeer-builder-core/blob/2edf903/docs/references/evidence/2026-10-12-dev-stack-paid-run.md);
[14 Oct, public orchestrators](https://github.com/NE-Build-Track/livepeer-builder-core/blob/2edf903/docs/references/evidence/2026-10-14-dev-stack-public-orchestrators.md);
[19 Oct, session log on tagged builds, nothing unattributed](https://github.com/NE-Build-Track/livepeer-builder-core/blob/2edf903/docs/references/evidence/2026-10-19-dev-stack-session-log.md).

### Items the 20 October update said were carried from M2

| Item | State on 31 Oct |
| --- | --- |
| Streaming, built and in review | Merged 21 Oct (#28) |
| Final retry semantics | Merged 29 Oct (#76, D57) |
| Upstream merge of SDK #77 | #77 closed; #81 replaced it, merged 21 Oct |
| A payment reference the caller owns | **Open** (T13, T16) |
| Two attribution cases, tested but not shown live | **Open.** Neither the M3 live suite nor `m3-traceability.md` covers them. The 7 October run showed a forged manifest on the old go-livepeer stack only |

## M3 tasks

Done dates are ticket closures. "Built by" is the pull request author, which differs from the board assignee on several tasks.

| Task | Board status | Closed | Board assignee | Built by | Where |
| --- | --- | --- | --- | --- | --- |
| ISS-08 Credentials | Done | 27 Oct | John | Mike | #48 (with #41) |
| ISS-09 Discovery | Done | 28 Oct | John | Mike | #46, then John's #87 |
| ISS-10 Rates | In progress | | John | John | #77, approved by Mike 31 Oct, not merged |
| ISS-11 Provisioning | Done | 30 Oct | Mike | Mike | #76 |
| ISS-12 Payment failures | In progress | | John | Mike | #78, needs a rebase (3 behind `releases/m3`, GitHub reports conflicts) |
| ISS-13 Funded configuration | In progress | | Mike | Mike | Builder Core Console #12, draft |
| ISS-14 Durable submission | Done | 30 Oct | Mike | Mike | #76 |
| ISS-15 History and results | In progress | | John | Mike | #81, draft |
| ISS-16 Usage correlation | Done | 24 Oct | John | Mike | #44, later hardened by #64 |
| ISS-17 Cost projections | Done | 24 Oct | John | Mike | #43 |
| ISS-18 Cost reports | In progress | | John | Mike | #82, draft. Stays partial while the feed is held |
| ISS-19 Jobs and matrix | Done | 27 Oct | Mike | Mike | Builder Core Console #1 (21 Oct) |
| ISS-20 REST for the journey | In progress | | Mike | Mike | Builder Core Console #12, draft |
| ISS-21 Access and catalog | Done | 27 Oct | Mike | Mike | Builder Core Console #1 (21 Oct) |
| ISS-22 Execution and reporting | Done | 27 Oct | Mike | Mike | Builder Core Console #1 (21 Oct) |
| ISS-23 Verification | In progress | | John | Mike | #83, draft |
| ISS-24 Journey guide | In progress | | Mike | Mike | Builder Core Console #12, draft |
| ISS-25 Funded proof | In progress | | Mike | Not run | Dry run by 13 Nov, spend capped at $1 |

Other engine work merged in M3 that no single task owns: streaming (#28), dependency injection (#41), own paid
call and failover (John's #61, #62), attempt cap (#65), native HTTP (#55), public offerings (John's #54), Neon
databases per pull request (John's #60), timings (#90).

Ahead of plan: on-chain discovery was still a stretch goal in the 21 October decision and merged on 26 October
(#46). JWT bearer (#50), the auditor credential (#69) and OIDC sign-in in the Builder Core Console (its #7) all fall under M4's ISS-33.

## Activity in October

Unique commits across all branches. A commit on several branches counts once. Merged counts include merges into
stack branches (9 of the 74).

| Repository | Commits | PRs merged | Open on 2 Nov |
| --- | --- | --- | --- |
| livepeer-builder-core | 303 | 45 | #32, #77, #78, #79, #81, #82, #83, #85 |
| builder-core-console | 48 | 9 | #12 |
| chatlpt-sample-enterprise-app | 60 | 7 | None |
| enterprise-ui | 41 | 5 | #7, #8 (Dependabot) |
| inference-gateway | 33 | 5 | None |
| livepeer-python-gateway (fork) | 28 | 3 | None |
| node (fork) | 87 | 0 | None |
| clearinghouse-batteries (fork) | 31 | 0 | None |

The fork commit counts are mostly upstream history, by Josh. The five non-fork repositories total 485 commits.
PRs merged by author: Mike 52, John 22. CI on `releases/m3` at `2edf903`: 1,534 passed and 50 skipped at 98%
coverage on SQLite, and 103 passed and 1 skipped on the PostgreSQL store suite.

## Live evidence

| Date | What | Result | Where |
| --- | --- | --- | --- |
| 7 Oct | Attribution on Arbitrum, old stack (go-livepeer) | Actors matched Batteries | Repo evidence, ISS-01 comment |
| 12, 14, 19 Oct | Funded runs | Above | Repo evidence |
| 21 Oct | Builder Core Console: 2 chats at $0.000111, 3 images at $0.003007 | $0.0092, matches allowance | [ISS-22](https://github.com/Cloud-SPE/Network-Engineering-SPE/issues/35) |
| 29 Oct | Repeat-safe commands on merged `a6ed9b5` | 37 engine and 14 UI checks passed | [Builder Core Console evidence](https://github.com/NE-Build-Track/builder-core-console/blob/ca43baa/docs/references/evidence/2026-10-29-d57-live-check.md) |
| 29 Oct | Inference gateway, paid native vLLM | 62 paid attempts reconciled, one orchestrator | [Gateway #6](https://github.com/NE-Build-Track/inference-gateway/pull/6) |
| 30 Oct | Live probe on #83 | 25 of 25 | [Probe evidence](https://github.com/NE-Build-Track/livepeer-builder-core/blob/901d90c/docs/references/evidence/2026-10-30-iss-23-live-probe.md) |
| 30 Oct | Engine suite A–G on a local merge | 41 of 41, three after runner fixes, $0.011 for the day | [Suite evidence](https://github.com/NE-Build-Track/livepeer-builder-core/blob/901d90c/docs/references/evidence/2026-10-30-m3-live-suite.md) |
| 30 Oct | Browser suite H–L | H 12/13, I 4/4, J 3/4, K 2/2, L 10/10 | **Local only**, below |
| 30 Oct | Journey rehearsal | 16 of 17, the miss was the script's parse, image re-run passed | **Local only**, below |

### Runs not in any repository

These results exist only in a temporary session directory. They are copied here so they aren't lost. The draft
relies on them for the two Builder Core Console defects and the journey rehearsal.

Build: `9676260` = #78 → #81 → #82 → #83 + #77, local and never pushed. Stack: Batteries `ca09e47`, signer `406b248`.

| Part | Result |
| --- | --- |
| Live probe | 26 passed, 0 failed |
| Builder Core Console engine checks (D57–D61) | 46 passed, 0 failed |
| Builder Core Console browser checks | 22 passed, 0 failed |
| Seven-outcome journey (streamed chat, FLUX schnell) | 16 of 17, the miss was the script's parse; image re-run inline |
| Pages, reconciliation, health | 11 pages 200; both actors balanced, unattributed 0 |

Observed cost: chat $0.000110659750758255, image $0.002987813270743978, one ticket each, delivered.

Browser run defects: H, the catalog doesn't show the rate's source (waits on #77). J, a revoked key doesn't end
the Builder session (fixed in Builder Core Console #12).

Session notes also record a rebuild on 31 October (`de16415`: probe 26, API 46, UI 22, journey 17, engine 41/42,
browser 32/33) and a live paid failover on the Builder Core Console stack on 28 October. No saved output backs either, so the
draft uses neither.

## Work after the period, and later tracker administration

Kept apart from October's work as the reporting task requires.

- **After 31 October:** inference-gateway #7 (1 Nov, cited as "just after this period"), #8, #9, tags `v0.1.0` and
  `v0.2.0` (1 Nov).
- **Administration in October, not delivery:** M1 tasks converted to issues and closed on 1 October (work done
  by 30 September). M1, M2 and M3 summary issues created on 13 October. M4 issues created on 27 October. The M2
  closing record and PR attribution comments added on 27 October, for work done by 19 October. ISS-19, ISS-21 and
  ISS-22 delivered 21 October, accepted 27 October.

## Left out of the public draft

| Item | Why |
| --- | --- |
| The partner's name in the latency report | The draft says "a partner". Issue #89, which it links, names them |
| Mike and John's review process, bot reviews, Cursor PRs | Process detail |
| x402 research (#68), discovery follow-ups (#70, #80), package split (#25), OIDC docs (#51), capability descriptions (#18) | Open proposals, no decision made |
| `price_usd` not sent by orchestrators in the 30 October run | Detail for ISS-10; relevant if USD rates come up |
| Enterprise desk (`enterprise-ui`) | Mike, 2 November: not referenced in this update. Its 5 PRs and 41 commits still count in the activity totals above |
| Known engine limits T15–T22 | Tracked in builder-core's tech-debt tracker. T13 and T16 are summarized under "Still open from M2" |

## Community requests in the forum thread

| Post | Request | State |
| --- | --- | --- |
| 22, chrishobcroft, 13 Oct | Leave room for a capability schema and an Ethereum-key access adapter; addressed to Mike directly, offering a write-up | **No reply posted.** Facts available: `Authenticator` is a replaceable interface with tested custom examples; capability descriptions are open as #18 |
| 5, hthillman | Uptime information, failover, and recourse for jobs failing partway | Failover merged. No uptime information. Recourse out of scope |
| 6, brad-ad-astra-video | Runner pricing in USD | #77 carries `price_usd` when advertised; the 30 October run's orchestrators did not send it |
| 8, dob | Self-sovereign access through agents | MCP is ISS-30, M4, planned |
| 14, r4topunk | SkateHive as a test case | No action recorded |

## Inconsistencies found, not changed

| Where | Issue |
| --- | --- |
| Project 13 README | Still says M2 is in progress, that no implementation tasks have started, and that all M2 tasks are Planned |
| Board assignees | ISS-12, ISS-15, ISS-18, ISS-23 are assigned to John; Mike's PRs build them |
| Production deploy | Deploy run for #90 (`2edf903`) has waited for approval on the `production` environment since 31 Oct 14:11 UTC. An unapproved run blocks later ones |
| builder-core #78 | Reports merge conflicts with `releases/m3`; the stack sits on it |
| `m2-traceability.md` | Still lists Josh's engine review as carried to M3; reviews moved to Mike and John on 21 October |
| builder-core #89 | Says we run node from our fork; #63 moved to `livepeer/node` on 28 October |
| ISS-16 acceptance | Closed "no gaps" on unit tests, while the 20 October update named the two live cases as carried |
| `docs/index.md` | September update still reads "not yet published"; it was posted on 1 October |
