# Pilot-stage product specification

Status: working specification  
Version: 0.2  
Decision owner: founder / accountable pilot sponsor  
Last updated: 2026-10-07

## Product intent

Perpetuity AI coordinates a project-specific digital-replica authorization packet across business affairs, rights holders or authorized representatives, production teams, and approved vendors.

The first product is an operated workflow, not a self-service platform. Its job is to reduce missing information, inconsistent review, uncontrolled handoffs, and weak closeout evidence while minimizing sensitive-data custody.

## Initial user and transaction

Primary buyer hypothesis: a production-side business-affairs, legal-operations, or production-technology owner accountable for the use of an existing or newly created digital likeness, voice, or performance asset.

Initial transaction: a reuse, adaptation, transfer, or vendor handoff in which scope, authority, restrictions, asset references, approvals, and closeout evidence must travel together.

## Jobs to be done

1. A requester can describe one intended use in a complete, comparable format.
2. A reviewer can identify the applicable authority, agreement, conflicts, and missing evidence.
3. An authorized human can approve, reject, condition, or return the request.
4. An approved vendor can receive only the instructions and references needed for its role.
5. A project owner can document exceptions, disposition, use, and closeout.
6. An authorized reviewer can reconstruct the decision and handoff later.

## Authorization packet

### Required entities

- Project and accountable requesting entity
- Participant, rights holder, estate, or authorized representative
- Human decision-makers and their roles
- Governing agreement or authority basis
- Intended purpose, context, media, territory, term, and distribution
- Digital-replica asset reference and current custodian
- Requested transformations and prohibited uses
- Approved vendors and role-specific instructions
- Compensation term reference and triggering events
- Retention, disposition, and closeout requirements

### Required events

- Request created and versioned
- Evidence attached or referenced
- Review requested
- Clarification, conflict, or exception raised
- Human decision recorded with basis
- Instructions delivered and acknowledged
- Material deviation or incident recorded
- Asset disposition or retention confirmed
- Project closed and evidence packet exported

## State model

`draft → evidence_required → under_review → changes_requested → approved_with_conditions | rejected → in_production → exception_review → closeout_pending → closed`

Every state change requires an actor, timestamp, reason, and prior version. No automated process may move a request into an approved state without an accountable human decision.

## Permission model

- Requester: creates and revises proposed use.
- Reviewer: checks completeness, agreements, authority, and conflicts.
- Approver: records the accountable human decision.
- Vendor: receives limited instructions and records acknowledgements or exceptions.
- Auditor: receives read-only access to an approved evidence subset.
- Administrator: manages access and configuration but cannot silently alter historical decisions.

Permissions must be scoped by organization, project, purpose, and time. Separation of duties is required where the buyer’s risk assessment calls for it.

## Non-goals for the pilot

- Holding raw biometric scans, voice models, performance captures, or trained model weights
- Determining legal ownership or issuing a universal rights credential
- Automatically granting consent, setting compensation, or interpreting ambiguous agreements
- Operating a talent marketplace or public identity catalog
- Monitoring the public internet for unauthorized uses
- Claiming regulatory compliance or security certification

## Pilot implementation

Use approved, access-controlled tools already acceptable to the buyer where possible. A structured data model and operated process are more important than custom code during validation. Record workarounds and repeated manual steps as product evidence.

## Acceptance criteria

- One live transaction completes from request through closeout.
- Required packet fields and exceptions are documented.
- Access and data inventory are approved before live information is introduced.
- Human approval is attributable and reconstructable.
- Vendors receive role-specific, bounded instructions.
- Baseline and outcome measures are comparable.
- The sponsor makes an explicit build, revise, or stop decision.
