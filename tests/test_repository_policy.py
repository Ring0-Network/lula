"""Negative controls for accidental research-note or credential publication."""
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from repository_policy import allowed

class PublicationBoundary(unittest.TestCase):
 def test_proof_and_test_paths_are_admitted(self):
  for name in ('README.md','proofs/lean/LulaProofs/Merkle.lean','proofs/lean/lean-toolchain',
    'proofs/easycrypt/SeedGuess.ec','models/fors.py','tests/fixtures/public_vectors.json',
    '.github/workflows/checks.yml'):
   with self.subTest(name):self.assertTrue(allowed(name))

 def test_work_files_cannot_be_added_by_changing_directories(self):
  for name in ('HYPOTHESIS.md','models/HYPOTHESIS.md','proofs/PROOF.md','proofs/handoff.json',
    'tests/editorial/receipt.json','proofs/drafts/unfinished.lean','models/.env',
    'proofs/lean/.lake/packages/mathlib/lakefile.toml','../model.py','publications/LULA-I.pdf',
    'snapshot/SOURCE-COPY-MANIFEST.json','scripts/first-derivation.json',
    'models/notes.json','proofs/finished-notes.json','tests/internal-notes.json'):
   with self.subTest(name):self.assertFalse(allowed(name))

if __name__=='__main__':unittest.main()
