"""Gera o PDF do relatório simples a partir do Markdown desta pasta."""
from pathlib import Path
import re
from xml.sax.saxutils import escape

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
)

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Relatorio_Grupo4.md"
OUTPUT = ROOT / "Relatorio_Grupo4.pdf"
FONT_DIR = Path("C:/Windows/Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(FONT_DIR / "arialbd.ttf")))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold")

INK = colors.HexColor("#243746")
BLUE = colors.HexColor("#123F5D")
TEAL = colors.HexColor("#157C80")
WIDTH, HEIGHT = A4
CONTENT_WIDTH = WIDTH - 84

styles = {
    "title": ParagraphStyle("title", fontName="Arial-Bold", fontSize=18,
                            leading=22, textColor=BLUE, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName="Arial-Bold", fontSize=12.5,
                         leading=16, textColor=BLUE, spaceBefore=12, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName="Arial-Bold", fontSize=10.5,
                         leading=13, textColor=TEAL, spaceBefore=10, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Arial", fontSize=9.4,
                           leading=13.2, textColor=INK, spaceAfter=7),
    "caption": ParagraphStyle("caption", fontName="Arial", fontSize=8.3,
                              leading=11, textColor=INK, spaceAfter=8),
    "cell": ParagraphStyle("cell", fontName="Arial", fontSize=8.5,
                           leading=11, textColor=INK),
}

def markup(value):
    value = re.sub(r"!\[\[([^\]]+)\]\]", r"\1", value)
    value = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^\]]+)\]\]", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = escape(value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"`([^`]+)`", r"<font color='#157C80'>\1</font>", value)
    return value.replace("  ", " ")

def paragraph(text, style="body"):
    return Paragraph(markup(text), styles[style])

def table_block(lines):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append([paragraph(c, "cell") for c in cells])
    if not rows:
        return []
    widths = [CONTENT_WIDTH / len(rows[0])] * len(rows[0])
    if len(rows[0]) == 3:
        widths = [CONTENT_WIDTH * 0.50, CONTENT_WIDTH * 0.22, CONTENT_WIDTH * 0.28]
    tab = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
    tab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E1EFF3")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#F5F8FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, TEAL),
    ]))
    return [tab, Spacer(1, 8)]

story = []
lines = SOURCE.read_text(encoding="utf-8").splitlines()
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    if line.startswith("|"):
        group = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            group.append(lines[i])
            i += 1
        story.extend(table_block(group))
        continue
    if line.startswith("![[") and line.endswith("]]"):
        image_path = ROOT / line[3:-2]
        with PILImage.open(image_path) as im:
            w, h = im.size
        max_w, max_h = CONTENT_WIDTH, 205
        scale = min(max_w / w, max_h / h)
        flowable = Image(str(image_path), width=w * scale, height=h * scale)
        if i + 2 < len(lines) and lines[i + 2].startswith("*Figura"):
            story.append(KeepTogether([flowable,
                                       paragraph(lines[i + 2].strip("*"), "caption")]))
            i += 3
        else:
            story.append(flowable)
            i += 1
        continue
    if line.startswith("# "):
        story.append(paragraph(line[2:], "title"))
    elif line.startswith("## "):
        story.append(paragraph(line[3:], "h2"))
    elif line.startswith("### "):
        story.append(paragraph(line[4:], "h3"))
    elif line.startswith("- "):
        story.append(paragraph("• " + line[2:]))
    elif line.startswith("*Figura"):
        story.append(paragraph(line.strip("*"), "caption"))
    else:
        story.append(paragraph(line))
    i += 1

def footer(canvas, doc):
    canvas.setFont("Arial", 8)
    canvas.setFillColor(INK)
    canvas.drawString(42, 27, "Grupo 4 | Deep Learning")
    canvas.drawRightString(WIDTH - 42, 27, str(doc.page))

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=42,
                        rightMargin=42, topMargin=38, bottomMargin=42,
                        title="Reconhecimento de letras e números em imagens")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
