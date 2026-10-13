# Accepted counters do not imply canonical cache contents

Status: PROVED conditional source lemma; PROVED obstruction to a universal transparency claim in the stated row random-oracle interface. This is not an EUF-CMA attack or a quantitative unforgeability failure.

## Subject and chronology

This derivation was saved before reading the new independent cache-obstruction derivation. The publication source is `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Source anchors below refer to that exact file. Earlier parent controls are cited evidence, not a new experiment: `code-review/RUNS.md:14-18` reports an accepted noncanonical counter, changed bytes and successful verification, a rejected counter that is recomputed, and an invalid used authentication node that is returned and fails verification. No implementation, forest preparation, timing run or fresh-message forgery was executed for this derivation.

## 1. Conditional source lemma

Fix a completing reference signing execution for a message m, a genuine route and a cached layer i. Let C be the genuine child value at entry to that layer, let the genuine WOTS leaf/public key and its authentication path be intact, and let c0 be the smallest accepted counter selected by `WotsC::grind`. Assume a distinct counter c1 in the same 32-bit counter space also satisfies `WotsC::accept(digits(digest(C,c1)))`. Change only the selected cached counter to c1. All other cache entries remain genuine and all other layers complete.

**PROVED.** The cache-using signer emits a signature on the same message that is different from the reference signature and verifies against the same public key. It does not abort or restore c0.

The source selects the cached counter, subtree root and path at lines631-644. It then recomputes the digest for that counter at lines647-648. The only fallback condition is `!w.accept(&dg)` at lines649-655; the hypothesis makes that condition false. The signer derives its own WOTS chain values at line656 and serializes c1 at line657. Thus distinct four-byte counters already imply distinct signatures, even if both counters yield identical digit vectors.

For each chain j write the addressed iterated functions as f_j,0,...,f_j,w-2. The signer returns the prefix from the genuine secret start through digit x_j. Verification applies the remaining addressed functions from x_j through w-2. The two compositions concatenate to the same genuine chain endpoint for every accepted digit vector. This is exact function composition, with no inversion, randomness or hardness assumption. It follows directly from `chain` lines239-246, `sign` lines264-267 and `pk_from_sig` lines269-276. Identical compression of those endpoints gives the genuine WOTS public key. The genuine path yields the same layer root (`root_from_path` lines322-331), which restores the same input to the next layer. Induction through the remaining layers gives the same final root. The verifier at lines715-729 tests acceptance and reconstructs the root; it does not test smallest-counter canonicality. The outer message digest, FORS values and route are unchanged.

**PROVED scope distinction.** If consistency means canonical reference contents, this edited cache is inconsistent but is neither rejected nor canonically reconstructed. If consistency means a counter accepted for the genuine child plus authentic nodes, this cache is consistent in that weaker sense but byte equality fails. Neither definition validates the original universal disjunction. The sentence in the source comment at lines650-652 is stronger than its acceptance-only branch enforces.

**PROVED non-attack distinction.** Both signatures here are legitimately generated on m. Since m was submitted to signing, the pair does not satisfy the fresh-message winning predicate in the requested EUF-CMA game. This lemma alone establishes no changed advantage, compromise or loss of unforgeability. Honest canonical snapshots retain their separate exact-transparency theorem.

## 2. Parameter obstruction in a target-row random oracle

Fix any representable parameter tuple with an operational cache-using layer, a nonempty acceptance predicate and at least two available counters. Let A be the accepted set of full digest outputs for that layer, p=|A|/2^128>0, and L=2^32. Condition on the genuine key graph, genuine child, addressed WOTS key and authentic path. The target-row inputs for counters0 and1 are distinct because their literal BE32 words differ. In the independent row-restriction random-oracle interface, their outputs are independent and uniform, so both are accepted with probability p^2>0. The first counter is then c0=0 and c1=1 is another accepted counter. The conditional source lemma applies.

**PROVED within that interface.** Merely varying (a,k,d,h,ell,S), while retaining an operational cached row and nonempty acceptance, cannot make acceptance imply canonicality for every cache state and every oracle realization. Even a singleton accepted digest set does not repair the implication: two distinct counters can hit the same accepted digest and their serialized counter words still differ. Empty acceptance or removal of every cache-using layer eliminates the operational premise; it does not restore the promised cached signer.

**OPEN source-wide probability transfer, smallest remaining obligation.** To use p^2 as an unconditional probability statement for the full shared raw oracle, exhibit a positive-support completing source execution in which these two row cells are fresh under the same conditional law, including private/raw aliases, setup completion and all other rows. The conditional deterministic source lemma does not need that extra probability claim. The historical parent finite control already refutes universal transparency for its tested implemented parameters, but it is not a proof about every retuned fixed-SHA configuration.

**PROVED fixed-h distinction.** For a concrete deterministic hash the conditional lemma applies whenever two accepted counters exist for the selected genuine row. It does not assert their existence for every possible parameter tuple and every deterministic function. No parameter impossibility for EUF-CMA or a numerical security target follows from this cache-transparency obstruction.

## 3. Consequences for the requested proof

**PROVED.** The already reviewed zero-loss transfer remains restricted to honest canonical preparation/restoration, absent-cache reconstruction and the declared atomic interface. Arbitrary edited caches require a new trust/validation interface or a distinct security analysis; they cannot be admitted by silently reusing canonical byte equality. A source repair is outside the present no-code-edit scope. This negative result resolves the requested universal transparency premise as false, rather than leaving an unnamed lemma to prove.

**OPEN.** A parameter tuple restoring the original complete security target remains unestablished. This obstruction addresses a different predicate and cannot substitute for the classical/QROM advantage and resource comparison requested by T3.
