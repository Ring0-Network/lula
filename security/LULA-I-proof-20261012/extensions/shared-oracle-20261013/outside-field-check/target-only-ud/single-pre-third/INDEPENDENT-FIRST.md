# Independent third derivation: one-target random-function PRE

Saved BEFORE reading any new root/peer single-PRE proof, including SINGLE-TARGET-PRE-RO.md. Parent supplied the planted-marker/zero-oracle direction, not its proof. This derives a QUERY bound for a random full-output function, not fixed-SHA hardness or a source-security kernel theorem. No actual source attack, timing run or large function table is generated.

## 1. Exact image-of-uniform-input experiment

Let N=2^n, n>=1. Fix one tweak T before public parameter P is revealed. The function has independent full outputs H(P',T',x)=(high_n,low_l), where x has n bits and all output limbs are random. Sample independent uniform hidden X in [N] and give Y=high_n H(P,T,X), then reveal P. There are no public H queries or H-dependent initial advice before that challenge. After P,Y the adversary makes at most Q coherent full-output H queries and returns ANY x with high_n H(P,T,x)=Y. Classical queries count as oracle queries too.

Condition on P,Y. Y is uniform and X is still uniform. The target row's high outputs have the following exact construction: draw X uniform; draw independent Bernoulli B_x of mean1/N at every input; set m(x)=[x=X] OR B_x. At a marked coordinate output high Y. At every unmarked coordinate output an independent uniform value in [N]\{Y}. Lower limbs are independent uniform at all coordinates; all other rows/words are independent full random outputs.

At X the output high is forcedY; elsewhere the distribution is exactly uniform because high equalsY with probability1/N and each of the N-1 misses has probability (1-1/N)/(N-1)=1/N. This matches the conditional full random-function law, including all lower limbs and repetitions. Hidden X is never given to the adversary or to the constructed Boolean-search algorithm.

The marks are NOT jointly independent. For every point x,

Pr[m(x)=1]=mu=1/N+(1-1/N)/N=2/N-1/N^2.

For distinct x,z, Pr[m(x)=m(z)=1]=3/N^2-2/N^3, so simply calling this an independent Bernoulli field of meanmu is false. The proof below needs only the per-point marginal bound AFTER conditioning on all oracle-independent auxiliary data.

## 2. Full-output completion independent of the marker

Sample a known auxiliary completion K. On the target row, K_high(x) is independently uniform in [N]\{Y}; K_low(x) is independently uniform in [2^l]. Elsewhere K has ordinary independent full outputs. K is independent of X/B/m given P,Y. Define

H_K,m(w)=K(w) off the target row;
H_K,m(P,T,x)=(Y,K_low(x)) if m(x)=1, and K(P,T,x) otherwise.

Thus H_K,m has EXACTLY the required conditional law. The completion does not suppress public lower limbs. Its random values are shared consistently when a raw word has multiple roles. For a byte-oracle embodiment, target-row membership is the exact literal encoding, and other lengths/parameters/tweaks route to K. An auxiliary known outside simulator must preserve all those aliases and its whole bounded-query budget; a separately sampled lower function is allowed only as this independent, persistent completion.

We may condition on P,Y and the complete K realization, and give K's description to the Boolean simulation as private auxiliary data. This strengthens the simulator but gives it no marker-dependent advice. The simulated original adversary receives only its original full H interface. Its initial state and all intervening known operations may depend on P,Y,K and arbitrary OTHER marker-independent coins. They may not receive X, m, or H-dependent advice predating the challenge. This conditional-independence obligation is essential: unconditional marginalmu alone would not help an algorithm handed a marked point as advice.

## 3. ONE ordinary marker query per full-function query

A straightforward compute-mark/conditional-write/uncompute-mark implementation uses TWO Boolean oracle calls per H query and would give a valid looser bound below. One call suffices using phase kickback and known completion data.

For a full XOR-H query on word w and response(z_high,z_low): reversibly compute K(w) in clean scratch and XOR it into both response limbs. Fourier-transform the main HIGH response, whose frequency is z_high. On target-row words compute D(w)=Y XOR K_high(w), and the one-bit mask a=parity(z_high AND D(w)); on other words let a=0. Store a in a clean one-bit response scratch and apply a Hadamard to it, so it is |+> for a0 or |-> for a1. Query the ORDINARY Boolean XOR oracle U_m with parsed x (a fixed valid dummy off-row), apply Hadamard to that scratch again and uncompute a. This yields phase (-1)^(m(x)*a) and clean scratch. Undo the HIGH Fourier transform and reversibly uncompute K(w).

The added phase represents exactly XOR of m(x)*D(w) into the high response. Combined with the first known K XOR, it changes K_high toY at marks and leaves K_low unchanged. Off-row a0 makes the Boolean query act trivially on |+>, without needing a controlled black-box oracle. The same identity holds in a superposition of target/off-target words and with arbitrary response/reference entanglement. No measurement is used. The completed H oracle therefore costs ONE ordinary unknown-marker query, plus two known K compute/uncompute evaluations, O(n+l) response/parity operations and reversible parsing/mask costs. Those known costs must be charged separately.

Consequently the simulated adversary has at most q=Q Boolean marker queries. Nothing in this count treats the completion as an unknown marker query. A two-marker scratch implementation would instead have q=2Q, and must not claim this sharper constant without the one-query construction.

## 4. Zero-oracle hybrid with CORRELATED marks

