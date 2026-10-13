# Blind independent first: quadratic one-target UD in the small-query regime

Saved before reading ANY new root/peer UD-polynomial proof. Parent supplied the proposed bound and proof direction, not the proof. **Manual finite-query random-function result, not fixed-SHA hardness, optimal advantage, efficient simulation or source-security kernel.**

## 1. Exact experiment and sufficient side-state condition

Let N=2^n, n>=1. An actual tweak is chosen ex ante independently of the random function. After the challenger samples a uniform parameter P, real UD gives Y=prefix_n H(P,T,X) for independent uniform hidden X; ideal UD gives independent uniform Y. No H query or H-dependent advice precedes the challenge. After P,Y, A makes at most Q coherent/classical COMPLETE output XOR queries and returns a decision bit.

After conditioning on P,Y, all known miss/lower/outside tables and the accessible auxiliary quantum state must have the SAME joint law in real and ideal and be independent of the respective hidden marker field. Mere marker independence separately in each world is insufficient: giving a free world-label bit, independent of the marker, distinguishes atQ0. Arbitrarily entangled/mixed auxiliary registers are allowed if this common conditional law holds; no accessible register or side service may receive hidden X or additional uncounted target answers. Independence is required for the service CODE/coins and the zero-query starting state, not for all outputs of services whose inputs legitimately depend on prior counted oracle replies.

## 2. One common full-output completion, two different marker laws

Condition on P,Y. Sample a common auxiliary table K_high(x) independently uniform in[N]\{Y}, common independent lower outputs L, and common independent full outputs outside the actual target row. The row's complete value is Y||L(x) if m(x)=1 and K_high(x)||L(x) otherwise. Off-row words use their unchanged full outside value. This preserves every output limb and repeat/alias relation.

In IDEAL UD, m is iid Bernoulli lambda=1/N. Its completed row is independent uniformly random H, independent of Y. In REAL UD, pick latent uniform X, set m(X)=1 and sample all other markers independently Bernoulli lambda. Conditional on X,Y this is the true full-function/image law. The real field is correlated. For any Boolean field m with weight k,

Pr_real[m] = k*Pr_ideal[m],

because Pr_real[m]=(k/N)*lambda^(k-1)*(1-lambda)^(N-k) and Nlambda=1. At k0 its real probability is0. This SIZE-BIAS IDENTITY, not just a per-point marginal, is the crucial distributional fact. Arbitrary pairs of correlated fields with similar marginals need not obey the bound.

A full XOR query is simulated with ONE ordinary Boolean query, using the already independently checked completion method: apply the known base XOR, Fourier-transform the response, compute parity of the frequency against the known hit/miss difference, put that parity in a |+>/|-> response scratch, query m on the parsed payload, undo scratch/parity and Fourier transform. Outside words have hit=miss and an invariant plus scratch. Complete lower limbs and arbitrary parameter superpositions are retained. There is no controlled unknown oracle, second marker uncomputation call, known-unmarked dummy or query measurement. Known table/mask/lookup gates and storage are charged separately.

## 3. Acceptance polynomial and symmetrization

Fix P,Y, the known tables and any purification of the marker-independent auxiliary density operator. After Q Boolean XOR calls, amplitudes are polynomials of degree<=Q in marker bits: each query multiplies at most once by m(x) or1-m(x), while all common intervening linear operations preserve degree. A final fixed acceptance projector/POVM gives a real multilinear acceptance polynomial a(m) of degree d<=min(2Q,N). Measurements/adaptive halting may be purified and padded with invariant-plus queries. This includes arbitrary retained reference entanglement and auxiliary services satisfying §1.

Average a(m) over uniformly selected weight-k marker sets to obtain p(k). Each degree-j monomial has average (k)_j/(N)_j for distinct j coordinates, so p is an ordinary real polynomial of degree<=d in k. On EVERY integer k0..N it lies in[0,1]. All those fields are legitimate Boolean oracle inputs, even where the real planted distribution has zero mass. Fixing a nonsymmetric known K table does not harm this mathematical averaging; the iid and planted marker laws themselves are uniform within each weight.

