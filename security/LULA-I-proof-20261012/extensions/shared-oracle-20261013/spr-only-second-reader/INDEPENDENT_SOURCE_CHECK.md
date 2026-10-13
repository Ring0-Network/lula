# Independent source-first SPR-only separation check

Saved before inspecting the supplied Lean separation and its check receipt. The pinned release source has SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`; actual WOTS+C code at225–275 checks a fixed digit sum, hashes through position-specific addresses, emits chain nodes at those positions, and completes them to public endpoints. Its lower-layer parameter literal has32 base16 chains, no omitted/forced-zero digits, and required sum240.

## Generic countermodel

Replace only the abstract length-preserving chain-step family by `F_A(x)=x` for every tweak/address A, on128-bit nodes. For every given x, equality `F_A(x')=F_A(x)` implies x'=x, so no distinct second preimage exists and every second-preimage advantage is exactly0. Nevertheless, F_A is publicly invertible: given an output y, its preimage is y. Chain start Xi, every position and endpoint are all the same128-bit value.

For32 chains and width16 choose

```
e  = [15]*16 ++ [0]*16,
e' = [0]*16 ++ [15]*16.
```

Both are within0..15 and sum240, yet are distinct and incomparable. Their full128-bit digit encodings are respectively `ff` repeated8bytes then `00` repeated8bytes, and the reverse. Thus they are distinct accepted full-width WOTS+C digit vectors, not a digest collision.

One honest signature on e contains every start Xi because the identity chains do not change values. The same node vector verifies against the same endpoint vector for e'. Its compression/public key remains identical even if PK compression itself is an ordinary secure hash. For a fresh message with accepted digest e', the attacker can emit those exposed nodes and the corresponding accepted counter without recovering any other secret. The calculation is conditional on such accepted message/digest evidence; the finite exact control can instantiate two distinct messages with these injectively encoded vectors.

Hence second-preimage resistance of the chain family alone cannot justify rejecting an altered accepted digest vector. The missing direction is a preimage/exposed-chain origin property: when e'_i<e_i, a preimage is needed, and identity supplies it. The fixed-sum antichain only rules out changing all coordinates solely by increasing positions; it does not turn an injective function into a one-way function.

## Boundaries

This is a generic assumption separation, not a forgery of LULA I under SHA-256, not a modified Rust benchmark, and not a complete-hypertree attack. It does not assert that an arbitrary variable-length compression function can literally be the identity with128-bit output. The identity is the abstract fixed-width chain primitive only. Digest and PK compression assumptions can be separate; no digest collision is used in the two-vector example. A complete security premise may include preimage resistance, random-oracle assumptions or other source-specific properties that exclude this countermodel.

The four supplied Lean algebraic declarations and their checker receipt will be reviewed separately. A Lean proof of identity injectivity is not by itself a machine-checked cryptographic security definition or WOTS forgery theorem.
