# Independent code-audit commands and scope

All commands below are private local controls. No original code or paper was changed. No full-parameter signing, full cache generation, timing campaign or remote publication was performed.

| Command | Result | Evidence |
|---|---|---|
| `python -I -B derive_counts.py` | exit 0 | `SOURCE_AND_COUNTS.json`; source hashes and exact symbolic counts |
| `cargo run --release --offline --manifest-path toy-cache-control/Cargo.toml --target-dir toy-cache-control/target` | exit 0 | unmodified release-library import, actual WOTS widths/sums with two height-one layers |
| `python -I -B check_domain_overlap.py` | exit 0 | `DOMAIN_OVERLAP_CONTROL.json`; structural equal-input control only |

Native stdout:

```text
accepted_noncanonical_counter: canonical=643, alternate=2377, different_bytes=true, verify=true
rejected_counter: recomputes_canonical=true
corrupt_authentication_node: signer_returns=true, verify=false
corrupt_unused_top_root: signature_unchanged=true
honest_cache: equals_uncached=true; all_controls=PASS
```

The first native invocation compiled the local crate with cached `sha2=0.10.9` dependencies offline. Its generated Cargo.lock and target artifacts stay beneath this audit folder; they are neither manuscript deliverables nor release artifacts. Tests are finite controls, not cryptographic security reductions.
