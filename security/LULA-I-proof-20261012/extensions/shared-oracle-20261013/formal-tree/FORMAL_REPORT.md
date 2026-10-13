# Addressed Merkle-path extraction

**PROVED — scope:** this extension strengthens a finite-list divergence observation into a hash-input witness for two addressed Merkle evaluations. It provides neither a security certificate nor a numerical SPR/TCR reduction. It modifies no manuscript, implementation, existing proof packet or global tool configuration.

## Exact model and declarations

**PROVED — representation:** `Node n` is a list of bytes together with a checked proof that its length is exactly `n`. `Step Addr n` contains an address, the Boolean indicating whether the current node is the right child, and one sibling node. `schedule` retains addresses and directions while discarding sibling values. `root H header` evaluates the bottom-up path; `trace H header` records every address and complete raw input to `H` encountered by that evaluation.

**PROVED — framing:** `frame header address left right` is exactly `header address ++ (left.bytes ++ right.bytes)`. The theorem `LulaTree.frame_children_injective` proves, rather than assumes, that equal framed inputs at the same address imply equality of both children. It follows from `LulaTree.cancel_prefix` and `LulaTree.split_fixed_left`, which proves unique splitting when the left parts have equal length. No collision-resistance premise is used. Injectivity of the address-to-header map is not assumed or needed for this same-address lemma.

**PROVED — principal declaration:** `LulaTree.same_root_agreement_or_witness` states, for any total deterministic hash `H : List UInt8 → Node n`, any fixed address-header map, any two paths and leaves:

```
schedule path1 = schedule path2
root H header leaf1 path1 = root H header leaf2 path2
  implies
    (leaf1 = leaf2 and path1 = path2)
    or there exist address, x, y such that
      (address,x) is in trace H header leaf1 path1,
      (address,y) is in trace H header leaf2 path2,
      x != y, and H(x) = H(y).
```

**PROVED — consequence:** `LulaTree.changed_leaf_or_path_yields_witness` adds only `leaf1 ≠ leaf2 ∨ path1 ≠ path2` to the two premises above and concludes the explicit witness alternative. The desired collision is a conclusion, not a premise. Full leaf/path agreement in the principal theorem also gives agreement of all framed inputs by substitution. The witness is restricted to inputs actually encountered in both evaluations at a common address; it is not an arbitrary existential collision elsewhere in the hash domain.

**PROVED — proof mechanism:** induct on the first path and use schedule equality to obtain equal head addresses/directions and another schedule equality for the tails. Apply the induction hypothesis to the two computed parent nodes. A witness from the tail remains a witness in both extended traces. If the tail nodes and paths agree, either the two first encoded inputs differ while their parent hash values agree, immediately giving a witness, or the first encoded inputs agree. In the latter case, the proved framing lemma forces equality of the two initial children, hence equality of the leaves, siblings and whole paths. Empty paths reduce root equality directly to leaf equality.

**PROVED — exact limits of the statement:** the recorded witness uses trace membership, not an exposed same-position index, a first-divergence/minimality claim, an executable extracted reduction adversary, or a quantified runtime. The induction compares corresponding levels, but those stronger output-interface properties are not separately certified by this declaration. Paths with different address/direction schedules are outside its premises. The model handles arbitrary length `n`, including the degenerate zero-length case, and assumes no random oracle, independent domains, uniformity, collision resistance, or secret-key property.

**PROVED (manual premise check):** the common-direction premise cannot simply be dropped. At a one-level route, a current node `A` on the left with sibling `B` and a current node `B` on the right with sibling `A` produce the same ordered framed pair `(A,B)`. For distinct nodes, the leaves and directions differ, but the sole raw inputs and roots agree under any hash. No different-input witness occurs in these one-element traces. This algebraic control explains the required common route; it is not an additional machine-checked declaration.

## Binding to LULA I

