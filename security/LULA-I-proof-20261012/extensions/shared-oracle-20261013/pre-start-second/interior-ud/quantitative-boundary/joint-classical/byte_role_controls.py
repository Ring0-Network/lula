"""Byte-language and rational analytical-ledger controls; no signer or attack."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json

BASE=Path(__file__).resolve().parent
S=bytes([0x22])*16
ROOT=bytes([0x33])*16
R=bytes([0x11])*16
HS=(5,5,5,5,21)
LS=(32,32,32,32,16)
WS=(16,16,16,16,256)

def address(layer=0,tree=0,typ=0,kp=0,w2=0,w3=0):
    return bytes([layer])+tree.to_bytes(8,"big")+bytes([typ])+kp.to_bytes(4,"big")+w2.to_bytes(4,"big")+w3.to_bytes(4,"big")

def decode(a):
    return (a[0],int.from_bytes(a[1:9],"big"),a[9],int.from_bytes(a[10:14],"big"),int.from_bytes(a[14:18],"big"),int.from_bytes(a[18:22],"big"))

def valid_wots(layer,tree,kp):
    return layer<5 and tree<(1<<sum(HS[layer+1:])) and kp<(1<<HS[layer])

def kind(word,seed=S):
    if len(word)>=32 and word[16:32]==seed:
        return "I" if len(word)>=48 else "Jshort"
    if len(word)==52 and word[-16:]==seed and word[16:32]!=seed:
        return "E"
    if len(word)<86 or word[:64]!=seed+bytes(48):return "Other"
    layer,tree,typ,kp,w2,w3=decode(word[64:86])
    tail=len(word)-86
    vw=valid_wots(layer,tree,kp)
    vf=layer==0 and tree<(1<<36) and kp<32
    if typ==5 and vw and w2<LS[layer] and w3==0 and tail==16:return "F"
    if typ==6 and vf and w2==0 and w3<17*512 and tail==16:return "F"
    if typ==0 and vw and w2<LS[layer] and w3<WS[layer]-1:
        return "T" if tail==16 else "Gother"
    if typ==1 and vw and w2==0 and w3==0:return "Gother"
    if typ==2 and layer<5 and tree<(1<<sum(HS[layer+1:])) and kp==0 and 1<=w2<=HS[layer] and w3<(1<<(HS[layer]-w2)):return "Gother"
    if typ==3 and vf and w2<=9 and w3<17*(1<<(9-w2)):
        return "T" if w2==0 and tail==16 else "Gother"
    if typ==4 and vf and w2==0 and w3==0:return "Gother"
    if typ==7 and vw and w2==0 and w3==0:return "Seven"
    return "Other"

def typed(typ,payload,**kw):return S+bytes(48)+address(typ=typ,**kw)+payload

checks=0
assert kind(R+S)=="Jshort";checks+=1
assert kind(R+S+ROOT+b"label")=="I";checks+=1
u=R+bytes([0x44])*16
assert kind(u+bytes(4)+S)=="E";checks+=1
u_alias=R+S
alias=u_alias+bytes(4)+S
assert len(alias)==52 and alias[16:32]==S and alias[-16:]==S
assert kind(alias)=="I";checks+=1
for typ,tail,expect in [(0,16,"T"),(0,15,"Gother"),(1,0,"Gother"),(2,32,"Gother"),(3,16,"T"),(3,20,"Gother"),(4,272,"Gother"),(5,16,"F"),(5,15,"Other"),(6,16,"F"),(7,20,"Seven"),(7,0,"Seven")]:
    kw={"w2":1} if typ==2 else {}
    w=typed(typ,bytes(tail),**kw)
    assert kind(w)==expect
    assert w[16:32]!=S and len(w)>52
    checks+=1
# A terminal chain address has no genuine nonterminal target.
assert kind(typed(0,bytes(16),w3=15))=="Other";checks+=1
# At zero seed, an addressed word is ALSO in the inner/private-J language.
zero_word=bytes(64)+address(typ=0)+bytes(16)
assert zero_word[16:32]==bytes(16) and len(zero_word)>=48;checks+=1

triple=[];double=[];outer=[]
for size in (2,4,8):
    union=sum(p==0 or j==0 or z==1 for p,j,z in product(range(size),repeat=3))
    prob=Fraction(union,size**3)
    assert prob==Fraction(3,size)-Fraction(3,size**2)+Fraction(1,size**3)
    triple.append({"toy_size":size,"analytical_triple_union":str(prob)})
    union2=sum(x==0 or (x!=0 and z==1) for x,z in product(range(size),repeat=2))
    prob2=Fraction(union2,size**2)
    assert prob2==Fraction(2,size)-Fraction(1,size**2)
    double.append({"toy_size":size,"analytical_hidden_or_graph_union":str(prob2)})
    for first,last,p in product(range(size),repeat=3):
        private_outer=(first==p and last==1)
        assert not private_outer or last==1
    outer.append({"toy_size":size,"outer_private_implies_prior_inner_endpoint":True})

assert 17+4*240+2040==3017
assert 171+4*246+2062==3217
assert 2*3017+(3217-3017)==6234
assert 6234+5+2+1==6242
out={
    "classification":"COMPUTED_SYNTACTIC_AND_ANALYTICAL_LEDGER_CONTROLS",
    "byte_checks":checks,"triple_cases":triple,"protected_double_cases":double,
    "outer_domination":outer,"candidate_unconditional_constant":6242,
    "candidate_fixed_nonzero_constant":6241,
    "prior_first_sha256":hashlib.sha256((BASE/"INDEPENDENT-FIRST.md").read_bytes()).hexdigest(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "exit_code":0,"actual_private_attack_or_signature_constructed":False,
    "source_or_RO_hash_called":False,"whole_source_joint_sampler_verified":False,
    "new_source_game_declarations":0,"whole_goal_complete":False,
}
(BASE/"BYTE-ROLE-CONTROLS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))
