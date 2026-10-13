# Root first derivation: small-query one-target UD

**PROVED candidate / OPEN independent review.** Saved before reading any new peer polynomial derivation. This is an information-theoretic full-random-oracle lemma with a fixed, ex-ante selected restriction, zero unknown-oracle evaluations before challenge, and auxiliary data independent of the whole Boolean marker field after conditioning on public challenge Y and P. It is not a fixed-SHA theorem or a category certificate.

## 1. One-target distribution and one-call completion

**PROVED.** Let the unknown restriction have N=2^n inputs and N possible prefix outputs. In the random branch Y is uniform independent of H, so b(x)=[H(x)=Y] are iid Bernoulli lambda=1/N. In the real branch sample hidden X uniformly, sample uniform Y, set b(X)=1, and sample all other b coordinates iid Bernoulli lambda. Independently sample exact miss outputs G(x) uniformly from outputs other than Y. Selected-prefix response is Y if b(x)=1, else G(x). Full lower limbs and every off-restriction response remain independent services. This constructs the exact two joint laws, not a coordinatewise-independent replacement of the real law.

**CITED / PROVED.** SINGLE-TARGET-PRE-RO.md supplies a clean one-Boolean-query full-word completion. For fixed known response pair r0(x),r1(x), use an invertible response-basis map sending r0 XOR r1 to a single bit; inactive response mask uses a plus state. No controlled unknown oracle or second uncomputation call is needed. Consequently Q full-hash queries become at most Q Boolean queries. Independently sampled auxiliary functions/state can be conditioned upon, even if their preparation costs enormous local work; these costs are charged separately, not silently made efficient. Auxiliary data may depend on Y/P, but may not reveal X or depend on b.

## 2. Polynomial acceptance and symmetrization

**CITED.** Beals, Buhrman, Cleve, Mosca and de Wolf, Quantum Lower Bounds by Polynomials, section4.1 acceptance-polynomial theorem, and Lemma3.2 symmetrization: acceptance probability of a Q Boolean-query algorithm is a real multilinear polynomial degree at most2Q; averaging over permutations gives a univariate polynomial p(k) degree at most2Q. Mixed initial states and intermediate measurements are allowed (paper footnote on page4). Primary source: https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf .

**PROVED.** Condition on all marker-independent auxiliaries. The resulting bit algorithm is defined on every Boolean table, and acceptance is in[0,1] on each table. For every integer k in[0,N], average over uniform weight-k tables; thus0<=p(k)<=1. Arbitrary asymmetry of the conditioned miss/outside tables does not obstruct this averaging. It is not necessary to assert p lies in[0,1] between grid points.

## 3. Grid-to-continuous derivative estimate

**CITED.** Markov's polynomial inequality on[-1,1]: degree-d g satisfies ||g'||<=d^2||g||. Shadrin, Twelve Proofs of the Markov Inequality, section1.1: https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf . Beals et al., Theorem4.12 states the corresponding integer-grid derivative inequality directly.

**PROVED.** Put g=p-1/2 and M=max_[0,N]|g|. Every point in[0,N] is within1/2 of an integer in[0,N]. The scaled Markov inequality is ||g'||<=2d^2 M/N. At a maximizer of |g| this yields M<=1/2+d^2 M/N. If d^2<N then M<=N/[2(N-d^2)], hence ||p'||<=d^2/(N-d^2). If d=0 the derivative iszero. This is also obtained by rearranging Beals Theorem4.12 with b1=0,b2=1. The denominator is essential; no illicit continuous-grid bound is assumed.

## 4. Exact weight coupling and advantage

**PROVED.** Let L~Bin(N-1,lambda) and B~Bernoulli lambda independently. The real table is exchangeable with weight1+L, and the random table is exchangeable with weightL+B. Their acceptance gap is exactly

`(1-lambda) E[p(L+1)-p(L)]`.

Taking absolute values after the expectation and using the derivative estimate gives

`Adv_UD(Q,n) <= min(1,(1-1/N)*4Q^2/(N-4Q^2))` when4Q^2<N; otherwise use1. Q=0 gives0. This absolute bound survives averaging over marker-independent Y/P/auxiliary parameters. The real table's coordinates are correlated; the proof uses its exact exchangeable law, not independence.

## 5. Source use and unresolved obligations

**OPEN caller review.** The accepted target-only UD source programs appear to satisfy the chronology and hidden-variable premises: challenge before source pre-key A execution, opaque X selected F/internal coin, honest selected edge replaced by Y, and all unknown target calls including terminal verifier counted in R=Q_A+1. Before integration independently verify no free target-row answer, no marker-dependent source advice, and no latent X read. The active-selector conditioning factor A_H is unchanged.

**PROVED candidate.** If that audit passes, the existing component becomes min(1,D_H*kappa(R)+A_H*Adv_UD(R,128)), with D_H=20229886488608768 and A_H=7628143271608320. It retains the original PRE term and the stronger direct H envelope. It does not change any old scalar table without a separate complete composition review.

**OPEN additional application.** A source-specific private-K hop might use the same degree/grid argument for a unique hidden marker versus all-zero table, giving4Q_A^2/(N-4Q_A^2). This requires a separate exact typed-domain simulation with all genuine F services, actual private-P services, and logical caches. It is not yet proved here. The S=0 alias branch cannot be omitted. No full-security or repaired-parameter claim follows from either component alone.
