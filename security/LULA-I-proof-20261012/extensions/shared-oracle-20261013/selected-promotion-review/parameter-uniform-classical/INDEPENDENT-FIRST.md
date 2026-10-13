# Independent parameter-uniform classical joint theorem

**COMPUTED — blind source-first provenance.** Written before reading any NEW root/peer parameter-uniform theorem. I read the pinned release source, the original four-event proof CLASSICAL-RO-THEOREM.md, the accepted adaptive coverage/source bridge, the existing joint4fa7 theorem and my source-first parameter/cost guard analysis. No retuned implementation, new root criterion or parameter scan is used as a proof. This file is a separate manual theorem, not a repair/capacity or kernel certificate.

## 1. Fixed family and experiment

**ASSUMED — parameters fixed ex ante.** Let p=(a,k,(h_i,ell_i,S_i)_{i=0}^{d−1}) be fixed before the oracle/key/adversary coins. Put r=k−1,t=2^a,h=sum_i h_i,B=2^h,N=2^128,Ctr=2^32. Keep n=16, FORS+C, lower lw4/w16 and top lw8/w256. The d=1 case has only the top base. Guards are:

* d>=1, layer IDs fit one byte;0<=h_i<=31,h<=63; all tree/keypair/global-FORS indices fit their u64/u32 fields;1<=a<=31,k>=2,r*2^a<=2^32 and k*a+h<=256.
* lfull_i=32 for non-top and16 for top;1<=ell_i<=lfull_i,z_i=lfull_i−ell_i. Every omitted digit is checked zero. All accepted vectors use the entire128-bit width4/8 digit word.
* Integer targets satisfy0<=S_i<ell_i(w_i−1). The strict upper bound is essential for the unexposed-WOTS case, not merely a completeness optimization. Acceptance coefficients are nonzero. Fixed root-compression/tail buffer limits hold, in particular r<=94. All other source arithmetic/array indices are nonoverflowing.
* Any cache is a consistent honest top segment or empty; the event interface is atomic, completed replies only, no private/cache-byte/timing leakage, absorbing noncompletion. Geometry does not assert enough physical RAM or fast setup. Failed/uninvoked rows are not globally normalized away or made into an artificial abort.

**ASSUMED — ordinary reference game.** Three independent uniform128-bit seed components(K,P,S), one complete full256 raw oracle and public p. A has at mostQ classical raw calls including pre-key and at mostq initiated atomic signing calls over all honest restores. One strict final verifier accepts only a fresh message. F(A) and J(m) are independent memoized full256 private maps in the coupling, not separate real hash functions assumed by name. The theorem below refers to the ordinary full-raw real marginal with actual private restrictions reconstructed at K/P. q,Q are deterministic pathwise caps. They are not observed counts or normalization by successful calls.

## 2. Parameter-uniform ordinary graph and safe continuation

**PROVED — unique restrictions and acyclic generation.** A WOTS start uses its type5 address, then its nonterminal steps use distinct type0 addresses(layer,tree,kp,chain,position). Its endpoint compression is type1 with a fixed ordered ell-node payload. A Merkle parent is a distinct type2(height,index) restriction, with input its already generated ordered children. FORS secrets are distinct type6(j*t+leaf) starts, images/internal nodes are type3(height,j*2^(a−height)+local), and the ordered r-root compressor is type4. Field guards make these literal tuples injective. Distinct source roles are separated by the type byte or complete address. Actual input-node collisions do not merge different addressed restrictions.

Generate the finite genuine graph from independent private prefixes and independently sampled genuine full images in topological order. Each designated restriction's input depends on other restrictions, never on that restriction's residual replies. Combine its one designated full cell with a uniform residual table. By deferred sampling this has the ordinary joint complete-function/graph marginal. All full lower128 output limbs are kept, including where source computation uses only the first16 bytes. Source graph size can be enormous; this argument is not an efficient eager simulator or graph generation instruction.

