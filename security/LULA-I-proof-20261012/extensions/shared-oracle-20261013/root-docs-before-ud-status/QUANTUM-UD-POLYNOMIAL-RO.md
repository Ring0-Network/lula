# Quadratic small-query one-target UD bound

**PROVED — manual finite-random-oracle lemma; final subject review pending.** Three separately saved derivations obtain the bound below. It is a successor component, not a replacement of any historical scalar theorem or a certificate for SHA-256, a NIST category, signing capacity or minimal parameter repair.

## 1. Experiment and exact auxiliary premise

**PROVED — definition.** Let N=2^n, n>=1. Choose the typed target restriction ex ante, before the public parameter P. There are zero public-H evaluations or H-dependent advice before receiving P,Y. REAL samples uniform hidden X and gives Y=prefix_n H(P,T,X); IDEAL gives independent uniform Y. After challenge, the distinguisher makes at most Q complete-output XOR queries and returns one bit. Classical queries count as special quantum queries.

**PROVED — required side-state condition.** Conditional on P,Y, the accessible initial quantum/classical state and independently supplied miss/lower/outside functions have the SAME joint distribution in both experiments, independent of the respective whole marker field. Separate independence alone is insufficient: an independently given experiment-label bit distinguishes at Q=0. No side service reads X or answers uncounted queries to the unknown restriction. Services may adapt to previously counted replies; their fixed code and independent initial coins must satisfy this condition. Mixed/entangled reference registers are included by purification. The simulator must use the same algorithm in both branches.

## 2. Common completion and exact marker laws

**PROVED.** Conditional on P,Y, independently sample miss values G(x) uniformly from[N] excludingY, independent lower limbs, and full outside responses. Let b indicate that the prefix equalsY. IDEAL has iid Bernoulli lambda=1/N coordinates. REAL chooses hidden uniform X, forces b(X)=1, and otherwise samples the same iid coordinates. The complete selected response is Y with its independent lower limb when b=1, or G(x) with that same lower limb otherwise. Both complete joint laws are exact. REAL coordinates are correlated, with

`Pr_REAL[b]=|b|*Pr_IDEAL[b]`.

**PROVED / CITED — one-query simulation.** The clean known-pair completion in SINGLE-TARGET-PRE-RO.md applies to these same hit/miss pairs. Apply the known miss XOR; Fourier-transform the response; compute the known parity of its frequency against the hit/miss difference into a plus/minus query scratch; make one ordinary Boolean XOR query; undo the known scratch preparation and transform. Off-restriction words have zero difference and use invariant-plus scratch. This simulates the complete output, including lower limbs and coherent outside branches, with at most one Boolean query per full call. It needs neither a controlled unknown oracle nor an additional unknown-oracle uncomputation call.

**PROVED — cost boundary.** Exact miss values have N-1 possible outputs. A finite eager miss table is a valid information-theoretic auxiliary construction; its entropy, storage, generation and lookup/circuit costs remain charged. It is not silently generated here or identified with a biased modulo sampler or an efficient binary-field family. These query bounds do not imply circuit lower bounds.

## 3. Acceptance polynomial and integer-grid derivative

