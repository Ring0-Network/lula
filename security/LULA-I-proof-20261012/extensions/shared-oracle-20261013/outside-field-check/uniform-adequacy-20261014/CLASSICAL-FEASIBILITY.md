# A guarded classical feasibility witness and its adequacy limit

**COMPUTED, conditional on the pinned manual source theorem.** The tuple below certifies success probability below 47/125 = 0.376 at adversarial raw-query budget Q_H=2^125 for every requested signing-query exponent 24, 30, 38, 40, 41, 44, 50 and 64. This is a sufficient classical constant-success query certificate. It does not establish the original 128-bit/category criterion, a smallest repair, an optimal attack threshold, a practical implementation or retuned QROM security.

The blind derivation `INDEPENDENT-FIRST.md` was saved before reading `PARAMETER-UNIFORM-CLASSICAL-THEOREM.md`, SHA256 e5fc68bc269ca98672caa99ec70d5695d3d578095a62ebbfc0f99f9d8fbc394b. That manual theorem is the inherited source bridge for this computation; its complete proof is not recertified by these finite controls. Its assumptions include uniform full-output random h, classical public queries, atomic completed signing replies, absorbing actual counter exhaustion, fresh-message strict verification and guarded source parameters. Fixed SHA hardness is not inferred. The original two goal attachments were read completely; the prior own criterion audit and baseline-only deliverables remain unchanged.

## Guarded candidate and exact positive coverage bound

Use n=16 bytes, r=17 real FORS trees, a=10, five layers of heights (10,10,11,11,21), digit widths (4,4,4,4,8), lengths (32,32,32,32,16), target sums (240,240,240,240,2040), BE32 counters and top-only caching. Here total height is 63, (r+1)a+h=243<=256 and r*2^a=17408<=2^32. Every height lies in [0,31]; every target sum is strictly below ell*(w-1); widths, addresses and fixed scratch buffers fit the source schema. These are mathematical source-schema parameters; no retuned executable was created.

For Z~Bin(q,2^-63), beta=1023/1024, the uniform theorem gives

    p_F = E[(1-beta^Z)^17]/1024.

The union inequality 1-(1-1/t)^z<=z/t for integer z>=0 gives p_F<=E[Z^17]/2^180. Expand Z as a sum of Bernoulli indicators. Partition the 17 ordered factors in Z^17 by their j distinct indicator indices; this proves exactly

    E[Z^17] = sum_(j=0)^17 S(17,j)*(q)_j*rho^j
             <= sum_(j=0)^17 S(17,j)*(q*rho)^j.

All coefficients are nonnegative. For q<=2^64, q*rho<=2 and therefore

    p_F <= 18880288847750 / 2^180 < 2^-135.

The integer 18880288847750 is the exact Touchard value T_17(2), obtained by the recurrence S(n+1,j)=j*S(n,j)+S(n,j-1). No Poisson equality or numerical cancellation is used: a Poisson raw moment only supplies a convenient positive polynomial upper bound for the exact binomial moment. The controls additionally evaluate the smaller q-dependent Touchard upper polynomial. For finite exhaustion, beta^(2^32)<=exp(-2^22)<2^-4096, using e>2 and 2^22>4096; thus q*beta^(2^32)<q/2^4096. No failed counter search is resampled or normalized away.

The final typed-call ledger is

    t_i=ell_i*(w_i-1)-S_i = (240,240,240,240,2040),
    H_p=3017, G_p=3256, C_p=H_p+G_p+d+3=6281.

Substitute these into the actual uniform classical theorem:

    E_p(q,Q)=cap((3Q+2q+6281)/2^128
       +(qQ+binom(q,2)+q)/2^256
       +q*(1023/1024)^(2^32)+(Q+1)*p_F).

Exact Fraction arithmetic supplies an outward upper certificate for each row, then rounds upward to a numerator over 2^256. The integer numerators in `CONTROL-RESULTS.json` are the certificates; decimal displays are rounded illustrations only. At Q=2^125, all eight rows have that exact outward certificate <47/125<1/2. The largest rounded display, at q=2^64, is 0.37552403328475864. Monotonicity is justified term by term: the scalar/bridge/tail are increasing in q, and the positive Touchard polynomial is increasing in q. At Q=2^64 all eight rows are also below one half; at Q=2^128 all rows cap at one. The last outcome means no guarantee from this envelope, not an actual attack.

The file also records a sufficient half-success query budget obtained by flooring (1/2-intercept_upper)/slope_upper. Because its coverage input is an upper bound, this is a sufficient budget, not an exact or optimal envelope crossing. No neighboring-budget failure is claimed.

