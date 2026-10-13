"""Abstract keyed-game/policy countermodels; no source crypto or forgery execution."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
OUT=Path(__file__).resolve().parent
def target_family(key,base):
    return key if base==(key^1) else base
def collision_exists(key,base,N):
    return any(v!=base and target_family(key,v)==target_family(key,base) for v in range(N))
rows=[]
for n in [2,3,4,5,6]:
    N=2**n
    # Target fixed before key; all choices are symmetric and have exactly two keys.
    standalone=[]
    for c in range(N):
        hits=sum(collision_exists(p,c,N) for p in range(N))
        assert hits==2
        standalone.append(hits)
    postkey=sum(collision_exists(p,p,N) for p in range(N))
    collection=sum(collision_exists(p,p,N) for p in range(N)) # other-tweak oracle reveals p
    independent=sum(collision_exists(r,p,N) for p in range(N) for r in range(N))
    assert postkey==collection==N and F(independent,N*N)==F(2,N)
    rows.append({'n':n,'N':N,'standalone_prekey_max_success':str(F(max(standalone),N)),
                 'postkey_success':str(F(postkey,N)),
                 'key_revealing_collection_success':str(F(collection,N)),
                 'independent_target_key_success':str(F(independent,N*N))})
def policy_family(base,counter):return 0 if counter==0 else base+1
policies=[]
for chosen in [0,1]:
    outcomes=[]
    for base in [0,1]:
        target=policy_family(base,chosen)
        # All nonzero counters repeat the same value, so these two exhaustive
        # equivalence classes also cover the unbounded nonnegative counter domain.
        collision=any(policy_family(1-base,c)==target for c in [0,1])
        outcomes.append(collision)
    policies.append({'chosen_counter':chosen,'target_always_satisfies_Prop':True,
                     'success':str(F(sum(outcomes),2))})
assert policies[0]['success']=='1' and policies[1]['success']=='0'
lo=sum(2**e for e in [41,36,31,26]); top=2**21
assert lo==2269957324800 and lo+top==2269959421952 and lo<2**42
out={'status':'PASS_ABSTRACT_PREKEY_COLLECTION_SHARED_KEY_AND_COUNTER_POLICY_SEPARATIONS',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'standalone_postkey_collection_rows':rows,'counter_policy_rows':policies,
     'conditional_wrapper_counts':{'lower_rows':lo,'lower_pad':2**42,'top_rows':top,'top_pad':top},
     'scope':'Abstract game countermodels only; no source attack, no SHA hardness or signing-category verdict.'}
(OUT/'COUNTERMODEL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'key_sizes':len(rows),'policy_successes':[p['success'] for p in policies]}))
