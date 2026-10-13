from pathlib import Path
import asyncio, json
from aristotlelib import Project, ProjectStatus

BASE = Path(__file__).resolve().parent
PROMPT = '''Produce a small standalone Lean 4 file importing Mathlib with namespace IndependentLula.
Prove exactly:
theorem fixed_sum_antichain {x y : List Nat}
 (hle : List.Forall₂ (· ≤ ·) x y) (hs : x.sum = y.sum) : x = y
Do not weaken this statement or add assumptions. No axioms, sorry, admit or native_decide.
Include #print axioms IndependentLula.fixed_sum_antichain. An induction on Forall₂ and sum monotonicity suffices.
This is only abstract nonsecret mathematics, not a cryptographic security proof.
Save the completed source as IndependentLula.lean. Record the exact Lean/Mathlib version used.'''

async def main():
    import sys
    if len(sys.argv) == 1:
        p = await Project.create(PROMPT)
        record = {'project_id': str(p.project_id), 'status':str(p.status), 'prompt':PROMPT}
        (BASE/'aristotle-project.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
        print(json.dumps(record,indent=2))
    else:
        rec=json.loads((BASE/'aristotle-project.json').read_text())
        p=await Project.from_id(rec['project_id'])
        await p.refresh()
        print('Status:',p.status)
        (BASE/'aristotle-status.json').write_text(p.model_dump_json(indent=2),encoding='utf-8')
        if p.status == ProjectStatus.IDLE:
            dest=await p.get_files(destination=BASE/'aristotle-returned')
            print('Files:',dest)
if __name__=='__main__': asyncio.run(main())
