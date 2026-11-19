# Open Benchmarks Grants OS — Portfolio Verification Notes

**Status: Public portfolio prototype available; final end-to-end walkthrough pending.**

Prior automated tests exercised key workflows in an isolated browser environment. The published GitHub Pages interface has been visually inspected, but full live-browser workflow verification remains pending.

This project demonstrates program management, financial governance, operational controls, and human-supervised AI evaluation using fictional data. It is not production software. 

## Verified against code and browser interaction

| Control area | Evidence and result |
| --- | --- |
| First-time visitor | PASS: five fictional applications, two active projects, documented exceptions, seven manually authored evaluation runs, guided six-stop tour |
| Financial dashboard | PASS: 185,000 illustrative authorized in-kind value; 108,950 used; 76,050 remaining; OBG-001 301/300 expert-hour exception |
| Award reversal | PASS: prior Rejected decision cannot be changed to Approved with the old comment or a missing/newly inadequate rationale; new substantive explanation permits a structured audit event |
| Active-award editing | PASS: award terms and decision controls render read-only once Active (browser-only safeguard) |
| Legacy status | PASS: seeded Active projects explicitly identified as historical demonstration records without contemporaneous authorization evidence |
| Resource safeguard | PASS: attempted further expert-hour usage over cap is rejected; original usage preserved |
| Resource amendment | PASS: request does not change authorization; self-reported requestor cannot approve same request; approved increase updates only category authorization; prior/proposed/approved values and rationale are preserved |
| AI test cases | PASS: distinct-case coverage 4/4, duplicate model–case runs separately counted, model-specific agreement calculated using most recent run per case; all predictions simulated |
| AI human oversight | PASS: disposition requires cause hypothesis, self-reported reviewer, reference and reason; original reference not silently altered; saved data persists on fresh document load using same test storage |
| Inline submission assistant | PASS: incomplete draft flags missing required fields; completed required fields result in nonbinding readiness, with optional clarification suggestions; original submission flow still records the application |
| Inline milestone assistant | PASS: requires progress narrative, invokes existing criteria/scope heuristic, records reviewer/decision/rationale in the original scope-review history and audit; does not automatically accept milestones |
| Review queue scalability | PASS: collapsible scientific-assessment rows and keyword/status filters |
| CSV exports | PASS: structured audit, evaluation governance, resource amendments, resource ledger and project summary downloaded in automated Chromium test |
| JavaScript | PASS: no uncaught script exceptions in targeted browser regression scenarios; Node syntax check passed |

**Test environment:** Browser navigation to file:// and localhost was blocked by administrator policy, so functional tests loaded the HTML using Playwright `page.set_content()` with a mocked, persistent `localStorage`. This permits meaningful workflow tests but **is not equivalent to a deployed website or clean-origin verification**. No assertion of complete security or production readiness follows from these checks.

## Portfolio audit: LinkedIn feedback translated into evidence

| Theme | Current proof | Qualification |
| --- | --- | --- |
| Business process automation | Inline application readiness and milestone review, deterministic completeness checks, decision gates, resource calculations, mismatch categorization and CSV generation | No actual AI agent or live model-powered automation |
| Root-cause investigation | Human can select a cause hypothesis, cite evidence, document rationale and corrective action | Hypotheses are not automated causal findings or scientifically validated |
| Solution evaluation | Four authored test scenarios; latest unique-case per-model agreement, duplicate counts and detailed review history | Fictional manual predictions, not verified performance on a real model |
| Independent verification | Named reviewers, self-attested evidence references and requirement checkpoints | No authenticated reviewers, independent scientific verification or cryptographic document proof |
| Business outcomes | Fictional capacity/exception visibility and a controlled amendment reconciliation | No deployed impact, measured savings, proven reduction in turnaround or actual compliance benefit |
| Forward-looking 12-month planning | Project duration appears in applications; yearly authorization date fields | No integrated twelve-month demand/capacity forecast or scenario simulator yet |

## Remaining portfolio verification checks

1. Open the **GitHub Pages URL** from a private or clean browser; validate fresh seeded data, guide links, live navigation and reset.
2. Manually confirm the decision-control example and resource-amendment scenario in the hosted build (one focused pass, not full UAT).
3. Inspect representative exported CSV rows for numeric consistency and audit actor/before/after/rationale fields in the hosted environment.
4. Confirm publication contains no confidential employer/client research or personal information.
5. Perform a concise five-minute demo rehearsal and finalize wording: **simulated**, **self-reported**, **independent prototype**.

## Residual limitations

A single-browser static demo cannot establish server-enforced separation of duties, actual approval authority, secure file custody, non-repudiable audit logging, independent signature authentication, real model quality or validated savings. Manual entries and browser storage can be edited locally; the interface illustrates governance intent, not enterprise control effectiveness.

**Next steps:** Complete a focused walkthrough of the published portfolio prototype, verify resource authorization and key governance controls, and confirm that all demonstrated capabilities and limitations are accurately represented before external sharing.