**PROVED — one genuine child at every WOTS address.** At layer0, the child is the FORS PK of that full(bottom tree,kp) instance, independent of which leaves a signature reveals. Above it, the child is the root of the lower subtree with global index g=(tree<<h_i)|kp. The root depends on fixed lower WOTS PKs, not on the current message. These identities hold for arbitrary guarded height vectors, including zero-height layers. Thus a completed use of a full WOTS address always signs the same child with the same smallest accepted counter and digit vector. Distinct restored branches do not create distinct children under this interface.

**PROVED — type7 row disintegration.** The genuine child is a public graph node independent of its own type7 restriction. For each row, disintegrate its complete function into bottom or first accepted counter/full128 target plus independent lower limb, the rejected same-child prefix, and uniform residual cells. The acceptance probability is the appropriate target-sum coefficient divided by w_i^lfull_i; it need not equal the original value. Rejected prefix cells cannot equal the accepted128-bit target. Other-child points and postaccepted residual points are not free advice. Noncompletion is retained; no successful-row conditioning of the full game is performed.

**PROVED — safe augmented surface.** Reveal only endpoints, FORS leaf images, public compressed/tree/root nodes and the above canonical prefix metadata. Hidden starts, interior WOTS coordinates, FORS secrets and the full F map are not revealed. This safe surface is independent of still-hidden predecessor coordinates and untyped I/E cells. A canonical row's child/success/digits depend on public graph values and its own outside restriction, not on hidden chain/FORS inputs. In the unflagged ghost, use retained genuine records for honest work, designated values at known/unprotected points and one O0 residual table at all still-hidden points. Completed signatures permanently disclose their FORS secrets and full forward WOTS suffixes. Install new designated known cells only if their public reply was not fixed; never overwrite old replies. Until a first hidden hit, such old disagreements cannot occur. Known suffix disclosure leaves all undisclosed predecessors unused and uniform.

**PROVED — REAL agreement, not complete-function identity.** Reconstruct the private restrictions at S||zero48||AD5/6||K and P||S||m from full F/J maps and combine the designated graph cells/residual cells. This gives the ordinary real full-raw marginal. It shares source observations, queried replies and honest computations with the ghost until the common first private/nonce/hidden/target/message-bridge event. It need not share its entire unqueried public function. K/P are unused by ghost routing; an unsigned J label is unused before its first atomic request, and there are no public slots during that request. Failure absorbs with no later winning continuation. Flags are analytical, never supplied to A. After a flag, the ghost may cease being an ordinary source oracle; no later source-law agreement is asserted. Uniformity is never claimed by conditioning on surviving guesses.

## 3. Exhaustive source witness cover is uniform under the strict guard

**PROVED — addressed Merkle descent.** Compare the final accepted top path with the genuine mathematical path for the same source-decoded route. Ordered parent inputs and actual address schedules coincide. A first merger of changed values gives a different-payload/equal-prefix type0–4 witnessG; absentG, its leaf/public key and ordered endpoint vector are genuine. This induction uses only field injectivity and fixed vector lengths, not the numerical heights41/5/21. The FORS global parent formula matches(j*t+leaf)>>level at every height, so it applies to any guarded(a,r).

**PROVED — WOTS case split.** At any genuine reconstructed WOTS PK:

1. Changed endpoint vector givesG in type1. A changed start that nevertheless reaches the genuine endpoint givesG at its first type0 merger.
2. Otherwise every supplied start is genuine. If the address is unexposed, ell_i(w_i−1)−S_i>0 forces a nonterminal first verifier callH. No canonical row needs to exist there.
3. If it is exposed, it has one canonical real digit tuple x. A different accepted tuple e with equal total sum forces e_j<x_j at some real coordinate. That genuine predecessor lies before the disclosed suffix, is nonterminal and yieldsH.
4. If e=x, omitted zeros and exact128-bit width4/8 decoding imply equality of the entire128 target. A different(child,counter) then gives exposed successfulD7. Otherwise the reconstructed child is the genuine fixed child and induction descends one layer.

