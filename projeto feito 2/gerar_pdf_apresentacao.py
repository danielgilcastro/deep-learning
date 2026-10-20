"""Cria a cópia em PDF (formato portátil de documento) dos slides renderizados."""
from pathlib import Path
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
SLIDES = ROOT / ".build-slides-simple"
OUTPUT = ROOT / "Apresentacao_Grupo4.pdf"
files = sorted(SLIDES.glob("slide-??.png"))
if len(files) != 10:
    raise RuntimeError(f"Esperados 10 slides; encontrados {len(files)}")

pdf = canvas.Canvas(str(OUTPUT), pagesize=(1280, 720))
for image in files:
    pdf.drawImage(str(image), 0, 0, width=1280, height=720)
    pdf.showPage()
pdf.save()
print(OUTPUT)