**COMPUTED — source identity:** `SOURCE_BINDING.json` binds the currently retained release library, SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`, with exact anchors for `Adrs`, `Ctx::th`/`Ctx::h`, `Subtree::build` and `root_from_path`. The existing proof packet's original abstract list lemma is unchanged. The exact goal attachment was reread before this extension.

**PROVED (manual source correspondence, not machine-checked translation):** for the selected construction, each node is 16 bytes. The raw node-hash input is

```
pk_seed[16] || zero[48] || ADRS[22] || left[16] || right[16]
```

The header is therefore 86 bytes and the complete pre-padding input is 118 bytes. `Ctx::h` concatenates the two nodes in that order; `Ctx::th` hashes this framing with normal SHA-256 padding and returns 16 bytes. The witness is for the **truncated 128-bit output function**. It does not assert a collision in the full 256-bit SHA-256 output.

**PROVED (manual address binding):** the 22-byte address is layer[1], tree[8], type[1], keypair[4], chain-or-height[4], hash-or-index[4], with multi-byte fields big endian. In `root_from_path`, round `lv` uses `base.w2(lv+1).w3(idx>>1)`, places the current node on the right precisely when `idx & 1 == 1`, then shifts `idx` right. For a fixed base, route and path length, two evaluations have the same schedule regardless of sibling contents. Fixed parameter heights fit the code's integer fields; the Lean theorem does not separately verify all casts/range conditions or global address-domain disjointness.

**OPEN — model/code gap:** Lean checks the stated byte-list model and its framing theorem, not SHA-256 implementation correctness, Rust arrays, parser validation, code extraction, or a Rust-to-Lean refinement theorem. The source correspondence above is a read-only manual argument. No private seed or cryptographic library source was uploaded: AXLE received only the small abstract Lean file.

## Efficient security reduction remains open

**PROVED (structural consequence):** if one path is the honest mathematical key graph at the forgery's chosen route, then equal public roots and a different leaf or sibling list yield a same-address equal-output/different-input witness. The honest path need not have appeared in an earlier signing transcript. A witness can therefore be structurally identified relative to an unqueried honest graph path; comparing only previously observed signature paths would miss that case.

**OPEN — smallest missing embedding lemma:** construct a simulator that supplies or lazily commits the relevant honest key graph while embedding the SPR/TCR challenge under the exact single shared-SHA input encoding, including adaptively selected routes, unknown challenge preimages, distinct-tweak conditions and selected public seed. Show how the witness produced from these paths solves the chosen challenge with explicit success, query and runtime loss. Merely possessing an existential collision after evaluating both supplied paths does not construct that simulator.

**OPEN — no node-count shortcut:** multiplying a generic hash advantage by the total number of conceptual Merkle nodes is not justified by this theorem. The target selection/programming cost and oracle-query budget remain unproved. The theorem likewise supplies no FORS coverage bound, chain inversion reduction, WOTS compression binding, cache-exposure simulation, complete EUF-CMA sum, or QROM statement.

## Verification receipts

**COMPUTED — local environment:** the existing WSL Ubuntu-24.04 toolchain was checked live: Lean 4.28.0, commit `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`, binary SHA-256 `3e0d0d3d801675359f2d4cf9815bfdb417b20b92fdd9d48b3b14c95bbae28bbf`; Mathlib commit `8f9d9cff6bd728b17a24e163c9402775d9e6a365`, `lake-manifest.json` SHA-256 `a89b59a9c917d113c32b931cc82a6b919d50be80ec1a701612f571bcd34f245a`. No installation or global reconfiguration was performed.

**PROVED / COMPUTED — local check:** run `python check.py` from this directory. It invokes the pinned `lake env lean` command recorded in `check.json`. The final source check returned exit 0 with no errors or warnings. All five declarations were audited with `#print axioms`; dependencies are subsets of `{propext, Classical.choice, Quot.sound}` and include no `sorryAx`. Earlier failed drafting checks are retained in `attempts/` and are not completion evidence.

**PROVED / COMPUTED — independent check:** run `python check_axle.py` when authorized to send the same abstract source. The installed AXLE SDK was used, not a presumed historical MCP service. `axle.json` records successful checking and successful statement comparison in environment `lean-4.28.0`, with `ignore_imports=False`. `STATEMENTS.json` preserves all five exact theorem signatures. The comparator transiently uses placeholder proofs only in its statement template; the accepted Lean artifact has no placeholder, admission, `native_decide`, or custom axiom. Source and receipt hashes are recorded separately; the provider may append a trailing newline to its returned content.

**PROVED — final verdict:** addressed Merkle-path **structural collision extraction is checked in the explicit fixed-length framing model**. Efficient cryptographic challenge embedding and the complete-signature security bound remain **OPEN**.