At the bottom genuine FORS PK, a changed root vector/compressed payload or changed Merkle leaf/path givesG. A different secret yielding its genuine leaf image givesG; a genuine unexposed secret yieldsH. If all real selected secrets were exposed and the verifier's zero filter passes, eventC_cov holds. There is no eighteenth/virtual secret. Thus Win implies C_cov orH orG orD7 for all guarded p. This proof fails at Smax, with ignored digest bits, or with extra exposure/corrupted state; those are excluded. It does not assume every WOTS address has been signed or every unused row succeeded.

## 4. Uniform rare-event partition and terminal counts

**PROVED — literal languages do not depend on the changed dimensions.** At fixed S!=0 the addressed prefix is S16||zero48, while private-J/inner words have second block S. Eligible E words have length52,suffixS and second block!=S. The same disjoint syntactic classes therefore exist for every p. Typed valid-address sets change, but their role weights do not: privateF/shortJ1, inner3, potentially hidden16-byte chain/FORS-leaf2, remaining graph/type7 targets1, eligibleE/Other0, all divided byN. Inner privateP/unusedJ/endpoint flags can overlap; hidden-input and different-input graph-target events share one opportunity. Neither is reclassified by hidden equality. All counts belong to the SAME unflagged continuation, pathwise total<=Q, giving weighted raw charge<=3Q/N.

Every fresh residual response has uniform prefix against its static target; true public points are excluded from changed-payload events, rejected canonical points cannot match the target, and previously matching residual points were charged on their first generation. Static targets may be public or still hidden: no full-secret G advice is merged into this ghost. UnsignedJ prediction nominates one literal message per raw inner word, without a q multiplier. Honest inner work has at most2(q+1)/N privateP/endpoint charge. Honest outer private-J alias implies the already charged inner endpoint-half=S, so no extra fee is needed.

**PROVED — exact terminal opportunity bounds.** Every accepted WOTS layer performs exactlyell_i(w_i−1)−S_i verifier chain calls. There are r FORS secret leaf calls, so

    H_fin(p)=r+sum_i[ell_i(w_i−1)−S_i].

Type0–4 terminal evaluations consist ofr(a+1) FORS leaf/path calls, one ordered FORS root compression, and at each layer its chain completions, one WOTS PK compression andh_i authentication calls. Hence

    G_fin(p)=r(a+1)+1+sum_i[ell_i(w_i−1)−S_i+1+h_i].

There are d final type7 calls. These counts are complete-hash opportunities, not compression blocks or secret graph cardinality. Until the common first event their unused/fresh-reply risks are charged by H_fin/N,G_fin/N,d/N in this same experiment. The first terminal inner fee is already in2(q+1); the terminal outer opportunity is accounted by the coverage bridge. No baseline3017/3217 is reused.

## 5. Uniform full256 bridge and adaptive coverage

**PROVED — complete message processing still uses the same aliases.** Source nonceR=prefix128 J(m), innerU=O(R||S||root||m) and outerD=O(U||BE32(c)||S) are unchanged. Different messages have different inner inputs even if their R repeat. On the common prefix, the endpoint-half exclusion separates honest outer namespaces from inner/private-J words. Each raw point nominates one relevant full256 value, either an inner output or an eligible outer input-prefix, in disjoint syntactic classes. Source/source collisions and the terminal fresh-message collision add separate fees. The predictable total bridge pair charge is

    [qQ+binom(q,2)+q]/N^2.

Raw retained candidates whose namespace later becomes honest require a paid preview/collision; a final fresh message accessing any old honest namespace requires a paid inner collision, including previously unevaluated counters there. Old rejected honest points fail the zero filter; old accepted points cannot be called fresh independent candidates. Repeated messages and points reuse memo values. These facts are dimension-independent and require no uniform-root assumption.

