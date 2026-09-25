# Open Builder Engine: Architecture and Sequences

**Status:** Diagram companion to the consolidated working proposal, not approved or implemented architecture\
**Updated:** 25 September 2026\
**Owner:** Mike Zupper

The [primary architecture](self-sovereign-open-builder-stack-draft.md) owns scope,
contracts, evidence limits and open decisions. The new backend has its own
repository. In the component diagram, `livepeer/console` is an existing prototype
used as reference material; its dotted arrow represents possible code or behavior
reuse, not a runtime connection or deployment dependency. See the
[reference-only role](self-sovereign-open-builder-stack-draft.md#repositories-and-application-roles).
Every new engine interface below is proposed. Arrows express responsibilities,
not a verified protocol ordering or accepted upstream API.

## Components and repository responsibilities

![Repository responsibilities](../assets/open-builder-components.png)

```mermaid
flowchart TB
    Console["livepeer/console<br/>Reference behavior and reusable code"]
    subgraph New["New backend repository - name pending"]
        REST["Runnable REST adapter"]
        MCP["Runnable MCP adapter"]
        Core["Installable core packages<br/>Access, discovery, jobs, reporting"]
        Exec["Execution adapter<br/>Uses Python gateway SDK"]
        Store[("Persistence interface<br/>SQLite required / PostgreSQL target")]
        Pay["Payment-provider adapter<br/>Management and evidence contracts"]
        REST --> Core
        MCP --> Core
        Core --> Exec
        Core --- Store
        Core --> Pay
    end
    SDK["livepeer/livepeer-python-gateway<br/>Discovery, rates, invocation and payments"]
    subgraph Upstream["Existing payment and network components"]
        Signer["go-livepeer remote signer<br/>Discovery and ticket signing"]
        Batteries["clearinghouse-batteries<br/>Authorization and accounting"]
        Events["Ticket event transport"]
        Network["go-livepeer Orchestrator / Live Runner<br/>Capability execution"]
        Signer -->|"Authorization callback"| Batteries
        Signer -.-> Events
        Events -.-> Batteries
    end
    Console -.->|"Extract or redesign selected behavior"| Core
    Exec --> SDK
    SDK -->|"Discover / request signing"| Signer
    SDK -->|"Invoke / receive result"| Network
    Pay -->|"Proposed provisioning / reporting"| Batteries
    Sample["Sample enterprise app<br/>Imported extension + HTTP variants<br/>Mock commerce, additional tools"]
    Sample -->|"Import public packages"| Core
    Sample -->|"Or call deployed API"| REST
```

Core discovery delegates through the SDK integration; the diagram does not
require independent duplicate discovery logic. REST, MCP and execution may
share a process or use separate entry points. The provider management/reporting
surface is a gap to agree, not an assertion that Batteries has those HTTP APIs.

## Enterprise deployment: two supported integration modes

![Enterprise integration variants](../assets/open-builder-enterprise-modes.png)

```mermaid
flowchart TB
    Browser["Customer browser"]
    Agent["MCP harness"]
    subgraph Enterprise["Enterprise deployment and trust boundary"]
        Front["Branded frontend"]
        Identity["Enterprise identity / policy<br/>Mock commerce in sample"]
        Customer[("Customer and retail records")]
        subgraph Imported["Variant A - import and extend"]
            Host["Enterprise backend + MCP host<br/>Adds routes, tools and authentication"]
            Package["Released core packages<br/>SDK integration + persistence adapter"]
            Host -->|"In-process public interfaces"| Package
        end
        subgraph Service["Variant B - call deployed service"]
            Backend["Enterprise backend / trusted access layer"]
            API["OSS REST and MCP service<br/>Same core release"]
            Backend -->|"Authenticated HTTP"| API
        end
        Data[("Engine records<br/>SQLite / optional PostgreSQL")]
        Front --> Host
        Front --> Backend
        Host --> Identity
        Backend --> Identity
        Identity --- Customer
        Package --- Data
        API --- Data
    end
    Payment["Payment deployment<br/>Self-operated or hosted provider"]
    Network["Orchestrator / Live Runner"]
    Browser --> Front
    Agent -->|"Enterprise MCP access"| Host
    Agent -->|"Protected service MCP access"| API
    Package --> Payment
    API --> Payment
    Package -->|"SDK invocation"| Network
    API -->|"SDK invocation"| Network
```

The variants are alternatives, not a requirement to run duplicate backends.
The shared storage symbol indicates the same record contract, not a requirement
that separate installations share a physical database. Enterprise/customer
records remain distinct from engine records even when hosted in one database.
Exposing MCP requires the selected authentication boundary; the diagram does
not imply anonymous public access. An enterprise can also add a remote MCP
facade that uses core REST APIs. The core does not require that extra process.

## Payment operation choices

![Self-operated and hosted payments](../assets/open-builder-payment-modes.png)

```mermaid
flowchart LR
    subgraph Own["Mode A - operator controls full stack"]
        A["Engine + SDK"]
        AM["Management / reporting adapter"]
        AB["Batteries + ledger"]
        AS["Remote signer + funded wallet"]
        AT["Ticket event transport"]
        A --> AM --> AB
        A --> AS
        AS -->|"Authorize"| AB
        AS -.-> AT -.-> AB
    end
    subgraph Client["Mode B - application operator"]
        B["Engine + SDK<br/>Configured service credential"]
    end
    subgraph Provider["Third-party payment operator"]
        BM["Scoped management / reports<br/>Contract to establish"]
        BB["Batteries + ledger"]
        BS["Remote signer + provider-funded wallet"]
        BT["Ticket event transport"]
        BM --> BB
        BS -->|"Authorize"| BB
        BS -.-> BT -.-> BB
    end
    B -->|"Provision / read evidence"| BM
    B -->|"Discover / request signing"| BS
    N["Orchestrators / Live Runner"]
    A -->|"SDK work / results"| N
    B -->|"SDK work / results"| N
```

The payment operator owns funds, wallet operations, ledger and event ingestion
in each mode. Provisioning allowance is distinct from funding the wallet.
Interfaces require compatibility evidence in both deployments. Provider
migration is not automatically lossless or seamless.

## Execution sequence: REST and MCP share core behavior

![Execution sequence](../assets/open-builder-execution-sequence.png)

```mermaid
sequenceDiagram
    actor C as REST / MCP caller
    participant E as Access adapter or enterprise host
    participant K as Shared core + persistence
    participant S as Python SDK integration
    participant P as Signer + Batteries
    participant N as Orchestrator / Runner
    C->>E: Authenticate and discover capabilities / rates
    E->>K: Validated actor and scoped request
    K->>S: Discover supported capabilities and rates
    S->>P: Read discovery evidence
    P-->>S: Capabilities, rates and source information
    S-->>K: Normalized discovery
    K-->>E: Network rates and assumptions
    E-->>C: Capability information
    C->>E: Invoke capability with operation reference
    E->>K: Authorized request
    K->>K: Persist owned job and attempt
    K->>S: Execute supported capability
    Note over S,N: Simplified payment order, verify each supported mode
    S->>P: Request authorized signed payment
    alt Payment accepted
        P-->>S: Payment material
        S->>N: Invoke with supported inputs
        alt Immediate completion
            N-->>S: Result or failure
        else Queue receipt
            N-->>S: Status / recovery reference
            S->>N: Poll supported status endpoint
            N-->>S: Result, failure or unresolved state
        end
        S-->>K: Outcome and payment correlation
    else Payment denied or unavailable
        P-->>S: Payment error
        S-->>K: Known failure or uncertain outcome
    end
    K->>K: Persist result references and status
    K-->>E: Result / failure / recoverable job reference
    E-->>C: Response or subsequent status query
    Note over C,K: Progress transport is not continuous inference streaming
```

The access adapter is part of the standalone service or enterprise host. In the
HTTP integration variant the enterprise calls that service; imported mode calls
the core in-process. Durable background execution and response timing require
implementation design; this sequence does not promise exactly-once execution,
automatic retries or cancellation. Persistent application endpoints belong to
the baseline, but do not themselves establish streaming support.

## Usage, network costs and example commerce

![Accounting and extension sequence](../assets/open-builder-accounting-sequence.png)

```mermaid
sequenceDiagram
    participant E as Enterprise / mock commerce
    participant K as Engine + job store
    participant P as Provider management + Batteries
    participant S as Signer + event transport
    E->>K: Configure access policy / allowance intent
    opt Provider allocation change needed
        K->>P: Authorized idempotent command
        P-->>K: Allocation reference
    end
    Note over E,P: Customer identity stays with enterprise, signer funding is separate
    K->>K: Record execution measurements and payment references
    K-->>E: Job / measured-usage event
    E->>E: Apply own retail policy, if any
    S-->>P: Ticket expected-value evidence
    P->>P: Deduplicate and post observed network costs
    K->>P: Read scoped accounting evidence after cursor
    P-->>K: Events and attribution / uncertainty
    K->>K: Update network-cost projection
    E->>K: Read versioned events after saved cursor
    K-->>E: Job-correlated cost / pending / correction
    E->>E: Deduplicate and reconcile retail records
    Note over E,P: Network cost, redeemed settlement and customer charge remain distinct
```

These are proposed reporting contracts, not existing guaranteed endpoints.
Mock commerce is an example/test fixture. Real customer billing may use a fixed
subscription, application usage or markup and need not await network-cost
reporting. Delayed/missing evidence is not zero; upstream event loss cannot be
repaired solely by replaying the engine projection.

## Persistence and accounting authority

SQLite plus an explicit persistence interface is the required minimum.
PostgreSQL is a delivery target, not a condition that replaces that minimum.
Both should implement the same contract for engine-owned access mappings,
jobs/attempts, result references, measured usage and cost projections, including
migrations and backup/restore. Retention must be configurable.

Enterprises can correlate stable engine identifiers with their own stores and
consume versioned events into billing/analytics. Supporting arbitrary enterprise
database schemas is not required. A PostgreSQL adapter alone does not prove
multi-instance scheduling, concurrency safety or high availability.

| Record | Authority | Meaning |
| --- | --- | --- |
| Job inputs/outputs, status and measured work | Engine/SDK execution path | What was attempted and observed; quantities only where supported |
| Allocations and ticket expected-value accounting | Batteries/payment provider | Network payment permission and observed ticket cost |
| Winning-ticket redemption | Payment operator settlement evidence | On-chain settlement; not an exact per-job cash receipt |
| Customer bill and commercial balance | Enterprise | Retail price/policy independent of network ticket settlement |

Engine reporting is a projection, not a second authoritative network ledger.
Correlate jobs, attempts, payment sessions/manifests and events explicitly; do not
assume these identifiers are interchangeable. Missing or delayed evidence is
pending/unknown, never automatically zero. Network expected-value accounting,
settlement and retail charges must remain visibly distinct.

Proposed provider management/read APIs need scoped authorization, exact units,
idempotency and stable references. Proposed reporting events need stable IDs,
versioned schemas, replay cursors and consumer deduplication. End-to-end event
completeness remains unproven. A replayable backend feed cannot recover evidence
that an upstream producer never delivered.

Allocations do not fund signer escrow. Existing evidence does not establish
strict spend reservations or hard ceilings. Revoking future access does not
reverse issued tickets, remove late fees or guarantee job cancellation. Hosted
provider switching may require credential replacement, allowance reconciliation
and handling outstanding jobs; an adapter does not make migration automatic.

## Evidence and open scope

Console `009a703d7b6434bab905902375f562e5980728af` is the pinned execution
reference. The [matrix](console-capability-and-gap-matrix.md) distinguishes
source paths from runtime verification. Additional text/media streaming is
undecided; API-key/OAuth policy and several provider
contracts are still recommendations. Diagram rendering validates syntax and
legibility, not implementation, interoperability or external commitments.
