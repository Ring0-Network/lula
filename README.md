# LULA

Current paper, reproducibility material, and security-proof research for LULA I.

The mechanism paper is published on Zenodo: **[LULA I — DOI 10.5281/zenodo.23353281](https://doi.org/10.5281/zenodo.23353281)**. The published main PDF has 22 pages. Older retained status records may describe the earlier 21-page draft or say that publication was pending; they are historical evidence, not the current publication status.

## Read the paper

- [Published main PDF](publications/LULA-I/LULA-I.pdf)
- [Editable TeX](publications/LULA-I/LULA-I.tex) and [editable source archive](publications/LULA-I/LULA-I-source.zip)
- [Curated reproducibility bundle](publications/LULA-I/release/README.md), including code, retained data, notices, and reproduction instructions
- [Final publication reviews](publications/LULA-I/editorial/zenodo-release-20261013/technical/POSTEDIT-REVIEW.md)

The main PDF contains the author's requested contact. The reproducibility bundle's repository-paper copy intentionally omits it. The paper proves honest-cache transparency and a conditional rollback-security transfer. It does not establish the full reference signer's 128-bit security, category 1, or a certified signing capacity.

The accompanying English [research note on Lugel](https://lugel.org/blog/lula) explains cache restoration, the measured costs and the conditional security scope.

## Read the security research

The retained proof archive is under [`security/LULA-I-proof-20261012/`](security/LULA-I-proof-20261012/). Start with the current shared-oracle extension:

- [Proof index](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/PROOF.md), [handoff](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/HANDOFF.md), and [open obligations](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/OPEN.md)
- [Current validation record](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/VALIDATION.json)
- [Guarded parameter-uniform classical theorem](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/PARAMETER-UNIFORM-CLASSICAL-THEOREM.md) and [406-pin promotion record](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/UNIFORM-CLASSICAL-PROMOTION.json)
- [Independent exact-binomial evaluation and review](security/LULA-I-proof-20261012/extensions/shared-oracle-20261013/pre-start-second/uniform-classical-numerics-20261014/FINAL-SUBJECT-REVIEW.md)

The research contains reviewed manual classical RO and finite-QROM results, independently checked numerical bounds, and explicit remaining obligations. The new uniform theorem keeps its guarded source, atomic partial-call, shared raw-oracle and honest-cache assumptions; it adds no checked whole-source/game declaration. An illustrative half-success query certificate is not an AES-normalized security category, successful minimal repair, or proof that the original complete-security goal is finished. **That goal remains incomplete.** Historical bounds, rows and review receipts are retained rather than rewritten.

## Snapshot integrity and reproduction scope

The files were copied byte-for-byte from the authorized research archive. [SOURCE-COPY-MANIFEST.json](snapshot/SOURCE-COPY-MANIFEST.json) maps original source paths and hashes to repository paths and copied hashes. [EXCLUSIONS.json](snapshot/EXCLUSIONS.json) records omitted build/dependency/cache/key artifacts, duplicate generated material and third-party reference documents, retaining their hashes and citation URLs. The existing license and notice files keep their original scope; no blanket relicensing of the proof archive or third-party references is implied.

Run a lightweight checkout integrity check with installed Python 3.13:

```sh
python -I -B scripts/verify_snapshot.py
```

The check verifies this snapshot's recorded bytes. It is not a new benchmark, security proof, or claim that every historical audit can be rerun from a fresh checkout. Some retained proof/calculation scripts and old receipts refer to the authoritative Windows archive or external proof tools. Those paths and records are preserved as provenance. The curated bundle documents its own portable reproduction scope and external dependencies separately.

This repository remains private. Its provenance manifests can contain original local paths; credentials, private keys, seed-bearing cache fixtures, compiled dependency trees, and unlicensed full reference PDFs/texts are excluded.
