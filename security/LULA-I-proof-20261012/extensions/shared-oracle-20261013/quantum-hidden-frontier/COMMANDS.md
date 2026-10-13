# Execution/source receipts

Write scope: `quantum-hidden-frontier` only.

1. Read actual release `src/lib.rs` chain/FORS slices with PowerShell `Get-Content -Encoding UTF8`; SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
2. Browse primary AHU author page and Jaeger arXiv HTML. Original AHU ePrint2018/904 and official CRYPTO2019 PDF requests returned403; no successful AHU PDF read is claimed. Those failed downloads created no local PDF.
3. Download primary `https://arxiv.org/pdf/2511.16009` with native PowerShell `Invoke-WebRequest` into this lane. SHA-256 `95609e630baf7fd7572591e5cdf2e4693d768dab51c8d2a095b9d120922d8965`. pypdf confirms24pages and directly extracts the fixed-permutation/AHU-restatement results on physicalpages8/9. An ASCII search for the HTML's numbering found no matches; direct page reading established the version distinction recorded separately. The extracted `.txt` is local reference material.
4. Save and announce `INDEPENDENT_DERIVATION.md` before reading any future hidden-quantum peer proof.
5. Run `python -I -B control.py`; exit0. Output retained in `CHECKS.json`.
6. After parent authorization, read root `DYNAMIC-QUANTUM-HIDDEN-DRAFT.md`, SHA-256 `1b139a3cdd93621c4ebc05f98145807f1bbd23a19d7892440df9d42b3ed0560d`. Save the own-lane second-reader review.
7. Run `python -I -B suffix_quantum_control.py`; exit0. Exact outputs retained in `SUFFIX_QUANTUM_CHECKS.json`.
8. Preserve the reviewed root draft as an own-lane review cut, if its identity still matches. Recheck source/PDF identities and create/verify a local SHA-256 manifest excluding itself.

No global installation, dependency change, private upload, proof-assistant run, timing campaign, cache construction, source edit or manuscript edit occurred. Exact finite controls do not constitute a general quantum-source verification.
