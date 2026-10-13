"""Tiny abstract row/chain/path controls only; no cryptographic signer execution."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import hashlib,json
E=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
vectors=list(product(range(4),repeat=2))
accept=lambda d:sum(d)==3
counts={'tables':0,'two_accepted':0,'same_vector_two_accepted':0,'reject_fallback':0,'no_completion':0}
for table in product(vectors,repeat=2):
 counts['tables']+=1
 canonical=next((i for i,d in enumerate(table) if accept(d)),None)
 if canonical is None:counts['no_completion']+=1;continue
 if canonical!=0:continue
 chosen=1 if accept(table[1]) else canonical
 if accept(table[1]):
  assert chosen==1 and chosen.to_bytes(4,'big')!=canonical.to_bytes(4,'big')
  counts['two_accepted']+=1
  counts['same_vector_two_accepted']+=int(table[0]==table[1])
 else:assert chosen==0;counts['reject_fallback']+=1
assert counts=={'tables':256,'two_accepted':16,'same_vector_two_accepted':4,'reject_fallback':48,'no_completion':144}
assert F(counts['two_accepted'],256)==F(1,4)**2

# Addressed finite chain functions; deliberately non-cryptographic.
prime=257
def step(key,chain,stage,v):return (3*v+11*key+7*chain+stage+1)%prime
def chain(key,i,x,a,b):
 for stage in range(a,b):x=step(key,i,stage,x)
 return x
def start(key,i):return (13+19*key+23*i)%prime
def leaf(key):return sum((i+1)*chain(key,i,start(key,i),0,3) for i in range(2))%prime
def combine(left,right):return (5*left+7*right+17)%prime
root=combine(leaf(0),leaf(1))
table=((0,3),(3,0),(3,3),(0,3))
def sign_abstract(proposed,sibling):
 # The SAME child and key are implicit fixed arguments of this tiny row.
 canonical=0
 chosen=proposed if accept(table[proposed]) else canonical
 d=table[chosen]
 sig=tuple(chain(0,i,start(0,i),0,d[i]) for i in range(2))
 encoded=chosen.to_bytes(4,'big')+b''.join(x.to_bytes(2,'big') for x in sig)+sibling.to_bytes(2,'big')
 return chosen,sig,sibling,encoded
def verify_abstract(sig):
 c,values,sibling,_=sig;d=table[c]
 if not accept(d):return False
 pk=sum((i+1)*chain(0,i,values[i],d[i],3) for i in range(2))%prime
 return combine(pk,sibling)==root
reference=sign_abstract(0,leaf(1))
alternate=sign_abstract(1,leaf(1))
same_digits=sign_abstract(3,leaf(1))
rejected=sign_abstract(2,leaf(1))
assert verify_abstract(reference) and verify_abstract(alternate) and verify_abstract(same_digits)
assert reference[3]!=alternate[3] and reference[3]!=same_digits[3]
assert reference[1]==same_digits[1] # Distinct bytes need no new digit vector.
assert rejected==reference
unauthentic=sign_abstract(1,(leaf(1)+1)%prime)
assert not verify_abstract(unauthentic)
composition=0
for key,i,x,d in product(range(2),range(2),range(17),range(4)):
 assert chain(key,i,chain(key,i,x,0,d),d,3)==chain(key,i,x,0,3)
 composition+=1
nonempty=0
for size in range(1,17):
 good=set(vectors[:size])
 both=sum(a in good and b in good for a,b in product(vectors,repeat=2))
 assert both==size*size>0
 nonempty+=1

# Literal full-word language separation for the support cylinder.
seed=bytes(range(1,17));P=bytes(16);mu=bytes(16)
adrs=lambda typ:bytes(9)+bytes([typ])+bytes(12)
word=lambda typ,c:seed+bytes(48)+adrs(typ)+mu+c.to_bytes(4,'big')
row0,row1=word(7,0),word(7,1)
assert len(row0)==106 and row0!=row1 and row0[73]==row1[73]==7
for typ in range(7):assert word(typ,0)!=row0 and word(typ,0)[73]!=7
untyped=(P+seed,bytes(16)+seed+bytes(16),bytes(32)+bytes(4)+seed)
assert tuple(map(len,untyped))==(32,48,52)
assert all(len(w)<86 and w not in (row0,row1) for w in untyped)

result={'status':'PASS_TINY_ABSTRACT_COUNTER_CHAIN_PATH_AND_RAW_LANGUAGE_CONTROLS',
 'script_sha256':sha(Path(__file__)),'first_sha256':sha(E/'INDEPENDENT-FIRST.md'),
 'support_proof_sha256':sha(E/'FULL-SHARED-RO-SUPPORT.md'),'row_counts':counts,
 'chain_composition_checks':composition,'nonempty_acceptance_sizes':nonempty,
 'genuine_same_child_different_counter_valid':True,'same_vector_different_counter_valid':True,
 'rejected_counter_canonical_recompute':True,'unauthentic_path_not_valid':True,
 'support_empty_message_lengths':[32,48,52],'type7_length':106,'type_offset':73,
 'actual_crypto_source_signature_cache_forest_attack_or_timing_run':False,
 'finite_controls_prove_general_source_theorem':False,
 'new_source_game_declarations':0,'whole_goal_complete':False}
(E/'CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
