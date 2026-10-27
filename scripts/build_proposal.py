#!/usr/bin/env python3
"""Build the five-page proposal from its editable Markdown source.

Supported source constructs: headings, paragraphs, simple links/bold/italics,
pipe tables, and explicit PAGEBREAK markers. No network access is needed.
"""
from __future__ import annotations
import html
import re
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'proposal' / 'proposal.md'
OUTPUT = ROOT / 'proposal' / 'proposal.pdf'
CRIMSON = colors.HexColor('#9E1B32')
INK = colors.HexColor('#252A31')


def inline(text: str) -> str:
    text = text.replace('–', '-').replace('—', '-').replace('−', '-').replace('’', "'").replace('“', '"').replace('”', '"')
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', lambda m: '<link href="' + html.escape(html.unescape(m[2]), quote=True) + '" color="#9E1B32">' + m[1] + '</link>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return text


def build() -> None:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='BodyR2R', fontName='Times-Roman', fontSize=10.2, leading=12.6, textColor=INK, spaceAfter=7, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='TitleR2R', fontName='Helvetica-Bold', fontSize=23, leading=27, textColor=CRIMSON, spaceAfter=10))
    styles.add(ParagraphStyle(name='H2R2R', fontName='Helvetica-Bold', fontSize=12.4, leading=15.5, textColor=CRIMSON, spaceBefore=8, spaceAfter=8, keepWithNext=True))
    styles.add(ParagraphStyle(name='H3R2R', fontName='Helvetica-Bold', fontSize=10.3, leading=13, textColor=INK, spaceBefore=8, spaceAfter=6, keepWithNext=True))
    styles.add(ParagraphStyle(name='TableR2R', fontName='Helvetica', fontSize=8.4, leading=10.3, textColor=INK))
    styles.add(ParagraphStyle(name='TableHeadR2R', parent=styles['TableR2R'], fontName='Helvetica-Bold', textColor=colors.white))
    styles.add(ParagraphStyle(name='RefR2R', parent=styles['BodyR2R'], fontSize=8.7, leading=10.3, spaceAfter=4))
    story = []
    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    i, in_refs = 0, False
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '<!-- PAGEBREAK -->':
            story.append(PageBreak())
            in_refs = False
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                raw = [v.strip() for v in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', v.replace(' ', '')) for v in raw):
                    style = styles['TableHeadR2R'] if not rows else styles['TableR2R']
                    rows.append([Paragraph(inline(v), style) for v in raw])
                i += 1
            width = letter[0] - 100
            widths = [115, width - 115] if len(rows[0]) == 2 else [width / len(rows[0])] * len(rows[0])
            table = Table(rows, colWidths=widths, repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),CRIMSON),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,0),(-1,-1),.35,colors.HexColor('#DCE0E3')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F5F3')])]))
            story += [table, Spacer(1,7)]
            continue
        if line.startswith('# '):
            story.append(Paragraph(inline(line[2:]), styles['TitleR2R']))
        elif line.startswith('## '):
            story.append(Paragraph(inline(line[3:]), styles['H2R2R']))
        elif line.startswith('### '):
            in_refs = line[4:] == 'Selected references'
            story.append(Paragraph(inline(line[4:]), styles['H3R2R']))
        else:
            para = [line]
            while i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith(('#','|','<!-- PAGEBREAK -->')):
                i += 1
                para.append(lines[i].strip())
            story.append(Paragraph(inline(' '.join(para)), styles['RefR2R'] if in_refs else styles['BodyR2R']))
        i += 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temp = OUTPUT.with_name('proposal.build.pdf')
    doc = SimpleDocTemplate(str(temp), pagesize=letter, rightMargin=50, leftMargin=50, topMargin=43, bottomMargin=42, title='Reasoning to Readiness - AAAI 2027 Spring Symposium Proposal', author='Proposed organizing committee', subject='Organizer-review draft; outstanding confirmations documented within', pageCompression=1)
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(CRIMSON)
        canvas.setLineWidth(.7)
        canvas.line(50, 31, 562, 31)
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(colors.HexColor('#515C65'))
        canvas.drawString(50, 20, 'R2R | AAAI Spring Symposium 2027 | Organizer-review draft | 27 October 2026')
        canvas.drawRightString(562, 20, f'{doc.page} / 5')
        canvas.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    reader = PdfReader(temp)
    if len(reader.pages) != 5:
        raise RuntimeError(f'Expected 5 pages; generated {len(reader.pages)}. Adjust source/layout and rebuild. Candidate: {temp}')
    for n, page in enumerate(reader.pages, 1):
        if not (page.extract_text() or '').strip():
            raise RuntimeError(f'Blank page {n}')
    temp.replace(OUTPUT)
    print(f'Built {OUTPUT}: 5 pages')


if __name__ == '__main__':
    build()
