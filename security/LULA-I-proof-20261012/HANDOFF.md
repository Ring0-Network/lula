# LULA I proof handoff

The complete security proof remains **OPEN**. This packet is a checked, source-bound partial development and a full obligation/verdict ledger, not a certificate of classical level 1 or quantum category 1. Do not edit the manuscript or change parameters to make a statement appear proved.

## State now

- `PROOF.md`: exact source-bound game, actual hash encodings, proposed H0–H6 reductions, structural lemmas, corrected cache theorem and explicit OPEN terms.
- `bounds.py`, `results/`, `numerics/`: all eight requested q values, independent model evaluations, exact target-sum counts and bounded toy checks. No full security total is assigned.
- `TERM-TABLE.md`: per-term verdict at 2^38,2^40,2^41.
- `formal/`: seven Lean declarations checked with pinned local Lean and AXLE, Aristotle's independently returned antichain rechecked, three EasyCrypt lemmas checked, K artifact UNCHECKED, source-attributed QROM applicability audit.
- `code-review/`: exact field/oracle/domain tables, native counter-corruption controls, namespace counts and independent second reading.
- `BASELINE.json`, `VALIDATION.json`: manuscript, PDF and implementation byte preservation and cross-lane consistency.

## Next discriminating proof obligation

Prove the shared-SHA input-encoding/prequery lemma before introducing independent primitive names. The literal PRF_msg/H_inner overlap is already demonstrated; bound the adversary's ability to hit secret-dependent inputs in a correctly coupled oracle game. Specify the raw-query transcript, hidden-input set, fresh-message behavior, shared output prefixes and primitive-key entropy. Do not assume that knowing a transmitted R never correlates with SK.prf, and do not count signing queries as free adversarial hash queries.

Then derive adaptive FORS selection under that game, rather than importing the fixed-instance average. Separately build the one-fixed-child WOTS certification reduction; the ordinary different-message occupancy model is wrong for this reference algorithm. Preserve arbitrary verification choices of R, counters, chain values and lower roots throughout.

## Unchanged interface limits

Honest rollback returns opaque snapshot handles and complete signature responses. It does not give the adversary the benchmark snapshot file, which contains the secret seed. Arbitrary accepted-counter cache corruption is a demonstrated transparency counterexample, not an honest-restoration result or an executed fresh-message forgery. Finite Option outcomes in the mechanized models do not directly encode Rust nontermination.

## Prior website task

The user changed the active objective while the website note was being prepared. Its English draft is at `C:/Users/angel/Desktop/g_lugel/lugel/website/src/content/lula-i.md`, and its preparation status is `website/docs/research/LULA-I-PREPARATION.md`. A loopback preview was started by that agent at port 3074, session 11348. The initial Ring0-style image was rejected. A Lugel-style DARK image was generated at `C:/Users/angel/.codex/generated_images/01a12c4d-c2cc-7bd3-b169-f4ee58af65a4/exec-f3767faf-e650-4e96-947a-dd868f329409.png`; LIGHT generation and final asset wiring remain pending. No old-task deployment or further image generation was performed after the objective changed.
