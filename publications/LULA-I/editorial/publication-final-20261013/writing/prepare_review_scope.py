from pathlib import Path
import hashlib,json,re
B=Path(__file__).resolve().parent;P=B.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=B/'baseline';baseline.mkdir(exist_ok=True)
inputs=['LULA-I.tex','operating-model.tex','stability-results.tex','comparison-results.tex','replay-results.tex','references.bib','ACADEMIC_STRUCTURE.md']
pins={}
for n in inputs:
    src=P/n;dst=baseline/n
    if dst.exists():assert dst.read_bytes()==src.read_bytes(),n
    else:dst.write_bytes(src.read_bytes())
    pins[n]=sha(src)
skills={}
for name in ['writing-skill','phd-paper-review']:
    root=Path('C:/Users/angel/.agents/skills')/name
    files=[root/'SKILL.md',*sorted((root/'references').glob('*.md'))]
    if name=='writing-skill':files+=sorted((root/'assets').glob('*'))
    skills[name]={str(f.relative_to(root)).replace('\\','/'):sha(f) for f in files if f.is_file()}
out=dict(scope='Read-only complete manuscript prose and all active includes, bibliography entries, inactive root tex tables and academic structure; primary cited publications not reread in this prose pass.',
 manuscript_pins=pins,active_includes=re.findall(r'\\input\{([^}]+)\}',(P/'LULA-I.tex').read_text(encoding='utf-8')),
 skill_pins=skills,writing_reference_nodes=95,writing_assets=7,phd_reference_nodes=24,
 protected='Mathematical statements, algorithms, evidence values, conditional reference-security/honest-cache scope,2^40 use objective, author Note.',
 no_manuscript_edits_authorized_for_this_reviewer=True)
(B/'READ-SCOPE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(paper=P.as_posix(),lines=len((P/'LULA-I.tex').read_text(encoding='utf-8').splitlines()),pins=pins,active_includes=out['active_includes'])))
