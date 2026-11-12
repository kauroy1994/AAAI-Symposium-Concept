#!/usr/bin/env python3
"""Check roster roles, program consistency, links, and the generated PDF."""
from pathlib import Path
from urllib.parse import urlsplit
from html.parser import HTMLParser
import re
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
readme = (root / 'README.md').read_text(encoding='utf-8')
proposal = (root / 'proposal/proposal.md').read_text(encoding='utf-8')
cfp = (root / 'cfp.html').read_text(encoding='utf-8')
pdf = PdfReader(root / 'proposal/proposal.pdf')
assert len(pdf.pages) == 5, 'Proposal must remain five pages.'
assert proposal.count('<!-- PAGEBREAK -->') == 4
pdf_text = '\n'.join(page.extract_text() or '' for page in pdf.pages)
organizers = ['Kaushik Roy', 'Shahram Rahimi', 'Subash Neupane', 'Noorbakhsh Amiri Golilarz', 'Himanshu Tripathi', 'Ashraf Abdul-Muumin']
speakers = ['Nigel Glenday', 'Raj Krishnan']
advisers = ['Alessandro Oltramari', 'Amit Sheth']
web_organizer_section = readme.split('## Organizers\n', 1)[1].split('## Dates and status\n', 1)[0]
web_organizers = web_organizer_section.split('### Advisory Committee\n', 1)[0]
web_advisers = web_organizer_section.split('### Advisory Committee\n', 1)[1]
web_speakers = readme.split('## Speakers\n', 1)[1].split('## Organizers\n', 1)[0]
source_section4 = proposal.split('## 4.', 1)[1].split('<!-- PAGEBREAK -->', 1)[0]
source_organizers = source_section4.split('### Advisory Committee', 1)[0]
source_advisers = source_section4.split('### Advisory Committee', 1)[1].split('### Submissions', 1)[0]
pdf_section4 = pdf.pages[3].extract_text()
pdf_organizers = pdf_section4.split('Advisory Committee', 1)[0]
pdf_advisers = pdf_section4.split('Advisory Committee', 1)[1].split('Submissions, review, and presentation', 1)[0]
source_speakers = proposal.split('## 5.', 1)[1]
for name in organizers:
    assert all(name in text for text in [web_organizers, source_organizers, pdf_organizers]), f'Organizer missing: {name}'
    assert name not in web_speakers, f'Organizer wrongly listed as speaker: {name}'
for name in advisers:
    assert all(name in text for text in [web_advisers, source_advisers, pdf_advisers, cfp]), f'Adviser missing: {name}'
    assert all(name not in text for text in [web_organizers, source_organizers, pdf_organizers, web_speakers]), f'Adviser listed in another role: {name}'
assert web_advisers.count('class="person-card advisor-card"') == 2
assert 'amit@sc.edu' in pdf_advisers and 'aoltrama@andrew.cmu.edu' in pdf_advisers
for name in speakers:
    assert all(name in text for text in [web_speakers, source_speakers, cfp, pdf.pages[4].extract_text()]), f'Speaker bio missing: {name}'
    assert all(name not in text for text in [web_organizers, source_organizers, pdf.pages[3].extract_text()]), f'Speaker still listed as organizer: {name}'
assert 'namirigolilarz@ua.edu' in web_organizers and 'namirigolilarz@ua.edu' in pdf.pages[3].extract_text()
assert 'Noorbakhsh Amiri Golilarz' in cfp
assert web_organizers.count('class="person-card"') == 6
assert web_speakers.count('class="person-card speaker-card"') == 2
for title in ['Overview', 'Research agenda', 'Industry readiness', 'Program', 'Participation', 'Speakers', 'Organizers', 'Dates and status', 'References']:
    assert f'## {title}' in readme, f'Missing section: {title}'
assert 'outcomes-and-resources' not in (root / '_layouts/default.html').read_text(encoding='utf-8')
assert 'href="#speakers"' in (root / '_layouts/default.html').read_text(encoding='utf-8')
for target in re.findall(r'\]\(([^)]+)\)', readme):
    if not target.startswith(('http:', 'https:', 'mailto:', '#')):
        assert (root / urlsplit(target).path).is_file(), f'Broken README link: {target}'
for target in re.findall(r'<img[^>]+src="([^"]+)"', readme):
    assert (root / target).is_file(), f'Broken portrait: {target}'
assert len((root / 'resources/interest-register-template.csv').read_text().splitlines()) == 1

class CallParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.targets = set(), []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if 'href' in attrs: self.targets.append(attrs['href'])
call = CallParser()
call.feed(cfp)
for target in call.targets:
    if target.startswith('#'):
        assert target[1:] in call.ids, f'Broken call anchor: {target}'
    elif not target.startswith(('https:', 'http:', 'mailto:')):
        assert (root / urlsplit(target).path).exists(), f'Broken call link: {target}'

