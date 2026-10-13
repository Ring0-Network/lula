# Independent positive-certificate and script review

**ACCEPTED — exact rational classical upper certificates only.**

The exact root note, calculator, parameter tuple and both 24-row certificate
files were read. Their complete input hashes are bound in the companion JSON.
The original script was executed with `-I -B` twice, with outputs directed to
this reviewer's fresh replay directory. Both calls exited0 and reproduced the
root certificate files byte for byte. Commands and outputs are recorded in
POSITIVE-CERTIFICATE-CONTROLS.json. No original output was overwritten.

## Independent mathematics and implementation check

For integer Z, 1-(1-1/t)^Z<=Z/t. The identity Z^r=sum_j S(r,j)(Z)_j has
nonnegative coefficients. For binomial Z, E[(Z)_j]=(q)_j/B^j<=q^j/B^j.
Hence pF<=min(1/t,T_r(q/B)/t^(r+1)). This is a positive upper bound on the
finite-binomial law; no Poisson distribution is substituted for that law.
The independent checker computes S(r,j) by its inclusion-exclusion closed
formula, rather than copying the root recurrence. It verifies all48 exact
rational rows, plus the tighter finite-binomial factorial-moment upper and
756 separate exact small-binomial cases, including q0/B1. There is no
floating arithmetic in a certificate comparison. Display logarithms only are
checked against recomputed approximations.

With L=2^32 and beta=1-1/t, ln(1-u)<=-u and e>2 yield beta^L<=2^(-L/t).
The integer exponent L/t=2^(32-a) is weakened downward to at most2048, making
the dyadic upper larger. All48 rows retain its q multiplier. Fifty-five exact
small counter checks additionally pass; they do not replace the analytic proof.

For r17/a10/heights(10,10,11,11,21), ell(32,32,32,32,16) and original sums:
H3017, G3256 and C6281; serialized signature6344bytes, public key32bytes,
top cache payload75497456bytes. The 6281 number is a theorem constant, not
signature bytes. Digest allocation243bits and all schema representation and
strict-target guards pass. Width/seed/message conventions are unchanged.
The top height remains21, so retained top payload stays the same; this says
nothing about the changed lower-tree setup/reconstruction cost or availability.

T17(2)=18880288847750<2^45, so for every q<=2^64, pF is bounded above by that
integer divided by2^180. The positive upper's display exponent is approximately
135.898053929941; it is not a security work factor. Every illustrated Q125
complete row is strictly below1/2. Since q/B powers and every bridge/honest/
counter term are nondecreasing for integer q>=0, the q64 row proves the same
claim for all integer q<=2^64, not merely the eight sampled capacities.
Every Q128 row caps1 because its public-slot fee already exceeds1. All full
terms are summed before capping, and all comparison flags agree exactly.

## Scope and preservation

No substantive defect was found. The root script's narrow valid-input schema
is sufficient for these two declared tuples; this review does not certify a
general CLI validation service or arbitrary malformed JSON exception behavior.
The baseline positive bound is conservative and remains separate from sharper
historical pF/threshold computations. The height example is an analytical
source-schema illustration, not a retuned binary, performance result, proved
availability condition, original128/category guarantee or minimal repair.
The classical uniform theorem and source/historical pins remain unchanged.
No retuned QROM follows. New source-game/kernel declarations0; whole goal
complete false. This is a technical certificate review, not core-index approval.
