# Resource and supporting-control clarification

The first derivation (6c44c1b3cce9cc5438f333031258b1c392069a171b1c6358e6354af6d9aab1af) is preserved. This clarification does not change its exact adapter identities or the assumed hardness interface.

## Query-cost convention

The first derivation explicitly excludes execution of the private challenger from the simulator runtime and gives its query counts separately. If total execution work is requested, REAL B_K additionally evaluates at most D private 102-byte f frames; add D*C_h^cl(102). REAL B_P evaluates at most q g frames of lengths 32+|M|; add their complete public-h evaluation costs (or q*C_h^cl(b) under the static bound). These are costs inside the ordinary PRF challenger, not extra simulator calls to an external Raw oracle. IDEAL challengers instead incur independent 16-byte sampling and memoization costs on their first labels. A coherent private-query challenger is unnecessary for these adapters. Classical oracle answer decoding/copy costs are already part of the simulator bookkeeping envelope.

The challenge public parameter S is sampled independently of its hidden key and is supplied to B; B withholds it from source A until successful setup. If the ordinary PRF advantage is instead defined for each fixed S, the exact pointwise identities apply there and one then averages the signed output-probability gaps. An average of absolute fixed-S gaps is an upper bound on the absolute averaged gap, not necessarily an equality. The public-parameter challenge in the first derivation defines the averaged experiment directly and therefore retains the displayed equality.

## Additional control: actual noncompletion

The first `control.py` and its result are preserved. Its toy hash's low bit always changes with the last counter bit, so its two-attempt setup search completes in every enumerated original world. Consequently its noncompletion metadata described the implemented absorbing branch, rather than an observed bottom outcome. `control-successor.py` adds eight worlds with another fixed public algorithm h(word)=0. In each world setup exhausts, the source and both ordinary adapters return the same absorbing nonwinning view, no pk is released, and B_P makes zero message-randomizer queries. Both algorithms are deterministic public code; no independently sampled side oracle is introduced.

The successor retains all original full-view, alias, prefix-only/private versus full/public, restoration, and public reversible-XOR controls. These remain finite interface discriminators, not a full-source security proof, SHA-256 pseudorandomness evidence, or a kernel-checked quantum theorem. Original first subject/control pins and protected files are unchanged.
