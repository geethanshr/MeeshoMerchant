"""Package the local app as one offline HTML file plus a source ZIP. No dependencies."""
from pathlib import Path
import base64
import zipfile

root = Path(__file__).resolve().parent
out = root.parent / 'outputs' / 'merchant-demo' if root.name == 'merchant-demo' else root / 'dist'
out.mkdir(parents=True, exist_ok=True)
html = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'styles.css').read_text(encoding='utf-8')
js = (root / 'app.js').read_text(encoding='utf-8')
for name, mime in [('products.png', 'image/png'), ('nunito-sans.woff2', 'font/woff2')]:
    uri = 'data:' + mime + ';base64,' + base64.b64encode((root / 'assets' / name).read_bytes()).decode()
    css = css.replace('assets/' + name, uri)
license_text = (root / 'assets' / 'FONT-LICENSE.txt').read_text(encoding='utf-8')
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + css + '</style>')
html = html.replace('<script defer src="app.js"></script>', '')
html = html.replace('</body>', '<script>' + js + '</script></body>')
html = html.replace('</head>', '<!-- Locally embedded Nunito Sans; SIL Open Font License.\n' + license_text.replace('--', '—') + '\n--></head>')
single = out / 'Meesho_Merchant_Demo.html'
single.write_text(html, encoding='utf-8')
archive = out / 'Meesho_Merchant_Demo.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(single, single.name)
    for name in ['README.md', 'DESIGN.md', 'index.html', 'styles.css', 'app.js', 'server.mjs', 'build-demo.py', 'package.json']:
        z.write(root / name, 'source/' + name)
    for p in (root / 'assets').iterdir():
        if p.is_file():
            z.write(p, 'source/assets/' + p.name)
    for p in (root / 'tests').iterdir():
        if p.is_file() and p.name in ('demo.test.cjs', 'quantity.test.cjs', 'offline.test.cjs', 'results.json', 'quantity-results.json', 'offline-results.json', 'standalone-results.json'):
            z.write(p, 'source/tests/' + p.name)
    sidecar = root / '.impeccable' / 'design.json'
    if sidecar.exists():
        z.write(sidecar, 'source/.impeccable/design.json')
    for name in ['results.json', 'quantity-results.json', 'offline-results.json', 'standalone-results.json']:
        z.write(root / 'tests' / name, 'verification/' + name)
print(f'Created {single.name} ({single.stat().st_size:,} bytes) and {archive.name}')
