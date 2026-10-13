# Independent finite-QROM reference composition

**INDEPENDENT_DERIVATION_SAVED_BEFORE_ROOT_COMPOSITION_CANDIDATE.** Derived from the pinned verifier and the previously reviewed scoped private/C/H/G/D7 lemmas. It uses a deterministic classical-output classification, not a quantum-query-history extractor. No new root quantum composition draft was read.

Source SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Single-key fixed-parameter partial source game, finite injective full256 raw-string register, uniform independent K/P/S, classical atomic honest keygen/signing, globally at most q initiated signing calls and Q coherent adversarial raw-oracle calls, one classical final message/signature and source verifier. Only completed signatures and public key are disclosed. Failed/noncompleting setup or requests are absorbing/nonwinning; no successful-completion normalization is used. No private state/hash transcript, timing, coherent signing, interruptions, compression oracle or corrupted-cache API is supplied.

## 1. Pathwise accepting-fresh-forgery classification

Fix one ordinary JOINT F/J ideal HJ function world and its genuine typed graph. Previously completed signatures expose selected FORS secrets and the canonical WOTS forward suffix at their actual full addresses. Their union persists across all honest branches. Their selected WOTS child is fixed at each address (FORS PK or child-subtree root), and their counter is the first accepted canonical one. Let C be final zero-filter FORS route coverage by those exposures, H a final-verifier evaluated genuine still-hidden FORS/type0 input, G an evaluated type0..4 alternative-payload same-address honest-prefix target hit, and D7 an evaluated alternative type7 payload yielding the canonical128bit digest/vector at that address.

An accepting final verifier has the fixed honest top root. Traverse its selected path downward against the honest graph. At a same-address internal hash/compressor whose output equals the honest node, either its concatenated payload is the exact genuine payload or it is a G witness. Exact concatenation is injective, so absent G its selected child and siblings agree with the honest graph. This propagates from the root through the selected top Merkle path to its genuine WOTS compressed key. The latter's genuine full concatenated endpoints follow unless its compressor is a G witness.

