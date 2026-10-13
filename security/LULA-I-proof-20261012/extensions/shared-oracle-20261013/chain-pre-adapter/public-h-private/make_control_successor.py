from pathlib import Path
HERE=Path(__file__).resolve().parent
original=(HERE/'control.py').read_text(encoding='utf-8')
extra='''# Exercise noncompletion under another FIXED public algorithm, not a side oracle.
original_h = h
h = lambda word: 0
bottom_worlds = 0
for s, k, p in product(range(2), repeat=3):
    expected = (('pre_public_full_h', 0), ('nonwinning_setup',))
    assert source(s, k, p) == expected
    assert bk(s, p, Interface(lambda a: f(s, k, a), None)) == expected
    randomizer_oracle = Interface(lambda i: g(s, p, (i >> 1, i & 1)), None)
    assert bp(s, (0,0), randomizer_oracle) == expected
    assert randomizer_oracle.queries == []
    bottom_worlds += 1
h = original_h

result = {'''
new=original.replace('result = {',extra).replace("'setup_noncompletion_nonwinning_no_pk': True,", "'setup_noncompletion_nonwinning_no_pk': True,\n    'noncompletion_under_second_fixed_h_worlds': bottom_worlds,")
new=new.replace("(HERE / 'CONTROL-RESULTS.json').write_text", "(HERE / 'CONTROL-SUCCESSOR-RESULTS.json').write_text")
(HERE/'control-successor.py').write_text(new,encoding='utf-8')
