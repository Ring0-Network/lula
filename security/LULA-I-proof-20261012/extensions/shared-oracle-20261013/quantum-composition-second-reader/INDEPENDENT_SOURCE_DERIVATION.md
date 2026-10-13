# Independent finite-QROM reference winning classification and composition

Saved before reading any root quantum-composition candidate. I re-read the actual final verifier and the accepted private/event lemma statements; the source classification below was derived directly. The C envelope remains a **conditional premise** pending its code-lane review. No unconditional complete-signer conclusion is promoted by this first save.

## 1. Subject, experiment and accepted interfaces

Pinned `release/code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Final verification at679–730 parses fixed-length bytes, computes a full256 message digest, enforces the omitted FORS digit, reconstructs17 leaf/path proofs, and processes five accepted WOTS+C layers. Chain completion/signing are at239–275. The lower four layers use32 base16 digits of sum240; the top uses16 base256 digits of sum2040. Both widths decode all128 digest bits and z=0.

The adversary has a finite injective raw-query register, Q coherent complete-output public-RO queries (including pre-key/local hashing), and q initiated classical atomic signing requests across all branches. Its final forgery is classical bytes. Private seeds K/P/S have independent uniform128-bit entropy supplied by the game, not enforced by the seed-copying Rust API. Only completed signatures and opaque honest snapshot handles are public. Timing, partial buffers, cache/seed contents, coherent signing, interruptions and arbitrary cache corruption are excluded. Noncompletion is absorbing/nonwinning.

Define N=2^128. Work conditionally on each fixed nonzero S, then charge the zero branch once. The accepted joint private replacement has fixed-nonzero event distance

```
delta_priv(q,Q) <= min(1,2Q/sqrtN + (2q+2)/N).
```

The +2 includes the actual final classical verifier's two possible private-P nominations. This is not merely a pre-verification transcript statement. Its reviewed author/private-source statements and `quantum-private-second-reader/REVIEW.md` explicitly account for setup, adaptive classical CQ handlers and full256 queries. Honest source-internal hash work is not an adversarial query charge.

All remaining events below refer to the **same ordinary HJ ideal-private source marginal**, not to a sequential chain of incompatible auxiliary exposures.

## 2. Events defined in the ordinary HJ final trace

-G: an evaluated type0–4 point has the same128-bit output as its canonical same-address target but different raw payload. This includes chain mergers, PK compression, hypertree parents, FORS leaves/parents and FORS-root compression.
-H: the final classical verifier evaluates a genuine still-legitimately-undisclosed chain predecessor or FORS leaf secret. Known records completed legitimate FORS disclosures and whole WOTS forward suffixes, permanently across branches; endpoints are initially known. It is coordinate-based, not numerical-alias closure.
-D7: a final type7 point at a successful canonical row has its accepted canonical128-bit digest slice but a different child/counter input. Canonicality is signer-side; the public parser checks acceptance, not minimality.
-C: the final raw digest satisfies the omitted zero digit and selects17 canonical FORS leaf indices all previously disclosed at its selected instance. Bounding this raw event is sufficient; the C lemma need not include every later verification condition.

These events are observable/classifiable from the classical final verifier plus its private canonical graph/exposure history. None asserts that a quantum superposition previously touched a hidden point.

## 3. Winning classification from source, top down

Fix any ordinary HJ world and a valid fresh final signature. Its computed top root equals the public canonical root. The raw address/route schedule is fixed by the final digest and indices. If a reconstructed leaf/path/child input differs while its addressed output equals a canonical target, the first divergence/merger in that path yields G. Thus, in the absence of G, the top authentication siblings/leaf and the top computed WOTS PK are canonical for that route.

The type1 endpoint compression also gives G if its full input vector differs from canonical endpoints but its PK output is canonical. Without G every verifier endpoint vector is canonical. In an individual position-labelled chain, starting from a different node at the same declared position and reaching the canonical endpoint creates a first same-address equal-output/different-input merger, again G. If zero hashes remain, the signature node itself is the canonical endpoint. Consequently no G implies every chain signature value is exactly the canonical node at its declared digit position.

For an unexposed WOTS key, only endpoints are initially known. Since an accepted fixed sum is strictly below `ell*(w-1)`, at least one declared digit is before the endpoint, so its first completion hash evaluates a genuine hidden predecessor: H.

For a legitimately exposed key, honest canonical signing always emits the same digit vector e_A. Its known suffix at chain i begins at e_A[i]. If a final digit e'[i]<e_A[i], its first hash is a genuine hidden predecessor, giving H. Otherwise e'>=e_A componentwise. The equal accepted sums imply e'=e_A by the fixed-sum antichain. The no-G condition then gives the same chain evidence vector as the honest signature.

The full128 decoder is injective for these widths, so equal accepted digits imply equal type7 digest slices. If the final child V'/counter c' differs from its successful canonical pair, D7 occurs. Without D7 the child value and counter are canonical. An actually exposed key necessarily has a successful canonical row; hypothetical failed unexposed rows were already caught by H and need no nonexistent D7 target.

Repeat this reasoning down all five layers. In the absence of G/H/D7, the reconstructed bottom child is the canonical FORS PK of the selected instance. If its17-root compression input differs, it gives a type4 G witness. Otherwise each FORS tree root is canonical. Its path reconstruction has the same route: any alternative secret/leaf/path yielding that root gives a first type3 merger/leaf collision G. Hence, without G, every final secret is the actual canonical secret at its selected leaf, with canonical siblings.

Every such canonical secret not previously legitimately disclosed is used by its final height0 leaf hash and gives H. Absence of H therefore means all17 selected leaf secrets have already been disclosed. Together with the source's zero-digit check, this is C. Pointwise,

```
Win_HJ => C union H union G union D7.
```

The argument handles a quantum adversary because only its final output/verification is classical. It does not extract or rewind a quantum query history. It uses the actual chain/PK/tree reconstruction and full-digit fixed-sum predicates; same-tweak SPR alone would not supply the event probability bounds.

## 4. Accepted event bounds and disjoint proof devices

On the same fixed-nonzero ordinary HJ experiment, the reviewed event results give

```
h(Q)=min(1,(2Q+sqrt3017)^2/N),
g(Q)=min(1,8*(Q+3218)^2/N),
d7(Q)=min(1,8*(Q+6)^2/N).
```

3017 counts17 FORS leaf calls and3000 chain hashes in the hidden terminal finder. Its common stopped examiner does not add those calls to coherent Q. 3217 counts all final type0–4 complete-hash calls in the graph-search reduction; its theorem+1 gives3218. D7 has at most five final calls, hence theorem+1 gives6.

Each auxiliary experiment preserves/projectively bounds its original HJ event. H exposes only safe graph outputs and suffix-closed legitimate disclosures; G may grant an entire canonical graph for its collision event; D7 grants canonical row targets and independent residual data. These stronger information views **must not be merged** and applied to another event. A union of their original-game event bounds requires no independence between events and creates no common auxiliary advice package.

## 5. Conditional C envelope

Until its source/code review passes, retain a symbol c(q,Q) for an applicable ordinary HJ C-event envelope. Its independently reviewed search stage, under exogenous q-template/Ui premises, and root candidate algebra suggest the following explicit **conditional** instantiation:

```
p_F(q) = (1/512) E[(1-(511/512)^K)^17], K~Bin(q,2^-41),
M_good = N^2-N,
Delta_row = min(1,q*(sqrt((Q+q+1)/M_good)+(Q+q+1)/(2*M_good))),
A_C = min(1,Delta_row+8*(Q+2)^2*(p_F(q)+1/N+q/N^2)),
c(q,Q) = min(1,(2Q+sqrtq)^2/N
                 +(2*(Q+2)/sqrtN+sqrt(A_C))^2).
