> Historical review of a prior manuscript revision. The current paper scope is defined in SCOPE_REVISION.md; earlier general-program assessments are not the scope of the published manuscript.

# LULA I requirements review — round 2

Status: delegated review and source corrections complete within scope; final build and visual checks are recorded in QA.md. Scientific closure remains open.

## Complete skill-node coverage

Three delegated reviewers read the full manuscript and all Markdown entry points/reference nodes in the requested skills. Mathematics graph screening was shared between the reviewers after the principal audit. Coverage records identify each file, its SHA-256, whether it was read, and application or exclusion reasoning. The graph is navigation, not a proof certificate.

| Skill | Files covered | Missing/hash mismatch |
|---|---:|---:|
| phd-mathematics | 100 | 0 |
| phd-paper-review | 25 | 0 |
| phd-paper-formatting | 8 | 0 |
| Total, including three entry points | 133 | 0 |

See editorial/requirements-r2/COVERAGE_CHECK.json and each reviewer's REPORT.md. Unrelated algebraic, geometric and frontier results were read and excluded; no result was imported from an analogy or keyword match.

## Corrections and validation

31 exact-span changes were integrated after independent checks: 31/31 editorial integration passes and 15/15 mathematical/model passes. The prior source and PDF, individual proposals, dispositions, diffs and verification history are preserved in editorial/requirements-r2. Prose-only score remains 4/5; a score is not a scientific certificate.

The partial signing-oracle lemma and transfer theorem now include matching termination behavior. The game explicitly assigns initial/sequential snapshot handles and has no winning completion after a nonterminating request. Diagnostic state is harmless only if it preserves both response availability and signature evidence. Native exhaustion, crash, timing and fault interfaces remain outside this model.

The hash-query preservation statement now concerns adversarial oracle queries and local simulator computation. This restricts the ambiguous original total-hash wording: reference recomputation can do billions of additional honest hashes. No total signing-service cost equality or new concrete security bound is claimed.

Geometric means and setup expectations are explicitly ideal unbounded independent-trial models. Finite 32-bit candidate spaces, their exhaustion probability, and the domains and attainable range of tail formulas are explicit. This does not certify actual unconditional expected runtime or termination.

Prose fixes introduce abbreviations, qualify captions, and distinguish first measurements from minima across six attempts. Archive contents were checked; the public-source and private-research packages are now described accurately. Bibliography fixes preserve cited preprint versions, add verified published counterparts and pin SHRINCS to a byte-matching immutable commit. Reproduction command flags retain two ASCII hyphens in the PDF.

Every displayed equation, algorithm body, tabular data body and vector diagram is unchanged. Labels and bibliography keys are retained, and numerical evidence and implementation hashes match their pre-revision values. Exact integer checks and a 120-digit occupancy evaluation agree with the manuscript; the omitted occupancy tail has an analytic bound. Finite antichain/share controls and a symbolic partial-oracle countermodel are bounded supporting checks, not universal security proofs.

## Venue and user requirements

The target is IACR Cryptology ePrint, with the established unmodified LNCS layout. Current official ePrint rules require visible author identity and an A4 or Letter PDF. Conference anonymity/page caps, ACM/IEEE templates and dissertation rules are inapplicable. The exact requested title, Luis Ángel Gonzalez, angel@r-0.org, Ring0 Labs research series and Lugel Labs publisher are preserved. The public manuscript/source package must contain no internal construction identifier.

SUBMISSION_METADATA.json supplies UTF-8 title, authors, plain-text abstract and keyword phrases of at most 40 characters. No submission or license selection is performed. Rights, author agreement and final licensing are submission-stage decisions. Editorial novelty/interest and acceptance are judgments, not mechanically passed formatting checks. See formatting/VENUE_REQUIREMENTS.json for primary-source URLs and classifications.

## Scientific requirements still open

The full exact-instantiation 128-bit classical EUF-CMA reduction at the declared adaptive signing budget, quantum reduction, primitive and multi-target bounds, leakage/fault/composition analysis, search-exhaustion API and hardened implementation remain open. The 5,720-byte signature does not meet the 64–128-byte objective. Recorded medians and finite maxima do not establish one-core worst-case latency, and cache-loss signing remains expensive. A matched comparison and broad novelty assessment remain incomplete. The paper states these limits; this review does not relabel them as solved.
