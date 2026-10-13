# Independent exact one-target random-Th PRE query bound

**COMPUTED — first-save provenance.** Saved before reading any new one-target PRE peer derivation. The parent supplied the original-input/alternative-input split and flagged exact nonbinary local-table sampling; the argument below independently audits the coherent oracle completion and derives an additional whole-mark bound. No real source execution, attack, benchmark, large function generation, source kernel declaration or manuscript edit occurs.

## 1. Exact experiment and proposed bounds

**ASSUMED — finite oracle model.** Let N=2^n, n>=1. H:P×T×[N]->[N] is a uniformly random tweakable function, with finite parameter/tweak registers. The target tweak t is fixed ex ante, independently of H. P is uniform, X is uniform[N], Y=H(P,t,X). The original A receives Y and P, never X, and makes at most Q quantum XOR queries to the WHOLE H afterward. Before this challenge it has zero public-H queries and no H-dependent auxiliary information. Its output V is a classical node or failure. Oracle-independent computations, measurements, quantum memory and independent side functions can be arbitrary; no efficiency is assumed by the query-only theorem. The challenger computes its target and checks final validity separately, not as A queries.

**PROVED — exact finite upper bounds, not exact optimal success.** The original-input event obeys

Pr[V=X] <= min(1,(2Q+1)^2/N).

Different-input success obeys both the primary-average-search envelope

Pr[V!=X AND H(P,t,V)=Y] <= min(1,8(Q+1)^2/N)

and a stronger directly proved marked-search envelope min(1,(2Q+1)^2/N). These use exactly one ordinary Boolean XOR query per simulated whole-H query; no unknown X is revealed to original A.

**PROVED — stronger combined bound.** A separate completion of the entire preimage marker gives

Pr[H(P,t,V)=Y] <= min(1,(2Q+1)^2*(2/N-1/N^2)).

At Q=0 this is the exact success probability 2/N-1/N^2. For Q>0 it is a proved finite upper envelope, not an optimality claim. It invokes no multi-target/length-preserving PRE conjecture. The constant N=1 degenerate case, if allowed, has success1 and is handled separately without an N-1 table.

## 2. Original X event: common hidden-point overlay

**PROVED — real joint law.** Sample independent P,X,Y and a random full family H_0. Define H_real(P,t,X)=Y and H_real=H_0 everywhere else. This is exactly the joint law of the experiment conditional on X,Y: all other H cells are independent uniform and the designated point has its actual challenge image. The original A initial state receives P,Y but no X. Zero prior H queries are crucial to this initial coupling.

**PROVED — ghost and query discrepancy.** Run A with H_0 instead. Its state and final output are independent of X, conditional on all its independent auxiliary data and P,Y. Hence Pr_ghost[V=X]<=1/N. The two XOR unitaries differ only at input(P,t,X). On a ghost query state the average mass there is <=1/N, even when the query is entangled over all parameters/tweaks and response bits. The purified vector difference per query is at most2/sqrt(N). Pad adaptive/halted branches into Q slots with an invariant plus-response query; common local isometries and product telescoping give ||Psi_real-Psi_ghost||<=2Q/sqrt(N).

**PROVED — final projection.** Apply the same inaccessible-environment projector checking classical V=X to both purified states. The square roots of event probabilities differ by at most the vector norm difference. Thus sqrt(Pr_real[V=X])<=(2Q+1)/sqrt(N). No final H query is needed to test original-input equality in this analysis, and no X test is performed by original A.

## 3. One Boolean query implements one full node-output query

**PROVED — exact output completion.** Let b:[N]->{0,1} be a Boolean marker and let G(x) be an independent uniformly sampled member of[N]\{Y} at each node. On the selected parameter/tweak row define H(x)=Y when b(x)=1, else G(x). Its base G and difference D(x)=Y XOR G(x) have D(x)!=0. For each nonzero D there is an invertible binary linear map L_D with L_D D=e_0: swap a nonzero pivot into position0, then use its bit as control to clear all other nonzero coordinates. The actual node XOR query is implemented by

1. XOR base G(x) into the n-bit response register.
2. Apply L_D to that response register.
3. Apply ONE ordinary Boolean XOR oracle query b(x) to response bit0.
4. Apply L_D inverse.

The net response addition is G(x) XOR b(x)D(x), exactly H(x). G/D/mask scratch is coherently uncomputed by local table-controlled operations. This avoids the ordinary compute-marker/use/uncompute-marker pattern that would use two Boolean calls.

**PROVED — coherent off-parameter routing.** For input rows different from(P,t), first XOR their independent ordinary H base value. Make the marker query inactive with a clean plus ancilla: coherently swap response bit0 with that |+> ancilla on inactive inputs, perform the SAME one Boolean oracle query, then swap back. XOR on a plus response is the identity, regardless of the unknown marker bit, so inactive branches are unchanged with no measurement, no known-unmarked dummy point, and no extra oracle call. Active branch response bit0 receives the actual b(x) toggle. The ancilla returns clean plus in every branch. The selected/private-X exclusion below is another deterministic inactive mask. All masks use public/input registers or simulator-private independent X, never an observed Boolean query result.

## 4. Different-input marker completion

