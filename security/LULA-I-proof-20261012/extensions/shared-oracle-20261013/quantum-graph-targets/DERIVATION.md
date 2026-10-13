# Quantum alternative-input target event for the honest typed graph

Independent derivation from the previously source-derived type0..4 ghost graph and the verified primary average-search theorem. Saved before the coherent simulation control. No other new quantum-lane proof was read. Scope is one information-theoretic collision event, not a complete QROM signer proof or a NIST category claim.

## 1. Primary theorem verification

**CITED(primary).** Andreas Hülsing and Mikhail Kudinov, *Recovering the tight security proof of SPHINCS+*, [ePrint2022/346](https://eprint.iacr.org/2022/346), §8.2, Definition9 and Theorem4 (attributed there to HRS16). For the average search problem on Boolean f drawn pointwise from the Bernoulli distribution D_lambda, a quantum algorithm with Q_B queries satisfies

    Succ <= 8 lambda (Q_B+1)^2.

The theorem concerns outputting ONE classical x with f(x)=1. It does not speak about measuring a quantum query history or simply replacing a classical union-bound Q by Q^2.

**COMPUTED / primary reading.** The current ePrint metadata page was accessible; its live PDF endpoint returned403. Two pre-existing local PDF copies have identical SHA-256 `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Direct `pdftotext -f23 -l23 -layout ... -` on the cached PDF verified Definition9 and Theorem4 on physical page23. No private source was uploaded. The local source is `M-measure/M2-sphincs-reparam/refs/eprint_2022_346_hulsing_kudinov_tight.pdf`; the other is `R8/R8B-immutable-authority/refs/eprint-2022-346.pdf`.

## 2. Explicit conditional experiment and finite encoding

**ASSUMED / inherited graph premise.** Fix a nonzero public seed S, independent key coins/ideal private maps, the complete designated type0..4 graph G, and the actual entire outside-domain FUNCTION TABLES. Honest designated inputs form an own-domain-blind finite DAG. The source-derived eager sampler has the ordinary complete-SHA random-function marginal. Conditional on this graph/outside-function view, all alternate input images in selected address domains remain independent uniform256-bit values. Conditioning on arbitrary adaptively generated outside-query LOGS instead would be invalid; query inputs can encode a previously read residual.

**PROVED — finite query-register interface.** Fix a finite maximum raw input length L large enough for the source's selected payloads, and encode each finite raw string injectively by an explicit length field and padded contents into an m-bit register. Invalid register words have a known eligibility mask and are given an independent outside value. A finite-register quantum algorithm can be embedded in this interface; a claim for unbounded register sizes needs a separate limiting formulation. Different lengths never alias solely because of padding.

Define e(x)=1 iff x is a valid encoded raw input `S||zero[48]||A||payload`, A is a legitimate type0..4 address, and payload differs from its designated honest payload. For each such x, let p_x be the honest target image's first128 bits. The selected event is an eligible alternative point whose first128 output bits equal p_x. Designated points themselves are known and are NOT marked by this event. All other inputs are outside the event.

**Boundary:** giving G includes secret-start payloads and can enable signature generation. This is an intentionally stronger SIDE-INFORMATION experiment for the target event alone, never the actual EUF game. Outside function tables and G are fixed independently of the residual Boolean marks below; they may be granted without increasing mark-query counts.

**PROVED — optional actual-RO private-start variant.** For this target event alone, independent ideal F/J maps are not essential. The graph can instead start with actual type5/6 outputs from their disjoint outside restrictions, conditioned on the fixed seed coins. On nonzero S, the secret-prefix message-randomizer input also has S at bytes16..31 and cannot belong to a selected addressed input language. Those whole outside functions and secret coins are permissible extra side information for target search. This variant proves no PRF/message-randomizer pseudorandomness and no complete signer security; it only preserves the selected graph's own-domain-blind residual argument. Quantum private-input replacement remains a separate obligation if needed for other branches.

## 3. Distribution-preserving Boolean factorization

**PROVED.** Independently sample B(x)~Bernoulli(lambda), lambda=2^-128, for ALL m-bit register words. At each eligible x, independently sample

    V1(x) = p_x || uniform128-bit tail,
    V0(x) = uniform256-bit value with prefix DIFFERENT from p_x.

These value-pair tables and B are mutually independent given G/outside tables. Set O(x)=V_(B(x))(x) for eligible points. Use the fixed honest full image at designated points and the independently supplied outside value at other points. The mixture weights give probability2^-256 for every eligible full output, and independent marks/value pairs give independent residual images across points. Thus the source's FULL256-bit function distribution is preserved, not merely its Boolean target predicate. At eligible points the collision predicate equals B(x) exactly.

For ineligible points, B is sampled but ignored. This lets the reduction use the primary theorem's iid Boolean oracle over the entire register universe rather than asserting a theorem for forced-zero marks on known designated points. If the reduction outputs an eligible marked witness, it wins ordinary average search. A default output when no witness exists may win accidentally; that only makes search success an upper bound for the target event.

## 4. Coherent function-oracle simulation and exact query cost

**PROVED — simple safe implementation.** In the standard XOR function oracle, compute B(x) into a clean ancilla, XOR the appropriate full value V_b into the output, and uncompute the ancilla. This uses TWO Boolean queries per simulated full-function query. Outside/designated branches can ignore the value. This already gives a valid conservative query reduction.

**PROVED — one-query information-theoretic refinement.** For eligible x, put delta_x=V0(x) XOR V1(x), which is nonzero because their prefixes differ. Choose a nonzero pivot bit and a known reversible linear map T_x that sends delta_x to that pivot basis vector. All these maps depend only on the independent value-pair tables, not on B. To simulate output XOR O(x):

1. XOR V0(x) into the output (or the fixed outside/designated value on ineligible x).
2. Apply T_x on the eligible output register.
3. Start a one-bit ancillary register in |+>. On eligible x only, swap the pivot output bit with that ancilla.
4. Make ONE Boolean XOR query `a <- a XOR B(x)` for every branch.
5. Undo the controlled swap and T_x.

On eligible x this XORs B(x)*delta_x into the translated output. On ineligible x the ancilla stays|+>, so XORing B(x) acts as the identity. In both cases the ancilla returns to|+> and is unentangled with the input/output. The resulting action is exactly `|x,y> -> |x,y XOR O(x)>`, including coherent superpositions across eligible and ineligible points. It does not assume a free controlled Boolean oracle or measure x. The inverse source oracle is the same XOR action and has the same cost.

**ASSUMED resource model / efficiency boundary.** Complete value-pair/outside tables and T_x lookups are permitted as arbitrary finite circuits independent of B. They can be exponentially large. This is a query-complexity/information-theoretic reduction, NOT an efficient black-box challenge embedder. The primary paper's mention of limited-independence simulation does not by itself prove an efficient simulator for this huge conditioned graph and these prefix-excluded value pairs. If the one-query refinement is not independently accepted, use the explicit two-query implementation and its larger bound.

## 5. Pre-key queries and honest work

**PROVED — no reprogramming.** Sample S, G, outside functions and the completed residual factorization consistently at time zero, then withhold disclosures to match the real chronology. Conditional on fixed S, the completed raw O marginal is ordinary; therefore all pre-key superposition queries act on the same oracle later used at verification. Exposing G earlier merely strengthens the target-search algorithm. Nothing is resampled over a prior quantum query, and no query transcript is measured to locate targets.

Honest type0..4 computation uses designated graph inputs only. Other honest functions belong to the outside restrictions in the nonzero-S branch. Their work can be simulated from graph/outside side information without a Boolean mark query. This claim is about the scoped target event, not about their efficiency or quantum signature security. Superposition signing interfaces and noncompletion observations are not newly invented here.

## 6. Observable final-verifier extraction

**PROVED — event definition.** Let A make at most Q coherent complete-SHA queries and eventually output classical message/signature bytes. Run the ordinary final verifier and record its actual classical target-family input/output calls. Event E_graph occurs iff this trace contains some eligible point whose node prefix equals its designated same-address target. The event is observable after this verification; it is NOT 'a marked point appeared somewhere in an earlier quantum query superposition.'

Knowing G, the reduction outputs the first such alternative point if one appears. It need not extract or measure A's quantum query history. The verifier's payloads may depend on previous verification answers and altered path fields; this is allowed adaptive oracle use. The fixed source verifier has at most3217 type0..4 complete-hash calls. Its five type7 checks and two unaddressed message calls use outside functions; they add no Boolean queries here. Repeated or designated target calls can be optimized away, but3217 is a deterministic conservative cap.

Thus the one-query implementation uses at most

    Q_B <= Q + 3217.

The classical verifier calls can be simulated using the quantum XOR oracle on basis inputs and measuring its full output, as in the actual classical trace. Counting them conservatively as mark queries is valid, although the resulting bound is not tight for purely classical verification. If E_graph occurs, the output witness is eligible and B(x)=1. Applying the verified average-search theorem gives

    P(E_graph | fixed nonzero S) <= min(1,8*2^-128*(Q+3218)^2).

With the two-query implementation instead,

    P(E_graph | fixed nonzero S) <= min(1,8*2^-128*(2*(Q+3217)+1)^2).

**CITED+PROVED boundary.** The8 and+1 come from the primary theorem;3217 comes from the exact source verifier inventory. The quadratic bound follows from the explicit coherent oracle reduction and witness extraction, not a casual replacement of Q by Q^2 in the earlier classical term.

## 7. Unconditional seed branch and remaining scope

**PROVED — uniform public seed.** For an unconditioned uniform S, charge its zero branch with success at most one. A conservative one-query bound is

    P(E_graph) <= min(1,2^-128 + 8*2^-128*(Q+3218)^2).

Seed selection must be independent of the raw oracle and any pre-key interaction, as in the inherited game. A caller choosing keys after quantum inspection is a different interface. No successful-setup conditioning or survivor-posterior renormalization is performed. Sharing this zero-seed charge with another game hop requires a common joint argument rather than silently subtracting it from separate unconditional inequalities.

**OPEN — complete QROM signer and efficient reductions.** This scoped event does not cover honest-node reuse, unexposed secret starts, FORS coverage, message/target-sum binding, private function replacement, full-verifier classification or quantum game composition. Earlier classical privatization/coverage bounds cannot simply be reused for quantum queries. A full-graph side-information experiment is particularly unsuitable for claiming unforgeability. No complete QROM advantage, quantum signing limit or category1 certificate is established.

**Final scoped status:** a distribution-preserving quantum average-search reduction is derived for the OBSERVABLE final-trace same-address alternative-input collision branch, with declared finite registers and information-theoretic tables. Its one-query simulation refinement passed the finite coherent control and awaits independent review; the two-query fallback is explicitly available.

**COMPUTED — coherent control.** `python -I -B control.py` returned exit0. The3-bit finite analogue checks73,728 basis vectors with a|+>ancilla (147,456 raw basis terms) over144 independent value-pair worlds and all16 Boolean mark tables. The compiled one-query XOR oracle matches the full function action and restores an unentangled|+>ancilla in every case, including coherent eligibility masking. Linearity extends these basis identities to arbitrary superpositions. The independently weighted Bernoulli1/4 mixture gives all64 pairs of residual3-bit images probability1/64. This validates the finite circuit/factorization control, not the full source theorem or an efficient simulator.
