# Independent quantum-cut selector averaging and resource derivation

**PROVED / COMPUTED / ASSUMED — saved before new quantum peer drafts.** I have not read chain-pre-independent/quantum-prefix or the adapter's quantum candidate. This derivation starts from the supplied per-coordinate square-root inequality; it does not prove its quantum source simulator premise. Existing classical promotion/current-document receipts remain immutable.

## Protected and interior-cut domains

Write A=2^41+2^36+2^31+2^26. WOTS protected coordinates number D_W=32*15*A+16*255*2^21=1,089,588,072,284,160. Their position-zero coordinates number U_W=32*A+16*2^21=72,638,667,948,032. Only positions r=1,...,w-2 have an unknown public predecessor-cell cut, so D_cut=32*14*A+16*254*2^21=D_W-U_W=1,016,949,404,336,128. Real FORS leaves number D_F=2^41*17*512=19,140,298,416,324,608; they have no public predecessor cut. The union D_H=D_W+D_F=20,229,886,488,608,768 is padded to L=2^55. The noncut valid labels number U_W+D_F=19,212,937,084,272,640. Dummy ranks have p_j=b_j=delta_j=0. Position-zero WOTS and real FORS labels have delta_j=0 under the proposed exact noncut simulator premise, not because their source security is zero.

## Correct averaging

Assume nonnegative p_j,b_j and delta_j for every padded rank, with sqrt(p_j)<=sqrt(b_j)+delta_j. Assume the source event probability P is bounded by sum_j p_j; a unique final-witness assignment would give equality, but that is a separate source-event premise. Let b_bar=(sum_j b_j)/L be the actual success probability of the padded-selector reduction, and assume delta_j<=delta=2Q/sqrt(N) on interior cuts and delta_j=0 elsewhere.

Squaring and summing gives sum p_j <= sum b_j+2 sum sqrt(b_j)*delta_j+sum delta_j^2. Cauchy-Schwarz bounds the mixed sum by sqrt(sum b_j)*sqrt(sum delta_j^2). Therefore

`P <= min(1, (sqrt(L*b_bar) + delta*sqrt(D_cut))^2)`

or equivalently

`P <= min(1, L*(sqrt(b_bar)+2Q*sqrt(D_cut/(L*N)))^2)`.

Expanded, the uncapped expression is `L*b_bar + 4Q*sqrt(L*b_bar*D_cut/N) + 4Q^2*D_cut/N`. The cross term contains sqrt(L), while the pure cut-error term contains D_cut, not L*D_cut or D_cut/L. Applying Jensen to average square roots in the opposite direction would not establish this bound. An average scalar error (D_cut/L)*delta is insufficient without the L2/Cauchy step; it underestimates the relevant squared-error average.

Since each p_j<=1, one may safely replace delta by min(1,delta) in the square-root inequality: when delta>1, sqrt(p_j)<=1<=sqrt(b_j)+1. Thus a capped-error variant is `min(1,(sqrt(L*b_bar)+sqrt(D_cut)*min(1,2Q/sqrt(N)))^2)`. This refinement matters only as a justified algebraic cap; for any positive integer D_cut it already caps globally at one when the error reaches one. Also b_bar is itself a probability in [0,1], and valid-only branches imply b_bar<=D_H/L. Do not replace a conditional valid-selector success by b_bar without the factor D_H/L.

## Query and source-resource accounting

A complete coherent raw router uses one selected XOR call and one outside XOR call per adversarial logical query, with inactive plus-state responses. Therefore Q logical adversarial calls cost Q coherent calls to each handle and2Q total, not Q total. The source-coupling delta premise uses whichever logical query definition its proof specifies; routing cost must not silently rename Q. A selected type0 or height-zero real FORS address occurs at most once in the final classical verifier at nonzero S. Honest selected-image use is intercepted; hence the selected challenge has Q coherent calls plus at most one final classical call, with target supplied separately.

The localized WOTS prefix/suffix preparation remains at most254 local outside hashes and one preparatory ideal-F label; the selected FORS branch needs zero preparatory hashes. Ordinary source setup/sign/public/private caps remain those of the accepted classical PRE program; final verification contributes at most3224 public calls. Total oracle forwarding includes2Q coherent handle calls plus H_setup+q*H_mode+3224+254 honest/local public work, if the quantum outside function is supplied as an actual oracle handle. If it is an explicitly implemented local coherent table circuit, circuit construction/lookup cost and memory must instead be accounted for; merely stating a lazy classical dictionary does not implement coherent queries on an unknown input.

F distinct labels remain bounded by min(N_D,1+2,181,038,080+q*U_mode), J<=q. Source/cache/tree/message/memo storage remains charged separately from4096 extra selected-chain node bytes. Arbitrary message/query lengths require the original byte-copy/dictionary costs. Local coherent oracle realization may require additional large finite circuit/table workspace and cannot be inferred cheap from the classical caps. No normal source preparation or full forest generation is run by this review.

**OPEN — simulator premise.** The per-coordinate delta inequality, lawful treatment of the unknown predecessor cell, exposure/partiality channels, full256 correlations, and actual PRE challenger interface must be checked independently. This report supplies only the exact namespace, padded averaging and resource consequences conditional on those premises. A quantum source theorem is not established by this algebra alone.
