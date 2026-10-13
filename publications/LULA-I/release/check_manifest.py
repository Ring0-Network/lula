"""Check the shipped byte manifest. SPDX-License-Identifier: Apache-2.0"""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
GENERATED={'recomputed','generated','reruns','build','output','.git','__pycache__'}
def shipped_paths():
    return {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(x in GENERATED for x in p.relative_to(ROOT).parts) and not (p.parent==ROOT/'paper' and p.suffix in {'.aux','.log','.out','.toc','.blg','.fls','.synctex'})}
def main():
    checked=[]
    for name in ['EVIDENCE-MANIFEST.sha256','MANIFEST.sha256']:
        count=0; listed=set()
        for line in (ROOT/name).read_text(encoding='utf8').splitlines():
            digest,rel=line.split('  ',1)
            path=(ROOT/rel).resolve()
            assert path.is_relative_to(ROOT.resolve()),rel
            assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,rel
            assert rel not in listed,rel
            listed.add(rel)
            count+=1
        if name=='MANIFEST.sha256': assert shipped_paths()-{'MANIFEST.sha256'}==listed, 'Unlisted or missing shipped file'
        checked.append({'manifest':name,'files':count,'status':'PASS'})
    print(json.dumps(checked))
if __name__=='__main__':main()