```

The honest guard/nonce projection, row-valued AR API/query ledger, partial/guard transitions and same-source marginal must be proved. The search acceptance alone is not that proof. Future q padded coordinates/labels must be exogenous independent data; adaptive message assignments are algorithm state, not independent advice. No numerical value for c or complete total is certified here while that gate is pending.

## 6. Single-seed composition

For each fixed S!=0,

```
Pr_REAL(Win | S) <= min(1,delta_priv(q,Q)+c(q,Q)+h(Q)+g(Q)+d7(Q)).
```

The private distance already includes the final checker, so no second private final-verifier charge is added. No additional global loss is needed merely because separate event reductions used augmented information: their inequalities refer to the same ordinary HJ marginal.

For independently uniform S, split on S=0 *before* composing. Assign that branch winning probability at most1 and average the fixed-nonzero inequalities. A conservative result is

```
Pr_REAL(Win) <= min(1,
  1/N + delta_priv(q,Q)+c(q,Q)+h(Q)+g(Q)+d7(Q)).
```

A slightly tighter expression weights the capped nonzero bracket by `1-1/N`. The single1/N is the common zero-seed branch. Do not start from the unconditional private bound `(2q+3)/N` and then also add every event lemma's unconditional zero-seed version. Nor may an extra charge be removed by silently subtracting it from unrelated unconditional triangle inequalities. Use their proved fixed-nonzero forms and this explicit initial split.

Key generation/signing remain partial. In the specified experiment an incomplete key or signing call cannot reach a winning completion, so no extra failure-probability term is needed for this unconditional winning upper bound. This does not mean keygen is total. Conditioning/rejection-sampling to always return completed keys changes the experiment and would require its own setup/distribution proof; no tau normalization is silently applied.

## 7. Honest rollback transfer

The source signer is deterministic in key/message and has no mutable authorization index. Honest prepared/restored/absent caches preserve the same partial reference signing function and termination status. Cached canonical counters exist after successful preparation and equal the reference's first accepted counters. Other searches are identical. The public key/verifier are unchanged.

A simulator forwards every classical Sign request to the reference oracle and implements opaque sequential snapshot handles/restores without changing cryptographic state. The same full public quantum RO is exposed in both games. Identical classical responses induce identical updates to the adversary's retained quantum state; this is a channel coupling, not merely equality of separate frozen-state distributions. There is no additional signing/hash-query loss. Permanent queried-message freshness and exposure histories span every restored branch.

Therefore the same finite-QROM bound transfers to the stated honest atomic rollback interface with q,Q preserved, conditional on the reference bound and its resource model. Simulator bookkeeping/runtime is separate; time, cache availability and private source computation costs are not leaked by this game. No statement applies to corrupted caches, mid-call restoration, partial publication, fresh/coherent signing randomness or other stronger observations without another model.

## 8. Status

The classification and conditional composition are independently manually derived from source. C remains a conditional premise until its code-lane source bridge is accepted. Full theorem/total remains unpromoted at this first save. Even after such a model-bound composition passes, it would be an information-theoretic finite-QROM statement, not a PPT challenge reduction, fixed-SHA theorem, machine-checked Rust proof,128-bit certificate or category1 claim.