**PROVED — exact conditional source law.** Internally sample independent uniform P,X,Y. Obtain an ordinary iid Bernoulli marker g(x), Pr[g(x)=1]=1/N for all x, independent of P,X,Y and G. In the selected row force H(X)=Y; for z!=X set H(z)=Y if g(z)=1 and G(z) otherwise. All other rows are independent uniform functions. For z!=X, the probability of EACH output is exactly1/N: Y occurs with probability1/N, and each other output with (1-1/N)/(N-1)=1/N. Independence across non-X cells is retained. Therefore this is exactly the original challenge's conditional family law.

**PROVED — lawful program and success inclusion.** The simulator keeps X private, uses the deterministic mask selected-row AND z!=X, and computes H(X)=Y locally. Original A receives only P,Y and oracle replies. Each full-H query uses one g query by the linear-map/plus-mask implementation. Return original A's V as the Boolean search candidate. On every different-input preimage event, V!=X and g(V)=1, hence that event is contained in the ordinary average-search win event. It is harmless if Boolean search additionally wins on V=X with g(X)=1. There is no conditioning on g(X)=0 and no setup query to find an unmarked point.

**CITED — primary alternative envelope.** HK22 section8.2 Theorem4 states average-search success <=8 lambda(Q+1)^2 for iid Bernoulli marks. With lambda=1/N and exactly Q Boolean calls, it gives the stated alternative envelope. The same argument below strengthens the coefficient without relying on that theorem's looseness.

## 5. Elementary marked-search lemma with arbitrary mark correlations

**PROVED — query-only lemma.** Let b be any random Boolean field such that for every fixed x, Pr[b(x)=1]<=mu, and let all initial/local auxiliary data be independent of b. For a Q-query Boolean-XOR algorithm outputting a classical V, compare its b-oracle computation to the zero-oracle computation. The latter quantum state and output are independent of b. At each query slot its averaged mass on marked input addresses is <=mu, so the purified query-unitary discrepancy is at most2sqrt(mu). Telescoping through common local/measurement isometries gives vector distance <=2Qsqrt(mu). In the zero computation, the same final mark projector has probability<=mu. Common projection then proves

Pr[b(V)=1] <= min(1,(2Q+1)^2 mu).

No independence between different b(x) coordinates is required. The whole distribution of b remains in an inaccessible purifying environment; its final mark check is analytical game verification, not an extra algorithm query. Auxiliary tables can be enormous but must be independent of b, conditional on any public P,Y on which their law depends.

**PROVED — sharper alternatives.** Apply this lemma to the ordinary iid g of section4 with mu=1/N. Simulator-private X, local G and outside H tables are independent of g. This proves the stronger different-input bound. It does not give X to original A or require inspecting its quantum query states.

## 6. Whole preimage marker, avoiding the union constant

**PROVED — distribution.** In the selected row sample a marker b by first choosing uniform latent X, setting b(X)=1, and assigning independent Bernoulli(1/N) bits elsewhere. For every fixed z,

Pr[b(z)=1]=1/N+(1-1/N)/N=2/N-1/N^2=:mu_PRE.

Choose Y independently uniform and G(z) independently uniform in[N]\{Y}; these auxiliary data are independent of the WHOLE marker field b, conditional on public P,Y. Complete H(z)=Y if b(z)=1 and G(z) otherwise, with all off-parameter/tweak rows independent uniform. The latent X is kept only in the mathematical coupling and is not needed by this simulator or supplied to A. Conditional on X,Y, the completion is exactly H(X)=Y plus independent uniform remaining cells, hence has the actual challenge law.

**PROVED — exact success equivalence and upper bound.** For valid V, H(P,t,V)=Y if and only if b(V)=1. One full-H query uses one b query with the section3 coherent implementation. Apply the correlation-tolerant marked-search lemma with mu_PRE; this yields min(1,(2Q+1)^2(2/N-1/N^2)). The planted mark creates correlations, so this direct argument must not call it an iid average-search oracle. For Q=0 any output independent of H's hidden inputs, even chosen from Y, hits the marker with probability exactly mu_PRE.

## 7. Exact local randomness/storage and limits

**ASSUMED / PROVED — query-only local tables.** G entries are EXACTLY uniform over an alphabet of cardinal N-1. Binary 2Q-wise functions followed by modulo(N-1) are not exact uniform samplers and are not used. The proof may fix the entire independent table G as local circuit data: N log2(N-1) bits of Shannon entropy and at most nN bits of explicit entry storage, plus the independent outside-row tables, masks, circuit/gate/workspace costs and quantum registers. No such table is generated by this task. If the number of parameter/tweak rows is R, an eager outside family uses at most(R-1)nN stored bits; all of this is finite but can be enormous. Independent local auxiliary gates are permitted by the information-theoretic query proof. Exact finite-alphabet sampling is a declared mathematical distribution, not a bounded binary-coin implementation claim.

**OPEN — efficiency and model lift.** This establishes no efficient polynomial-time marker completion using small exact nonbinary tables, no fixed-SHA hardness and no source-game refinement. Existing binary polynomial-method implementations must not be imported blindly for[N]\{Y} sampling. A full256 raw shared-oracle source interface with arbitrary lengths/lower limbs would need its own joint-domain lift and resource ledger; off-parameter routing within the random-Th model above is proved, not that source lift. Prior target history/H-dependent advice, adaptive challenge selection using H, multiple targets and real fixed-function structure are outside this first theorem.
