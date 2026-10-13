"""Independent check and statement comparison of abstract nonsecret mathematics."""
from pathlib import Path
import asyncio, dataclasses, hashlib, json, re
from axle import AxleClient
BASE=Path(__file__).resolve().parent

async def main():
    source=(BASE/'AddressedMerkle.lean').read_text(encoding='utf-8')
    pattern=re.compile(r'(?ms)^(theorem\s+(\w+).*?) := by\n(.*?)(?=^\S|\Z)')
    declarations=[{'name':name,'signature':signature} for signature,name,proof in pattern.findall(source)]
    assert len(declarations)==5
    statement={'declarations':declarations,'scope':'Selected explicit theorem statements; definitions/context preserved in comparator template',
               'context_source_sha256':hashlib.sha256(source.encode()).hexdigest()}
    statement_path=BASE/'STATEMENTS.json'
    if statement_path.exists():
        previous=json.loads(statement_path.read_text(encoding='utf-8'))
        assert previous['declarations']==declarations, 'A theorem statement changed'
    else:
        statement_path.write_text(json.dumps(statement,indent=2),encoding='utf-8')
    formal=pattern.sub(lambda m:m[1]+' := by sorry\n\n',source)
    # The placeholder template is for comparison only; not a proved artifact.
    client=AxleClient(base_timeout_seconds=150,max_concurrency=1)
    try:
        check=await client.check(content=source,environment='lean-4.28.0',ignore_imports=False,timeout_seconds=120)
        compare=await client.verify_proof(formal_statement=formal,content=source,environment='lean-4.28.0',ignore_imports=False,timeout_seconds=120)
        rec={'check':dataclasses.asdict(check),'statement_comparison':dataclasses.asdict(compare),
             'transmitted_source_sha256':hashlib.sha256(source.encode()).hexdigest(),
             'statement_only_sha256':hashlib.sha256(statement_path.read_bytes()).hexdigest(),
             'compare_template_contains_placeholders_only':True}
        (BASE/'axle.json').write_text(json.dumps(rec,indent=2),encoding='utf-8')
        print(json.dumps({'check':check.okay,'statement_comparison':compare.okay,'errors':check.lean_messages.errors,'comparison_errors':compare.tool_messages.errors,'infos':check.lean_messages.infos},indent=2))
        if not check.okay or not compare.okay: raise SystemExit(1)
    finally: await client.close()
if __name__=='__main__':asyncio.run(main())
