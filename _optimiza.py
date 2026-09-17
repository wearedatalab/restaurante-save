# -*- coding: utf-8 -*-
"""Optimiza las imagenes del sitio: redimensiona y exporta a WebP."""
import os
from PIL import Image, ImageOps

BASE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(BASE, "_originales")
PLA = os.path.join(BASE, "img", "platillos")
OUT = os.path.join(BASE, "img", "w")
os.makedirs(OUT, exist_ok=True)

# nombre -> ancho maximo
ANCHOS = {
    "hero-mar": 2400,
    "hero-palapa": 1920,
    "og": 1200,
    "textura-agua": 1920,
    "playa-glorias": 1600,
    "hielo-mariscos": 1400,
    "salon": 1400,
    "terraza": 1400,
    "eventos": 1400,
    "bodas": 1400,
    "domicilio": 1200,
    "pescador": 1100,
    "chef-aguachile": 1100,
    "camaron-hielo": 1000,
    "bar-coctel": 1000,
    "area-ninos": 1100,
    "deportes": 1100,
}

def exporta(src, dest, ancho, calidad=80):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im).convert("RGB")
    if im.width > ancho:
        alto = round(im.height * ancho / im.width)
        im = im.resize((ancho, alto), Image.LANCZOS)
    im.save(dest, "WEBP", quality=calidad, method=6)
    return im.size, os.path.getsize(dest) // 1024

total = 0
for f in sorted(os.listdir(GEN)):
    if not f.lower().endswith(".jpg"):
        continue
    name = os.path.splitext(f)[0]
    ancho = ANCHOS.get(name, 1400)
    size, kb = exporta(os.path.join(GEN, f), os.path.join(OUT, name + ".webp"), ancho)
    total += kb
    print("%-18s %sx%s  %s KB" % (name, size[0], size[1], kb))

for f in sorted(os.listdir(PLA)):
    if not f.lower().endswith((".jpg", ".png")):
        continue
    name = "p-" + os.path.splitext(f)[0].lower().replace("_", "-")
    size, kb = exporta(os.path.join(PLA, f), os.path.join(OUT, name + ".webp"), 900, 82)
    total += kb
    print("%-28s %sx%s  %s KB" % (name, size[0], size[1], kb))

# OG social en JPG (mayor compatibilidad), 1200x630
im = Image.open(os.path.join(GEN, "og.jpg")).convert("RGB")
im = ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=(0.5, 0.5))
im.save(os.path.join(BASE, "img", "og-save.jpg"), "JPEG", quality=84, optimize=True, progressive=True)
print("og-save.jpg", os.path.getsize(os.path.join(BASE, "img", "og-save.jpg")) // 1024, "KB")

# Certificaciones y apps: recomprimir a webp pequeno
for f, w in (("1_Distintivo_H-1024x675.jpg", 320), ("esr.png", 320)):
    src = os.path.join(BASE, "_originales", f)
    if os.path.exists(src):
        n = "cert-h" if "Distintivo" in f else "cert-esr"
        size, kb = exporta(src, os.path.join(OUT, n + ".webp"), w, 86)
        print(n, size, kb, "KB")

print("TOTAL webp aprox %.1f MB" % (total / 1024.0))
