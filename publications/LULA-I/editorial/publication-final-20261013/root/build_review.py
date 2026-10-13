"""Compile both authorized mechanism-paper copies and retain complete private logs."""
from pathlib import Path
import hashlib,json,re,subprocess,time
P=Path(__file__).resolve().parents[3]
E=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
for label,directory in [('main',P),('repository',P/'release/paper')]:
    before=sha(directory/'LULA-I.tex')
    for i,command in enumerate([
        ['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex'],
        ['bibtex','LULA-I'],
        ['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex'],
        ['pdflatex','-interaction=nonstopmode','-halt-on-error','LULA-I.tex']]):
        started=time.time()
        run=subprocess.run(command,cwd=directory,capture_output=True,encoding='utf8',errors='replace')
        log=E/f'{label}-build-{i}.txt'
        log.write_text(run.stdout+run.stderr,encoding='utf8')
        row={'copy':label,'command':command,'exit_code':run.returncode,'elapsed_s':time.time()-started,
             'log':log.name,'log_sha256':sha(log)}
        records.append(row)
        if run.returncode:
            (E/'BUILD-CHECKS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf8')
            raise RuntimeError(row)
    assert before==sha(directory/'LULA-I.tex')
    text=(directory/'LULA-I.log').read_text(encoding='utf8',errors='replace')
    critical=re.findall(r'Overfull[^\n]*|(?:LaTeX Warning: )?(?:Citation|Reference)[^\n]*undefined|There were undefined[^\n]*|Label\(s\) may have changed[^\n]*|Emergency stop|Fatal error',text)
    assert not critical,critical
    print(json.dumps({'copy':label,'source_sha256':before,'pdf_sha256':sha(directory/'LULA-I.pdf'),
                      'critical_diagnostics':critical}),flush=True)
(E/'BUILD-CHECKS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf8')
