from pathlib import Path
import hashlib,json,subprocess

E=Path(__file__).resolve().parent
source=E/'SeedGuess.ec'
linux='/mnt/'+source.drive[0].lower()+str(source)[2:].replace('\\','/')
cmd=['wsl','-d','Ubuntu-24.04','--','/root/.opam/ec/bin/easycrypt','compile','-no-eco','-p','Z3',linux]
r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf8',timeout=120)
receipt={'command':cmd,'exit_code':r.returncode,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'stdout':r.stdout,'stderr':r.stderr}
attempt=E/'attempts'/receipt['source_sha256'];attempt.mkdir(parents=True,exist_ok=True)
(attempt/'SeedGuess.ec').write_bytes(source.read_bytes())
(attempt/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
(E/'easycrypt-current.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
(E/'easycrypt-current.log').write_text(r.stdout+r.stderr,encoding='utf8')
print(json.dumps({'exit_code':r.returncode,'diagnostics':(r.stdout+r.stderr)[-2800:],'source_sha256':receipt['source_sha256']}))
raise SystemExit(r.returncode)
