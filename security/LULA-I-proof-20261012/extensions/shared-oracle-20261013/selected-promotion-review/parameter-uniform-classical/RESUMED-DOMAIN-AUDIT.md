# Resumed guarded-domain audit

Both complete original objective attachments and this reviewer's independently
saved first proof and reciprocal receipt were reread. The final root subject was
then read in full and checked against the actual release source and the fixed
joint classical theorem. No new source-uniform defect was found.

## Source anchors and exact scope

- `lib.rs:121–147`: one literal framed hash; source 24-block tail scratch.
  Its largest variable input is the ordered r-node FORS compressor, so r<=94
  gives ceil((22+16r+9)/64)<=24. Arbitrary raw adversarial words have no such
  length restriction. This is a full-hash RO schema, not a compression oracle.
- `lib.rs:161–187`: private F and message J frames, full256 inner word and
  52-byte outer frame. No private-J/inner vs typed alias is assumed away at S=0;
  the single outer seed-zero charge handles it. K=P or P=S by themselves do not
  invalidate the nonzero-S literal-frame separation.
- `lib.rs:212–235,269–276`: fixed lw4/8, lfull=128/lw, active ell=lfull-z;
  omitted digits really are checked zero. Hence acceptance probability is
  coefficient(S;ell,w)/w^lfull, not coefficient/w^ell. Its rare/finite-bottom
  law is retained, with no successful-row normalization. Strict Smax guarantees
  a nonterminal verifier step even on an unexposed row; endpoint-only maximal
  sums are outside this proof, although representable by the code.
- `lib.rs:333–412`: r=k-1 real FORS trees; the forced coordinate exposes no
  secret. Global parent indices are j*2^(a-level)+(leaf>>level). Ordered root
  inputs retain multiplicity and order, even if numerical node values coincide.
- `lib.rs:470–495`: below+height shift must be <=63 and leaf height <=31.
  A zero-height layer still has a distinct layer ID and a single addressed
  WOTS leaf. Child g=(tree<<height)|leaf is message independent.
- `lib.rs:512–595,601–668`: cache correctness requires a consistent honest
  top segment with canonical first counters and true authentication data.
  A cache is not an arbitrary table of accepted counters. Actual invoked
  unsuccessful search is absorbing, unused rows need not all succeed, and
  the atomic interface reveals neither partial work nor timing/private bytes.
- `lib.rs:679–729`: exact signature-length and digest filters remain strict.
  Accepted layer i completes exactly ell_i(w_i-1)-S_i chain calls.

## Uniform coupling obligations

The subject reconstructs the same ordinary complete raw function by acyclic
addressed restrictions and fresh residual cells; it does not replace one shared
oracle by independent named primitives. Canonical metadata, endpoints and public
roots form a safe surface; hidden starts/interiors, full F and postaccept row
answers do not. The unflagged ghost never routes on an undisclosed coordinate or
private guess flag. Only source observations and queried/honest replies agree
up to first bad; complete unqueried functions need not agree. Permanent suffix
disclosure and install-only-if-fresh memoization preserve the unused-coordinate
property. There is no public adversarial slot during an atomic request or after
an absorbing noncompletion, so an unsigned J coin has not leaked in a failed
partial request before a later public slot.

Strict-target and full128 decoding yield the uniform accepted-witness cover;
no unexposed-row canonicality premise is inserted. The raw 3Q fee accounts for
overlapping inner and H/G risks in one continued world, not separate advice
worlds or a false one-query partition. Full256 U, distinct inner inputs even for
repeated nonces, and the common preview flags retain the N^2 bridge denominator.
The coverage argument uses independent padded coins only after its stop, not
postselection on an actual surviving execution. Counts q and Q+1 are pathwise;
an expected eligible-query count is insufficient.

## What is and is not concluded

The final constants are H=r+sum tails, G=r(a+1)+1+sum(tails+1+h_i), and
C=H+G+d+3=r(a+2)+2sum tails+h+2d+4, including seed zero exactly once.
Baseline H3017/G3217/C6242 agrees with the preserved fixed joint theorem.
The min1 envelope is a manual classical source-RO statement for guarded
ex-ante parameters and an atomic partial interface. Rare completion can make
the theorem unhelpful for availability; no successful retuning follows.
No retuned QROM, fixed-SHA hardness, optimal attack lower bound, AES resource
normalization, new kernel/source-game theorem or completed original goal follows.
The limitation Q<N/6 for this half-success certificate is a limitation of this
particular sufficient upper bound, not an attack or impossibility theorem.
