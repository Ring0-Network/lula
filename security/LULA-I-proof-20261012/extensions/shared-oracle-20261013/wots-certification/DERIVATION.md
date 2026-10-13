# Independent addressed WOTS+C evidence classification

**PROVED / OPEN scope:** this derivation classifies certificate evidence for one fixed WOTS address in the actual LULA I encoding. It is a structural case analysis, not an SPR theorem, a numerical reduction, or a complete EUF-CMA bound. It was derived from the pinned source and saved before reading another new WOTS proof. No manuscript, implementation or existing proof packet is changed.

## 1. Exact executable object

**COMPUTED (source binding):** release `code/lula1/src/lib.rs` has SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Relevant code is `WotsC` at 202–278; full verification accepts the digest at 720–723, reconstructs the WOTS public key at 725–726, and then reconstructs a Merkle root at 728–729. There is no independent WOTS public-key equality test in `pk_from_sig`; that function returns a node. Equality to the honest WOTS public key must first come from the addressed Merkle certification argument, or a Merkle hash witness must be charged instead.

**PROVED (source parameters):** lower layers use `(w,ell,S)=(16,32,240)` and the top uses `(256,16,2040)`. Both have `z=0`, so the accepted position vector includes all 128 digest bits: 32 four-bit digits or 16 eight-bit digits. Every digit is in `[0,w-1]` and the sum is `S`. For these fixed encodings, equal complete digit vectors imply equal 16-byte digests. This last implication cannot simply be asserted for an arbitrary lossy message encoder.

**PROVED (source framing):** let `A=(layer,tree,keypair)` and `B=pk_seed[16]||zero[48]`. Define one shared truncated output function `H128(x)=first16(SHA256(x))`. Chain, compression and digest functions use different literal address types, not independently assumed hash functions:

```
F_A,i,t(v) = H128(B || ADRS(type0,A,chain=i,position=t) || v[16])
T_A(E)    = H128(B || ADRS(type1,A,0,0) || E0[16] || ... || E_(ell-1)[16])
D_A(V,c)  = H128(B || ADRS(type7,A,0,0) || V[16] || BE32(c))
```

The complete raw input lengths are 102 bytes for a chain step, 598/342 bytes for lower/top endpoint compression, and 106 bytes for the child/counter digest. Chain starts are separately derived at address type 5. Counter serialization is fixed-width big endian. At a fixed address, all these child/value framings are injective in their fixed-width fields. Equal truncated outputs do not imply equal full 256-bit SHA images.

## 2. Honest graph, exposure and arbitrary forged evidence

**ASSUMED / defined object:** fix the key and the successfully defined honest graph. For chain `i`, let `C_i(0)` be its secret start and `C_i(t+1)=F_A,i,t(C_i(t))` for `0<=t<w-1`. Its endpoint is `E_i=C_i(w-1)`. The honest WOTS public key is `PK_A=T_A(E)`.

**PROVED (honest fixed-child invariant, manual source argument):** the honest child `V` at an address is fixed. The successful canonical search chooses its smallest accepted 32-bit counter `c`; write `x=digits(D_A(V,c))` and `X_i=C_i(x_i)`. Every honest completed signature at this address returns that same counter/vector/chain-value tuple. Existence of the canonical result presupposes successful search; the source's counter can otherwise wrap or panic. This document does not turn the search into a total algorithm.

**DEFINED / ASSUMED exposure flag:** separately record whether the adversary actually received the canonical certificate `(c,X)` at this address. The honest graph and canonical vector may exist at an unqueried address; that does not mean its chain values have been exposed. The one-exposure attack model permits this certificate and ordinary public hashes, not arbitrary private-context access or another accepted cached counter returned by the real secret-key signer.

**PROVED (source-controlled forgery fields):** the verifier may receive arbitrary `V*`, `c*`, and `ell` chain values `U_i`. `V*` is the previous reconstructed FORS/root value, not necessarily its honest counterpart. It checks acceptance of `e=digits(D_A(V*,c*))` but does not check minimality of `c*`. It computes

```
C*_i(e_i) = U_i
C*_i(t+1) = F_A,i,t(C*_i(t))  for e_i <= t < w-1
E*_i = C*_i(w-1)
PK* = T_A(E*)
```

before its Merkle step. The comparison below is to the entire honest graph at this chosen address, not only previously observed paths.

## 3. Complete structural split

**PROVED (class 0, no PK binding):** if `PK* != PK_A`, no WOTS certificate for the honest key has been established. The enclosing Merkle/hypertree argument must classify this altered leaf against the honest routed path. Acceptance of the target-sum predicate alone cannot eliminate this class.

