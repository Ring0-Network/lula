# LULA I: mechanism-focused editorial purge

The current paper has 21 pages and a 94-word abstract. This revision implements the author's request to describe the mechanism rather than narrate the execution and publication process.

## Applied changes

Removed the Implementation section, Experimental evaluation/Methods headings, compiler and priority details, workload-gate procedure, fixture/key schedules, replay inventories and the experimental-distribution figure. Selected latency results now form one short subsection within computational costs. The recovery table is summarized in a paragraph preserving its sample scope, paired median and three individual cold observations.

Removed the pending-public-deposit sentence, the unavailable-experiment list, all author TODO comments, the retained-counter-JSON reference and archival scenario-grid narration. Implementation-specific parser and seed-passing descriptions are replaced by the mechanism's mathematical interface. Benchmark history is removed from the abstract, contributions and conclusion. The conclusion explains the authorization/cache distinction and its computational consequence.

The five input files and extracted PDF were checked for TODO, manifest, deposit, fixture, campaign, audit, reproduction and execution-cutoff markers; these operational markers are absent. Security premises and domain statements about adversarial execution remain, because they define the mechanism's guarantee.

## Validation and preservation

Main and contact-free repository PDFs compile to 21 pages without unresolved references, changed-label requests or overfull boxes, and with vector fonts. All 21 main pages were visually inspected; the costs, latency tables, conclusion and final note were also checked individually. Five algorithm bodies, two lemmas, one theorem, three proofs, five equation environments, two align environments, two construction diagrams and all displayed formulas are identical to the frozen 25-page baseline. The bibliography source is unchanged. Six current table labels and 37 listed rows/fields pass the saved-data checker; its 21-table/141-field archival checks remain separate.

The conditional reference-bound premise, honest-cache and completed-call conditions, FORS+C component-only interpretation, unstable verification cells, individual cold observations, incomparable backend/state assumptions and absence of a real SHRINCS forgery remain explicit. No result was invented and no benchmark was rerun.

Exact changes, baseline hashes, validation and build receipts are in `editorial/mechanism-purge-20261012/`. The current generator is `scripts/mechanism_purge.py`; the preceding generator is guarded against restoring the retired material. Current source/release ZIPs match this revision. Earlier reports are historical records of their own cuts.

This scoped editorial review does not establish the open reference-signer security bound or publish the repository. Questions about public deposit, funding/interests and historical binary correspondence remain in repository/editorial records rather than as placeholders in the paper.

Outcome: COMPLETE_WITHIN_SCOPE.