The quantum polynomial and symmetrization ingredients are checked against the original [Beals–Buhrman–Cleve–Mosca–de Wolf paper](https://homepages.cwi.nl/~rdewolf/publ/qc/focs98.pdf), Lemma4.2 and Lemma3.2, PDF pages4 and2 (indices). Its mixed-state remark is on PDF page1. We have independently given the relevant amplitude/monomial argument above; no total Boolean decision-problem lower bound is being imported as a UD theorem.

## 4. Exact binomial finite-difference identity

Let K~Bin(N,lambda), lambda=1/N. The signed real-minus-ideal acceptance gap is

D=E[(K-1)*p(K)].

For Z~Bin(N-1,lambda), E[K p(K)]=Nlambda E[p(Z+1)]=E[p(Z+1)], while E[p(K)]=(1-lambda)E[p(Z)]+lambda E[p(Z+1)]. Therefore

D=(1-lambda) E[p(Z+1)-p(Z)].

This identity holds for every acceptance function on the integer weights, before using its polynomial degree. Consequently |D|<=(1-1/N)*max_(k=0..N-1)|p(k+1)-p(k)|. Average the signed gap over common P,Y/K/auxiliary environments only AFTER bounding its absolute value; all conditional bounds are uniform, so the global advantage has the same upper bound.

## 5. Derive the discrete-grid Markov bound, do not assume a continuous range

Suppose a real polynomial p has degree d,0<=p(k)<=1 at all k0..N, and d²<N. Let q=p-1/2 and M=max_(t in[0,N])|q(t)|. Classical Markov's first-derivative inequality rescaled from[-1,1] gives ||q'||_[0,N]<=2d²M/N. At a point attaining M choose a nearest integer k, distance<=1/2. Since |q(k)|<=1/2,

M<=1/2+(1/2)||q'||<=1/2+(d²/N)M.

Thus M<=N/[2(N-d²)] and ||p'||<=d²/(N-d²). Each adjacent grid difference is at most that derivative norm. This bridge is necessary: the acceptance polynomial need not stay in[0,1] BETWEEN integer weights. We use the exact first-derivative classical Markov inequality, not a probability-tail inequality named Markov.

For verification of this analytic theorem/proof, the author-provided [Shadrin, Twelve Proofs of the Markov Inequality](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.1, gives the sharp first-derivative constant d² on[-1,1] and includes proof treatments. Its original1889 reference is historical attribution, not an original paper claimed read here. The author-hosted quantum primary paper above is the primary reference for the query/symmetrization step; the discrete-grid consequence is derived here explicitly.

## 6. Verdict and explicit finite envelope

Substituting d<=2Q gives the proposed lawful small-query bound:

Adv_one-target_UD(Q,n) <= min(1,(1-1/N)*4Q²/(N-4Q²)) if4Q²<N;
Adv_one-target_UD(Q,n) <=1 otherwise.

At Q0 the value is0, as required because public Y/P and the common auxiliaries have identical marginal laws. At N1, if that degenerate case were allowed, both experiments are identical and advantage0; this first fixes n>=1 to avoid an empty miss alphabet. The rational envelope may exceed1 even before the denominator vanishes; the outer min1 is legitimate and must not be omitted when interpreting it as a probability.

The theorem uses the exact iid-ideal/planted-real pair, ONE marker query per full call, and common conditional marker-independent side data. It does NOT follow from the previous PRE marginal-only lemma. A two-marker simulation would only justify degree4Q and the weaker replacement16Q²/(N-16Q²). A caller with Q_A+1 unknown-target evaluations must use Q=Q_A+1, not drop its final examiner call. Efficient exact nonbinary miss/outside implementation and the caller's side-state/query audit remain separate obligations.

## 7. Exact sampling resources and controls to run

The known high miss table has N-1 values per entry. Exact sampling may reject the n-bit integer N-1 and then skipY. It has expected N/(N-1) draws per entry, unbounded worst-case sampling time, nN entry storage and expected nN²/(N-1) random bits for the target row, plus independent lower/outside tables and charged lookup/parity/response scratch gates. No biased modulo sampler, free table or efficient nonbinary polynomial family is claimed. The query theorem may condition on finite known tables; no large table is generated by this task.

Exact small-N controls will enumerate the two marker laws and weight bias, verify the signed binomial identity for nonsymmetric low-degree acceptance polynomials, check small-grid polynomials that overshoot the continuous range, and test actual one-query phase/entangled completion states. Negative controls must include marker-dependent advice, world-dependent independent advice, and treating the real field as iid. These controls can refute faulty reasoning but cannot establish source security or optimal quantum advantage. No source/manuscript/old-scalar edits or new source/game kernel declaration accompany this first.
