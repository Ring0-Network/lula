"""Promote only after both source-first complete-composition readers accept."""
from pathlib import Path
import hashlib
X=Path(__file__).resolve().parent
draft=X/'QUANTUM-COMPOSITION-DRAFT.md'
assert hashlib.sha256(draft.read_bytes()).hexdigest()=='71d3f23a3d161c7ade049dcf4f5d2a0467fe7a4a6a0bf97a899eb63bff708b89'
coverage=X/'QUANTUM-COVERAGE-THEOREM.md'
assert hashlib.sha256(coverage.read_bytes()).hexdigest()=='24a031417b42ba03d266c638a4c3f94dae8887ffd8cf13f584b21387e6d01217'
numeric=(X/'quantum-composition-numeric/CONDITIONAL-GATE-CLOSED.md').read_text(encoding='utf8')
assert 'ACCEPTED_MANUAL_FINITE_QROM_COMPOSITION_WITHIN_DECLARED_MODEL' in numeric
reader=X/'quantum-composition-second-reader/SECOND_READER.md'
assert reader.exists(), 'Do not promote without separate complete-union reader'
review=reader.read_text(encoding='utf8')
assert 'ACCEPTED' in review and '71d3f23a3d161c7ade049dcf4f5d2a0467fe7a4a6a0bf97a899eb63bff708b89' in review
assert '24a031417b42ba03d266c638a4c3f94dae8887ffd8cf13f584b21387e6d01217' in review
s=draft.read_text(encoding='utf8')
s=s.replace('# Complete finite-QROM source-game composition — review candidate','# Reviewed finite-QROM advantage theorem for the LULA I source game')
start=s.index('**OPEN — promotion gate.**');end=s.index('\n\n## 1.',start)
s=s[:start]+'''**PROVED — manual finite-query source-model theorem, independently reviewed twice.** The immutable composition draft71d3f23a… and corrected coverage theorem24a03141… are preserved. `quantum-composition-numeric/ROOT_REVIEW.md` together with `CONDITIONAL-GATE-CLOSED.md`, and `quantum-composition-second-reader/SECOND_READER.md`, accept the complete common-HJ union, private hop, budgets, single seed and honest-cache transfer. Their source-first derivations precede the root composition read. The theorem is an unconditioned winning-probability upper bound in the declared partial atomic finite-query QROM experiment. No security category, efficient generic primitive reduction or fixed-SHA certificate follows.'''+s[end:]
s=s.replace(', subject to review.',' — reviewed.').replace(', subject to common-game review.',' — reviewed.')
s=s.replace('**PROVED — component formulas already reviewed or explicitly gated.**','**PROVED — independently reviewed component formulas.**')
s=s.replace('The c formula is licensed only after the pending source/AR gate passes.','The c formula is licensed by QUANTUM-COVERAGE-THEOREM.md and its source/AR/search review receipts.')
s=s.replace('The proposed unconditional theorem is','The accepted unconditional theorem is')
s=s.replace('the proposed epsilon_QROM transfers unchanged','the accepted epsilon_QROM transfers unchanged')
s=s.replace('the candidate sum is vacuous','the accepted sufficient sum is vacuous')
s=s.replace('## 6. What the theorem would and would not resolve','## 6. Scope and remaining targets')
start=s.index('**OPEN — independent acceptance.**')
s=s[:start]+'''**PROVED — independent review scope.** Both complete-composition readers accept the pointwise partition for quantum-produced classical transcripts, projection of each separate event to ordinary HJ, private-hop final handler, initiated calls, row reads, single seed-zero charge and honest-cache view equality. Component controls and all sixteen numerical rows are separately reproducible. This is a manually reviewed mathematical theorem; component Lean/EasyCrypt checks are not a mechanical verification of the full Rust implementation or quantum proof.

**OPEN — original level/category goal.** The theorem does not certify a classical/quantum signing capacity, category1, efficient generic PRF/PRE/SPR/TCR embeddings, actual SHA-256, physical leakage or broad corrupt-cache/total-failure APIs. The sufficient Q=2^64 bound is vacuous. A tighter event-specific private hop is separately proposed in QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md; it does not alter this accepted conservative theorem. The complete-security goal remains active and its printable level/category assertion remains “not established.”
'''
(X/'QUANTUM-RO-THEOREM.md').write_text(s,encoding='utf8')
print(hashlib.sha256((X/'QUANTUM-RO-THEOREM.md').read_bytes()).hexdigest())
