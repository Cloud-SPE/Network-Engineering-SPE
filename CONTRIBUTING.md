# Contributing

Thank you for helping make the Cloud SPE's contribution to the wider Network
Engineering SPE more legible, measurable, and reproducible. Contributions here
must relate to a Cloud SPE-owned task, deliverable, dependency, or handoff; this
repository does not track the SPE as a whole.

## Before you begin

Read [ARCHITECTURE.md](ARCHITECTURE.md) and [docs/index.md](docs/index.md) to
identify the correct knowledge category. Check Beads before starting:

```bash
bd prime
bd ready
bd search "relevant terms"
```

Claim an existing issue or create one with a concrete description and
acceptance criteria. Do not use Markdown TODO lists as a second task tracker.

## Choose the right document type

- Put dated observations, research, and source notes in `docs/references/`.
- Put approved intended behavior and acceptance evidence in
  `docs/product-specs/`.
- Put durable technical constraints in `docs/design-docs/`.
- Put accepted choices and rationale in `docs/decisions/`.
- Put work state, dependencies, blockers, and handoffs in Beads.

Work owned by another Network Engineering SPE participant belongs in that
owner's source of truth. Reference it here only when it directly constrains or
blocks a Cloud SPE deliverable.

Every technical baseline should identify the repositories, commits, review
date, method, and limits. Distinguish source inspection from deployed behavior.

## Make focused changes

- Preserve source provenance and status labels.
- Link to the source of truth instead of copying large sections.
- Avoid declaring a cross-system contract before its owners accept it.
- File unrelated discoveries as Beads issues linked with `discovered-from`.
- Update the relevant documentation index when adding a durable document.

## Authorship policy

Do not add `Co-authored-by` trailers, co-author attribution, or equivalent
co-author messages to commit messages, pull-request titles, or pull-request
bodies. Commits and pull requests should identify only their actual author
unless the repository owner explicitly overrides this policy for a specific
change.

This applies to contributions produced with coding agents as well as manually
prepared changes. Describe tool assistance in process notes only when required;
do not represent a tool as a co-author.

## Validate

Run all repository checks before requesting review:

```bash
python3 scripts/check_docs.py
python3 scripts/check_attribution.py --all-history
git diff --check
bd lint
```

## Pull requests

A pull request should:

- link the Beads issue and any governing decision or specification;
- state the outcome, not merely list edited files;
- identify evidence reviewed and its date;
- disclose unresolved assumptions or cross-repository dependencies;
- include the validation commands and results; and
- avoid co-author attribution under the policy above.

Reviewers should verify document status, source precedence, acceptance evidence,
and links before approving.
