# Independent hidden-value derivation

Saved before reading the new `hidden-values` author's derivation. This is a classical information-theoretic event analysis in the joint F/J ideal game, not a complete EUF-CMA result, a QROM result, or a claim about SHA-256.

## 1. Source and scope

The fixed source is `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Relevant anchors: address encoding 69-98; public hashing 122-160; WOTS digest/grinding/chaining 216-276; FORS leaf construction and verification 341-414; fixed child value 486-499; honest signing 601-667; final verification 679-733.

Fix a nonzero public seed S. Private type-5/type-6 outputs are replaced by independent address-indexed 128-bit F values; private message randomizers are an independent J map. Public O returns full independent 256-bit strings, with its first 128 bits used by addressed node functions. No private F/J output is supplied as extra advice. Message-inner queries and addressed queries have different raw languages when S is nonzero; outer message queries have length 52 bytes and cannot be addressed queries. Raw encodings, not API names, define the classes.

## 2. Latent coordinates and permitted advice

For each WOTS chain, write X_0 = F(start address) and X_(p+1) = Trunc O(A_p, X_p), for p = 0,...,w-2. Each A_p is distinct because the source places p in the full address. Its endpoint X_(w-1) is public. For each FORS leaf write X = F(leaf address), Y = Trunc O(A_leaf, X).

One can sample every chain-position value and every FORS secret independently and uniformly, sample the full hash images' unused tails independently, and insert each designated equation into its own addressed random function. Complete each residual function with independent values. This produces the ordinary random-oracle marginal: for any address, conditioning on the designated input and its independently uniform full output inserts one independent ordinary random-function table entry. The dependency order between addresses is acyclic, and the designated input of an address does not inspect that address's residual table.

Allowed public advice consists of WOTS endpoints, FORS leaf images, and the WOTS-PK/Merkle/FORS-root graph built from those public images. It can also contain independent outside-function tables, including type-7 functions. It must NOT include intermediate WOTS chain images: X_(p+1) is itself the next chain's hidden payload. Nor can it include FORS secret payloads or the full residual type-0/FORS-leaf functions. Conditional on permitted advice, the unrevealed WOTS prefixes and FORS secrets start as independent uniforms. A root-only advice view is weaker than this admissible enlarged view.

## 3. Source exposure is predictable and closes suffixes

At each full WOTS address the source signs the same child value: layer 0 signs the fixed FORS public key; higher layers sign the uniquely addressed child-subtree root. The smallest accepted type-7 counter and its digit vector are therefore functions of permitted public graph values and the separate type-7 function. They do not inspect chain prefixes. On a completed honest reference call, reveal the signature positions X_d and, for proof convenience, their entire forward suffixes X_d,...,X_(w-1). Repeated honest visits reveal the same suffix. A FORS call reveals the secret at each selected leaf; its selected labels are determined by the routing stream, not by inspecting those leaf secrets.

The exposure scheduler may adapt to public replies and already revealed values. It must choose the next labels before observing the values it is about to reveal. Revealing a WOTS position always removes the complete forward suffix from the hidden set. Otherwise a known predecessor would compute a supposedly hidden successor deterministically.

## 4. The necessary stopped oracle coupling

The true programmed oracle's posterior is NOT uniformly distributed after arbitrary unsuccessful guesses. Already for a two-element hidden X, conditioning on a first guess not hitting X fixes X to the other value. A proof must not assert conditional 1/2^128 hit probability on the surviving REAL history.

Instead define an input-oblivious comparison experiment. Before a coordinate is exposed, answer public queries in its domain from an independently sampled residual function without inspecting that coordinate. Record a hidden-input event if the supplied payload equals the still-hidden X for that full address, but do not feed that flag to the adversary or scheduler. Once an exposure reveals X and its WOTS suffix, make the corresponding designated replies available. If any such input was queried earlier while hidden, the recorded event has already occurred. On paths without that event, these newly designated entries were never publicly answered, so no previous reply is overwritten. Private honest evaluations use the pre-sampled designated graph; they are not adversarial guesses.

This comparison experiment is a public-oracle hybrid, not by itself an ordinary single public random oracle: a still-hidden designated point returns a residual value to public calls and its graph value to private graph evaluation. Up to the first hidden-input event the hybrid and the actual programmed ordinary RO have identical public transcripts and completed honest outputs. This is enough for the usual identical-until-bad event bound. It must be stated explicitly, rather than silently reprogramming a public function.

In the unflagged comparison experiment, a still-hidden coordinate has never been used to generate public information. Conditioning on the adversary's public history and all revealed other coordinates leaves it uniform. For a query selected from that history, its address either has no eligible hidden coordinate, or identifies exactly one coordinate, and its payload is a single fixed candidate. Consequently its event probability is at most 2^-128. Sum over a deterministic bound M on public and selected final-verifier calls: Pr[hidden-input event] <= min(1, M * 2^-128). Repeated candidates may improve the true union bound but cannot increase it. This calculation uses the unflagged comparison probability; it does not condition on previous non-hits. Adaptive labels are safe under the predictable exposure condition, because unobserved coordinates remain unused and mutually independent in the comparison experiment.

## 5. Prequeries and the final verifier

Sample the fixed seed and latent graph before the adversary's prekey oracle phase. Prekey guesses at the eventual key's eligible addresses are included in the same event list; the adversary need not know the seed. There is no free table reprogramming after seeing those guesses. Genuine raw aliases must be excluded or charged separately. For unconditional uniformly chosen S, add at most 2^-128 for S = zero; combining this with other game hops requires explicit joint-event accounting rather than subtracting repeated seed charges informally.

The event includes any eligible input made by final verification after adaptive submission of m,R,c and signature payloads. For the fixed parameter set, WOTS chain completion takes at most four times (32*15 - 240) plus (16*255 - 2040) = 3000 type-0 calls. FORS leaf hashing adds 17 calls. Thus the final verification adds at most 3017 eligible candidate calls. Early rejection only reduces that count. FORS internal nodes, WOTS-PK compression, Merkle nodes, and FORS-root compression belong to the separate public-graph collision event, not this hidden-payload guessing event. Verification type-7/message-digest calls also are outside this class when raw-language disjointness holds.

With Q_H a deterministic bound on all adversarial full public-O calls, the scoped conclusion is Pr[hidden-input event] <= min(1,(Q_H + 3017)/2^128) for fixed nonzero S. With a separately sampled uniform seed it is <= min(1,(Q_H + 3018)/2^128) if the zero-seed branch is counted once in this standalone analysis. This does not bound the complete forgery event: public-graph collisions, accepted WOTS digest changes, routing coverage, and the actual F/J-to-source bridge remain separate obligations.

## 6. Discriminating controls to run

1. Enumerate the smallest leaf original distribution (uniform X, ordinary binary random function, Y=f(X)) and its independently sampled X,Y plus programmed residual representation, and verify equality of complete joint masses.
2. Show that conditional survival posterior uniformity fails, while the unflagged input-oblivious union argument remains valid.
3. Test exposure after an old query: keep all previous replies fixed, flag the previously hit hidden point, and only install new designated values at fresh points on unflagged paths.
4. A reveal-selected-by-hidden-value scheduler is an explicit invalid-scope control; predictable scheduler selection is essential.
5. A chain successor marked hidden after revealing its predecessor is an explicit invalid-scope control; suffix closure is essential.

Status: INDEPENDENT_DERIVATION_SAVED. The new author's lemma has not yet been read. The coupling above is scoped to an information-theoretic enlarged-advice event experiment with explicit public-query hybrid semantics. It is not an efficient full-signer reduction.
