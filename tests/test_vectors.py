"""Public known answers, serialization rejection and restoration equality.

These are finite validation cases, not an unforgeability or rollback reduction.
"""
from collections import defaultdict
from pathlib import Path
import json
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from verifiers.lula import verify

class PublicVectors(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.v=json.loads((ROOT/'tests/fixtures/public_vectors.json').read_text(encoding='utf8'))
  cls.spec=cls.v['parameter_spec']
  cls.cases=[]
  for c in cls.v['cases']:
   key=cls.v['public_keys'][c['key']]
   cls.cases.append((c,bytes.fromhex(key['pk_seed_hex']),bytes.fromhex(key['pk_root_hex']),
    bytes.fromhex(cls.v['messages_hex'][c['message']]),bytes.fromhex(cls.v['signatures_hex'][c['signature']])))

 def test_only_public_fixture_fields(self):
  self.assertEqual(set(self.v),{'schema_version','parameter_spec','public_keys','messages_hex','signatures_hex','cases'})
  self.assertEqual(len(self.cases),53)
  for key in self.v['public_keys'].values():self.assertEqual(set(key),{'pk_seed_hex','pk_root_hex'})
  for c,*_ in self.cases:self.assertEqual(set(c),{'id','key','message','signature','scenario'})

 def test_known_answers_and_exact_wire_lengths(self):
  for c,seed,root,msg,sig in self.cases:
   with self.subTest(c['id']):
    self.assertEqual(len(seed+root),32);self.assertEqual(len(sig),5720)
    self.assertTrue(verify(self.spec,seed,root,msg,sig))

 def test_changed_message_is_rejected(self):
  for c,seed,root,msg,sig in self.cases:
   with self.subTest(c['id']):self.assertFalse(verify(self.spec,seed,root,bytes([msg[0]^1])+msg[1:],sig))

 def test_changed_signature_is_rejected(self):
  for c,seed,root,msg,sig in self.cases:
   bad=bytearray(sig);bad[len(bad)//2]^=1
   with self.subTest(c['id']):self.assertFalse(verify(self.spec,seed,root,msg,bytes(bad)))

 def test_changed_public_root_is_rejected(self):
  for c,seed,root,msg,sig in self.cases:
   with self.subTest(c['id']):self.assertFalse(verify(self.spec,seed,bytes([root[0]^1])+root[1:],msg,sig))

 def test_public_key_node_width_is_enforced(self):
  _,seed,root,msg,sig=self.cases[0]
  for size in (0,1,15,17,32):
   with self.subTest(size=size):
    self.assertFalse(verify(self.spec,b'\0'*size,root,msg,sig))
    self.assertFalse(verify(self.spec,seed,b'\0'*size,msg,sig))

 def test_truncated_and_overlong_signatures_are_rejected(self):
  for c,seed,root,msg,sig in self.cases:
   with self.subTest(c['id']):
    self.assertFalse(verify(self.spec,seed,root,msg,sig[:-1]))
    self.assertFalse(verify(self.spec,seed,root,msg,sig+b'\0'))

 def test_same_public_key_message_matches_across_saved_scenarios(self):
  groups=defaultdict(list)
  for c,seed,root,msg,sig in self.cases:groups[(seed,root,msg)].append((c['scenario'],sig))
  cross=0
  for group in groups.values():
   if len({scenario for scenario,_ in group})>1:
    self.assertEqual(len({sig for _,sig in group}),1);cross+=1
  self.assertGreater(cross,0,'No saved cross-scenario equality was actually checked')

if __name__=='__main__':unittest.main()
