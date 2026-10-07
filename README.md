# Perpetuity AI

Perpetuity AI is an early-stage venture developing authorization operations for digital-replica reuse, transfer, and production handoffs.

The current objective is not to build a biometric vault, generation model, or talent marketplace. It is to validate one buyer-led workflow that connects a specific request to human authority, bounded terms, vendor instructions, and a reviewable closeout record.

## Current stage

- Public company and pilot narrative
- Proposed 12-week concierge pilot
- Product requirements and authorization-packet schema
- Research-integrity and claim-register system
- Initial trust posture and threat model
- No production software, security certification, customer adoption, or legal-clearance service is claimed

## Repository map

| Path | Purpose |
| --- | --- |
| `index.html` | Public company site |
| `pilot.html` | Pilot offer, fit, phases, deliverables, and measures |
| `trust.html` | Public security, privacy, and governance posture |
| `evidence.html` | Dated evidence room and source register |
| `privacy.html` / `terms.html` | Public-preview notices |
| `docs/PRODUCT_SPEC.md` | Pilot-stage product requirements |
| `docs/PILOT_PLAYBOOK.md` | Engagement and measurement playbook |
| `docs/TRUST_AND_RISK.md` | Data boundary, threat model, and assurance gates |
| `docs/AI_RESEARCH_PROTOCOL.md` | Model-assisted research and integrity workflow |
| `docs/LAUNCH_ROADMAP.md` | Company launch gates, owners, and exit criteria |
| `docs/DISCOVERY_GUIDE.md` | Structured buyer, user, rights-holder, and vendor interviews |
| `docs/FINANCIAL_MODEL.md` | Bottom-up financial model and capital gates |
| `schemas/authorization-packet.schema.json` | Machine-readable pilot data contract |
| `templates/` | Pilot measurement and risk-register templates |
| `research/claim-register.csv` | Claims, evidence status, sources, and next actions |
| `tools/site_audit.py` | Dependency-free site-quality check |

## Local preview

```bash
python3 -m http.server 4173
```

Open `http://localhost:4173/`.

## Quality check

```bash
python3 tools/site_audit.py
```

The audit checks internal links, referenced assets, page titles, descriptions, heading structure, canonical links, image alternatives, and accidental repository promotion in rendered pages.

## Decision rule

Do not build a broad platform until at least one paid pilot demonstrates repeatable buyer value, a useful authorization packet, acceptable risk boundaries, and a path to value without central custody of raw biometric assets.
