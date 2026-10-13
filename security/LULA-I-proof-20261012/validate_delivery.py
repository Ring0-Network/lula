"""Scope/provenance checks; no complete security theorem is inferred."""
from pathlib import Path
import hashlib, json

D = Path(__file__).resolve().parent
R = D.parents[1]
P = R / 'publications' / 'LULA-I'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

baseline = D / 'BASELINE.json'
if not baseline.exists():
    names = ['LULA-I.tex','comparison-results.tex','stability-results.tex','operating-model.tex','replay-results.tex','references.bib','LULA-I.pdf']
    record = [{'path':str(P / n),'sha256':sha(P / n)} for n in names]
    assert record[0]['sha256'] == 'd33229794b2b69644aa77851e09e146dda53480f8b2e70721c06b81d91587ebe'
    record += [{'path':str(R / 'R6' / 'R6A-state-as-accelerator' / 'work' / 'rust' / 'src' / 'lib.rs'),'sha256':'c5b16f35ec9e3a826e5d8100dbbc4d3a8287e3e52fd567a24e95f03bb7243ab5'},
               {'path':str(P / 'release' / 'code' / 'lula1' / 'src' / 'lib.rs'),'sha256':'ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'}]
    baseline.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
before = json.loads(baseline.read_text(encoding='utf-8'))
assert all(sha(Path(row['path'])) == row['sha256'] for row in before), 'Protected source changed'
data = json.loads((D / 'numerics' / 'bounds.json').read_text())
assert data['rows'][3]['log2_signatures'] == 40
assert abs(data['rows'][3]['FORS_binomial_bits'] - 132.563419944) < 1e-8
assert all(row['total_euf_probability'] is None and row['total_euf_bits'] is None for row in data['rows'])
count = json.loads((D / 'code-review' / 'SOURCE_AND_COUNTS.json').read_text())
assert data['inventories']['total_PRF_secret_input_universe'] == count['all_secret_prf_locations']
assert data['inventories']['top_cache_bytes'] == count['cache_payload'] == 75497456
table = ['# Full-term status table','','Every FORS number is a fixed-instance model computation. OPEN cells are not zero and are not assigned bits.','',
         '| Term / status | q=2^38 | q=2^40 | q=2^41 |','|---|---|---|---|']
for name in ('Secret-derivation PRF advantage','Message-randomizer/shared-SHA advantage','Adaptive FORS forgery bound','Full WOTS certification bound (all five layers)','Merkle/FORS-root extraction bound','H_msg and free-counter contribution','Full EUF-CMA total'):
    table.append(f'| {name} | OPEN | OPEN | OPEN |')
qrows = {r['log2_signatures']:r for r in data['rows']}
table += ['| FORS raw-candidate model exponent | '+' | '.join(f"COMPUTED {qrows[q]['FORS_binomial_bits']:.9f}" for q in (38,40,41))+' |',
          '| Honest different-child WOTS reuse subevent | PROVED 0 | PROVED 0 | PROVED 0 |',
          '| Honest-cache probability transfer loss | PROVED 0, conditional | PROVED 0, conditional | PROVED 0, conditional |','',
          'PROVED 0 for one subevent does not close the full WOTS term. Zero transfer loss does not establish the reference bound.',
          'The smallest full signing-limit crossing and full quantum q_max are not established.']
(D / 'TERM-TABLE.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
receipt = {'status':'PASS_SCOPED_DELIVERY_CHECKS','source_files_unchanged':len(before),'component_numeric_output_sha256':sha(D / 'numerics' / 'bounds.json'),'namespace_and_cache_counts_independently_agree':True,'all_full_security_totals_remain_null':True,'complete_security':'OPEN / not established'}
(D / 'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