**CITED.** Beals et al., Quantum Lower Bounds by Polynomials, Lemma4.2 bounds the acceptance-polynomial degree by2Q; Lemma3.2 supplies symmetrization. The statements are read in the [author-hosted primary paper](https://homepages.cwi.nl/~rdewolf/publ/qc/polynomials.pdf). Its Theorem4.12 also states the integer-grid derivative inequality used below. These are polynomial ingredients, not a cited pre-existing UD theorem.

**PROVED.** Condition on common marker-independent auxiliaries and purify measurements. Acceptance is a real multilinear polynomial of degree d<=min(2Q,N), bounded in[0,1] on every Boolean table. Its weight-k average p(k) is an ordinary polynomial of degree<=d: a j-coordinate monomial averages to(k)_j/(N)_j. Therefore0<=p(k)<=1 for integer k=0,...,N, even if the conditioned miss/outside tables are asymmetric. No continuous range claim follows from those grid values alone.

**CITED / PROVED.** Classical Markov's polynomial derivative inequality, rescaled to[0,N], gives ||g'||<=2d^2||g||/N. The sharp first-derivative constant is also stated and discussed in [Shadrin's proof-bearing treatment](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), section1.1. Put g=p-1/2 and M=||g||_[0,N]. A maximizer is within1/2 of an integer grid point, so M<=1/2+d^2 M/N. For d^2<N,

`M<=N/[2(N-d^2)]`, `||p'||<=d^2/(N-d^2)`.

This is also the rearranged Beals Theorem4.12 with integer bounds0 and1. The denominator retains possible between-grid overshoot.

## 4. Advantage theorem

**PROVED.** For L~Bin(N-1,lambda) and independent B~Bernoulli lambda, REAL weight is1+L and IDEAL weight isL+B. Both laws are uniform within weight. Thus their signed acceptance gap is exactly

`Delta=(1-lambda) E[p(L+1)-p(L)]`.

The mean-value theorem and the grid derivative bound imply, for4Q^2<N,

`Adv_UD(Q,n) <= u(Q,n)=min(1,(1-1/N)*4Q^2/(N-4Q^2))`.

When4Q^2>=N use u=1. At Q=0, u=0. Absolute values are taken after each signed conditional expectation; the uniform envelope then bounds the average over common P,Y/auxiliary environments. This requires the exact iid/planted laws, not merely their one-point marginals. An alternative valid HK22 linear envelope can still be retained by taking the minimum of applicable bounds.

## 5. Actual source caller and selector weight

**PROVED — manual source-interface application, final subject review pending.** The active UD programs in FIXED-H-HIDDEN-PREDECESSORS.md choose T_r before challenge, then run source A's pre-key phase after challenge. X is an opaque private-F start or an independent internal prefix-replacement coin. The selected designated edge returns Y; preceding connecting edges are already replaced; suffix, root, cache nodes and counters use Y and independently sampled data. A complete response that would disclose X is gated before release; allowed response positions satisfy e>p>r. The decision uses known suffix images and counted final calls, never a hidden-X equality test. The SAME conditional local code/coins apply in both branches. No naturally failing request is made retryable.

**PROVED.** All-P/full-word routing preserves literal aliases and lower limbs. At S!=0 other honest source calls do not hit the selected unknown restriction. Every A raw query counts, and at most one terminal verifier call reaches that restriction, hence R=Q_A+1. Honest outside computation remains charged by the prior whole-call cap. Inactive selectors return the same bit0. At r, their actual active count is

`A_r=32*(2^41+2^36+2^31+2^26)*max(14-r,0)+16*2^21*(254-r)`.

Condition on activity before bounding the signed gap. Summing r=0,...,253 gives A_H=7,628,143,271,608,320. With the unchanged PRE selector count D_H=20,229,886,488,608,768 and kappa from SINGLE-TARGET-PRE-RO.md,

`Pr_HJ[O][Win AND H_final AND S!=0] <= min(1,D_H*kappa(R,128)+A_H*u(R,128))`.

This charges the source zero-seed branch once outside a complete composition. It does not sum standalone seed-zero charges for every component.

## 6. Exact arithmetic, stronger existing bound and open goal

**COMPUTED.** root-ud-polynomial/controls.py produces108 exact low-degree acceptance-polynomial controls and17 exact marker-weight checks; negative advice controls distinguish permitted/common auxiliaries from leaked hidden markers. Its32 rational source-component rows retain all eight q values and both cache modes. At Q_A=2^32 this new envelope is approximately0.01042740466035393; at Q_A=2^64 it caps1. Uncapped expression crossings have adjacent pass/fail integers29,741,080,993/29,741,080,994 at1/2 and42,060,240,100/42,060,240,101 at1. These are sufficient-envelope crossings, not attacks.

**PROVED — preserve the stronger source route.** The historical direct H bound min(1,(2Q_A+sqrt(3017))^2/N) remains substantially stronger at Q_A=2^32. No old calculator, theorem or complete total is replaced by this weaker interface route. The new result supplies an explicit small-query ordinary-primitive constant with verified caller conditions.

**OPEN.** A complete adequate original level/category/capacity certificate and a successful smallest parameter repair remain unestablished. The separate source-specific private-K polynomial application is still a candidate. No manuscript/source/timing change or new machine-checked whole-source/game declaration accompanies this lemma. The printable full-security claim remains "not established".
