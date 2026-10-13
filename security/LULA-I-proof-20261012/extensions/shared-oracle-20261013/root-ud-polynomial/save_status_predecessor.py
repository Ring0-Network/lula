from pathlib import Path
import hashlib
X=Path(__file__).resolve().parent.parent
text=(X/'QUANTUM-UD-POLYNOMIAL-RO.md').read_text(encoding='utf8')
text=text.replace('**PROVED — manual finite-random-oracle lemma.** Three separately saved derivations obtain the bound below. Its acceptance is recorded in independently pinned final-subject receipts.', '**PROVED — manual finite-random-oracle lemma; final subject review pending.** Three separately saved derivations obtain the bound below.')
text=text.replace('**PROVED — manual source-interface application.**','**PROVED — manual source-interface application, final subject review pending.**')
assert hashlib.sha256(text.encode('utf8')).hexdigest()=='55971b61f6fd7cba54fe589c100d61351e67f7373182515593cf2c63d83bb7d5'
p=X/'root-docs-before-ud-status/QUANTUM-UD-POLYNOMIAL-RO.md'
assert not p.exists()
p.parent.mkdir(exist_ok=True)
p.write_bytes(text.encode('utf8'))
print('EXACT_PRE_STATUS_SUBJECT_PRESERVED')
