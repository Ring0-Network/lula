"""Refined event-bound evaluation; conservative source calculator stays pinned.

First run bounds.py at the required Q budget. Then:
python -I -B bounds-event-specific.py --base root-checks/bounds-QH64/bounds.json --out root-checks/refined-Qq32
No signing, caches, timings or new source parameters are evaluated.
"""
from pathlib import Path
import argparse
import hashlib
import json
import mpmath as mp
assert mp.__version__=='1.3.0'
X=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--base',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    source=json.loads(args.base.read_text(encoding='utf8'))
    assert source['parameters']=={'h':41,'a':9,'k':18,'n':16}
    assert source['script_sha256']==sha(X/'bounds.py')
    assert source['quantum_theorem_sha256']==sha(X/'QUANTUM-RO-THEOREM.md')
    assert (X/'QUANTUM-EVENT-SPECIFIC-THEOREM.md').exists()
    rows=[]
    with mp.workdps(220):
        N=mp.mpf(1<<128)
        for r in source['rows']:
            q=int(r['q']);Q=int(r['Qq'])
            e=min(mp.mpf(1),sum(mp.mpf(r[k]) for k in (
                'quantum_COVER_final_event_bound_nonzero',
                'quantum_hidden_final_event_bound_nonzero',
                'quantum_graph_final_event_bound_nonzero',
                'quantum_canonical_final_event_bound_nonzero')))
            b=min(mp.mpf(1),mp.mpf(2*q+2)/N)
            a=2*mp.mpf(Q)/mp.sqrt(N)
            event=min(mp.mpf(1),1/N+(a+mp.sqrt(min(mp.mpf(1),b+e)))**2)
            conservative=mp.mpf(r['quantum_total'])
            best=min(conservative,event)
            exponent=lambda x:float(-mp.log(x,2))
            rows.append({'log2_q':r['log2_q'],'q':str(q),'Qq':str(Q),
                'HJ_winning_envelope':mp.nstr(e,45),'HJ_envelope_bits':exponent(e),
                'source_alias_bound':mp.nstr(b,45),'purified_gap_bound':mp.nstr(a,45),
                'event_specific_total':mp.nstr(event,45),'event_specific_total_bits':exponent(event),
                'conservative_total':r['quantum_total'],'conservative_total_bits':r['quantum_total_bits'],
                'best_reviewed_total':mp.nstr(best,45),'best_reviewed_total_bits':exponent(best),
                'status':'COMPUTED_FROM_REVIEWED_MANUAL_EVENT_SPECIFIC_FINITE_QROM_THEOREM',
                'category1_status':'NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY'})
    assert len(rows)==8
    args.out.mkdir(parents=True,exist_ok=True)
    record={'parameters':source['parameters'],'rows':rows,
       'base_output_sha256':sha(args.base),'base_script_sha256':source['script_sha256'],
       'conservative_theorem_sha256':sha(X/'QUANTUM-RO-THEOREM.md'),
       'refined_theorem_sha256':sha(X/'QUANTUM-EVENT-SPECIFIC-THEOREM.md'),
       'script_sha256':sha(Path(__file__)),'precision_decimal_digits':220,
       'qualification':'High-precision evaluation with serialized component inputs; not formally directed-rounded intervals. Exponents are probability bounds, not security levels.'}
    (args.out/'bounds.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
    lines=['# Refined finite-QROM probability envelopes','',
      'COMPUTED from reviewed source-model theorems. Q_q='+rows[0]['Qq']+'. q counts initiated calls. Seed-zero is charged once. Values are -log2 probability upper bounds, not work factors.','',
      '| log2 q | HJ event-union exponent | conservative source exponent | refined source exponent | best reviewed exponent |',
      '|---:|---:|---:|---:|---:|']
    for r in rows:
        lines.append(f"| {r['log2_q']} | {r['HJ_envelope_bits']:.9f} | {r['conservative_total_bits']:.9f} | {r['event_specific_total_bits']:.9f} | {r['best_reviewed_total_bits']:.9f} |")
    lines.extend(['','OPEN: level/category certification, exact capacity, efficient generic embeddings, source/channel refinement and broader cache APIs.'])
    (args.out/'bounds.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(json.dumps({'status':'REFINED_SOURCE_ARITHMETIC_GENERATED_INDEPENDENT_CROSSCHECK_REQUIRED','rows':8,'Qq':rows[0]['Qq']}))

if __name__=='__main__': main()