**PROVED (class 1, endpoint compression witness):** assume `PK*=PK_A`. If `E* != E` as endpoint vectors, their fixed-length concatenations differ. Hence the two distinct type-1 raw inputs have the same `H128` output. This is an explicit same-address endpoint-compression witness. It is not an assumed collision-resistance fact and does not require an exposed signature at the address. A security reduction must still embed the correct honest compression target.

**PROVED (class 2, position-labelled chain merger):** now assume `E*=E`. If some `U_i != C_i(e_i)`, compare the forged and honest chain states at the same positions from `e_i` through `w-1`. They differ initially and agree at the final endpoint. There is therefore a position `t` with

```
e_i <= t < w-1,
C*_i(t) != C_i(t),
F_A,i,t(C*_i(t)) = F_A,i,t(C_i(t)).
```

The two framed inputs differ at the same chain address and step label. This is a truncated-output collision/second-preimage witness relative to the honest chain input at `t`. In particular `e_i=w-1` cannot have a changed initial value and the same endpoint. The witness does not follow from comparing unlabelled iterated chains: the position label matters.

**PROVED (class 3, genuine predecessor):** if no class-2 discrepancy exists, every forged start is exactly `U_i=C_i(e_i)`. If `e != x`, the two accepted vectors have equal sum `S`, so at least one coordinate satisfies `e_i<x_i`. Advance the forged value from position `e_i` through position `x_i-1`. This obtains a value `Z=C_i(x_i-1)` satisfying

```
F_A,i,x_i-1(Z)=X_i=C_i(x_i).
```

Since `x_i>=1`, this step exists. It is a preimage witness for the honestly exposed position value when the exposure flag is true. It need not be a different-input collision: `Z` may be the genuine predecessor. A generic SPR hypothesis does not by itself cover this route. If some changed starts already yielded class 2, that class suffices and no claim that the other starts are genuine is needed.

**PROVED (class 4, digest/child/counter witness):** the remaining case has `e=x` and every `U_i=X_i`. For this source's full digit encoding, `D_A(V*,c*)=D_A(V,c)`. If `(V*,c*)!=(V,c)`, the fixed-width child/counter inputs differ, giving a type-7 digest target-collision witness. This includes a different child with the same vector, a different counter for the same child with the same vector, and both fields changed. The vector's antichain property does not rule out any of these hash-binding routes.

**PROVED (class 5, canonical equality):** if also `(V*,c*)=(V,c)`, the whole WOTS certificate is identical to the mathematically canonical certificate. With a true exposure flag this is certificate reuse, not a standalone fresh-child forgery. With a false exposure flag it is correct but **unexposed** evidence; it must not be assigned zero probability or called transcript replay. Its acquisition remains a security obligation.

**PROVED (exhaustiveness):** these alternatives follow by Boolean splits on public-key equality, endpoint-vector equality, existence of a changed start at its accepted position, accepted-vector equality, and child/counter equality. They require no collision-resistance or preimage assumption. Equal sums imply `e>=x` coordinatewise only in the equal-vector case; hence an exclusively forward derivation from one exposed vector cannot produce a different accepted vector. This observation is only one branch of the full split.

## 4. Unexposed addresses require another reduction route

**PROVED (structural predecessor at an endpoint):** in class 5 with no exposure, or in the all-genuine-start part of class 3 without using exposure, the accepted sum satisfies `S<ell*(w-1)` for both selected configurations. Consequently at least one chain has `e_i<w-1`. Advancing its genuine forged value to position `w-2` gives a preimage `Z` of `E_i` under `F_A,i,w-2`. The honest endpoint vector and the relevant target may be hidden inside compressed/Merkle data, so this is an evidence witness relative to the full graph, not a ready-made ordinary PRE challenge reduction.

**OPEN — smallest unexposed-key lemma:** provide a multi-instance, addressed endpoint-preimage or secret-start security experiment whose challenge can be embedded in the simulator's honest graph while it supplies the public key and all other signing responses. Show how a certificate at an adaptively selected unqueried address yields a solution, with correct side information, target distribution, prequery accounting and loss. Merely declaring an unqueried canonical certificate “equal to honest” does not discharge this term.

## 5. Why these witnesses are not automatically ordinary SPR/PRE reductions

**OPEN — compression/digest target embedding:** the honest type-1 endpoint string and type-7 `(V,c)` input are functions of the key graph, shared public hashes and canonical acceptance search. The adversary chooses its forgery address, child and counter after seeing earlier transcripts and may prequery the relevant raw domains. A quantitative theorem must specify which targets are committed when, whether the challenger supplies preimages, how distinct addresses are guaranteed, and how the simulator answers all other computations. The desired lemma is an addressed selected-target/selected-counter TCR bound for this exact framing, not an unqualified collision bound for SHA.

