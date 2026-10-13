# Separate successor review: Fourier one-query completion

**PROVED (manual algebra).** Accepted independently after the base two-query review was saved. Root subject `root-keyed-review/ONE-QUERY-COMPLETION.md` SHA7def78f7f5e771e397373f7ad81c7977674669d2064a3b2ce1a31e13d31bf1f0 is a new algebraic construction, not an edit to either prior restricted-row first proof. This review preserves `PEER-REVIEW.md` and its base receipt. No numerical script, source, manuscript or earlier theorem is changed.

## 1. Exact circuit derivation

**PROVED.** In the Fourier response basis z, a translation by a known w-bit word a acts as phase `(-1)^<z,a>`. For independent fixed completions r0(x),r1(x), set delta=r0 xor r1 and compute d=<z,delta>. The unknown Boolean XOR oracle on a scratch Hadamard eigenstate contributes phase `(-1)^(f(x)*d)` and leaves that eigenstate unchanged. Applying H then uncomputing the SAME d restores clean scratch0. The additional known phase for r0 yields precisely the character of `r0 xor f*delta`. Fourier inversion therefore produces the required complete-word XOR translation.

The unknown oracle is invoked exactly once, unconditionally. Computing d, routing x, evaluating known completions, the known phase and uncomputing those registers are f-independent operations; none hides a second f evaluation. Input registers and the Fourier response are preserved except for the desired translation. The amplitude formula is exact, not up to an x-dependent global phase. Consequently it extends by linearity to every coherent input and any reference entangled with it.

**PROVED.** For side/raw-malformed words take r0=r1 equal to their SAME static full response and route to any valid payload. Delta=0 makes the scratch |+>, so the unconditional oracle acts as identity in those branches. The same circuit handles superpositions spanning changed and side regions. No controlled-U_f interface, membership measurement, support test or query history is assumed. Full256 hit and miss completions are retained; no prefix-only replacement is made.

## 2. Application and exact resource change

**PROVED, with the restricted experiment already reviewed separately.** Conditional on pre-A side data, changed-base equality marks remain independent Bernoulli(1/N). Hit/miss completions and the entire genuine-child target row are independent of those marks. Therefore M fullRaw queries can be simulated by M Boolean queries, instead of2M. Citing SPHINCS+C Appendix E, Theorem E.3 (https://eprint.iacr.org/2022/778), the sufficient component bound becomes `min(1,8*(M+1)^2/N)`.

The previous literal final-evaluation adapter still has M<=Q+1, hence `min(1,8*(Q+2)^2/N)`. The independently described NEW stopping extractor has M<=Q, hence `min(1,8*(Q+1)^2/N)`. Neither count silently changes an old program. Search success can strictly contain the full source selected winning event, so the extractor need not certify eventual root acceptance before returning its candidate.

**PROVED.** First literal BE32 accepted counter, rejected-counter correlations, lower limbs and bottom mass remain exactly the prior side data. No1/tau enters the proof. An optional tau target-existence factor can be kept unnormalized. The P!=0 structural exclusions and external single seed-zero charge remain. Every adversarial Raw call, classical or coherent, is counted; honest source work remains charged in execution resources even where its f-independent value can be supplied without Boolean queries.

This is a query bound with potentially enormous known completion/side functions. It does not establish efficient whole-oracle realization, fixed-SHA hardness, a cryptographic category, a signing limit, or a checked full-source game. No improvement of existing scalar bounds is asserted by this review.

## 3. Independent finite controls

**COMPUTED, actual execution recorded by the successor receipt.** `one_query_control.py` uses exact Fraction pairs over Q(sqrt2). Its two-bit Raw register represents two changed inputs, one same-base input and one off-length input; its three-bit response preserves complete words. Outside completions are equal in both tables. Four Boolean functions and all64 combinations of two fixed three-bit affine completion sweeps are compared on every clean input basis state and on coherent vectors spanning all four regions. These sweeps are fixed in advance of the bounded run, not selected by its results. This covers256 worlds,8,192 basis states and256 mixed-region coherent states; it is not an exhaustive enumeration of four independent completion words. Equality of these resulting matrices covers any entangled reference for each tested world. These controls supplement the general amplitude proof; they do not mechanize the cryptographic game.

The initially attempted16,384-world exhaustive completion control was stopped at the parent's request after92.96 seconds elapsed (88.5 CPU seconds). It produced no result artifact, and its source is preserved as `one_query_control-exhaustive-terminated.py`. No pass or completion count is attributed to that terminated run. The replacement bounded scope was chosen for coverage of distinct changed and side branches rather than by inspecting any result of the terminated computation.

**Verdict: ACCEPTED_MANUAL_ONE_QUERY_COMPLETION_SUCCESSOR.** No material algebraic or query-count defect found. The preserved base two-call receipt remains correct as a conservative sufficient result. This successor establishes why its factor2 can be removed using a different circuit, not by omitting mark uncomputation from the old circuit.
