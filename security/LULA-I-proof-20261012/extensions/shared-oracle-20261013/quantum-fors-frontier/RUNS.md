# Commands and provenance

1. Re-read source/game and save `INDEPENDENT_DERIVATION.md`; no future peer quantum-FORS report read.
2. Web primary search found Grilo-Hövelmanns-Hülsing-Majenz, *Tight adaptive reprogramming in the QROM*, arXiv2010.15103v2. Direct primary PDF inspection verified Figure2, Theorem1 Eq(2), and Theorem6 with post-instruction query access. IACR PDF open failed; no theorem was inferred from that failure.
3. Download the public author PDF to `primary-arxiv-2010.15103.pdf` in this owned directory. SHA-256 checked as `9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d`.
4. `pdftotext -f 6 -l 7 -layout` produced `primary-ar-theorem-excerpt.txt`. A path mistake initially placed that newly generated excerpt in the parent directory; it was immediately moved into this owned directory using native Move-Item. The parent path was checked absent and root was informed. No source/peer file was changed.
5. Save the primary-backed first-call candidate in `DERIVATION.md`, preserving the earlier source-first derivation.
6. `python -I -B control.py` in this directory exited0; exact finite controls and candidate arithmetic saved to `CHECKS.json`.
7. Source hash and final owned manifest checked. No signing/keygen/cache execution, performance experiment, global installation, manuscript edit, frozen-packet change, private upload or peer-script write occurred.

This is a candidate first-call reduction awaiting independent review. Full quantum FORS/QROM security remains OPEN.
