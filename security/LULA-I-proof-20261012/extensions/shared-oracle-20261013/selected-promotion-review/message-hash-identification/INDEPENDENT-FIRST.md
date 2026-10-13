# Source-first fixed-h message-hash/subset-resilience identification

Saved before reading ANY new peer proposal for this gate. Source lib.rs SHA256ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. This derives a conditional message-hash coverage adapter, not fixed-SHA hardness, a new complete signature bound or an identification of HJ[h] with HJ[O]. No old proof, source, scalar or manuscript is edited.

## 1. Primary definition actually read

The official SPHINCS+ round3 specification, https://sphincs.org/data/sphincs%2B-round3-specification.pdf, Section9.1, printed48/PDFindex47, defines PQ-ITSR for a family H_K(M) and a map producing k tuples with one common route I. On a chosen message, the oracle draws a fresh uniform K and returns BOTH K and its mapped output. The candidate(K,M) must be a different input pair whose mapped tuple set is covered by the registered targets. The adversary knows the function description and can evaluate candidates locally; these evaluations do not enlarge the coverage set. The actual official PDF was downloaded into this folder and its complete text extracted locally.

HK22, eprint2022/346 AppendixA Definition11, printed30/PDFindex29, restates that notion and uses it in the GAME2-to-GAME3 hop. Its displayed prose says only return G(K_i,M_i), while its subsequent formula calls the(K_i,M_i) pairs responses and has an R/K symbol mismatch. I do not silently repair that typography into a new definition: the original official specification explicitly supplies the nonce/key with the output and removes the simulation ambiguity. No formal definition named C-ITSR was found or invented here.

Primary ITSR samples K per target query; it does NOT by itself dictate which arguments of the source H_msg must be folded into K. In particular the real source seed/root are common public context, not fresh uniform root values for each signature. An instantiation may freeze p=(S,T) and take K=R, but then its assumed security must apply to those actual source-generated contexts and auxiliary state. A theorem about independently uniform target roots or an unspecified context average is not that assumption.

## 2. Exact source functions and bit map

For one fixed public full256 implementation h and common S16,T16=pk.root define

U_p(R,M)=h(R16||S16||T16||M),

D_p(R,c,M)=h(U_p(R,M)32||BE32(c)||S16).

Use the SAME h at both calls and at all public graph/addressed/private-composition words. All aliases and full output limbs remain literal evaluations of this deterministic function. No independently sampled inner/outer family is inserted.

For source parameters k18,a9,h41: acceptance is bits153..161 equal zero (the18th9-bit coordinate). The REAL17 coordinates are J_j=bits9j..9j+8, j=0,...,16. Route I=bits162..202 inclusive,41 bits. Define

G_p(R,c,M)={(I,j,J_j):0<=j<17}

only when acceptance holds. The routing identifier maps bijectively to bottom(tree=I>>5,kp=I mod32), so indexed-FORS-secret exposure uses the same common-I tuple namespace. The unused forced18th coordinate is not a revealed18th secret tree. Do not truncate this message hash to128 bits: the route is in its lower limb.

The canonical target counter c0_p(R,M) is the first c in[0,2^32) with acceptance. Missing c0 is bottom, an absorbing nonwinning source request. The verifier accepts ANY provided32-bit c satisfying acceptance; it does not check that c is the first. Source R_M=J(M) is a uniform16-byte memoized ideal value. The same message always reuses R_M, c0, digest and signature bytes under honest reconstruction/cache restores.

## 3. What matches ordinary ITSR and what does not

**Repeated messages are not a fundamental mismatch.** Query a nonce-returning primitive only on a first distinct message; retain its R/output and signature source state. On repeats do not call the primitive and return the exact memoized source response. Independent uniform R for new distinct messages matches the ideal J law, including nonce collisions across distinct messages. Permanent new-message freshness M* not in initiated source queries implies candidate-pair freshness regardless of nonce collisions. Count q_distinct<=q_initiated.

