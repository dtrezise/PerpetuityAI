# Trust and risk plan

Status: pilot-stage design posture, not a certification  
Last updated: 2026-10-07

## System boundary

Perpetuity AI should operate the authorization control plane while approved custodians retain raw likeness, voice, performance, rig, model, and biometric assets whenever feasible.

### Control plane

Requests, structured terms, authority references, human decisions, access instructions, acknowledgements, exceptions, and closeout evidence.

### Asset plane

Protected digital-replica payloads held by approved production, studio, performer, agency, or specialist custodians.

### Evidence plane

Versioned event history and exports sufficient for authorized review, subject to retention and access rules.

## Data-class default

| Class | Default posture |
| --- | --- |
| Raw biometric or performance asset | Do not collect |
| Asset locator or opaque identifier | Collect only when required |
| Identity and representative reference | Minimize and verify through approved process |
| Contract or agreement | Reference or extract approved fields; avoid unnecessary full copies |
| Approval and decision basis | Record with actor, time, version, and scope |
| Compensation information | Store only required terms or event references |
| Vendor instructions | Deliver least-privilege view |
| Audit and security events | Retain under documented schedule |

## Priority threats

1. Unauthorized or conflicted representative.
2. Approval outside scope or after material context change.
3. Sensitive-data overcollection.
4. Cross-project or cross-tenant disclosure.
5. Vendor receives broader rights or access than intended.
6. Historical decision altered without evidence.
7. Technical provenance mistaken for legal truth.
8. Automated output treated as legal or compensation decision.
9. Retention or deletion obligation not propagated.
10. Security incident without a clear owner or evidence trail.

## Required controls before live pilot data

- Written data inventory and flow diagram
- Named controller/owner and custodian for each data class
- Approved systems and subprocessors
- Multifactor authentication where available
- Role and project access matrix
- Secure delivery method
- Encryption in transit and at rest through approved services
- Versioned change and decision log
- Retention and disposition schedule
- Backup and restoration expectation
- Incident and escalation path
- Participant notice and contractual terms
- Counsel review of the matter-specific legal boundary

## AI use boundary

Models may help classify documents, extract candidate fields, compare versions, find missing information, draft summaries, and surface possible conflicts. They may not independently determine authority, legal sufficiency, consent, compensation, or approval.

Any model-assisted result used in a decision requires:

- source references;
- output version and timestamp;
- human reviewer;
- uncertainty or exception handling;
- prohibition on undisclosed training use where required; and
- approved data environment for confidential or personal information.

## Assurance gates

### Gate A — before live data

Threat model, access matrix, tools, pilot contract, incident path, retention schedule, and participant notice approved.

### Gate B — before repeat pilots

Environment separation, centralized identity, audit events, deletion tests, restoration tests, secure-development checks, and vendor inventory operating.

### Gate C — before enterprise claims

Independent penetration test, formal policies, control evidence, response exercise, privacy review, legal review, insurance review, and selected external assurance path.

## Claims prohibited before evidence

- “Secure” without stating the tested control and scope
- “Compliant” without named requirement, scope, assessor, and date
- “Verified rights” when only an assertion or document reference exists
- “Immutable” without specifying the technical mechanism and correction process
- “Anonymous” when re-identification remains reasonably possible
- “Enterprise-ready” without operational and assurance evidence
