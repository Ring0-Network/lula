"""Verify retained public vectors using the independent specification verifier.

No key, cache, benchmark, or signer is loaded. Failure is a nonzero exit status.
Checks accept/reject behavior and selected serialized-byte equality, not security.
"""
from pathlib import Path
from collections import defaultdict
import hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'recomputed/verification'
OUT.mkdir(parents=True,exist_ok=True)
path=ROOT/'code/python/verify_lula.py'
spec=importlib.util.spec_from_file_location('independent_lula',path)
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
PARAMS='18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1'
campaigns=[];ok=True
for campaign,glob in [('a1','lula1-*.vec.txt'),('b1','*.vec.txt')]:
    files=sorted((ROOT/'data'/campaign/'raw').glob(glob));groups=defaultdict(list);rows=[]
    assert len(files)==(14 if campaign=='a1' else 36),(campaign,len(files))
    for f in files:
        d=dict(l.split() for l in f.read_text().splitlines() if len(l.split())==2)
        seed,root,msg,sig=[bytes.fromhex(d[k]) for k in ['pk_seed','pk_root','msg','sig']]
        mutated=bytearray(sig);mutated[len(mutated)//2]^=1
        z={'file':f.relative_to(ROOT).as_posix(),'valid':v.verify(PARAMS,seed,root,msg,sig),
           'changed_message_rejected':not v.verify(PARAMS,seed,root,bytes([msg[0]^1])+msg[1:],sig),
           'changed_signature_rejected':not v.verify(PARAMS,seed,root,msg,bytes(mutated)),
           'message_bytes':len(msg),'signature_bytes':len(sig),'signature_sha256':hashlib.sha256(sig).hexdigest()}
        rows.append(z);ok &= z['valid'] and z['changed_message_rejected'] and z['changed_signature_rejected']
        groups[(d['pk_seed'],d['pk_root'],d['msg'])].append((f.name,sig))
    gs=[{'public_key_seed':a,'public_key_root':b,'message_bytes':len(bytes.fromhex(m)),'files':[f for f,s in vs],'distinct_signatures':len({s for f,s in vs})} for (a,b,m),vs in groups.items()]
    ok &= all(g['distinct_signatures']==1 for g in gs)
    campaigns.append({'campaign':campaign,'vectors':rows,'complete_public_key_message_groups':gs})
katfiles=[ROOT/'data/replay'/name for name in ['vectors_LULA-I.txt','vectors_mini.txt','vectors_KN.txt','vectors_NC.txt']]
kat=subprocess.run([sys.executable,'-I','-B',str(path),*map(str,katfiles)],text=True,capture_output=True)
ok &= kat.returncode==0
(OUT/'historical-independent-check.txt').write_text(kat.stdout+kat.stderr,encoding='utf8')
result={'independent_verifier_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'campaigns':campaigns,'historical_KAT_exit_code':kat.returncode,'all_checks_pass':bool(ok),'scope':'Finite accepted-vector, selected bit-flip rejection and same-public-key/message byte equality checks; no cryptanalytic or adaptive-forgery guarantee.'}
(OUT/'VECTOR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'all_checks_pass':bool(ok),'a1_vectors':len(campaigns[0]['vectors']),'b1_vectors':len(campaigns[1]['vectors']),'a1_groups':len(campaigns[0]['complete_public_key_message_groups']),'b1_groups':len(campaigns[1]['complete_public_key_message_groups']),'historical_KAT_exit_code':kat.returncode}))
sys.exit(0 if ok else 1)
