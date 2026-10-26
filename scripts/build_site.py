"""Validate committed PDF publications and stage the static asset host."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
assert manifest['editions'], 'Empty publication manifest'
total = 0
seen = set()
for edition in manifest['editions']:
    assert {file['theme'] for file in edition['files']} == {'light', 'dark'}, edition['edition_id']
    assert len({file['pages'] for file in edition['files']}) == 1, edition['edition_id']
    for file in edition['files']:
        path = (ROOT / file['path']).resolve()
        assert path.is_relative_to(ROOT / 'books'), path
        assert path not in seen, path
        seen.add(path)
        assert path.name.endswith(f"-{file['theme']}.pdf"), path
        data = path.read_bytes()
        assert data.startswith(b'%PDF-'), path
        assert len(data) == file['bytes'], path
        assert hashlib.sha256(data).hexdigest() == file['sha256'], path
        total += len(data)
assert total < 1_000_000_000, 'PDF publications exceed the Pages size budget'
site = ROOT / '_site'
site.mkdir(exist_ok=True)
shutil.copytree(ROOT / 'books', site / 'books', dirs_exist_ok=True)
shutil.copy2(ROOT / 'manifest.json', site / 'manifest.json')
(site / '.nojekyll').write_text('', encoding='utf-8')
(site / 'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=https://bookstacks.org/"><title>Bookstacks</title><p><a href="https://bookstacks.org/">Bookstacks</a></p></html>', encoding='utf-8')
print(f'Validated {len(seen)} PDFs ({total:,} bytes) for {len(manifest["editions"])} editions.')
