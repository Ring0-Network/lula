"""Read-only pinned master/own comparison; writes only new local receipt."""
from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps=180
HERE=Path(__file__).resolve().parent
X=HERE.parent
EXPECTED_THEOREM='94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607'
EXPECTED_SCRIPT='2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd'
EXPECTED_REVIEW='0ea6c1761c7c2f0157da81e746c1797e99b1bcbde508e5eee4cc59ab3639a267'
EXPECTED_OWN='2a6320bd6689ada00bf25265aa08dde009700c489930736521f26c8d4762026a'
EXPECTED_OUTPUTS={
 'bounds-QH64':'95588a3415ca5c328f3a7107cdb47a97f4319f4f7f7cfe842ab8fc4ba8a44593',
 'bounds-QH128':'fed0563b108525cf18a5569b10b87e8cab994f15cd236faa7ca44a4ffb188a59'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def capped(x):return min(mp.mpf(1),mp.mpf(x))
def exact_value(s):
    if '/' in s:
        a,b=s.split('/')
        return mp.mpf(a)/mp.mpf(b)
    return mp.mpf(s)
def neglog(x):return -mp.log(capped(x),2)

def main():
    assert sha(X/'QUANTUM-RO-THEOREM.md')==EXPECTED_THEOREM
    assert sha(X/'bounds.py')==EXPECTED_SCRIPT
    assert sha(X/'quantum-composition-second-reader'/'SECOND_READER.md')==EXPECTED_REVIEW
    assert sha(HERE/'OWN-BOUNDS.json')==EXPECTED_OWN
    original=json.loads((HERE/'SHA256SUMS.json').read_text(encoding='utf-8'))
    preservation={name:sha(HERE/name)==digest for name,digest in original.items()}
    assert all(preservation.values())
    own=json.loads((HERE/'OWN-BOUNDS.json').read_text(encoding='utf-8'))
    independent={(r['q_exponent'],r['Qq_exponent']):r for r in own['rows']}
    assert len(independent)==16
    records=[]
    for name,Qhe,Qqe in [('bounds-QH64',64,32),('bounds-QH128',128,64)]:
        path=X/'root-checks'/name/'bounds.json'
        digest=sha(path)
        assert digest==EXPECTED_OUTPUTS[name]
        master=json.loads(path.read_text(encoding='utf-8'))
        assert master['script_sha256']==EXPECTED_SCRIPT
        assert master['quantum_theorem_sha256']==EXPECTED_THEOREM
        frozen=X.parents[1]/'numerics'/'bounds.py'
        assert master['frozen_calculator_sha256']==sha(frozen)
        assert master['parameters']=={'h':41,'a':9,'k':18,'n':16}
        assert len(master['rows'])==8
        assert [r['log2_q'] for r in master['rows']]==[24,30,38,40,41,44,50,64]
        for row in master['rows']:
            qe=row['log2_q']
            assert int(row['q'])==2**qe
            assert int(row['Qq'])==2**Qqe and int(row['QH'])==2**Qhe
            o=independent[(qe,Qqe)]
            # Every numeric quantum component, seed and total. Independent
            # raw components are capped according to the theorem's convention.
            values={
              'FORS_binomial_per_raw_candidate':mp.mpf(o['conditional_FORS_probability']),
              'seed_zero_probability':mp.mpf(o['seed_probability']),
              'quantum_private_hop_nonzero':capped(o['private_quantum_hop_uncapped']),
              'quantum_private_hop_unconditional':capped(mp.mpf(o['private_quantum_hop_uncapped'])+mp.mpf(o['seed_probability'])),
              'quantum_ROW_reprogramming_bound':capped(o['ROW_uncapped']),
              'quantum_programmed_coverage_envelope':mp.mpf(o['A_C_capped']),
              'quantum_COVER_final_event_bound_nonzero':mp.mpf(o['C_probability']),
              'quantum_hidden_final_event_bound_nonzero':mp.mpf(o['H_probability_capped']),
              'quantum_graph_final_event_bound_nonzero':mp.mpf(o['G_probability_capped']),
              'quantum_canonical_final_event_bound_nonzero':mp.mpf(o['D7_probability_capped']),
              'quantum_total':mp.mpf(o['candidate_reference_probability'])}
            probabilities={}
            for key,v in values.items():
                root=mp.mpf(row[key])
                relative=abs(root-v)/v
                assert relative<=mp.mpf('1e-43'),(name,qe,key,relative)
                probabilities[key]={'root':row[key],'relative_error':mp.nstr(relative,18),'PASS':True}
            bit_map={
              'FORS_binomial_bits':'FORS_binomial_per_raw_candidate',
              'quantum_private_hop_nonzero_bits':'quantum_private_hop_nonzero',
              'quantum_COVER_final_event_bound_bits':'quantum_COVER_final_event_bound_nonzero',
              'quantum_hidden_final_event_bound_bits':'quantum_hidden_final_event_bound_nonzero',
              'quantum_graph_final_event_bound_bits':'quantum_graph_final_event_bound_nonzero',
              'quantum_canonical_final_event_bound_bits':'quantum_canonical_final_event_bound_nonzero',
              'quantum_total_bits':'quantum_total'}
            exponent_checks={}
            for key,pkey in bit_map.items():
                ref=neglog(values[pkey])
                error=abs(mp.mpf(str(row[key]))-ref)
                assert error<=mp.mpf('2e-12'),(name,qe,key,error)
                exponent_checks[key]={'root':row[key],'absolute_error':mp.nstr(error,18),'PASS':True}
            assert row['quantum_status']=='COMPUTED_FROM_REVIEWED_FINITE_QROM_SOURCE_GAME_UNION'
            assert row['quantum_category1_status']=='NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY'
            for k in ['WOTS_generic_primitive_reduction','tree_generic_primitive_embedding']:
                assert row[k] is None
            records.append({'output':name,'q_exponent':qe,'Qq_exponent':Qqe,
                'probabilities':probabilities,'exponents':exponent_checks,
                'scope_status_checks':'PASS'})
        # Pin again after the full read so mutable concurrent output cannot
        # silently change the subject recorded by this receipt.
        assert sha(path)==digest
    assert sha(X/'bounds.py')==EXPECTED_SCRIPT
    assert sha(X/'QUANTUM-RO-THEOREM.md')==EXPECTED_THEOREM
    receipt=dict(status='PASS_ALL16_PINNED_QUANTUM_COMPONENT_TOTAL_AND_EXPONENT_CROSSCHECKS',
      source_theorem_sha256=EXPECTED_THEOREM,master_script_sha256=EXPECTED_SCRIPT,
      complete_composition_review_sha256=EXPECTED_REVIEW,
      independent_own_bounds_sha256=EXPECTED_OWN,
      root_output_sha256=EXPECTED_OUTPUTS,
      crosscheck_script_sha256=sha(Path(__file__)),
      historical_manifest_checks=preservation,
      probability_checks=16*11,exponent_checks=16*7,
      relative_probability_tolerance='1e-43 (root displays45 significant digits)',
      absolute_exponent_tolerance='2e-12 (root stores float exponents)',
      rows=records,
      conclusion='Reviewed finite-QROM reference advantage arithmetic accepted; no capacity/category/fixed-SHA certificate',
      root_master_recomputed=False,unrelated_classical_tests_recomputed=False)
    (HERE/'ROOT-CROSSCHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print('PASS:16 rows;176 probability components;112 exponents; source theorem/script/review/output pins; historical files unchanged.')

if __name__=='__main__':main()