**OPEN — chain merger embedding:** the class-2 honest input `C_i(t)` is at a position selected by the forgery and depends on iterated chain evaluations. It is not automatically an independent uniformly sampled SPR challenge. Define the target family `(A,i,t)`, the allowed exposure of chain suffixes and compressed endpoints, the simulator's unknown preimage obligations and the adaptive target-selection loss. A witness at an unknown honest node is structurally valid even when producing the target instance efficiently is not established.

**OPEN — backward-preimage embedding:** class 3 targets the exposed `X_i` under function `F_A,i,x_i-1`, whose position is selected by the canonical digest and forgery. The reduction must simulate the honest child/counter grind and the chain segment without knowing the embedded challenge predecessor, while preserving all published endpoints and responses. This is one-way/preimage security with particular auxiliary information and address selection. Its distribution cannot be justified merely by writing “random oracle” or quoting a `w*ell` union factor. **CITED:** the repaired WOTS security proof distinguishes preimage, undetectability and target-restriction obligations; these cannot be silently dropped ([Hülsing–Kudinov, ePrint 2022/346](https://eprint.iacr.org/2022/346)). This citation is context for the missing obligation, not an application of that theorem to LULA I.

**OPEN — counter/resource accounting:** digest target search on raw hash candidates and search conditional on acceptance use different denominators. For a single fixed 128-bit vector, ideal fresh raw-digest equality would have probability `2^-128`; conditional equality among accepted vectors would involve the slice cardinality. Neither probability is established against this adaptively selected actual target by the antichain lemma. Every reduction needs its actual oracle queries, grinding work, target count and completion contract; this document supplies no numerical `w*ell` loss.

**PROVED (event-union interpretation only):** a union bound is available for the probabilities of the witness classes **in the same fully specified game** once they are defined as actual extraction events. Replacing those event probabilities by standard primitive insecurity functions requires the missing embeddings above. No complete-signature advantage sum is asserted here.

## 6. Honest cache scope and final verdict

**PROVED (scope distinction):** honest restored caches preserve the fixed child and canonical vector. An accepted noncanonical cached counter can make the real secret-key signer reveal another position vector at the same address. That is additional exposure, so the one-canonical-exposure premise no longer holds; its genuine predecessors cannot be called an adversary's preimage breakthrough. The existing corruption control addresses that larger interface, not an honest-rollback failure. Arbitrary cache writes remain outside the one-exposure certification model.

**PROVED — useful progress:** the source-bound classification covers endpoint compression, position-labelled chain merger, genuine predecessor recovery, equal-vector but different child/counter, and canonical certificates at both exposed and unexposed addresses. It corrects the incomplete claim that antichain safety alone proves one-time WOTS+C security.

**OPEN — printable status:** “The addressed WOTS+C verification evidence admits a complete structural classification. Quantitative selected-target, chain-preimage and unexposed-key reductions for the actual construction remain unestablished.” No full-security, signing-capacity or QROM claim follows.

## 7. Small mechanized components

**PROVED / COMPUTED:** `ChainEvidence.lean` checks eight declarations with the existing pinned local Lean 4.28.0 / Mathlib commit `8f9d9cff6bd728b17a24e163c9402775d9e6a365`. `chain_start_equal_or_witness` and `changed_chain_start_witness` prove that two different starts evaluated through the same address-labelled suffix and ending at the same node yield a same-address, different-raw-input/equal-output witness in both traces. Single-node framing injectivity is proved by prefix cancellation. `run_append` and `last_step_preimage` certify the dataflow for explicitly advancing a supplied start through a known last step. `sum_monotone` and `fixed_sum_antichain` check the forward-order/equal-sum argument.

**PROVED / scope:** the finite suffix address list explicitly carries the chain/position labels. The mechanized witness records trace membership, not a separately certified first/minimal merger index or extraction runtime. These declarations do not encode the entire WOTS classification, digest-bit decoding, endpoint-vector concatenation or source refinement; those parts above remain explicit manual structural arguments. In particular the last-step result proves a concrete preimage equation, not its computational hardness.

**COMPUTED (reproduction):** run `python check.py` in this directory. The actual pinned local checker returned exit 0 without warnings/errors. `#print axioms` for the eight declarations uses only `propext` and `Quot.sound`; two dataflow declarations use no axioms. No `sorry`, admission, `native_decide` or new custom axiom occurs in the Lean source. Source SHA-256: `453643faa6f720424819e0b48562bd857fd99929faa93c023b8baa074e4388d1`. `check.json`, `check.log`, `STATEMENTS.json`, source binding and hashes preserve the verification scope. No cryptographic implementation source was uploaded to a service.
