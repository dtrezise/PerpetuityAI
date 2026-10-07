# Perpetuity AI project instructions

## Mission

Move Perpetuity AI toward a responsible paid-pilot business for project-specific digital-replica authorization operations. Optimize for buyer evidence, rights-holder protection, minimal sensitive-data custody, and honest claims.

## Role selection

Before substantive work, select the relevant review lenses and state them briefly. Use the smallest set that covers the task:

- product and venture strategist;
- research director and evidence editor;
- entertainment and AI policy issue spotter;
- security, privacy, and data-governance architect;
- financial and operating-model reviewer;
- UX, accessibility, and publication editor; and
- implementation and quality-assurance engineer.

Use applicable Codex skills when they materially improve the work. Delegated agents remain subject to the active system and task policy.

## Source of truth

- Public narrative: root HTML pages.
- Product boundary: `docs/PRODUCT_SPEC.md`.
- Pilot execution: `docs/PILOT_PLAYBOOK.md`.
- Trust boundary: `docs/TRUST_AND_RISK.md`.
- Research standard: `docs/AI_RESEARCH_PROTOCOL.md`.
- Claims and evidence: `research/claim-register.csv`.
- Launch gates: `docs/LAUNCH_ROADMAP.md`.

Reconcile changes across these artifacts rather than allowing them to drift.

## Claims

- Label verified facts, observations, inferences, recommendations, hypotheses, and superseded claims.
- Prefer primary or authoritative sources and include an as-of date.
- First-party vendor pages establish public positioning, not independent performance.
- Do not claim customers, adoption, legal clearance, verification, compliance, security certification, revenue, market size, or ROI without direct evidence.
- Treat bills, law, labor agreements, standards, vendor terms, and model capabilities as time-sensitive.
- Keep technical provenance separate from the truth or legal sufficiency of an authority claim.

## Product boundary

- Start with one buyer-led authorization workflow.
- Keep human decision-makers accountable.
- Prefer references to custodian-held assets over raw biometric custody.
- Do not expand into capture infrastructure, a talent marketplace, a universal rights registry, automated legal decisions, or an automated royalty engine before paid evidence supports the move.
- Record explicit build, revise, and stop gates.

## Data safety

Do not place biometric files, performance assets, confidential contracts, credentials, or personal data in repositories, public artifacts, or unapproved AI services. Before live pilot data, require the controls in `docs/TRUST_AND_RISK.md`.

## Public presentation

- Describe the project as a private-pilot venture until evidence supports a stronger claim.
- Do not link to or promote the source repository from rendered website pages.
- Keep privacy, terms, trust, evidence, status, and contact paths current.
- Do not add third-party analytics, trackers, forms, fonts, or embeds without a documented purpose and privacy review.
- Preserve responsive layout, keyboard access, reduced-motion behavior, semantic headings, and visible focus.

## Verification

For website changes:

1. Run `python3 tools/site_audit.py`.
2. Run JavaScript syntax, JSON, XML, and `git diff --check` validation.
3. Test the site in a real browser at desktop and mobile widths.
4. Check navigation, console errors, internal links, overflow, and key calls to action.
5. Confirm that no unsupported claim or repository promotion was introduced.

For research or strategy changes, update the claim register and source date. For pilot or product changes, update the related specification, playbook, risk plan, and roadmap.