**All signature auxiliaries can be simulated, if context selection is legal.** B draws its own persistent ideal F, computes the source setup/root/caches with the same public h, and subsequently computes FORS and WOTS signatures/authentication paths using that same F/h. The primitive need supply only R and message-hash target data, not signatures. Giving B a root drawn independently of its F would obstruct this program: B cannot simply manufacture F consistent with a challenger-selected root. Conversely, B may legally retain its own F if the primitive allows B's source-generated context registration. No hash transcript/private cache is exposed to A.

**Canonical targets versus free-counter candidates is the central message-hash interface gap.** Define Hcan_p(R,M)=G_p(R,c0_p(R,M),M), with explicit bottom. Ordinary ITSR for Hcan only checks the canonical candidate, whereas the actual verifier permits noncanonical accepted c*. Enlarging the input to(M,c) instead makes ordinary ITSR choose that c BEFORE its oracle draws R. The source instead chooses c0 AFTER R, so the target distribution does not match. Enlarging the key to(R,c0) gives a message/function-dependent counter distribution rather than the primitive's uniform independent K. No equality follows from predicate matching.

The gap is structural, even with source acceptance coordinates. An abstract exact countermodel can set all17 real indices and the forced coordinate to0, make the first accepted counter0, and route the canonical pair(R,M) injectively to I=(R,M) in a toy route namespace. Canonical ITSR then has zero success for any fresh pair with one target: all canonical tuple sets have distinct I. Define an accepted counter1 for a fresh message M1 to use the same route as(R,M0). After the target for M0 returns R, candidate(R,1,M1) is covered with probability1. This is an interface countermodel, not actual SHA/source-forgery code. It shows that canonical-family ITSR does not alone bound arbitrary accepted-counter coverage. Its full formal finite control can be saved separately.

**Context/security distribution is a second explicit gate.** Source S is uniform but T and cached setup success are functions of S,F,h. A single common T persists across every target. Neither treating T as independently uniform nor resampling T per oracle query preserves that joint law. One may assume a bound uniform over all public contexts and all allowed setup-derived advice independent of future R draws, or define a registered-context game below and quantify over source B's actual setup strategy. A bound in a different parameter distribution needs a separate transfer lemma.

## 4. Precise additional property and legal conditional program

Name the new property **registered-context canonical-target/arbitrary-counter subset resilience**, abbreviated RC-CTAC-SR(h). This is an EXPLICIT ADDITIONAL source-specific primitive assumption, not a cited published name or a proved hardness theorem. Its predicate concerns only message-hash subset coverage, not validity of a signature.

Game:

1. A quantum primitive adversary B knows the fixed public full h and may compute it locally. B generates/registers ONE common context p=(S,T), retaining its auxiliary state. The chosen security statement must specify whether it is worst-case context, or B's actual source law (uniform S, persistent F, source root/setup, pre-key continuation). No independent target root is silently substituted. No signing target is issued before registration.
2. Classical target oracle Target(M) maintains a nonce dictionary. On first M it samples uniform R16, computes the source U/D, searches the canonical BE32 counter up to2^32, and stores bottom or(R,c0,fullD). On repeat M it returns that SAME stored value. A bottom branch has no target tuple set. Missing source setup or signing completion remains absorbing nonwinning in the source adapter.
3. On successful targets return(R,c0,fullD) and register G_p(R,c0,M). All local h computations remain public code and never register extra covering sets. If subsequent source signature work fails, this oracle's extra registered set only enlarges the primitive coverage set; source A receives no fabricated response. For a fully exact matching ledger one may add a Commit token after completed response, but the superset version suffices for the one-sided bound.
4. B outputs(R*,c*,M*), with c*32 bits. Win iff acceptance of D_p holds, M* is not a previously requested target message, and G_p(R*,c*,M*) is covered by all successful registered target tuple sets. The candidate need not be canonical. All randomness and bottom mass are unnormalized. This strong new-message freshness matches source permanent freshness; permitting the ordinary weaker pair-freshness condition would also yield a valid larger winning event.

