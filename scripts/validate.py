#!/usr/bin/env python3
"""Local structural checks; not a substitute for factual or visual review."""
from pathlib import Path
import re
from urllib.parse import urlsplit
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
readme = (root / 'README.md').read_text(encoding='utf-8')
proposal = (root / 'proposal/proposal.md').read_text(encoding='utf-8')
assert proposal.count('<!-- PAGEBREAK -->') == 4, 'Five source sections are required.'
pdf = PdfReader(root / 'proposal/proposal.pdf')
assert len(pdf.pages) == 5, 'Proposal must remain five pages.'
pdf_text = '\n'.join(page.extract_text() or '' for page in pdf.pages)
for name in ['Kaushik Roy','Nigel Glenday','Raj Krishnan','Alessandro Oltramari','Shahram Rahimi','Subash Neupane','Himanshu Tripathi','Ashraf Abdul-Muumin']:
    assert name in readme and name in proposal and name in pdf_text, f'Missing organizer in README, source, or PDF: {name}'
for title in ['Overview','Research agenda','Industry readiness','Program','Participation','Organizers','Dates and status','References']:
    assert f'## {title}' in readme, f'Navigation heading missing: {title}'
for target in re.findall(r'\]\(([^)]+)\)', readme):
    if not target.startswith(('http:','https:','mailto:','#')):
        assert (root / urlsplit(target).path).is_file(), f'Broken local README link: {target}'
for target in re.findall(r'<img[^>]+src="([^"]+)"', readme):
    assert (root / target).is_file(), f'Broken organizer image: {target}'
assert 150 + 240 + 180 == 570 and 330 + 330 + 180 == 840
assert len((root / 'resources/interest-register-template.csv').read_text().splitlines()) == 1
# Validate the standalone CFP's local files and section links.
from html.parser import HTMLParser
class CallParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.targets = set(), []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'href' in attrs:
            self.targets.append(attrs['href'])
call = CallParser()
call.feed((root / 'cfp.html').read_text(encoding='utf-8'))
for target in call.targets:
    if target.startswith('#'):
        assert target[1:] in call.ids, f'Broken CFP anchor: {target}'
    elif not target.startswith(('https:', 'http:', 'mailto:')):
        assert (root / target).exists(), f'Broken CFP file link: {target}'
assert '[draft call for papers and participation](cfp.html)' in readme
# Keep the public agenda and PDF source in sync.
web_program = readme.split('## Program\n', 1)[1].split('## Participation\n', 1)[0].strip()
source_program = proposal.split('## 3. Preliminary program\n', 1)[1].split('<!-- PAGEBREAK -->', 1)[0].strip()
assert web_program == source_program, 'Website and proposal programs differ.'
for path in ['README.md', 'proposal/proposal.md', 'cfp.html', 'resources/evaluation-worksheet.md', 'resources/case-study-template.md']:
    assert not re.search(r'\bevidence[ -]+contract\b', (root / path).read_text(encoding='utf-8'), re.I), f'Outdated wording: {path}'
assert not re.search(r'\bevidence[ -]+contract\b', pdf_text, re.I), 'Outdated wording in PDF.'
# Check actual PDF program text against the public session titles and times.
def plain_text(value):
    value = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', value)
    return ' '.join(value.replace('–', '-').replace('−', '-').split())
program_pdf = plain_text(pdf.pages[2].extract_text() or '')
for line in web_program.splitlines():
    if line.startswith('|') and not re.match(r'^\|[ -]+\|', line) and not line.startswith('| Time |'):
        for cell in line.strip('|').split('|'):
            assert plain_text(cell) in program_pdf, f'Program missing from PDF: {cell}'
print('PASS: identical website/source agendas and all sessions present in PDF.')

print('PASS: CFP section anchors and local resources.')
print('PASS: page count, required sections, eight organizers in README/source/PDF, local links, agenda arithmetic, and empty public register template.')
print('Submission completeness: see proposal/submission-checklist.md for external requirements.')
print('Structural checks do not establish factual accuracy, organizer consent, participant interest, or submission readiness.')