For an endpoint-genuine WOTS chain, compare the forged accepted digit vector d' with the address's canonical d. Each vector has the same exact target sum and fixed dimension. If unequal, some d'_i<d_i; that cannot be waived by choosing other coordinates because their sums are equal. The canonical source only exposed positions d_i onward at that address. The lower position d'_i is therefore still hidden. A forged supplied start equal to that genuine position creates H at its first type0 evaluation (d'_i<d_i implies it is not a terminal no-hash position). A different supplied start that nevertheless reaches the genuine endpoint has a first differing-to-genuine transition and creates G at its position-specific address. Thus without H/G the accepted vector must be exactly d.

All128 digest bits are consumed by the lower32x4bit or top16x8bit vectors. If that vector equals d but the type7 child/counter payload differs from its canonical genuine payload, its actual evaluated type7 image is a D7 witness. Otherwise its child is genuine. Repeat this argument at all five layers; absent H/G/D7, the bottom child is the genuine FORS compressed key.

Traverse the FORS compressor and selected paths the same way. Absent G, every selected leaf image is genuine. Its supplied secret is then either the genuine leaf secret or an alternative type3 payload mapping to that honest leaf image (G). A genuine secret that was not previously exposed creates H in the actual leaf-hash call. Therefore absent H/G/D7 every selected secret has already been exposed in its bucket/tree index. The accepted digest's omitted digit is0 by the actual verifier's check. Its real17 indices consequently satisfy C. This gives the pointwise implication

    fresh-message accepting verification => C or H or G or D7.

The final message must be fresh; a repeated-message signature is not EUF freshness. R,c and every proof field are adversarial. No first-accepted constraint is imposed on the forger's c; the source only uses that rule for canonical honest exposures. The classification uses only classical final-verifier calls and equality predicates, so it is unchanged by coherent query history or auxiliary entanglement.

## 2. One ordinary HJ, distinct event views

The four lemmas all project the original ordinary HJ event probabilities for fixed nonzero S. Their proof-side advice can be different. H uses only public endpoint/leaf-image/internal-node surface and predictable suffix disclosures; it does not receive hidden payloads. G can expose the whole honest graph for its alternative-input event. D7 can expose canonical child/counter/digest rows. C's outer and inner search helpers give different independent outside tables; their adaptive assignment labels are generated rather than frozen as advice. These are separate dominating event experiments, not one stronger EUF adversary given the union of all advice. Summing their scalar bounds requires a common HJ projection, not a common secret-advice interface.

Let N=2^128,M=N^2-N and write `p_F(q)` for the exact binomial FORS coverage expectation with its forced1/512 filter factor. With the accepted conservative one-Boolean-query simulations:

    D_ROW = min(1, q[sqrt((Q+q+1)/M)+(Q+q+1)/(2M)]),
    A = min(1, D_ROW+8(Q+2)^2[p_F(q)+1/N+q/N^2]),
    C_bound = min(1, (2Q+sqrt(q))^2/N
                       +[2(Q+2)/sqrt(N)+sqrt(A)]^2),
    H_bound = min(1, (2Q+sqrt(3017))^2/N),
    G_bound = min(1, 8(Q+3218)^2/N),
    D7_bound = min(1, 8(Q+6)^2/N).

Here3217 is the final classical type0..4 cap and5 the type7 cap, with the search theorem's extra1 included. H's3017 is the classical protected-candidate finder cap in its common stop-before-hit examiner, not3017 extra coherent comparisons. C's2 counts the conservative final inner/outer examiner; its ROW cap already includes q private post-instruction reads. These are local helper allowances in separate lemmas; they do not increase the original adversary's budget or get charged repeatedly as new adversarial Q values. Q includes its own local verification computations and all pre-key raw queries.

Union on the **same ordinary HJ** gives

    Pr_HJ[Win | fixed S!=0] <= min(1,C_bound+H_bound+G_bound+D7_bound).

No independence of those events is needed. If any event's source projection were unresolved, the full total would stay null rather than replacing that term by zero. The separate coverage review in this lane has accepted the source stages1–3 and candidate envelope, subject to the root's other independent gate; full composition promotion awaits the root candidate and a separate reader.

## 3. Private hop, seed accounting, and complete reference envelope

The already accepted joint-private hop for the REAL ordinary complete RO to HJ, **fixed nonzero S**, is

    Delta_private = min(1,2Q/sqrt(N)+(2q+2)/N).

The2q counts at most two public private-family nominations per initiated classical signing service. The final+2 is one actual final source verifier's two possible public nominations. Its quantum discrepancy is averaged on an unused-key HJ prefix. It is not inferred from classical literal guessing, and it includes the full256 function values and retained adversarial quantum memory. Honest addressed setup/public graph calls are disjoint from these private families; there is no setup-query multiplier.

For each fixed S!=0 the REAL winning probability is at most this distance plus the HJ union. Average that conditional statement over all nonzero S, and charge the actual zero-seed branch with success at most1. There is **one** seed charge1/N, not one charge per event plus another private-hop seed charge. A sufficient unconditional finite-reference expression is

    B_QROM(q,Q) = min(1,
       1/N + Delta_private+C_bound+H_bound+G_bound+D7_bound).

Using uncapped nonnegative component expressions inside the final cap is equivalent for the overall envelope, but individual tables must identify their cap conventions. This is an information-theoretic query-bounded reference winning bound. It is not an efficient PPT reduction, a fixed-SHA proof, or a security-category/work-factor certification. Source refinement and those interpretations remain distinct obligations.

No extra `q(511/512)^(2^32)` is needed for this **partial/nonwinning** winning experiment: failed rows retain a latent route and never return a winning transcript. It would be a separate term in an always-completing/normalized comparison and cannot simply be omitted from such a different game. The same applies to source canonical-counter noncompletion at setup/signing.

## 4. Honest rollback transfer

The construction's secret key, ideal maps and ordinary public hash functions are fixed globally. Valid completed cache snapshots only memoize deterministic genuine graph/canonical-counter values; restoring an older valid snapshot or recomputing a missing entry reproduces the same reference signature. Messages repeated across branches reuse R,U and the same canonical source operation. The analysis exposure union is global over all branches, while the q/Q budgets count all initiated calls/queries across them. Restore cannot erase an adversary's retained quantum memory or refresh J/the public oracle.

Under that transcript-identity hypothesis the source rollback game is emulated by this stateless reference, with no additional probabilistic loss. Restoring a corrupted cache, observing private snapshots/in-flight buffers/timing, new keys, or allowing unbounded retryable calls is a different game. No performance measurement proves this identity; it rests on the accepted source canonical-cache invariant and explicit honest-restore boundary.

## 5. Numeric and promotion boundaries

The candidate sum can be computed only after all event reviews and this common-game composition are accepted. Until then numeric fields may be called candidate envelopes, and the promoted complete quantum total must remain null. At Q=2^64 the private-hop sufficient bound alone is capped1, so this envelope cannot establish a useful total at that budget. Even at Q=2^32 its2Q/sqrt(N) term is about2^-31, dominating small-q coverage/target terms. Neither statement proves an attack; both identify weakness/vacuity of the sufficient theorem.

**Outcome: INDEPENDENT_FINITE_QROM_PARTITION_AND_COMPOSITION_SAVED_PENDING_ROOT_COMPARISON.**