The actual B_cov_h program:

* Run A's source pre-key phase with the public h algorithm and no S/pk/private service, retaining quantum continuation. Independently draw S and persistent F, execute exact source setup using h, including finite canonical-cache partiality. On setup failure return primitive failure/source nonwinning0. Otherwise register the computed(S,T), retaining the SAME F/caches. This is legitimate before A sees p and requires registered source-generated context, not an independent root challenger.
* For each initiated signing M, call Target only when a nonce has not yet been obtained. On its bottom stop nonwinning. Use returned R,c0/fullD (or locally recompute from public h) to execute the ordinary source FORS/hypertree signing, with the same F/h, bytes and caches. Cache only successful response bookkeeping; mark permanent freshness for all initiated messages as in the source game. Repeated messages reuse nonce/target and recomputed deterministic source outputs.
* On A's final classical message/signature, parse R*/c* and compute its message-hash tuples through actual h. If the source indexed coverage event holds, the candidate's17 tuples belong to previously completed signature tuple sets, which are a subset of primitive registered target sets. Output(R*,c*,M*). It may output without recognizing later full source acceptance; the source winning-covered branch implies primitive success. Malformed/unreached outputs may simply fail.

This gives the conditional, selector-free inequality

Pr_SrcFJideal_h[Win AND indexed C_cov] <= Succ_RC-CTAC-SR(h)(B_cov_h).

There is no seed-zero penalty in this interface identity: the SAME actual h handles aliases even at S=0. No assumption of uniform U, fullD, FORS tuple or route is used. Root/F/h correlation is retained in registered context and B's aux state; ideal J target nonces are independent on new labels only. For variable source message lengths define the property on bounded injectively framed message strings, or take a separate primary instance per length; do not identify two different byte concatenations.

The new property deliberately makes the unresolved fields explicit: canonical target/freely accepted candidate, bounded bottom, context generator/advice, nonce-return/full-image linkage, memoized label semantics. It is not automatically conventional ITSR. Memoization may instead be implemented by B caching a NONMEMOIZED fresh-nonce target oracle on first messages, yielding the same source law with q_distinct calls. The canonical/free-counter and context gates survive that simplification.

## 5. Resource and quantum-interface accounting

At most q_initiated distinct target calls, and no target call for a repeated label. Target challenge preprocessing includes one inner hash length48+|M| and at most2^32 outer hashes length52 per new target, plus digit tests and target output storage. B's local source setup/signature/final graph hashes retain the previously accepted H_setup,qH_mode,3224 caps, private F dictionary/caches and all message/response bytes. Avoid charging locally omitted digest searches twice as both source B and challenger work; complete experiment resources nevertheless retain them. Full h coherent evaluations made by A/B use its public clean circuit, with generation/gates/workspace costs; there is no coherent private signing oracle. The new primitive does not hide runtime behind a nominal A hash-query count.

Source setup and pre-key can be kept in ordinary source order as above. If moved earlier, for fixed h,F,S the key-only preparation and A's h-only pre-key channel use disjoint private registers and commute; no posterior conditioning is required. Quantum A's continuation is untouched. This is an untimed atomic-source statement, not timing/cache-file/corruption safety.

## 6. Open frontier and exact outcome

Derived: exact source hash/map/memoized-label interface; legal conditional RC-CTAC-SR adapter with source-generated context and same-h F signature auxiliaries. OPEN: numerical hardness of this named property for actual SHA, a legal quantitative transfer from a particular published ITSR instance, public addressed graph/PRE/TCR properties and adequate complete fixed-h signature security/category/capacity. The existing RO coverage calculations are not imported. No new kernel declaration, source attack, benchmark or public paper edit.
