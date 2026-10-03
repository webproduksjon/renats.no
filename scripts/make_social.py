#!/usr/bin/env python3
"""Draw the source-controlled Open Graph image with exact brand copy."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
out = root / "social-preview.png"
img = Image.new("RGB", (1200, 630), "#f6f5ef")
d = ImageDraw.Draw(img)
regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = lambda size, heavy=False: ImageFont.truetype(bold if heavy else regular, size)
d.rectangle((0, 0, 1200, 14), fill="#142c2a")
d.rounded_rectangle((70, 65, 146, 141), radius=15, fill="#142c2a")
d.text((82, 72), "w/", font=font(38, True), fill="#d9f076")
d.text((169, 86), "webproduksjon.no", font=font(32, True), fill="#142c2a")
d.text((74, 206), "En nettside som", font=font(67, True), fill="#142c2a")
d.text((74, 293), "gjør det lett å velge deg.", font=font(55, True), fill="#142c2a")
d.rectangle((74, 379, 813, 389), fill="#d9f076")
d.text((75, 445), "Enkle nettsider for små bedrifter", font=font(31), fill="#34504d")
d.text((75, 494), "Fra 4 990 kr  ·  Skriftlig kontakt", font=font(25), fill="#34504d")
d.rectangle((960, 420, 1130, 590), fill="#d9f076")
d.text((985, 463), "↗", font=font(88, True), fill="#142c2a")
img.save(out, optimize=True)
print(out)
