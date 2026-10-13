# Validation of the LULA I cache and signatures (this campaign)

All items below are [measured] from files in `raw/` and `results/independent-check.txt`. Scope: one key (the campaign fixture
key), message 32 B for the byte comparison, replicate 0 of each run.

1. **Independent verifier.** `scripts/independent_check.py` replays every `raw/lula1-*.vec.txt` through the publication's
   independent Python verifier `verify_ra.py` (written from `SPEC.md`, not from the Rust code). 14 of 14 vectors: signature
   verifies (5,720 B), one flipped message bit rejects, one flipped signature byte rejects. The vectors cover the prepared
   cache (32 B, 1 KiB, 64 KiB), 10 fresh processes loading the persisted cache, and the total-cache-loss run.
2. **Byte equality across cache states.** For key and message (32 B, replicate 0), the signature from the in-memory prepared
   cache, from 10 separate fresh processes with the persisted cache, and from the total cache loss (seed only, rebuilt on the
   fly) has the same SHA-256 prefix `af011dbad3c680d9`: 12 of 12 identical.
3. **What this does and does not show.** It shows that the harness serializer round-trips the cache without changing the
   output of the signer and that cold reconstruction gives the same bytes. It does not prove the rollback theorem, whose
   reference bound is a premise (see `security-matrix.md`). The historical public key differs from this campaign's key, so
   nothing here compares with the historical vector by key.
4. **Driver negative tests.** `m3_ra` asserts, at replicate 0 of every run: flipped signature bytes at four positions, a
   truncated signature, an extended signature, a flipped public-key byte, and a flipped message byte are all rejected.
