# Independent review of the root one-query successor

**ACCEPTED MANUAL QUERY-IDENTITY SUCCESSOR.** Subject root-keyed-review/ONE-QUERY-COMPLETION.md SHA2567def78f7f5e771e397373f7ad81c7977674669d2064a3b2ce1a31e13d31bf1f0. Root explicitly did not claim blind derivation. Both independent conservative first proofs and my reciprocal review were saved before this root successor was read. They stay unchanged: their2-query constructions remain valid sufficient constructions, not lower bounds.

## Algebra checked directly

For each fixed input x and Fourier response z, let r0,r1 be the two known fullword completion branches and Delta=r0 xor r1. Preparing the scratch in H|d> with d=<z,Delta> gives an X eigenstate of eigenvalue(-1)^d. One standard Boolean XOR query applies exactly phase(-1)^(f(x)d) and leaves the eigenstate unchanged. H maps it back to|d>; uncomputing d restores|0>, even when x,z are superposed. Multiplying the known phase(-1)^<z,r0> gives

(-1)^(<z,r0>+f(x)<z,Delta>)=(-1)^<z,r0 xor f(x)Delta>.

Walsh conjugation is exactly translation of the response by r0 xor f(x)Delta. The result on every clean-input basis vector is|x,y xor R_f(x),0>, with no extra x-dependent phase or residual scratch. Linearity extends this exact isometry to arbitrary response/input superpositions, arbitrary entangled untouched reference systems, and mixed states. It is not merely equality of the measured output distribution.

For an arbitrary raw byte word u, retain u while computing the known payload pi(u) reversibly. On outside/malformed words set both branches to the SAME outside fullword. Then Delta=0 and scratch is|+>; the single unconditional Boolean query is exactly inactive there. Region superpositions require no controlled-f oracle, support test, measurement or history inspection. Uncompute pi after the call; u was preserved. Aliased full raw inputs continue to address the same fixed output.

The restricted-game completion tables and outside side data are independent of Bernoulli f. The two branches can have huge public/private descriptions, but they are known interquery operations after conditioning only initial independent side data. Granting these descriptions does not reveal f. The full256 product law, finite BE32 canonical/bottom and same-C correlations are those already independently reviewed; this identity does not alter them or extend the game to unrestricted pretarget Raw access.

## Primary query bound and source variant

TheoremE.3 of the pinned SPHINCS+C primary PDF gives8 lambda(k+1)^2. The successor uses k=M, lambda=2^-128, hence min(1,8(M+1)^2/2^128). This is a justified improvement over the older sufficient k=2M construction.

Preserved final-digest program: M<=Q+1, bound8(Q+2)^2/N. NEW pre-digest stopped extractor: M<=Q, bound8(Q+1)^2/N. The latter does not first recognize full Win; every source winning final changed-base branch is an eligible marked output, while other candidate outputs do not invalidate the one-sided search-success inclusion. Earlier source honest calls avoid the changed domain at S!=0 by the previously checked literal106-byte/type/inner/outer exclusions; runtime/gates remain charged. Target-success tau may be retained without normalization; nonzero production-seed charge belongs once to the parent convention.

## Independent execution and boundary

Pinned script89128e32d5a3eeb7da92c4fe22fbcbc5de725e5c235f0625480832f9981cd9c1 rerun with ONLY output destination redirected in memory into my own one-query-rerun folder: exit0. Its results are byte-identical to the root control. Exact Q(sqrt(2)) arithmetic verifies1024 worlds,8192 clean-basis inputs and2048 Delta0 cases. Omitting the known r0 phase or scratch uncomputation fails the included negative controls. Source/root input files are not modified. The immutable subject's Section4 execution label predates these recorded runs; this receipt supplies actual execution evidence without rewriting that historical label.

Accepted only as a manual exact oracle identity plus the previously scoped restricted-RO query consequence. It does not establish efficient completion/outside tables, actual SHA hardness, concrete PRF security, arbitrary HK collection conjectures, new source-game/kernel declarations, signing capacity/category or full original-goal closure. No manuscript, source or existing scalar result changed.