## Exact cost consequences

All counts below are analytic source counts, without timing, namespace enumeration or cryptographic execution. Tail compressions refer to the source's public-prefix optimization; the once-per-Ctx prefix compression is separately charged.

| Quantity | Candidate |
| --- | ---: |
| Signature bytes | 6344 |
| Logical top-cache payload bytes | 75497456 |
| Top cold-subtree reconstruction tail compressions | 8602517503 |
| Top-only keygen fixed tail compressions | 2250573348863 |
| One cached signing call, fixed tail compressions | 3262542 |

The signature formula is 16+4+16*r*(a+1)+sum_i[4+16*(ell_i+h_i)]. The top cache contains (2^22-1) 16-byte nodes and 2^21 four-byte counters; it contains no secret seeds. Logical payload is distinct from a driver fixture's serialized metadata and secret seed.

A lower WOTS public key costs 32*16+9=521 tail compressions, including private starts; a top public key costs 16*256+5=4101. A height-h subtree costs 2^h*leaf_cost+(2^h-1). Each top keygen leaf additionally computes its immediate height-11 child subtree, costing 1069055. Thus fixed setup is 2^21*(4101+1069055)+(2^21-1), versus baseline 43631247359. Add all 2^21 canonical top-row trial counts, one tail compression per trial, and the public-prefix Ctx initialization. The unchanged cold top subtree reconstructs only public keys and Merkle nodes; it does not include child-root generation or canonical-row preparation, so it cannot substitute for keygen cost.

The cached-signing fixed count comprises FORS 52229, four lower subtree reconstructions 3207164, five WOTS signature chains/private starts 3144 and five reevaluations of the accepted type7 digest. Add message nonce/inner SHA blocks, outer counter trials and four uncached lower-row trial counts. These extra costs depend on message length/counters; none is omitted as free work. The exact accepted-digest coefficients are recorded over denominator 2^128, including the full omitted-zero rule. Positive dynamic programming proves lower-row acceptance >=2^-8 and top-row acceptance >=2^-12. For an isolated genuine fresh row with cap C=2^32, expected charged trials are (1-(1-theta)^C)/theta, with bottom retained. Neither those coefficients nor the fixed counts assert successful completion of the whole key/signing experiment.

## What is still required for the original target

**PROVED limitation of this classical envelope for every guarded tuple.** Strict sum guards give integer t_i>=1. Consequently C_p=r(a+2)+2*sum t_i+h+2d+4>=11. Even at Q=q=0, this particular numerical upper envelope exceeds 1/N. At Q=N, its 3Q/N term alone caps it at one. Hence no parameter search within this theorem can make its certificate satisfy the literal success<=2^-128 at Q_H=2^128 reading. This is a statement about a sufficient upper certificate, not a lower bound on actual forgery probability or impossibility of a stronger proof.

**CONDITIONAL limitation of an unchanged QROM proof architecture.** The blind first proves that if the current four positive public-component formulas were extended uniformly unchanged, their union envelope has floor cap((36+8*sqrt(2))*(Q/2^64)^2). At Q=2^61 this floor exceeds one half. Exact rational enclosure of sqrt(2) checks that discriminator. A genuinely new uniform QROM proof might change the coefficients or decomposition, so this is not asserted of all possible QROM proofs. The current root uniform theorem proves only the classical family; retuned QROM source certification remains open. No hypothetical retuned QROM numerical value is promoted here.

The smallest useful next scientific obligation depends on the declared criterion. For the stated classical constant-success proxy, the inherited uniform theorem plus these arithmetic certificates supply a concrete costed witness. For a retuned quantum proxy, a source-uniform QROM theorem is still needed before parameter substitution. For the literal tiny-probability/full-budget goal, these architectures must be strengthened or the intended criterion must be precisely resolved; further coverage optimization alone cannot close it. For AES category1, a justified comparison in the relevant circuit/resource metrics is required; raw query counts, probability exponents and half-success envelope thresholds do not establish that comparison. No unconditional SHA or compiler proof is added as a prerequisite.

No size/computation ordering over repairs was specified, no complete parameter-domain search was performed and no smallest-repair claim is made. New source/game kernel declarations: zero. Whole original goal: not established.

## Reproduction

Run `python -I -B controls.py` in this directory. It checks immutable source/theorem pins, 720 exact toy binomial/coverage inequalities, 24 full outward rows and one conditional architecture inequality, for 745 counted checks. Additional asserted geometry, counts and positive dynamic-programming identities are not included in that count. The toy tests corroborate the stated finite identities; the mathematical arguments above carry the general quantifiers.
