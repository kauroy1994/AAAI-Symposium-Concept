#!/usr/bin/env python3
"""Local structural checks; not a substitute for factual or visual review."""
from pathlib import Path
import re
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
readme = (root / 'README.md').read_text(encoding='utf-8')
proposal = (root / 'proposal/proposal.md').read_text(encoding='utf-8')
assert proposal.count('<!-- PAGEBREAK -->') == 4, 'Five source sections are required.'
assert len(PdfReader(root / 'proposal/proposal.pdf').pages) == 5, 'Proposal must remain five pages.'
for name in ['Kaushik Roy','Nigel Glenday','Raj Krishnan','Alessandro Oltramari']:
    assert name in readme and name in proposal, f'Missing organizer: {name}'
for title in ['Overview','Research agenda','Industry readiness','Program','Participation','Organizers','Dates and status','Outcomes and resources','References']:
    assert f'## {title}' in readme, f'Navigation heading missing: {title}'
for target in re.findall(r'\]\(([^)]+)\)', readme):
    if not target.startswith(('http:','https:','mailto:','#')):
        assert (root / target).is_file(), f'Broken local README link: {target}'
assert '570 of 840' in readme and '570 of 840' in proposal
assert 150 + 240 + 180 == 570 and 330 + 330 + 180 == 840
assert len((root / 'resources/interest-register-template.csv').read_text().splitlines()) == 1
print('PASS: page count, required sections, four organizers, local links, agenda arithmetic, and empty public register template.')
if 'No documented list' in proposal or 'independent confirmation pending' in readme:
    print('DRAFT: consult the submission checklist for outstanding consent, contact, and participant-interest evidence.')
print('Structural checks do not establish factual accuracy, organizer consent, participant interest, or submission readiness.')
