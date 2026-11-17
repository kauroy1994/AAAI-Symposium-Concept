#!/usr/bin/env python3
"""Validate the local EasyChair proposal without publishing its respondent list."""
from pathlib import Path
import argparse,json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,default=ROOT/'private/proposal-submission.md')
parser.add_argument('--pdf',type=Path,default=ROOT/'private/proposal-submission.pdf')
parser.add_argument('--register',type=Path,default=ROOT/'private/participant-interest.json')
args=parser.parse_args()
source=args.source.read_text(encoding='utf-8')
register=json.loads(args.register.read_text(encoding='utf-8'))
reader=PdfReader(args.pdf)
assert len(reader.pages)==5 and source.count('<!-- PAGEBREAK -->')==4
assert re.findall(r'^## ([1-5])\.', source, re.M)==['1','2','3','4','5'], 'Duplicate or out-of-order section headings'
assert len(register['rows'])==65
assert sum(r['interest']=='Yes' for r in register['rows'])==60
assert sum(r['interest']=='Maybe' for r in register['rows'])==5
def plain(value):
    value=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',value)
    return ' '.join(value.replace('–','-').replace('−','-').replace('’',"'").split())
text=plain('\n'.join(p.extract_text() or '' for p in reader.pages))
last=plain(reader.pages[4].extract_text() or '')
interest=source.split('## 5. Participant interest',1)[1]
listed=[]
for line in interest.splitlines():
    if not line.startswith('|') or line.startswith('| Name') or line.startswith('| ---'):continue
    cells=[x.strip() for x in line.strip('|').split('|')]
    assert len(cells)==4
    for name,affiliation in [(cells[0],cells[1]),(cells[2],cells[3])]:
        if name:listed.append((name,affiliation))
expected=[(r['name']+(' (Maybe)' if r['interest']=='Maybe' else ''),r['affiliation']) for r in register['rows']]
assert len(listed)==65 and len(set(listed))==65 and set(listed)==set(expected)
for name,affiliation in expected:
    assert last.count(plain(name))==1, f'Name/status missing or duplicated: {name}'
    assert plain(affiliation) in last, f'Affiliation missing: {affiliation}'
assert '@' not in interest and '@' not in last
public=(ROOT/'proposal/proposal.md').read_text(encoding='utf-8')
web=(ROOT/'README.md').read_text(encoding='utf-8')
program=public.split('## 3. Preliminary program\n',1)[1].split('<!-- PAGEBREAK -->',1)[0].strip()
submission_program=source.split('## 3. Preliminary program\n',1)[1].split('<!-- PAGEBREAK -->',1)[0].strip()
assert program==submission_program
program_pdf=plain(reader.pages[2].extract_text() or '')
for line in program.splitlines():
    if line.startswith('|') and not line.startswith(('| Time','| ---')):
        for cell in line.strip('|').split('|'):
            assert plain(cell) in program_pdf, f'Program cell missing: {cell}'
committee=public.split('## 4.',1)[1].split('<!-- PAGEBREAK -->',1)[0].strip()
assert committee in source
for email in re.findall(r'\*\*Email:\*\* ([^\s.]+@[^\s]+)\.',committee):
    assert email in text,email
assert 'All six organizing committee members and both steering organizers have agreed to serve.' in text
speaker_section=public.split('## 5.',1)[1].split('**Invitations and participation.**',1)[0]
for paragraph in speaker_section.split('\n\n'):
    if paragraph.startswith(('**Nigel Glenday','**Raj Krishnan')):
        assert plain(paragraph.replace('**','')) in text
assert '60 "Yes" and five "Maybe."' in text
public_files=['README.md','cfp.html','proposal/proposal.md','proposal/submission-checklist.md','SOURCES.md']
public_text='\n'.join((ROOT/p).read_text(encoding='utf-8') for p in public_files)
public_pdf=plain('\n'.join(p.extract_text() or '' for p in PdfReader(ROOT/'proposal/proposal.pdf').pages))
for r in register['rows']:
    if r['name'] not in ['Nigel Glenday','Raj Krishnan']:
        assert r['name'] not in public_text and plain(r['name']) not in public_pdf, 'New respondent identity in public copy'
print('PASS: submission has five pages and all 65 unique names/affiliations: 60 Yes, five marked Maybe.')
print('PASS: respondent emails/comments omitted; public files contain aggregate totals and existing speakers only.')
print('PASS: full schedule, both labs, posters, speaker biographies, organizer contacts and agreement retained.')
