# Independent conditioned-row count and abstract amplification audit

Saved before reading root-preimage-criterion/DEPENDENCY_SUCCESSOR.md. This is a read-only mathematical/probabilistic audit. No source-signature construction, attack implementation, real SHA search or source-to-abstract binding is performed.

## 1. Exact sampling hypothesis

Let the finite function have a full output alphabet whose designated prefix has N equally likely values, N>=2. Sample outside variables, choose one input P* using only them, sample its full image Y, and complete all other inputs with mutually independent uniform full images. Let Sigma=(outside,P*,Y). The **necessary hypothesis** is conditional iid uniformity of the residual images given Sigma, not merely absence of a syntactic direct hash call. Outside variables containing residual-derived information would break that hypothesis.

Choose a row of exactly N distinct inputs injectively as a function of Sigma, before inspecting residual values. Conditional on Sigma, the row and target prefix prefix(Y) are fixed. Its residual points have independent match indicators Bernoulli1/N. Therefore:

* If P* is outside the row, M~Bin(N,1/N).
* If P* is in the row, its image matches by definition and M~1+Bin(N-1,1/N).

If membership varies with Sigma, the unconditional law is a mixture of these two distributions; it need not be either single law. However both cases have the same exact singleton probability

    Pr(M=1 | Sigma)=(1-1/N)^(N-1)=p_N.

Thus the event M=1 is independent of Sigma, even though M itself need not be. Injectivity is essential: repeating one row point can create perfectly correlated indicators and invalidates the binomial law.

For N>=2, log(1-1/N)>-1/(N-1), hence p_N>e^-1. The elementary series bound e<3 gives p_N>1/3. For N=1 the singleton probability is1 (interpret the formal0^0 as1); no asymptotic approximation is needed.

## 2. Prerequisite probabilities without invented independence

For two events A,B with marginal probabilities strictly greater than31/32, the union bound gives

    Pr(A and B)>15/16.

Their product is not justified. If A and B are Sigma-measurable in the exact sampler above, the constant conditional singleton probability gives

    Pr(A and B and M=1)=p_N Pr(A and B)>5/16.

This is an actual conditional-independence consequence, not an assumption that A and B are independent of each other. If the prerequisites are not known to be Sigma-measurable and may depend on residual row outputs, only the general bound is available:

    Pr(A and B and M=1)>p_N-1/16>13/48.

The latter is still positive but differs from the product. A residual-dependent prerequisite can remove some singleton worlds. Source-level identification of the outside sigma algebra/prerequisite measurability is OUTSIDE this audit.

## 3. Abstract search interface and exact rotation

Assume an accessible injective row index unitary, a uniform superposition over its N indices, the known target prefix, and a full-output XOR function oracle. Computing the word, comparing its prefix to the target with a phase flip, then uncomputing the word implements one clean marked phase using two function queries. The reflection about the uniform index state requires no function queries. These are abstract interface assumptions; no actual source row circuit or available payload is supplied here.

Conditional on M=1, let theta=asin(1/sqrt(N)). The two-dimensional reflection/phase product is a rotation by2theta, so after t marked phases the measured singleton success is

    sin^2((2t+1)theta), with function-query cost2t.

For N=s^2 with even integer s>=2 and Q=s, t=s/2 uses exactly Q queries, if the final mathematical success test is not charged to the algorithm. Its angle is (s+1)asin(1/s). That angle decreases from pi/2 to1 for s>=2: its derivative is negative using asin(x)<x/sqrt(1-x^2). Consequently the success is at least sin^2(1)>1/2. This lower bound does not use an estimated maximum runtime or a source attack.

If a final classical oracle check must also fit inside Q, choose t=floor((s-1)/2)=s/2-1, leaving one query available. The angle is (s-1)asin(1/s). For s>=8 it lies above7/8>pi/4 and below pi/2, hence success>1/2. Small s differs: s=2 gives1/4; s=4 gives a value below1/2. The budget convention must be stated.

At N=2^128, s=2^64. Both conventions have success close to sin^2(1), about0.7080734183; exact large-integer t differs by one. No claim is made about realizing this abstract interface against any real implementation.

## 4. Combined lower-bound interpretations

If prerequisites are Sigma-measurable and the stated abstract algorithm can be run on every successful prerequisite world, the generic product with the conditional singleton search lower bound gives success>5/32. Without that measurability, the uniform-in-all-singleton-worlds search lower bound and the general union estimate give success>13/96. These are **conditional abstract experiment** probabilities, not a source-level forgery probability, a concrete hash attack, or an implementation security verdict.

The audit requires separate proof of conditional residual independence, row injectivity/accessibility, prerequisite marginal meanings and query accounting. Source-to-abstract binding is explicitly OUTSIDE scope and remains unverified here.

**Status: INDEPENDENT_ABSTRACT_COUNT_UNION_AND_AMPLIFICATION_DERIVATION_SAVED.**