Fix P,Y,K and all other marker-independent auxiliary data. Purify the adversary's randomness/measurements and pad to q queries if needed; its initial state and fixed unitaries are independent of m. Let psi_m be its final state with U_m, and psi_0 its final state when every marker-oracle query is the identity (the zero Boolean oracle). Let phi_(0,j) be its state just before query j in the ZERO computation. For each fixed m, telescoping query replacements and triangle inequality give

||psi_m-psi_0|| <= sum_(j=1)^q ||(U_m-I)phi_(0,j)||.

If Pi_m projects onto marked query-input coordinates, ||(U_m-I)phi||<=2||Pi_m phi||. Each phi_(0,j) is independent of m. Therefore

E_m ||Pi_m phi_(0,j)||^2 = sum_x Pr[m(x)=1]*Pr_zero[query input x] <= mu.

This calculation uses NO joint independence of marker coordinates. By the L2 triangle inequality over m,

(E_m ||psi_m-psi_0||^2)^(1/2) <= 2q sqrt(mu).

Let R_m project the FINAL output register onto returned marked points (and any valid-output condition). The zero algorithm's output is marker-independent, so E_m||R_m psi_0||^2<=mu. Projection contraction and another L2 triangle inequality give

sqrt(E_m||R_m psi_m||^2)
 <= sqrt(E_m||R_m psi_0||^2) + sqrt(E_m||psi_m-psi_0||^2)
 <= (2q+1)sqrt(mu).

This remains valid for arbitrary correlated distributions of Boolean fields with per-point marginal at mostmu CONDITIONED on every fixed initial/auxiliary datum. Pointwise support could contain many marks or be empty; those possibilities do not change the derivation. For our planted field it is always nonempty. Unfix P,Y,K and coins to obtain the average success bound.

## 5. Explicit ANY-preimage bound

Every original successful ANY-preimage output is exactly a marked point in the completed random function, with the same full-output query law. With the one-marker simulation q=Q,

kappa_PRE(Q,n) <= min(1,(2Q+1)^2*(2/N-1/N^2)).

At Q0 this is the correct random-guess successmu, not1/N: the image-of-uniform-input target is size-biased and includes the hidden planted point plus other collisions. A simpler conservative bound is min(1,8*(Q+1)^2/N). The factor8 follows from (2Q+1)<=2(Q+1) and mu<=2/N. A two-marker simulation would yield min(1,(4Q+1)^2*mu), or the simpler conservative32*(Q+1)^2/N; that looser route is legal but not needed.

For the already reviewed target-only source program Q<=Q_A+1, this supplies min(1,(2Q_A+3)^2*(2/2^128-1/2^256)) for its ordinary one-target PRE term, subject to the existing source/router hypotheses. It does not change old direct bounds, prove fixed-SHA hardness, or by itself improve the much larger aggregate UD envelope. These are distinct conclusions.

## 6. Exact N-1 completion sampling and actual costs

Exact miss sampling must not be replaced by biased modulo reduction. Draw J uniform in0,...,N-2 and map J to J if J<Y, else J+1. This is a bijection to [N]\{Y}. Implement the J draw using independent n-bit uniform draws and rejecting only N-1. Its expected draws are N/(N-1)<=2. Sampling all N target-row high cells therefore has expected n*N^2/(N-1) random-bit cost (plus indexing/storage), with n*N high-output storage bits; target lower storage is l*N bits and costs l*N independent bits. This is an explicitly finite target-row TABLE of sizeN, NOT a practical construction. It is a proof-side auxiliary distribution; NO such large table is actually generated here.

For a finite total raw domain of D words, a direct full completion table uses O(D*(n+l)) bits of storage, expected O(n*N^2/(N-1)+(D-N)*(n+l)+l*N) random bits, and a reversible linear table-lookup implementation has O(D*(address_bits+n+l)) gates per lookup, with compute/uncompute charged twice. Independent outside raw rows may instead use the already accepted finite simulator, but that does not automatically provide an exact N-1 alphabet target-row simulator.

The exact rejection construction has unbounded worst-case sampling TIME and almost-sure termination with the stated expected charge; it is not a deterministic bounded-fair-coin sampler. In particular, non-dyadic probabilities1/(N-1) cannot generally be produced by a fixed finite fair-bit circuit. A finite-time truncation needs an explicit error term, or an alternative exact algebraic simulator with a proved key-sampling/evaluation cost. No such improvement is assumed for the query proof above. Once the finite table is sampled, lookup circuits have fixed bounded size independent of the marker. The zero-oracle query argument allows arbitrary finite known gates or independently randomized preprocessing; it imposes no polynomial runtime claim. If a polynomial-time reduction is demanded, an efficient exact bounded-query N-1-valued completion is an additional implementation lemma, not a reason to invent a uniform-miss sampler for free.

## 7. Controls and proof boundary

Small controls should enumerate the planted correlated marker distribution for N2/N4, check each marginalmu and non-product pair probabilities, verify full high/lower completion and repeated replies, verify the one-marker phase circuit on entangled states, and exhibit the difference between ANY-preimage success and equality with hidden X. They should also test a deliberately marker-dependent advice counterexample to show why the conditional-independence premise is necessary. No real inversion/search or large table is required.

This is a manual general zero-comparison/query-completion proof. It uses no collection conjecture or asymptotic Theta-to-constant inference. Formal mechanization and efficient exact miss-table simulation are separately open. Zero source/game kernel declarations, no global/source/manuscript/scalar edits and no claimed whole-goal completion accompany this first.
