"""Own exact affine inversion and lower-precision quantum endpoint checks."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util, json, hashlib

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ownthresholds', HERE/'thresholds.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
data=json.loads((HERE/'THRESHOLDS.json').read_text(encoding='utf-8'))
checks=[]
for k in m.QS:
    q=1<<k
    pl,pu=m.PF[k]
    al=F(6,m.N)+F(q,m.N*m.N)+pl
    au=F(6,m.N)+F(q,m.N*m.N)+pu
    common=F(3*q+6243,m.N)+F(q*(q-1)//2+q,m.N*m.N)
    bl=common+pl
    bu=common+pu+F(q,1<<4096)
    guaranteed=(m.TARGET-bu)//au
    possible=(m.TARGET-bl)//al
    row=next(r for r in data['rows'] if r['log2_q']==k and r['model']=='classical')
    assert guaranteed==possible==int(row['Q_pass'])
    checks.append({'q_log2':k,'method':'exact affine inversion','Q_pass':str(guaranteed)})

precision_counts={}
straddling_64=[]
for row in data['rows']:
    m.P=64; m.SCALE=1<<64
    k=row['log2_q']; q=1<<k; pf=m.I(*m.PF[k])
    for which,expected in (('Q_pass','PASS'),('Q_fail','FAIL')):
        Q=int(row[which]); actual=m.formulas(q,Q,pf)[row['model']]
        try: assert m.certify(actual)==expected
        except ArithmeticError: straddling_64.append([k,row['model'],which])
for p in (128,256):
    m.P=p; m.SCALE=1<<p
    count=0
    for row in data['rows']:
        k=row['log2_q']; q=1<<k; pf=m.I(*m.PF[k])
        for which,expected in (('Q_pass','PASS'),('Q_fail','FAIL')):
            Q=int(row[which]); actual=m.formulas(q,Q,pf)[row['model']]
            assert m.certify(actual)==expected
            count+=1
    precision_counts[str(p)]=count

out={'outcome':'PASS','exact_affine_inversions':checks,
     'lower_precision_endpoint_comparisons':precision_counts,
     'sqrt64_straddling_endpoints':straddling_64,
     'meaning':'independently arranged own checks, not a second external reader; all128/256-bit sqrt enclosures prove the same32 adjacent crossings',
     'script_sha256':hashlib.sha256((HERE/'crosscheck.py').read_bytes()).hexdigest(),
     'threshold_script_sha256':data['script_sha256'],
     'threshold_data_sha256':hashlib.sha256((HERE/'THRESHOLDS.json').read_bytes()).hexdigest()}
(HERE/'CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
