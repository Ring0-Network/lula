# Second-reader review: joint shared-oracle privatization

**PROVED (review verdict, manual argument):** no blocking counterexample was found to the displayed classical statistical game-distance bounds **under the exact restricted games stated in the reviewed derivation and stress test**. The joint idealization and continued-after-Bad independence repair the earlier circular posterior argument. This is not a machine-checked statistical theorem, a Rust refinement proof, an efficient security reduction or a complete EUF-CMA result.

**COMPUTED (review binding):** the independent Merkle derivation was saved and checked before this review. I then read `code-game/DERIVATION.md` in full, SHA-256 `341b0343445c661075ea07daee26412620851cd53369e65241972d2b2009ef40`, and `code-game/STRESS-TEST.md` in full, SHA-256 `c199480100f6f9329110a4282d9cc9e4a01a8791daf674266d08b46187d84321`. I reread the actual release library, SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`, including secret splitting, all hash call sites, setup, the message hashes and final verification. I inspected the finite control source but did not rerun it or treat it as a cryptographic proof. This lane writes only this review file.

## 1. Independent reconstruction from the source

**ASSUMED (key distribution):** let `K=SK.seed`, `P=SK.prf`, and `S=PK.seed` be independent uniform 128-bit strings. The source merely splits a caller-supplied 48-byte seed at lines 498–506. It does not establish this distribution and benchmark fixed seeds do not satisfy the security experiment's secret-key assumption.

**PROVED (source encoding, manual):** the addressed secret derivation calls at 161–163, 248–250, 348–350 and 390 encode

```
D_K(A) = S || zero[48] || A[22] || K
```

with address type 5 or 6. Their raw SHA input is 102 bytes. Message randomization at 164–168 encodes

```
M_P(m) = P || S || m
```

for arbitrary finite messages. Both consume the first 16 bytes of a full 32-byte hash image. Addressed public calls use types 0,1,2,3,4 or 7. The remaining public calls are the inner input `I=R||S||root||m` at 170–172 and the 52-byte outer input `E=U||BE32(counter)||S` at 174–187.

**PROVED (separation, manual):** when `S != zero[16]`, bytes 16–31 of an addressed input are zero while bytes 16–31 of every `M_P` input equal `S`. Hence an addressed input is outside `M_P`, including all public tree/chain/digest operations. An inner input is outside `D_K` for the same reason. An outer input is outside `D_K` by its length. Public addressed types cannot hit `D_K` because the type byte differs. The source-bound exclusions survive adversarially chosen node values and repeated type-7 grinding.

**PROVED (eligibility, manual):** a raw adversarial query can supply at most one candidate key across the two hidden families on nonzero `S`. Eligible `D_K` strings nominate their last 16 bytes for `K`; eligible `M_P` strings nominate their first 16 bytes for `P`. Those two eligibility classes are disjoint. A huge private-address namespace does not make one raw string nominate many keys.

## 2. Full-image coupling and prequeries

**PROVED (manual statistical construction):** on nonzero `S`, take independent full 256-bit memoized tables `F(A)`, `J(m)` and `O_pub(x)`. Map `F` to the complete `D_K` set and `J` to the complete `M_P` set; use `O_pub` on their complement to define `O_real`. The encodings into each hidden set are injective and the sets are disjoint. Conditional on `K,P,S`, distinct raw input strings therefore receive independent uniform 256-bit images. Thus `O_real` has the correct REAL random-oracle marginal, independent of the seed coins in the ordinary RO experiment.

**PROVED (prequery treatment):** the construction must use the entire hidden sets, not only private points that honest execution has already touched. A pre-key or pre-signature raw query to a future hidden point is already a Bad event. REAL must return its fixed full `F/J` image there; IDEAL returns its independent full `O_pub` image. No later private call is allowed to overwrite a previous public reply and pretend agreement held. Sampling only 128-bit hidden prefixes would leave the full public raw-oracle reply underspecified; the reviewed text correctly samples complete images.

**PROVED / required completion detail:** on `S=zero[16]`, the disjoint reconstruction is inapplicable because hidden sets can overlap. The correct global coupling must charge this event immediately and continue REAL with its original shared-RO marginal; IDEAL may continue its defined independent maps. One may couple these runs arbitrarily once agreement has failed, but cannot replace REAL by inconsistent independent `F/J` answers on overlapping private inputs. Since the reviewed REAL experiment is defined separately before the good-event construction, this missing implementation sentence can be supplied without changing the bound. It is a clarification, not a counterexample to the stated restricted lemma.

## 3. UNUSED keys must remain unused throughout IDEAL

**PROVED (manual source-model noninterference):** after both private families are replaced jointly, the key graph, root, signature randomizers, grinding decisions and raw public computations depend on `F,J,O_pub,S` and public/adversarial coins. The numerical values `K,P` are not used in these computations. The source stores them in `Ctx`, but in the modeled IDEAL execution their only dereferencing uses are the two replaced private operations. Setup does not call `PRF_msg`; setup's other hash operations are the private derivation family or public addressed types.

**ASSUMED / interface obligation:** opaque snapshot handles and restoration-validity responses must likewise be generated and checked without consulting `K/P` or a secret-dependent serialization/hash of them. This is an explicit game-interface stipulation, not something proved by the snapshot fixture's Rust code. That fixture contains the 48-byte seed. A handle implemented by exposing those bytes, or a newly introduced validation computation depending on them, is outside the reviewed coupling until separately modeled. Nothing in “opaque handle” alone specifies a concrete Rust implementation.

**PROVED (continued execution):** the analytical Bad flag must not affect IDEAL's output, branch selection, request acceptance or stopping. Even after a hidden-point hit, IDEAL must answer with `O_pub` and continue its ordinary program. In particular its final verifier still uses the public `O_pub` interface, not a mode switch to `O_real`. Otherwise later candidate choices could depend on `K/P` through disclosed hits and the complete-list argument would be circular.

**PROVED (unconditional list lemma):** fix the complete unflagged ideal execution, including `S`, adversarial coins and all tables. Its candidate sets `G_K,G_P` are then fixed independently of the unused keys. For `M=2^128`,

```
Pr[K in G_K or P in G_P | unflagged ideal execution]
    <= (|G_K| + |G_P|) / M.
