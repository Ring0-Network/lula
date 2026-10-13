"""Build the actual source archive in an isolated directory; never touch delivered PDFs."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
import fitz
P=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent
D=E/'source-archive-build'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={name:sha(P/name) for name in ('LULA-I.tex','LULA-I.pdf','LULA-I-source.zip','LULA-I-release.zip')}
D.mkdir(exist_ok=True)
with zipfile.ZipFile(P/'LULA-I-source.zip') as z:
    assert all(Path(name).name==name for name in z.namelist())
    z.extractall(D)
commands=[['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex'],['bibtex','LULA-I'],
          ['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex'],
          ['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex']]
rows=[]
for i,cmd in enumerate(commands):
    run=subprocess.run(cmd,cwd=D,capture_output=True,encoding='utf8',errors='replace')
    log=D/f'isolated-build-{i}.txt';log.write_text(run.stdout+run.stderr,encoding='utf8')
    rows.append({'command':cmd,'exit_code':run.returncode,'log_sha256':sha(log)})
    assert run.returncode==0,rows[-1]
def pages(path):
    doc=fitz.open(path)
    return [page.get_text() for page in doc]
assert pages(D/'LULA-I.pdf')==pages(P/'LULA-I.pdf')
assert before=={name:sha(P/name) for name in before}
log=(D/'LULA-I.log').read_text(encoding='utf8',errors='replace')
assert not re.search(r'Overfull|There were undefined|Label\(s\) may have changed|Emergency stop|Fatal error',log)
record={'status':'PASS_ISOLATED_SOURCE_ARCHIVE_BUILD','source_archive_sha256':before['LULA-I-source.zip'],
        'delivered_files_unchanged':before,'commands':rows,'pages':len(pages(D/'LULA-I.pdf')),
        'every_page_extracted_text_exactly_matches_submission_pdf':True}
(E/'SOURCE-ARCHIVE-CHECK.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps(record))
