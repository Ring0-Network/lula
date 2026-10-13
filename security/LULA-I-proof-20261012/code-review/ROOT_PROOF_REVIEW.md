# Independent review of root synthesis

Reviewed `../PROOF.md` and `../TERM-TABLE.md` against my previously saved source-bound game, count inventory, cache controls and second reading. No manuscript or implementation was changed.

**Verdict: ACCEPT_WITH_TWO_PRECISE_CORRECTIONS.** The synthesis does not claim a complete classical/QROM bound, does not infer a certified capacity from the FORS model, and preserves every material OPEN term. Its code semantics, adversarial fields, fixed-child WOTS invariant, omitted FORS tree, cache-corruption distinction and structural full-key-graph split agree with the independent audit.

## Correction 1: partial versus total oracle requirement

**Locator:** `PROOF.md` §2, completion-convention paragraph: “A lossless signing-oracle theorem requires a finite-search/failure model and its probability.”

**Problem:** As written, this conflicts with the explicitly declared common partial completed-call interface and the valid conditional lossless transfer in §9. Finite exhaustion is needed to claim totality or a specified finite failure response, not to simulate two identical partial computations with no response after nontermination.

**Suggested replacement:** “A theorem for a total or finitely failing signing oracle requires a finite-search/failure convention and its probability. The declared common partial completed-call interface permits the conditional lossless transcript transfer of §9 without assuming totality.”

**Check:** Source `WotsC::grind` and FORS search have `u32` increments with no exhaustion response; the exact partial interface in §2 treats a nonterminating call as preventing further completed interaction. The honest-cache lemma establishes the matching completion behavior. No universal crash/abort equivalence is claimed.

## Correction 2: bind setup mode to honest PRF invocation bounds

**Locator:** `PROOF.md` §2's “fixed key-generation algorithm(seed)” and §4's `U_cold` / `U_prepared` formulas.

**Problem:** `U_cold(q)=33,554,432+33,567,393q` is valid for cache-disabled *minimum key generation* followed by uncached signing. The parameter configuration actually prepares the top cache unless its cached flag is disabled. Prepared setup followed by `sign(...,false)` still incurs 2,181,038,080 setup PRF invocations; it cannot use the minimum setup constant. Preparation additionally searches all top canonical counters, so changing setup also changes its possible completion event. The game must state which setup mode it uses rather than silently exchanging these partial procedures.

**Suggested addition:** “The first bound applies to key generation with cache preparation disabled. The second applies to prepared setup and prepared signing. If the experiment retains configured prepared setup but queries the uncached reference signer, the honest invocation bound is `2,181,038,080 + 33,567,393q`. Setup-mode completion/conditioning is kept explicit.”

**Check:** `Signer::keygen` 518–567 consults `LayerP.cached`; each prepared top leaf derives its 16 chain starts plus all 32×32 child-layer chain starts. `SignRef` uses `sign(m,false)` but does not undo the work already performed by key generation. Independent counts in `SOURCE_AND_COUNTS.json` give these exact constants. These counts remain honest-execution counts, not an established reduction resource bound.

## Accepted boundaries

- **Full security:** OPEN cells remain unknown, never zero. Per-try FORS work exponents are separate from a probability bound at a fixed query budget.
- **Tree classification:** Comparison is with the complete honest graph, including unseen routes. Changed internal child pairs, compressed endpoint changes, chain/digest certification and FORS changes are all acknowledged; challenge embedding/time/query losses remain OPEN.
- **Hybrid ledger:** All real-to-ideal transitions are explicitly proposed, with simulator consistency and extraction obligations OPEN. No informal “similarly” closes a missing reduction.
- **Cache corruption:** Alternative accepted counters, invalid used paths, ignored top-root slots and malformed-container panics are distinguished. No arbitrary-cache abort/recompute theorem is asserted for the Rust code.
- **Cache disclosure:** Payload recomputability with sk is not public reconstructibility; the seed-bearing benchmark fixture is separated from a public auxiliary-information model.
- **Quantum:** Component square-root search reading is identified as such; no QROM theorem, universal ten-bit loss, or NIST certificate is invented.
- **Mechanization:** Checked abstract lemmas remain distinct from Rust refinement. Optional-abort model behavior is not substituted for arbitrary corrupt-cache execution.
- **TERM-TABLE:** Correct as written. `PROVED 0` applies to the different-child reuse subevent and conditional probability transfer, not full WOTS or full signer advantage.

After the two corrections above, the synthesis is suitable for a technically honest **NOT_ESTABLISHED** handback. It makes useful structural progress without turning missing reductions into assumptions presented as proofs.
