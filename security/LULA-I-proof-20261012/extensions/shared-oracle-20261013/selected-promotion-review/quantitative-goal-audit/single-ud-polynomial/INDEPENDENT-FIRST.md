# One-target random-function UD: independent small-query polynomial derivation

Saved before reading ANY new root/peer polynomial-UD derivation. Parent supplied the candidate direction; I do not claim independent discovery of that direction. The calculation below independently derives its finite constant and audits the grid-to-continuum step. No source/paper/scalar edits or actual attack/measurement occur.

## 1. Exact experiment and shared completion

ASSUMED: N=2^n, n>=1; one tweak is fixed independently before the challenge; there are zero prior public-function queries or target-function-dependent initial data. The full random function has an independent n-bit prefix at every selected framed input x in[N]. Public P and challenge Y are uniform. In the REAL UD branch Y is the image of a hidden uniform X; in the RANDOM branch Y is independently uniform. A makes at mostQ full-word XOR queries and finally outputs an acceptance bit. Independent outside functions, lower limbs and auxiliary data are retained and charged separately; they must be independent of the marker field conditional on public P,Y. This is a finite query-only random-function model, not fixed-SHA hardness or a source calling theorem.

PROVED: condition on P,Y and independently sample a non-Y prefix table G(x), full lower limbs and truly outside tables. Complete the selected row as prefixY when b(x)=1, elseG(x). RANDOM uses iid b(x)~Bernoulli(p), p=1/N. REAL plants one uniformly chosen X with b(X)=1 and independently samples all other bits with the same p. The conditional complete-function/challenge laws are exact. All local tables are independent of the WHOLE field b in both branches. The latent planted input does not enter the algorithm or local metadata. The previously derived Fourier/linear-map completion gives ONE ordinary Boolean XOR call per full-word query, including delta-zero outside words with a plus response. Raw aliases are classified by actual bytes. Thus the simulated acceptance algorithm hasQ Boolean queries, not2Q.

## 2. Acceptance degree and symmetrization

CITED(primary): Beals, Buhrman, Cleve, Mosca and de Wolf, *Quantum Lower Bounds by Polynomials*, arXiv:quant-ph/9802049v3, Lemmas4.1–4.2, gives amplitude degree<=Q and acceptance-probability degree<=2Q for Boolean XOR queries. Its Lemma3.2 symmetrizes a multilinear polynomial into a univariate polynomial in Hamming weight without increasing degree. I read the actual primary PDF, pages3–5 (one-based), and cached it locally. Adaptive measurements/mixed states can be purified with copied outcomes and at-mostQ slots padded by an invariant plus query; local auxiliary gates independent of b do not increase degree.

PROVED: for each fixed independent auxiliary realization, acceptance is a real multilinear polynomial in the N mark bits of degree d<=2Q, and is in[0,1] on EVERY Boolean input, including the all-zero field. Average over the independent auxiliary distribution and all mark-coordinate permutations. The resulting univariate a(k) has degree<=d and satisfies0<=a(k)<=1 at every integer k=0,...,N. REAL and RANDOM fields are exchangeable; conditional on weightk their bit patterns are uniform. Consequently both branch acceptances are expectations of this SAME a at their respective weight laws. Symmetrizing an arbitrary algorithm is analytical averaging, not a claim the actual algorithm is symmetric.

## 3. Exact binomial difference identity

PROVED: let J~Binomial(N-1,p). RANDOM weight has law K=J+B with independent B~Bernoulli(p), whereas REAL weight is J+1. Therefore the SIGNED difference is exactly

    E_real accept - E_random accept
      = (1-p) E_J[a(J+1)-a(J)].

Equivalently the planted weight law is size-biased by k/(Np), withNp=1. No Poisson approximation, query-history sampling or conditional survival law is used. Hence the absolute gap is at most(1-p)*max_{0<=k<N}|a(k+1)-a(k)|. Averaging side data before absolute value is essential; an arbitrary per-label absolute gap is not being substituted for a signed ordinary advantage.

## 4. Grid-to-continuum step: the denominator cannot be omitted

CITED(primary): A. Markov, *On a question by D. I. Mendeleev* (original1889/1890, English translation at history-of-approximation-theory.com/fpapers/markov4.pdf), ProblemNo.2, final conclusion on printed16, proves for degree<=d real polynomials on[a,b], ||u'||<=2d^2||u||/(b-a). I checked that conclusion in the actual translated primary paper. Shadrin's exposition was used only to locate/check the classical normalization, not as a substitute for this primary source.

PROVED: put u(t)=2a(t)-1 and M=max_{t in[0,N]}|u(t)|. On integer nodes |u(k)|<=1, but M may exceed1. Markov on[0,N] gives ||u'||<=2d^2 M/N. For any realt choose an integer k at distance<=1/2, including the endpoints. Then

    |u(t)| <= 1 + (1/2)||u'|| <= 1+(d^2/N)M.

Taking the supremum and assuming d^2<N yields M<=N/(N-d^2). Since a'=u'/2,

    ||a'|| <= (d^2/N)M <= d^2/(N-d^2).

Each unit adjacent difference is at most that derivative supremum. This explicitly proves the discrete-grid extension and retains the centering factor2. Treating grid boundedness as continuous boundedness and writing d^2/N directly is NOT justified. No analytic derivative is taken of a piecewise discrete acceptance table; it is the univariate polynomial extension supplied by symmetrization.

## 5. Finite one-target conclusion

PROVED, conditional on the stated model and cited polynomial/Markov theorems: if4Q^2<N,

    Adv_UD(A) <= min(1,(1-1/N)*4Q^2/(N-4Q^2)).

The function d^2/(N-d^2) is monotone on0<=d^2<N, so replacing the actual degree d by2Q is valid. If4Q^2>=N use1, without a negative/zero denominator. AtQ=0 both branch input distributions coincide to A and the advantage is0, matching the formula. The bound is an upper envelope, not an optimality theorem. For largeQ it may be vacuous and can be combined with the preserved12Q/sqrtN bound only within the same exact primitive/query interface.

PROVED(scope): the exactN-1 miss tables may be enormous and require exact finite-alphabet randomness, local circuit/data/storage and lower/outside resources. No binary modulo or efficient2T-wise nonbinary sampler is inferred. The degree theorem counts the unknown Boolean queries; all other gates/data remain explicit resources. A source adapter must separately prove its zero prequeries, independent ghost side-state and remote query cap. This theorem does not remove a selector loss, retune source parameters, identify SHA with a random function or certify category/capacity. New checked source/game declarations:0. Whole goal complete:false.
