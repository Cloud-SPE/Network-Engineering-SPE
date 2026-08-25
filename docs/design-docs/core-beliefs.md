# Core Beliefs

**Status:** Proposed
**Last reviewed:** 25 August 2026

These principles shape the repository scaffold. They are proposed operating
constraints, not substitutes for committee decisions.

## Outcomes need observable evidence

Shipping components is not sufficient evidence for a Cloud SPE deliverable. A
claim is complete when its assigned outcome can be reproduced and, where the
builder journey is in scope, identity, invocation, payment, result, usage, and
network fee can be correlated.

## One concept should have one canonical contract

Credentials, capability identifiers, prices, job identifiers, and usage records
should each have an explicit owner and stable boundary. Compatibility adapters
may exist, but ambiguity should not be normalized as architecture.

## Facts, intent, and work state are different

References describe evidence, specifications describe desired behavior,
decisions record accepted choices, and Beads records work. Keeping these roles
separate prevents drafts and stale observations from becoming accidental policy.

## Progressive disclosure beats a large instruction manual

Entry-point documents should provide a map. Detailed knowledge belongs near its
domain and should be linked, dated, and reviewable.

## Constraints should become feedback loops

If a rule matters repeatedly, encode it in validation, tests, or CI. A concise
error with remediation guidance is more useful to future agents than another
paragraph in a global instruction file.

## Cross-repository work needs end-to-end acceptance

A local merge is not sufficient evidence for a multi-system Cloud SPE outcome.
Delivery criteria should name the environment, client journey, correlation
evidence, responsible owners across repositories, and the boundary between
Cloud SPE work and external dependencies.
