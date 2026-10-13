"""Rerun scoped controls and store actual command/exit/source receipts."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
import sys

X=Path(__file__).resolve().parent
O=X/'root-checks/runs'
O.mkdir(parents=True,exist_ok=True)
def run(rel):
    source=X/rel
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    cmd=[sys.executable,'-I','-B',str(source)]
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf8',timeout=120)
    assert before==hashlib.sha256(source.read_bytes()).hexdigest(), 'Control source changed while running'
    record={'command':cmd,'exit_code':p.returncode,'source_sha256':before,'stdout':p.stdout,'stderr':p.stderr}
    (O/(str(Path(rel).parent)+'.json')).write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
    assert p.returncode==0,(rel,p.stderr)
    return {'script':rel,'exit_code':p.returncode,'source_sha256':before}
paths=['graph-targets/control.py','fors-source-bridge/bridge_checks.py',
       'fors-source-second-reader/expected_cap_counterexample.py']
with ThreadPoolExecutor(max_workers=3) as pool:
    for result in pool.map(run,paths):
        print(json.dumps(result))
