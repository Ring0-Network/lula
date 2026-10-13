"""Current pinned refined successor crosscheck against preserved independent data."""
from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps=180
HERE=Path(__file__).resolve().parent
X=HERE.parent
PINS={
 'bounds.py':'2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd',
 'QUANTUM-RO-THEOREM.md':'94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607',
 'QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md':'081545e57dd6ac3341bca85e4c2a22ff016747c4c58591a110324e80d397d8e2',
 'bounds-event-specific.py':'4f06f80befae967479a582fb644d4d24bcb40b9051324709f529abcf683a8a81',
 'QUANTUM-EVENT-SPECIFIC-THEOREM.md':'d28e99570c0b6819f7a45169882252ffedc6e31cfad150751f7084a9fdea02f1',
 'root-checks/bounds-QH64/bounds.json':'95588a3415ca5c328f3a7107cdb47a97f4319f4f7f7cfe842ab8fc4ba8a44593',
 'root-checks/bounds-QH128/bounds.json':'fed0563b108525cf18a5569b10b87e8cab994f15cd236faa7ca44a4ffb188a59',
 'root-checks/refined-Qq32/bounds.json':'24c6e770835ba269f12ebcb42b1e8c88e21bc498503ecc98ba0b4e1fe85da33e',
 'root-checks/refined-Qq64/bounds.json':'d635fbed31532e66e3be5a8681ef0dad1a643f9c46250cb7be6a2c2ee526fe31'}
EXPECTED_CANDIDATE='b1e7305710268af6a71045449724fc5b7eab46057f1de402acd068c3a070607d'
EXPECTED_QUALIFIER='High-precision evaluation with serialized component inputs; not formally directed-rounded intervals. Exponents are probability bounds, not security levels.'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bits(p):return -mp.log(mp.mpf(p),2)

def main():
    pin_checks={p:sha(X/p)==h for p,h in PINS.items()}
    assert all(pin_checks.values())
    candidate=HERE/'CANDIDATE-BOUNDS.json'
    assert sha(candidate)==EXPECTED_CANDIDATE
    historical=json.loads((HERE/'SHA256SUMS.json').read_text(encoding='utf-8'))
    preserved={n:sha(HERE/n)==h for n,h in historical.items()}
    assert all(preserved.values())
    data=json.loads(candidate.read_text(encoding='utf-8'))
    own={(r['q_exponent'],r['Qq_exponent']):r for r in data['rows']}
    assert len(own)==16
    rows=[]
    for Qe,base in [(32,'root-checks/bounds-QH64/bounds.json'),(64,'root-checks/bounds-QH128/bounds.json')]:
        rel=f'root-checks/refined-Qq{Qe}/bounds.json'
        d=json.loads((X/rel).read_text(encoding='utf-8'))
        assert d['parameters']=={'h':41,'a':9,'k':18,'n':16}
        assert d['base_output_sha256']==PINS[base]
        assert d['base_script_sha256']==PINS['bounds.py']
        assert d['conservative_theorem_sha256']==PINS['QUANTUM-RO-THEOREM.md']
        assert d['refined_theorem_sha256']==PINS['QUANTUM-EVENT-SPECIFIC-THEOREM.md']
        assert d['script_sha256']==PINS['bounds-event-specific.py']
        assert d['precision_decimal_digits']==220 and d['qualification']==EXPECTED_QUALIFIER
        assert [r['log2_q'] for r in d['rows']]==[24,30,38,40,41,44,50,64]
        for r in d['rows']:
            qe=r['log2_q'];o=own[(qe,Qe)]
            assert int(r['q'])==2**qe and int(r['Qq'])==2**Qe
            event=mp.mpf(o['candidate_rare_quantum_total'])
            conservative=mp.mpf(o['accepted_conservative_reference_probability'])
            expected={
              'HJ_winning_envelope':mp.mpf(o['source_HJ_union_probability']),
              'source_alias_bound':mp.mpf(o['honest_alias_probability_capped']),
              'purified_gap_bound':mp.mpf(o['stopped_vector_gap']),
              'event_specific_total':event,
              'conservative_total':conservative,
              'best_reviewed_total':min(event,conservative)}
            fieldchecks={}
            for k,v in expected.items():
                err=abs(mp.mpf(r[k])-v)/v
                assert err<=mp.mpf('1e-43'),(Qe,qe,k,err)
                fieldchecks[k]={'root':r[k],'relative_error':mp.nstr(err,18),'PASS':True}
            bitchecks={}
            for k,pk in [('HJ_envelope_bits','HJ_winning_envelope'),
                         ('event_specific_total_bits','event_specific_total'),
                         ('conservative_total_bits','conservative_total'),
                         ('best_reviewed_total_bits','best_reviewed_total')]:
                err=abs(mp.mpf(str(r[k]))-bits(expected[pk]))
                assert err<=mp.mpf('2e-12'),(Qe,qe,k,err)
                bitchecks[k]={'root':r[k],'absolute_error':mp.nstr(err,18),'PASS':True}
            assert r['status']=='COMPUTED_FROM_REVIEWED_MANUAL_EVENT_SPECIFIC_FINITE_QROM_THEOREM'
            assert r['category1_status']=='NOT_ESTABLISHED_NO_CERTIFIED_CAPACITY'
            rows.append({'q_exponent':qe,'Qq_exponent':Qe,'numeric_fields':fieldchecks,
                         'exponents':bitchecks,'scope_status':'PASS'})
    assert all(sha(X/p)==h for p,h in PINS.items())
    source=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I\release\code\lula1\src\lib.rs')
    source_pin=sha(source)
    assert source_pin=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
    successor={'status':'PASS_REFINED_SINGLE_PROJECTOR_SUCCESSOR_IDENTITIES_AND_SOURCE_SCOPE',
        'source_sha256':source_pin,'artifact_pins':PINS,
        'historical_rare_manifest_checks':preserved,
        'review_scope':'physical CQ active-prefix/common pre-response source stop/single B-or-W projection; accepted refined sufficient model theorem, no category or fixed-SHA certificate',
        'material_change_from_original':'single-projector square replaces valid looser sum of two squares; explicitly justified in preserved own COMBINED-PROJECTOR and independent reviews',
        'check_script_sha256':sha(Path(__file__))}
    (HERE/'SUCCESSOR-CHECK.json').write_text(json.dumps(successor,indent=2)+'\n',encoding='utf-8')
    result={'status':'PASS_ALL16_ROOT_REFINED_ROWS_FIELDS_AND_EXPONENTS',
       'independent_candidate_sha256':EXPECTED_CANDIDATE,'artifact_pins':PINS,
       'check_script_sha256':sha(Path(__file__)),
       'numeric_field_count':16*6,'exponent_count':16*4,
       'relative_serialization_tolerance':'1e-43','absolute_float_exponent_tolerance':'2e-12',
       'root_precision_decimal_digits':220,'independent_precision_decimal_digits':240,
       'root_precision_qualification':EXPECTED_QUALIFIER,'rows':rows,
       'historical_rare_manifest_checks':preserved,
       'root_recomputed':False,'unrelated_old_tests_recomputed':False}
    (HERE/'ROOT-REFINED-CROSSCHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: successor pins/scope;16 refined rows;96 numeric fields;64 exponents;220-digit serialized qualification; historical manifest unchanged.')

if __name__=='__main__':main()
