from pathlib import Path
import json
P=Path(__file__).resolve().parent
b=598
m=1<<(max(256,8*b+1)-1).bit_length()
V=(256**(b+1)-1)//255
Q=2**32
hs=2**21*(19505+2**32)-1
modes={'hot':82090+5*2**32,'cold':8560574463+82090+6*2**32}
rows=[]
for e in (24,30,38,40,41,44,50,64):
 q=2**e
 for mode,hm in modes.items():
  T=Q+hs+q*hm+3224+254+6000
  k=min(2*T,V)
  assert k==2*T and m==8192
  rows.append(dict(log2_q=e,mode=mode,Q_adversarial=Q,T_all_outside_evaluations=T,
      k=k,m=m,coefficient_random_bits=k*m,coefficient_bytes=k*m//8,
      F_distinct_cap=min(19212937084272640,162+2181038080+q*({'hot':12816,'cold':33567232}[mode])),
      J_cap=q))
out={'status':'COMPUTED_DETERMINISTIC_SIMULATOR_RESOURCE_CAPS_NOT_SECURITY_RESULTS',
 'b_example':b,'m':m,'classifier_Raw_extra':6000,'classifier_F_extra':161,
 'query_budget_formula':'Q+Hsetup+q Hmode+3224+254+6000','rows':rows}
(P/'RESOURCE-CAPS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'rows':len(rows),'m':m,'q40_hot':next(r for r in rows if r['log2_q']==40 and r['mode']=='hot')},indent=2))
