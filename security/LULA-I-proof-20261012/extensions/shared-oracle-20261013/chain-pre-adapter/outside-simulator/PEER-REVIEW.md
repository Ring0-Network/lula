# Independent second reading of the finite outside simulator

Verdict: ACCEPT_SCOPED_MANUAL_B_ONLY_REPLACEMENT. This additional review does not replace any already promoted subject or receipt. My own first derivation (939f4c5fc75e4f8be5dbbb56d45dd8a70f9d6c839e03625776ca271691df7c9e) was saved before I opened the peer derivation or the third reader's derivation.

## Exact subjects

The peer subjects are `chain-pre-independent/outside-simulator/INDEPENDENT-DERIVATION.md` (5555569b844c8a30ee5d58bdca9121e84a45fe5dd62474d0f0fb64df5c009680), `CLARIFICATION.md` (4e0ae20f94a1af80b5a86cd14bab4b8873589a62f4c15eb519757bf3e64f01c7), and `ROUTES-CLARIFICATION.md` (383dc9c6b0de9417fe44ca6c66dc69874143aba970b98511df745e256461ede4). I also read the independently saved `outside-field-check/first-independent-derivation.md` (c6b1b31b95100e10d484e06ba839d2b36d2e1393d18add5e7710d6bf52364a69) and its receipt `SECOND-READER.json` (331f0e648cdf7bc5b3496f4ab4e151071f2bd64cc488b0d6e26bdd2dab820dbf).

## Algebra and compiler

The quadratic tower is deterministic. At each level a trace-one element gives an irreducible Artin--Schreier quadratic. For the peer's basis search, nonzero trace implies that a basis vector with trace one exists; searching all basis vectors is polynomial. Its final generator is not in the degree-half subfield. Since the total dimension is a power of two, its Frobenius orbit has the full final dimension. The conjugate product therefore produces a binary irreducible polynomial of that dimension. The stated quartic deterministic preprocessing bound is conservative and avoids an uncharged irreducibility search.

The direct tower of my first derivation and the third reader has the simpler highest-coordinate trace-one element. Multiplication uses four lower-field products, giving quadratic Boolean gate count. The two implementations need not use the same coordinates or encoding. Both have an injective fixed finite domain embedding, balanced 256-bit output projection, and an ordinary Vandermonde argument for all distinct tuples of at most the available independence degree.

Validity of the physical input register must be checked reversibly. Invalid encodings use the same fixed extension in both compared worlds; they cannot be treated as extra random-function entries. Coefficients are sampled once and can be read only inside Eval. Every honest and adversarial Eval uses that same key. A clean Horner circuit must preserve inputs and scratch and cannot overwrite the accumulator by multiplication at zero.

Uniform generation of a circuit is charged separately from executing it. A bound on emitted gate records is not a bound on a bit-serialized list of indexed wire labels. My successor clarification records the additional logarithmic wire-index factor if bit serialization is the chosen metric. This resource distinction does not change the probability identity.

## Probability preservation and chronology

The sufficient route replaces only the executable reduction's outside random function. Its target success is the output of a complete T-query quantum algorithm, including all honest setup, signing, preparation, and final checks. Zhandry's Fact 2 applies to this compiled algorithm; it does not give the full random-function law outside the bounded interaction. The all-honest-call count is essential. My exact negative control has three honest reads and one adversarial read: sizing independence only for the latter changes parity success from one half to one.

For type 7, the selected child C is computed before registration but can depend on the outside function. Fix the independent full Row function as auxiliary randomness; compute C and register its first accepted row later. Do not condition on the resulting Y or c0 before applying the bounded-query theorem. My additional exact adaptive control compares the complete (C,c0,Y,success) law, retaining the full output word and a bottom branch.

The inherited B-only caps are T_PRE = Q + H_setup + q H_mode + 3224 + 254 and T_ROW = Q + H_setup + q H_mode + 3224 + 17392. Row preprocessing of at most 2^32 selected challenge evaluations is separate. I reviewed the source-call accounting against the inherited adapters; this report does not independently rederive the complete Rust call graph. The optional full SOURCE comparator needs its extra classifier costs and is unnecessary for the accepted B-only probability replacement.

## Limits

This is a source-relative manual proof with exact finite supporting controls, not a new proof-assistant theorem or a practical quantum runtime claim. It preserves the already established reduction probability under the inherited bounds. It does not identify conventional fixed-SHA PRE, TCR, or PRF assumptions, transport external-oracle bounds to SHA-256, or certify any security category. All protected source, paper, numerical, and earlier receipt files are unchanged by this review.