**PROVED — generalized acceptance coordinates.** Source digest usesr disjointa-bit real indices, one disjointa-bit forced-zero coordinate, thenh disjoint route bits. The guardka+h<=256 ensures they fit without overlap. A fresh full256 response has independent uniform coordinates and unused bits. First acceptance amongCtr independent outer points depends only on that one forced coordinate, so the accepted route/real indices are uniform on[B]×[t]^r, independent of canonical counter/rejection noise. This remains true when all256 bits are used. Finite no-acceptance probability is(1−1/t)^Ctr, charged byq times that value. WOTS failure after this internal route draw yields no completed response or later winning continuation; padding can include its internal draw without falsely declaring a completed exposure.

**PROVED — same-world source-prefix coupling and candidate cap.** The safe graph/row surface is independent of untyped streams. Attach iid X exposure values to fresh successful honest message namespaces and iid Y raw candidate values to fresh eligible nonhonest points, continuing with fresh unused coins after the first common stop. Before that stop no literal cell receives inconsistent independent assignments. Adaptive message/point names only consume stream prefixes; the flags pay interference. Do not declare the actual postbad ghost iid or condition on avoiding Bad. Pad to q exposure values and Q+1 candidate values, a deterministic cap; the completed source exposure set is a subset. A caller's deterministic eligible-outer cap b_E can replaceQ, but an expected E-query count cannot.

For each fixed padded exposure transcriptT, the raw coverage probability is

    p(T)=(1/(B*t))*sum_b product_{j=1}^r |C_bj|/t.

GivenR~Binomial(q,1/B) exposures at a selected instance, each real tree's exposed-leaf fraction has expectation1−(1−1/t)^R and the r trees are conditionally independent. Therefore

    p_F(q;a,k,h)=(1/t)*E[(1−(1−1/t)^R)^r].

Adaptive retention/prefix stopping is included by monotone independent padding, giving(Q+1)p_F or its trivial cap. The one forced coordinate provides only1/t; it exposes no omitted tree. This proof works at B=1 and for arbitrary finite r/t under the guards, without a Poisson approximation or expected-candidate substitution.

## 6. Complete uniform inequality and boundaries

**PROVED — manual theorem in the stated source-RO family.** At fixed nonzeroS, the common first-bad union, exhaustive source cover and independent-stream padding give the complete envelope with constantH_fin+G_fin+d+2. Average these fixed-S inequalities, pay uniform Szero once and conservatively omit the harmless nonzero-S mass factor. Put

    C_p=H_fin(p)+G_fin(p)+d+3
       =r(a+2)+2*sum_i[ell_i(w_i−1)−S_i]+h+2d+4.

Then every adversary in the stated family satisfies

    Pr[Win] <= min(1,
       (3Q+2q+C_p)/N
       +(qQ+binom(q,2)+q)/N^2
       +q*(1−2^-a)^(2^32)
       +(Q+1)*p_F(q;a,k,h)).

All arithmetic terms are untruncated before this final cap. The corresponding finer weighted role ledger is available only for expected role counts of the same ghost and a pathwise candidate cap. The once-onlySzero rule does not subtract charges from unrelated old inequalities. Original parameters recoverH_fin3017,G_fin3217,d5,C_p6242 and the reviewed4fa7 bound exactly.

**PROVED — honest cache transfer only.** For a consistent guarded cache, fixed-child/canonical-counter identities and exact node/path reconstruction preserve the reference signature bytes whenever signing terminates. Atomic honest restore therefore transfers this event/query envelope with no loss. An accepted-but-noncanonical counter, private/cache timing disclosure or arbitrary corruption is outside this theorem and cannot be included by renaming it a cache.

**OPEN — independent acceptance and original goal.** This first is a full manual parameter-uniform classical source argument, requiring a separate independent source-first reader before promotion. It is not checked Rust/game refinement, efficient simulation, a retuned QROM theorem, an actual measured implementation or a proof of adequate128/category1/capacity. The invariant private/message coefficients remain; no full parameter repair follows from the uniform theorem. Source overflow, changed widths or dimensions outside guards require a separate representation/proof. No source, old scalar, cache, timing or manuscript is edited; the whole goal remains incomplete.
