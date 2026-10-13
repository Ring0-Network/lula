"""Exact tiny comparisons of full and sparse lifting; no source signing run."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
rows=[]; weighted_cases=0
for q in range(1,5):
    L=2;k=min(17,q);Q=1<<(q-1).bit_length()
    selector_vectors=list(product(range(1,Q+1),repeat=k))
    complete=Counter();nonwinning=0
    # Exogenous uniform4-valued nonce map. Nonce3 means true sourcebottom.
    # Message repetition/new-label choice is adaptive to earlier source nonces.
    for table in product(range(4),repeat=q):
        current=0;next_label=1;seen=[];records=[];failed=False
        for request in range(q):
            if request and table[current]&1:
                current=next_label;next_label+=1
            if current not in seen:seen.append(current)
            R=table[current]
            if R==3:failed=True;break
            records.append((current,R,R&1))
        if failed:nonwinning+=1
        else:complete[(len(seen),tuple(records))]+=1
    source_mass=Fraction(sum(complete.values()),4**q)
    assert source_mass+Fraction(nonwinning,4**q)==1
    for (N,records),weight in complete.items():
        witness_sets={tuple(range(1,N+1)),(1,),(N,)}
        for Wtuple in witness_sets:
            W=set(Wtuple);d=len(W)
            # Full-register/non-abort program requires only witness guesses.
            full=Fraction(1,L**d)
            baseline_abort=Fraction(1,L**N)
            assert full>=Fraction(1,L**k) and baseline_abort>=Fraction(1,L**q)
            sparse_good=0
            for slots in selector_vectors:
                selected=set(slots)&set(range(1,N+1))
                if W<=selected:
                    # One guess per DISTINCT selected new label; duplicates inactive.
                    sparse_good+=L**(q-len(selected))
                    assert len(selected)<=k
            sparse=Fraction(sparse_good,Q**k*L**q)
            assert sparse>=Fraction(1,(Q*L)**k)
            # Particular padded witness selector list has EXACT probabilityQ^-k.
            padded=tuple(sorted(W))+tuple([min(W)]*(k-d))
            assert padded in selector_vectors and set(padded)==W
            weighted_cases+=1
    rows.append({'q':q,'k':k,'Q':Q,'source_completion_mass_unnormalized':str(source_mass),'source_bottom_worlds':nonwinning,'source_nonce_worlds':4**q,'selector_vectors':Q**k,'full_counter_loss_lower':'L^-k','sparse_loss_lower':'(Q*L)^-k'})
result={'scope':'Exact finite coupling/probability controls only, no SHA/source attack or quantum kernel proof','rows':rows,'source_adaptive_history_witness_cases':weighted_cases,'new_label_ordinals_with_repeats':True,'sparse_duplicates_dummy_slots_retained':True,'source_bottom_not_normalized':True,'full_nonabort_needed_guesses_vs_baseline_all_new_guesses':True,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'LIFT-COMPARISON-CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
