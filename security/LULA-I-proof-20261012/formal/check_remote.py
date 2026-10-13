"""Check only abstract, nonsecret source on the configured AXLE service."""
from pathlib import Path
import asyncio, json, hashlib, dataclasses
from axle import AxleClient

BASE = Path(__file__).resolve().parent
async def main():
    source = (BASE / 'LulaLemmas.lean').read_text(encoding='utf-8')
    client = AxleClient(base_timeout_seconds=150, max_concurrency=1)
    try:
        result = await client.check(content=source, environment='lean-4.28.0', ignore_imports=False, timeout_seconds=120)
        body = dataclasses.asdict(result)
    except Exception as e:
        body = {'available':False, 'exception_type':type(e).__name__, 'message':str(e)[:1000]}
    finally:
        await client.close()
    body['source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
    (BASE / 'axle-check.json').write_text(json.dumps(body, indent=2), encoding='utf-8')
    print(json.dumps(body, indent=2))

if __name__ == '__main__': asyncio.run(main())
