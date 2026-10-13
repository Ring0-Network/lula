# Positive rational certificate for an analytical height illustration

**PROVED — probability upper method.** For integer Z>=0 and t>=2, Bernoulli's inequality gives 1-(1-1/t)^Z<=Z/t. If Z~Binomial(q,1/B), then E[(Z)_j]=(q)_j/B^j <=(q/B)^j. Expanding Z^r in falling factorials with nonnegative Stirling numbers S(r,j) proves

    p_F(q) <= min(1/t, T_r(q/B)/t^(r+1)),
    T_r(mu)=sum_(j=0)^r S(r,j)*mu^j.

This is an upper bound on the exact finite-binomial moment, not a Poisson equality. Every coefficient is nonnegative, so it is monotone in q/B and can be evaluated with exact rational arithmetic without cancellation. The code uses the moment only inside the independently reviewed guarded classical source theorem.

**PROVED — finite-counter envelope.** With L=2^32 and beta=1-1/t, beta^L<=exp(-L/t)<=2^(-L/t). Here L/t=2^(32-a) is an integer. Replacing its exponent with min(2048,2^(32-a)) weakens this to a tractable exact dyadic upper. It does not declare counter exhaustion zero. The final source probability upper is formed from all nonnegative fees before the final cap1.

**COMPUTED — fixed-n16 illustration, not an executable retuning.** Let r17,a10 and heights(10,10,11,11,21), with original widths, chain counts and targets. This satisfies strict-target and source-coordinate guards; (r+1)a+h=243<=256. Its source-schema signature size is6344 bytes; public key32 bytes; retained top payload75497456 bytes=72MiB minus16. The formula has H3017,G3256,C6281. At q<=2^64, mu=q/2^63<=2, and

    T_17(2)=18880288847750 <2^45,
    p_F <=18880288847750/2^180 <2^-135.

The display exponent135.89805392994097 is the negative logarithm of this p_F upper, not a full-security work factor. The unchanged top height keeps the retained cache size while taller lower trees alter reconstruction/setup work and larger a changes the FORS payload.

**COMPUTED — concrete sufficient classical certificates.** uniform_bounds.py emits all eight requested q values, each at Q2^64,2^125,2^128, using exact Fraction numerators/denominators. Every height-illustration row at Q2^125 has complete upper<1/2. Every Q2^128 row caps1, just as the uniform public3Q/N fee predicts. The finite-counter upper used is q/2^2048, a conservative weakening of the much smaller a10 exhaustion term. The baseline run is a separate positive certificate and does not replace any sharper exact baseline p_F or prior query threshold.

**PROVED — certification ceiling and interpretation.** Any E_p<=eta<1 requires (3Q+2q+C_p)/N<=eta. Hence even perfect coverage tuning cannot make this proof certify eta1/2 at Q>=N/6. This is a limitation of this sufficient family, not an upper bound on actual construction strength or a forgery. The illustration certifies a raw-query success statement at Q2^125 under the source-schema model; it does not certify the original128-bit/AES/category target, availability, a minimal repair or any retuned quantum statement.

**COMPUTED — reproducibility.** Run installed Python with -I -B on uniform_bounds.py, first without --params and then with --params height63-illustration.json. Required --out writes a chosen new JSON output. Each invocation checks the theorem/source hashes, 756 exact small-binomial inequalities, five rejected proof-guard cases and baseline verifier counts/signature/cache sizes. All arithmetic certificate comparisons are exact. Approximate logarithms are display only. No tree, cache, signature, timing measurement or attack is generated.

**OPEN — remaining original goal.** A resource-normalized adequate complete bound and successful smallest repair remain unestablished. Guarded availability and signing/setup cost comparisons must accompany any future feasibility optimization. No undocumented parameter ordering or full-QROM substitution is accepted. Source, manuscript and historical scalars are preserved.
