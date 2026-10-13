"""Independent tiny ordinary-source and stopped-cut controls; no cryptographic runs."""
from itertools import product
from pathlib import Path
import hashlib, json

OUT=Path(__file__).resolve().parent
N=2
words=list(product(range(N), repeat=2))
funcs=list(product(words, repeat=N))
worlds=list(product(range(N), funcs, funcs))
assert len(worlds)==512
rows=[]
for policy in range(3):
    source_events=0
    selected_wins=[0,0]
    coupled_selected_first=0
    lower_limb_replies=0
    for start,f0,f1 in worlds:
        values=[start, f0[start][0]]
        endpoint=f1[values[1]][0]
        functions=[f0,f1]
        # Two pre-key queries, then endpoint-only setup and one atomic disclosure,
        # then adaptive post-key/final candidates using complete earlier replies.
        q0=(policy%2, (policy//2)%2)
        r0=functions[q0[0]][q0[1]]
        q1=(1-q0[0],r0[1])
        r1=functions[q1[0]][q1[1]]
        digit=(endpoint+r1[0]+policy)%3
        stream=[('q',q0),('q',q1),('disclose',digit),
                ('q',(1,endpoint)),('q',(0,r1[0])),('q',(1,r0[1]))]
        exposed=[False,False]
        first=None
        for index,(kind,data) in enumerate(stream):
            if kind=='disclose':
                exposed=[p>=data for p in range(2)]
            else:
                p,z=data
                if not exposed[p] and z==values[p]:
                    first=(index,p)
                    break
        source_events+=first is not None
        for selected in range(2):
            target=functions[selected][values[selected]]
            won=False
            for index,(kind,data) in enumerate(stream):
                if kind=='disclose':
                    if data<=selected:
                        break
                    continue
                p,z=data
                if selected==1 and p==0 and z==start:
                    break  # Unknown predecessor image is never answered.
                reply=functions[p][z]
                if p==selected and reply==target:
                    won=True
                    break  # Full-image challenge succeeds before source reply.
                lower_limb_replies+=1
                if first and first[1]==selected:
                    assert index<first[0], 'selected genuine first hit was bypassed'
            selected_wins[selected]+=won
            if first and first[1]==selected:
                assert won, 'source first hit lost despite selected coordinate'
                coupled_selected_first+=1
    assert sum(selected_wins)>=source_events
    assert coupled_selected_first==source_events
    rows.append({'policy':policy,'worlds':512,'source_events':source_events,
                 'selected_success_sum':sum(selected_wins),
                 'selected_first_hit_couplings':coupled_selected_first,
                 'complete_response_reads_before_stops':lower_limb_replies})

# Independent prefix/lower-limb factorization: every full two-point function has
# exactly one pair of prefix and lower-limb functions; source target lower limb
# is irrelevant to any query surviving the prefix-match success stop.
prefixfuncs=list(product(range(N),repeat=N))
full_factorized={tuple((f[i],r[i]) for i in range(N)) for f,r in product(prefixfuncs,prefixfuncs)}
assert full_factorized==set(funcs)
prefix_survival_checks=0
for x,f,r in product(range(N),prefixfuncs,prefixfuncs):
    target=f[x]
    for z in range(N):
        if f[z]!=target:
            assert z!=x
            prefix_survival_checks+=1

w=480*(2**41+2**36+2**31+2**26)+4080*2**21
f=2**41*17*512
assert w+f==20229886488608768 and 2**54<w+f<2**55
assert 17+4*(32*15-240)+(16*255-2040)==3017
qrows=[]
L=2**32
setup=2**21*(19505+L)-1
for exponent in [24,30,38,40,41,44,50,64]:
    q=2**exponent
    qrows.append({'q_exponent':exponent,'hot_honest_public_plus_254':setup+q*(82090+5*L)+3224+254,
                 'cold_honest_public_plus_254':setup+q*(8560574463+82090+6*L)+3224+254,
                 'hot_F_distinct_cap':min(19212937084272640,1+2181038080+q*12816),
                 'cold_F_distinct_cap':min(19212937084272640,1+2181038080+q*33567232)})
result={'status':'PASS_SCOPED_ORDINARY_WORLD_STOPPED_PREFIX_AND_RESOURCE_CONTROLS',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'ordinary_worlds':512,'prekey_atomic_disclosure_postkey_policies':rows,
        'prefix_fullword_factorization_functions':len(full_factorized),
        'prefix_survival_checks':prefix_survival_checks,
        'protected_namespace':w+f,'padded_selector_loss':2**55,
        'selected_handle_cap':'Q_H+1','public_cap':'Q_H+H_setup+q*H_mode+3224+254',
        'q_resource_rows':qrows,
        'scope':'Finite controls only, not a complete source, conventional primitive or quantum theorem.'}
(OUT/'PRE-CONTROL-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'worlds':512,'policies':len(rows),'q_resource_rows':len(qrows)}))