```

Average this inequality over the ideal execution. Do not condition each next guess on no earlier hit and still use `1/M`: the surviving conditional posterior is supported on the complement of earlier guesses. The reviewed stress test correctly makes this distinction. Key generation alone would not justify posterior independence for arbitrary REAL transcript outputs.

## 4. Source-bound candidate counts and final verification

**PROVED (manual count):** raw adversarial oracle access contributes at most `Q_H` candidates in total. A signing attempt computes one private randomizer `R`, one inner output `U`, and then outer calls using that same `U`. Its inner point can be in `M_P` only if `R=P`. Its outer point can be in `M_P` only if `U[0:16]=P` and `U[16:32]=S`. All outer counters share this one possible prefix candidate, including wraparound repeats. Hence each initiated Sign contributes at most two candidates for `P`, not two per grinding trial. Typed private derivations are not public hits, and the remaining honest hash calls are excluded by the parsing argument above.

**PROVED (final-verifier count):** `verify_root` checks length, then computes the inner and outer hashes once at 699–700. These contribute at most two additional `P` candidates. Remaining verification calls use types 3/4, 7/0/1 and 2; none are eligible hidden inputs on nonzero `S`. A malformed-length signature can reduce this count, never increase it. Local verification performed by the adversary consumes its raw-oracle budget. Uncharged external verifier calls would change the interface and add their own candidate counts.

**PROVED (manual game-distance bound):** let `N_I` bound initiated atomic signing attempts and assume one final challenger verification. On nonzero `S`, total candidates are at most `Q_H+2N_I+2`. With the zero-public-seed event charged separately,

```
Pr[Bad] <= 1/M + (1-1/M)*(Q_H+2N_I+2)/M
        <= (Q_H+2N_I+3)/M.
