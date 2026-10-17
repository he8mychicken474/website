from pypdf import PdfReader
from pathlib import Path

pdf = Path('assets/files/resume_core.pdf')
out = Path('resume_text.txt')
reader = PdfReader(str(pdf))
texts = []
for p in reader.pages:
    t = p.extract_text()
    if t:
        texts.append(t)

out.write_text('\n\n'.join(texts), encoding='utf-8')
print('WROTE', out)
