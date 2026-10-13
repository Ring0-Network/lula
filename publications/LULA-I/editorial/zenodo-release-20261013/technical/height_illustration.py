"""Analytical height illustration only; no source implementation or hash runs."""
from pathlib import Path
import hashlib,json,math
import mpmath as mp
P=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I')
O=Path(__file__).parent
def calc(qexp,h,dps,poisson):
    with mp.workdps(dps):
        q=2**qexp;rho=mp.mpf(2)**-h;r=1-mp.mpf(2)**-9
        terms=[]
        for j in range(18):
            delta=r**j-1
            moment=mp.exp(q*rho*delta) if poisson else mp.exp(q*mp.log1p(rho*delta))
            terms.append((-1)**j*math.comb(17,j)*moment)
        prob=mp.fsum(terms)/512
        assert 0<prob<1
        return mp.nstr(prob,160),mp.nstr(-mp.log(prob,2),160)
rows=[]
for q,h,tag in [(40,41,'evaluated_baseline'),(40,40,'analytical_top_height_20'),(41,41,'old_comparison_row')]:
    row=dict(label=tag,log2_signing_queries=q,total_height=h)
    for mode in ['binomial','poisson']:
        low=calc(q,h,600,mode=='poisson');high=calc(q,h,900,mode=='poisson')
        assert low==high,(q,h,mode)
        row[mode]=dict(p_raw=high[0],negative_log2_p_raw=high[1],display=f'{float(high[1]):.1f}',precision_check='600 vs 900 dps; all 160 reported digits agree')
    rows.append(row)
assert rows[0]['binomial']['display']=='132.6'
assert rows[1]['binomial']['display']==rows[1]['poisson']['display']=='125.9'
assert rows[1]['poisson']==rows[2]['poisson']
assert rows[1]['binomial']['p_raw']!=rows[2]['binomial']['p_raw']
counts=[]
for top in [21,20]:
    node_bytes=16*(2**(top+1)-1);ctr_bytes=4*2**top
    counts.append(dict(top_height=top,total_height=20+top,node_bytes=node_bytes,counter_bytes=ctr_bytes,cache_payload_bytes=node_bytes+ctr_bytes,signature_bytes=16+4+17*10*16+4*(4+32*16+5*16)+4+16*16+top*16,uncached_top_suffix_compressions=4102*2**top-1))
assert [r['cache_payload_bytes'] for r in counts]==[75497456,37748720]
assert [r['signature_bytes'] for r in counts]==[5720,5704]
assert [r['uncached_top_suffix_compressions'] for r in counts]==[8602517503,4301258751]
result=dict(status='ANALYTICAL_COMPONENT_ILLUSTRATION_ONLY',source_sha256=hashlib.sha256((P/'release/code/lula1/src/lib.rs').read_bytes()).hexdigest(),baseline_q_exp=40,fors_height=9,real_fors_trees=17,forced_zero_bits=9,model='Independent uniform address and real-tree selections; exact Binomial occupancy or named Poisson approximation; per raw candidate, not full-signature insecurity',rows=rows,counts=counts,implemented_new_set=False,measured_new_set=False,new_security_category_or_capacity=False,whole_goal_complete=False)
(O/'HEIGHT-ILLUSTRATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(rows=[dict(label=r['label'],binomial=r['binomial']['negative_log2_p_raw'][:68],poisson=r['poisson']['negative_log2_p_raw'][:68],display=r['binomial']['display']) for r in rows],counts=counts),indent=2))
