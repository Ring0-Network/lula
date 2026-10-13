# Ordinary ITSR lift with explicit counter-guess loss

**MANUAL NEW SUCCESSOR, independent review pending.** This was derived after reading the independently saved message-hash proposals, so it does not claim blindness to them. First540ae17b, context-lift514cc206 and reciprocal review/receipt are unchanged. No new peer proposal for this counter-guess argument was read. It removes the impossibility of a LEGAL ordinary-ITSR program, but may be quantitatively useless. It does not refute the earlier countermodel for the DIFFERENT canonical family H_can.

## 1. Exact total family

Fix the public full256 h. Define a public virtual total keyed family H_free with uniform128-bit key R and logical input X=Enc(S16,T16,M,c32), where Enc is injective and bounded. Parse X, compute EXACT source U=h(R||S||T||M) and D=h(U||BE32(c)||S), then output the17 real9-bit indices and a route field (S,T,I41). Thus a primary MAP with k17,t512 and route width297 produces {(S,T,I,j,J_j):0<=j<17}. A concrete bit-output layout is153 real-index bits followed by256 context bits and41 source-route bits,450 bits total. Context tags are virtual output/input metadata, NOT inserted into actual h words. This total family ignores the acceptance filter as a primitive restriction; any supplied counter produces an output, and source-eligible candidates are a subset of primary candidates. Its outputs are not claimed uniformly random450-bit strings.

Use ordinary nonce-returning ITSR from the actual official primary definition: on X the oracle samples uniform R, returns R and MAP(H_free(R,X)), and registers that pair. No canonical oracle, acceptance selection, context sampler, memoization API, commit API or same-key re-registration is needed. The security assumption is ITSR of this PRECISE linked-h lifted family, not hardness of an untagged or independently sampled-root family and not a generic450-bit RO bound.

## 2. Legal program

Let L=2^32. B executes the source pre-key phase with h and no S/pk; draws source S/ideal persistent F; executes exact source setup/root/cache partiality with the SAME h. Setup failure gives output failure. B retains its F and actual common context(S,T), so signature auxiliaries are legal and correlated.

On first source signing label M:

1. Draw g_M uniform in[0,L), BEFORE the primitive nonce R is obtained.
2. Query the ordinary target oracle on Enc(S,T,M,g_M). Receive uniform R_M and its mapped target. Retain R_M. The mapped target is NOT given to source A and is NOT used to decide the source signing digest.
3. Locally compute the source actual first accepted c0_M by searching the same h with R_M, M and finite BE32 counters. On exhaustion stop nonwinning. Otherwise produce the exact canonical source signature with R_M,c0_M and persistent F/h.
4. On repeated M reuse R_M and the exact canonical result, without another target query. There are at most q_distinct<=q_initiated oracle targets. The primary registered target uses g_M even when g_M!=c0_M; this difference is intentional and paid below, not hidden.

On the final fresh source M*, parse R*,c* and output the ordinary primary candidate(R*,Enc(S,T,M*,c*)). B may restrict output to the source winning-covered branch by running the exact verifier/classifier; an enlarged eligible-final output event also suffices. Source fresh M* ensures that candidate input was never registered, for ANY R*/c*, so ordinary pair freshness holds. Candidate c* is arbitrary; no final-counter guess is needed.

## 3. Exact source-view coupling

For every target input, the primary key R_M is uniform independent of input/guess, even though its mapped response depends on g_M. B ignores that response in every operation shown to A and performs all source signing from R_M and actual canonical c0_M. Therefore the complete source-facing marginal channel, including A's retained quantum state and local coherent h evaluations, has exactly SrcFJideal_h law and is independent of the guess vector.

One can couple by sampling ideal J for each new message, an independent32-bit guess sequence and source F/S/A randomness. The ordinary oracle's key draws use those J values; its extra reply registers are private to B and cannot influence source services. All literal h evaluations are read-only computations of the same public algorithm. Source messages may be adaptive, but their source-visible transcript/state never reads guesses. This joint independence is about B's private counter guesses, not random-function-query freshness or no-hit postselection. No coherent history is measured.

## 4. At most17 witness labels, not q counter guesses

On each source Win AND C_cov realization, each of its17 final tuples has a completed honest source response disclosing that indexed tuple. Choose deterministically the first such completed response for each j. Delete repeated message labels from this witness list. At most r<=17 DISTINCT source labels remain. Repeated labels have one identical canonical response, so deleting repeats loses no tuple witness.

The source realization determines those labels and their canonical c0 values independently of guesses. Each witness-label guess equals its c0 with probability1/L, independently. Thus conditional on the source realization,

Pr[all chosen witness guesses match]=L^-r >=L^-17.

On that event, the corresponding ordinary registered primary outputs equal the source canonical tuple sets, despite being chosen before R. They cover every final tuple. Extra primitive targets from wrong guesses can only enlarge the covering union. Bottom or downstream-source-failure branches have no source winner and contribute zero without normalization. A source winning branch cannot contain an earlier absorbing failed signature.

Consequently

Succ_ITSR(H_free)(B) >= L^-17 Pr_SrcFJideal_h[Win AND C_cov],

Pr_SrcFJideal_h[Win AND C_cov] <= min(1, 2^544 Succ_ITSR(H_free)(B)).

There is NO q^17 factor because B registers a guessed target for EVERY first distinct label, and the witness set has size at most17. There is NO loss for guessing the final counter, no seed-zero penalty in this same-h identity, and no division by a counter-success probability. The factor2^544 is enormous; this result must not be presented as an adequate128-bit security bound or an improvement to the prior RO bound.

## 5. Work and scope

Each primary target evaluates one full inner and one outer source hash plus mapping. B locally executes actual source canonical search, all source setup/sign/final/F/cache operations, bytes and public clean-h circuits. Costs of B and challenger are separately counted. B does not know an unknown hash oracle needing programming; it computes the fixed public h algorithm. Its independently sampled F and actual root/context are retained, rather than matching an external uniform root. Classical target calls and source signatures preserve post-quantum A continuation.

The ordinary primitive interface is now explicit under a precise virtual family. Existing source first proofs' gap remains a gap to a LOSS-FREE or quantitatively adequate transfer, and canonical H_can ITSR alone still does not bound arbitrary-counter candidates. The named CTAC property may furnish a much stronger direct assumption-parametric statement; this ordinary lift instead supplies a legal but potentially vacuous conventional-family bound. ITSR hardness of H_free, any useful counter-sensitive refinement, other public graph/PRE properties, complete fixed-h security/category/capacity remain unestablished. No previous scalar/source/manuscript artifact changed and zero kernel declarations added.
