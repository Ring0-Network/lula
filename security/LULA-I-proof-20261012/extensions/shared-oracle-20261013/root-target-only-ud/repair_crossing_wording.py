from pathlib import Path
import hashlib,json
X=Path(__file__).resolve().parent.parent
path=X/'TARGET-PRE-PROMOTION.json'
data=json.loads(path.read_text(encoding='utf8'))
old='Exact adjacent component-envelope crossings are pass99/fail100 at1/2 and pass200/fail201 at1.'
new='Exact adjacent UNCAPPED component-expression crossings are pass99/fail100 at1/2 and pass200/fail201 at1; the capped probability envelope never exceeds1.'
for name,expected in data['documents'].items():
    p=X/name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,name
    text=p.read_text(encoding='utf8')
    assert text.count(old)==1,name
    p.write_text(text.replace(old,new),encoding='utf8')
    data['documents'][name]=hashlib.sha256(p.read_bytes()).hexdigest()
path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
template=X/'root-promote-target-pre.py'
text=template.read_text(encoding='utf8')
assert text.count(old)==1
template.write_text(text.replace(old,new),encoding='utf8')
print(json.dumps({'repaired_documents':len(data['documents']),'numerical_changes':0,'predecessor_backups_changed':False}))
