# Explicit finite preimage bound for one ex-ante random target

**PROVED — manual information-theoretic derivation; exact final-subject review pending.** Let N=2^n, n>=1. This result concerns a random function and a single tweak selected independently before the challenge, with ZERO prior public-function queries. It is not fixed-SHA hardness, an efficient reduction or a complete LULA security theorem. Both readers saved independent firsts for the original-input/different-input split before exchanging their new work. One additionally derived the stronger correlated whole-marker argument in that first; the other reviewed it after the exchange. Neither provenance statement claims independent discovery of the supplied candidate direction.

## 1. Exact challenge and side-state condition

**ASSUMED — experiment.** A uniformly random complete function has a genuinely independent n-bit prefix restriction at each injectively framed word W(P,T,x), x in[N]. The target tweak T is ex ante; the challenger samples uniform P,X and gives A only P and Y=prefix H(W(P,T,X)), not X. A then makes at most Q ordinary full-output XOR queries, with arbitrary retained quantum memory, measurements and classical output V in[N] or failure. An algorithm-chosen final output is tested by the challenger without charging an additional A query. Any permitted auxiliary initial state, interquery service and outside functions must be independent of the hidden variable/mark field in the stated zero-oracle experiment; they cannot disclose X or supply extra unknown-target evaluations outside Q. This side-state property is not assumed merely from a primitive's name.

## 2. A correlation-tolerant Boolean query lemma

**PROVED — marginal mark lemma.** Let B(x) be ANY random Boolean field with Pr[B(x)=1]<=mu for every fixed x, independent of the algorithm's initial/local auxiliary data. The coordinates need not be independent. Compare a Q-query Boolean-XOR algorithm with its zero-oracle computation on the same sampled environment. A zero-oracle prefix state is independent of B. Its averaged squared query support on marked coordinates is at most mu, by summing Pr[B(x)=1] times its input weights. The two query unitaries agree elsewhere and differ by norm at most2 on that support. In a common purification this gives per-query vector discrepancy at most2 sqrt(mu).

**PROVED — adaptivity and termination.** Pack the common local operations and copied measurement histories between adversarial query slots into common isometries. Pad halted branches with a query acting on a plus response. Product telescoping evaluates each difference on its zero-oracle prefix, yielding final vector distance at most2Q sqrt(mu). Apply the SAME terminal projector checking B(V)=1 in both experiments. Under the zero computation its probability is at most mu, including outputs selected adaptively from independent auxiliary data. Projection plus triangle inequality therefore yields

`Pr[B(V)=1] <= min(1,(2Q+1)^2*mu)`.

This final test is analytical/challenger verification, not an extra algorithm query. No query history is measured, no no-hit posterior is used, and no iid assumption is inserted for a correlated B.

## 3. Whole preimage marker and full-word completion

**PROVED — conditional function law.** Sample independent P,Y and a latent uniform X. Define B(X)=1 and sample each other B(x) independently Bernoulli(1/N). At every fixed z,

`mu_PRE = Pr[B(z)=1] = 1/N+(1-1/N)/N = (2N-1)/N^2`.

Independently of the WHOLE marker field, sample G(x) uniformly from[N] excluding Y. Sample uniform full lower limbs L at each raw word and independent full outside outputs. Set the selected prefix to Y if B(x)=1 and to G(x) otherwise; its lower limb is L in either case. Conditional on X,Y, the designated word has prefix Y, and every other prefix value is uniform: Y has probability1/N and any other value has probability(1-1/N)/(N-1)=1/N. The cells are independent conditional on X,Y. Thus this constructs the EXACT complete-function/challenge joint law. The latent X is used only to define that distribution and need not be read by the simulator. Public lower limbs and off-parameter/off-tweak/malformed words are retained, not silently erased.

**PROVED — one ordinary Boolean query per complete XOR call.** Let r0(word),r1(word) be the known full miss/hit values. Fourier-transform the main response frequency z, compute the parity d=<z,r0 XOR r1> into response scratch, Hadamard that scratch, make ONE ordinary Boolean-XOR B query on the parsed payload, reverse the Hadamard and uncompute the known parity. Apply the known base phase for r0 and undo the main Fourier transform. The net phase is exactly the desired inner product with r0 XOR B(x)*(r0 XOR r1), and scratch is clean. On outside/invalid words choose r0=r1; d0 makes the Boolean query act on a plus eigenstate, so it has no effect. No controlled unknown oracle, known-unmarked dummy or two-query marker compute/uncompute is assumed.

An equivalent linear response-basis change maps a nonzero difference r0 XOR r1 to one response bit, performs one B XOR there and restores the basis. A coherent plus-register swap makes it inactive on equal-value/outside branches. Both exact constructions permit arbitrary entangled query registers. The public/raw domain's fixed ex-ante finite encoding and unitary extension are explicit inputs to this proof.

## 4. Explicit bound and comparative split

**PROVED — whole preimage bound.** For a valid output V, its real PRE relation holds iff B(V)=1. The simulated algorithm uses at most Q Boolean queries and its auxiliary G/L/outside tables are independent of B conditional on public P,Y. Applying the correlation-tolerant lemma gives

`kappa_PRE(Q,n) <= min(1,(2Q+1)^2*(2/N-1/N^2))`.

At Q0 the baseline2/N-1/N^2 is exact; at larger Q this is an upper envelope, not an optimal success theorem. The planted field is correlated and is NOT described as an iid average-search oracle.

**PROVED / CITED — preserved weaker comparison.** The separately derived original-input/different-input split gives original V=X at most(2Q+1)^2/N by a one-point ghost overlay. A known-X marker completion for V!=X uses one Boolean query per full call and outputs V without a digest test, so HK22 section8.2 Theorem4 (https://eprint.iacr.org/2022/346) gives alternatives at most8(Q+1)^2/N. Their sum is min(1,(12Q^2+20Q+9)/N). The whole-marker envelope is no larger. The split proofs/firsts remain preserved; no length-preserving or collection PRE conjecture supplies the constants here.

## 5. Resource and scope boundaries

**ASSUMED / COMPUTED — exact local tables.** G's range has N-1 elements. Binary polynomial outputs followed by modulo(N-1) are NOT an exact uniform construction and are not used. This information-theoretic query proof can condition on the full independent G table as local circuit data, requiring N log2(N-1) bits of entropy and at most nN bits of entry storage, plus full lower-limb/outside tables, mask gates, workspace and coherent registers. These finite but potentially enormous costs are charged; no table is generated. The mark oracle is the sole unknown resource counted by Q. An efficient exact nonbinary table replacement is a separate lemma, not part of this claim or a prerequisite for this query-only bound.

**COMPUTED — controls.** One reader checked65536 complete-overlay worlds, exact miss mixtures and1024 Fourier worlds/8192 basis states, including a wrong-phase negative control. The other checked2000 clean one-query unitary columns and72 exact marker-law relations. These are finite abstract controls, not source signing runs or whole-source/kernel security proofs.

**OPEN — source application and certification.** TARGET-ONLY-UD-RO.md must supply the honest-service exclusion, all-P/full-limb raw router, zero prequeries, ghost-independent auxiliary state and actual Q_A+1 remote cap for the calling program. Generic fixed-h hardness, efficient circuit implementation, category/capacity and complete quantitative adequacy remain separate. No source/manuscript/old scalar is changed and no whole-source/game kernel declaration is added.
