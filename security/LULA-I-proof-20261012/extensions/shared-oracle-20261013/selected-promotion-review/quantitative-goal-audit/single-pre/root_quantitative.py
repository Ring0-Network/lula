"""Exact rational arithmetic for a separate, conservative RO interface envelope."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
E=Path(__file__).resolve().parent
N=1<<128
keys=sum(1<<h for h in (41,36,31,26))
A=[32*keys*max(14-r,0)+16*(1<<21)*(254-r) for r in range(254)]
AH=sum(A)
DH=480*keys+4080*(1<<21)+(1<<41)*17*512
assert AH==7628143271608320 and DH==20229886488608768
mu=F(2*N-1,N*N)
slope=F(12*AH,1<<64)
assert slope==F(682009155,137438953472)
cap=lambda x:min(F(1),x)
def row(qa):
    qe=qa+1
    pre=cap((2*qe+1)**2*mu)
    pre_source=DH*pre
    ud_source=slope*qe
    return {'QA':str(qa),'effective_Q':str(qe),
      'PRE_numerator':str(pre.numerator),'PRE_denominator':str(pre.denominator),
      'PRE_source_numerator':str(pre_source.numerator),'PRE_source_denominator':str(pre_source.denominator),
      'UD_source_numerator':str(ud_source.numerator),'UD_source_denominator':str(ud_source.denominator),
      'hidden_component_cap':str(cap(pre_source+ud_source))}
rows=[]
HS=(1<<21)*(19505+(1<<32))-1
hot=82090+5*(1<<32)
cold=8560574463+82090+6*(1<<32)
for e in (24,30,38,40,41,44,50,64):
  for mode,hm in [('prepared',hot),('absent',cold)]:
    for qe in (32,64):
      r=row(1<<qe)
      r.update({'log2_q':e,'mode':mode,'log2_QA':qe,
                'outside_query_cap':str((1<<qe)+HS+(1<<e)*hm+3224+254),
                'status':'COMPUTED_FROM_MANUAL_RANDOM_ORACLE_COMPONENT_ONLY'})
      assert r['hidden_component_cap']=='1'
      rows.append(r)
def envelope(qa):
    r=qa+1
    return DH*cap((2*r+1)**2*mu)+slope*r
thresholds=[]
for c in [F(1,2),F(1)]:
  lo,hi=0,256
  while lo+1<hi:
    mid=(lo+hi)//2
    if envelope(mid)<=c:lo=mid
    else:hi=mid
  assert envelope(lo)<=c<envelope(hi)
  thresholds.append({'target':str(c),'QA_pass':lo,'QA_fail':hi,
                     'pass_value':str(envelope(lo)),'fail_value':str(envelope(hi))})
assert [(r['QA_pass'],r['QA_fail']) for r in thresholds]==[(99,100),(200,201)]
out={'classification':'COMPUTED exact random-oracle interface envelope',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'N':str(N),'D_H':str(DH),'sum_active_counts':str(AH),
 'marker_mu':str(mu),'UD_slope':str(slope),'rows':rows,
 'constant_probability_crossings':thresholds,
 'unchanged_old_scalar_tables':True,'fixed_SHA_or_category_certificate':False,
 'warning':'Upper envelope capped1 is not a forgery, insecurity proof or minimum-parameter repair'}
(E/'QUANTITATIVE-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'rows':len(rows),'all_caps_one':True,'crossings':thresholds,'security':'not established'}))