web_program = readme.split('## Program\n', 1)[1].split('## Participation\n', 1)[0].strip()
source_program = proposal.split('## 3. Preliminary program\n', 1)[1].split('<!-- PAGEBREAK -->', 1)[0].strip()
assert web_program == source_program, 'Website and proposal programs differ.'
day_minutes = []
for day in web_program.split('### ')[1:]:
    minutes, previous_end = 0, 0
    for start, end, session in re.findall(r'^\| (\d{2}:\d{2})[–-](\d{2}:\d{2}) \| (.+) \|$', day, re.M):
        start_min = int(start[:2]) * 60 + int(start[3:])
        end_min = int(end[:2]) * 60 + int(end[3:])
        assert start_min >= previous_end and end_min > start_min, 'Overlapping or invalid sessions.'
        previous_end = end_min
        if not any(word in session.lower() for word in ['coffee break', 'lunch', 'aaai series']):
            minutes += end_min - start_min
    day_minutes.append(minutes)
assert day_minutes == [330, 330, 180], f'Incomplete timetable: {day_minutes}'
monday = web_program.split('### Monday', 1)[1].split('### Tuesday', 1)[0]
tuesday = web_program.split('### Tuesday', 1)[1].split('### Wednesday', 1)[0]
assert re.search(r'09:20–10:00 \| .*Nigel Glenday', monday)
assert re.search(r'09:00–09:40 \| .*Raj Krishnan', tuesday)
assert '14:00–15:30 | Lab 1:' in monday
assert '11:00–12:30 | Lab 2:' in tuesday
assert '16:00–17:00 | Poster session:' in tuesday

def plain_text(value):
    value = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', value)
    return ' '.join(value.replace('–', '-').replace('−', '-').split())
program_pdf = plain_text(pdf.pages[2].extract_text() or '')
for line in web_program.splitlines():
    if line.startswith('|') and not re.match(r'^\|[ -]+\|', line) and not line.startswith('| Time |'):
        for cell in line.strip('|').split('|'):
            assert plain_text(cell) in program_pdf, f'Program entry missing from PDF: {cell}'
for path in ['README.md', 'proposal/proposal.md', 'cfp.html', 'resources/case-study-template.md']:
    text = (root / path).read_text(encoding='utf-8')
    assert 'poster session' in text.lower(), f'Poster policy missing: {path}'
    assert 'without a presentation slot' not in text.lower(), f'Outdated poster policy: {path}'
for text in [readme, proposal, cfp, pdf_text]:
    assert not re.search(r'\bevidence[ -]+contract\b', text, re.I), 'Outdated terminology.'
    assert 'speakers have not yet been confirmed' not in text.lower(), 'Outdated speaker status.'
assert 'Lab 1' in cfp and 'Lab 2' in cfp
# Keep the reported expressions of interest inside the submitted document.
interest_list = proposal.split('### Participant interest\n', 1)[1].split('**Relationship to existing meetings.**', 1)[0]
for name, affiliation in [('Nigel Glenday', 'Graphite Atlas'), ('Raj Krishnan', 'AI For Services')]:
    assert name in interest_list and affiliation in interest_list, f'Missing interested participant: {name}'
    assert name in pdf.pages[0].extract_text() and affiliation in pdf.pages[0].extract_text(), f'Interest list missing from PDF: {name}'
assert 'Participant interest' in pdf.pages[0].extract_text()
# Keep development notes and boilerplate off public pages and out of the PDF.
boilerplate = [
    r'about this website', r'maintainers:', r'photo credits', r'photographs:',
    r'github pages renders', r'privacy safeguards', r'ua-inspired colors',
    r'provided by the organizing team', r'supplied by the organizing team',
    r'sources checked', r'as confirmed by the lead organizer',
    r'maintained by the', r'provenance record'
]
for label, content in [('homepage', readme), ('call', cfp), ('layout', (root / '_layouts/default.html').read_text(encoding='utf-8')), ('proposal', proposal), ('PDF', pdf_text)]:
    for pattern in boilerplate:
        assert not re.search(pattern, content, re.I), f'Boilerplate on {label}: {pattern}'
assert 'MAINTAINING.md' not in readme and 'PHOTO-SOURCES.md' not in readme
assert 'Acceptance pending' in (root / '_layouts/default.html').read_text(encoding='utf-8')
print('PASS: public pages and PDF contain no development or provenance boilerplate.')

print('PASS: both confirmed expressions of interest are included in the PDF.')

print('PASS: six organizers, two advisers, and two speakers, in the correct sections, with biographies.')
print('PASS: both labs, poster session, speaker assignments, full timetable, and no overlaps.')
print('PASS: identical website/source programs and every session present in the PDF.')
print('PASS: five pages, valid local links and portraits, CFP anchors, and private-register template.')
print('Submission requirements still open are listed in proposal/submission-checklist.md.')