```

Until the first Bad event, coupled public responses, private outputs used by the programs, completion behavior and final public acceptance agree. Therefore the difference in probabilities of any bounded public event is at most `min(1,(Q_H+2N_I+3)/M)`. This is the displayed `+3` bound when `q=N_I`; no factor for the number of private addresses is necessary.

**PROVED (budget distinction):** if `q` instead counts completed requests and the interface permits at most one additional pending request before absorbing nontermination, then `N_I <= q+1` and the conservative bound is `min(1,(Q_H+2q+5)/M)`. The additional two are for the pending request, not a change in final-verifier accounting. Arbitrary retryable aborts, timeouts, interrupted frames or unbounded pending requests do not satisfy this convention and require an initiated-attempt bound.

## 5. Challenges and counterexamples under changed hypotheses

**PROVED (manual key-exposure counterexample in the completed-response interface):** if an adversary receives `P`, then after one completed signature on a fixed message `m` of at least 32 bytes it queries the raw point `P||S||m` and compares its first 16 bytes with the transmitted `R`. For nonzero `S`, this point is not an honest addressed input; its length differs from the sole inner input and from all 52-byte outer inputs. Thus in IDEAL its fresh raw image is independent of the private `J(m)`, including conditioning on that completed response. REAL matches with probability one; joint IDEAL matches with probability `1/M`. The conditional distinguishing distance is `1-1/M`. In the unconditioned partial experiment, a completion-weighted expression must be used instead of silently asserting probability one. Either way, exposing `P` invalidates the unused-key premise: no small unconditional loss follows from candidate counting alone. The reviewed restrictions exclude this expanded interface; the seed-bearing fixture cannot be added to its transcript unnoticed.

**PROVED (manual fixed-known-seed counterexample):** the same distinguisher applies if key generation uses publicly known fixture seeds instead of independent uniform secret components. The nonzero-public-seed parser condition alone is insufficient. This confirms why fixture verification is not evidence for this statistical key-distribution claim.

**PROVED (failure-interface warning):** a completed-query count does not bound the number of initiated requests if aborts are retryable. The displayed `+5` does not cover arbitrary aborted-query histories. The reviewed text explicitly excludes this failure interface, so this is a missing premise for any future generalization rather than a current contradiction.

**OPEN / source refinement:** compression-function oracle access, additional private-context methods, timing/telemetry or newly exposed derived payloads require renewed input and noninterference analysis. They are not automatically covered by this complete-hash RO model. Excluding them is sufficient for the reviewed mathematical argument, but does not prove that every application exposing the real Rust library obeys these restrictions.

## 6. Statistical distance, efficient simulation and EUF-CMA

**PROVED (manual statistical result only):** the joint replacement has the bounded event-probability loss above in the specified classical partial game. It is valid to avoid assuming a REAL posterior-independence lemma by first defining an ideal execution with unused keys and coupling it to REAL.

**OPEN — efficient simulator:** this mathematical coupling does not show that a reduction can emulate setup and all signing calls within a polynomial worst-case runtime or a given concrete budget. Lazy tables avoid materializing the complete address namespace, but do not eliminate large Merkle computations, private-oracle calls, memory consumption or counter-search partiality. Their execution cost must be charged in a real simulator and their completion conventions matched. Classical adversarial raw-query count and honest computation cost are different quantities.

**OPEN — complete EUF-CMA:** the IDEAL forgery advantage remains unbounded by this step. Its public inner and outer hashes are still shared, so adaptive route/coverage analysis is not established by private-map replacement. WOTS child-digest binding, chain/endpoint security, the addressed Merkle embedding, FORS coverage and composition are still required. The structural Merkle theorem already saved in this lane supplies a witness under its model, not the missing SPR/TCR challenge simulator.

**OPEN — quantum extension:** a quantum oracle query can place many possible key prefixes/suffixes in superposition. The one-literal-candidate counting argument is classical. Neither the `+3`/`+5` bound nor a casual square-root change supplies a QROM result.

**PROVED — final review status:** the manually derived joint statistical coupling is accepted **conditionally on the reviewed key distribution, shared full-hash RO, continued unflagged IDEAL execution, exposure rules, atomic partial-game convention and query counts**. Explicitly complete the zero-seed REAL-marginal clause and opaque-handle interface specification before presenting a fully specified simulator. No blocking defect was found within those conditions. Efficient reduction and full EUF-CMA remain **OPEN**.
