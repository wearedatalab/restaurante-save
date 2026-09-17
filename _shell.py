# -*- coding: utf-8 -*-
"""Cascaron comun: head, header, footer, iconos y datos estructurados."""
import json
from _data import (SITIO, MARCA, SUCURSALES, REDES, RESERVAS, MENU_PDF,
                   HORARIO, HORARIO_TXT, CARTA, DELIVERY)

# ---------------------------------------------------------------------------
# Iconos SVG
# ---------------------------------------------------------------------------
def ico(nombre, s=18):
    d = {
        "flecha": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "flecha-d": '<path d="M9 6l6 6-6 6"/>',
        "tel": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "wa": '<path d="M20.5 3.5A11.9 11.9 0 0 0 12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6A12 12 0 0 0 12 24c6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.5-8.5zM12 22a10 10 0 0 1-5.1-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A10 10 0 1 1 12 22zm5.5-7.5c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1l-.9 1.1c-.2.2-.3.2-.6.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.8-1.5.1-.2 0-.4 0-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.3 5.2 4.6 1.9.8 2.7.9 3.6.8.6-.1 1.8-.7 2-1.5.3-.7.3-1.3.2-1.4 0-.2-.2-.3-.5-.4z" stroke="none" fill="currentColor"/>',
        "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
        "reloj": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
        "auto": '<path d="M5 17h14M6.5 17v2M17.5 17v2M3 13l1.6-5A2 2 0 0 1 6.5 6.5h11A2 2 0 0 1 19.4 8L21 13v4H3v-4z"/><circle cx="7.5" cy="13.5" r="1"/><circle cx="16.5" cy="13.5" r="1"/>',
        "llave": '<circle cx="8" cy="8" r="5"/><path d="M11.5 11.5L21 21M17 17l2-2M19 19l2-2"/>',
        "nino": '<circle cx="12" cy="7" r="4"/><path d="M5 21c0-3.9 3.1-7 7-7s7 3.1 7 7"/><path d="M9 6.5h.01M15 6.5h.01"/>',
        "tv": '<rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 21h8M12 18v3"/>',
        "aire": '<path d="M3 8h11a3 3 0 1 0-3-3M3 13h15a3 3 0 1 1-3 3M3 18h8"/>',
        "estrella": '<path d="M12 2l3 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.9 21l1.2-6.8-5-4.9 6.9-1z"/>',
        "chef": '<path d="M7 21h10M6 17h12v4H6zM6 17a5 5 0 0 1-1-9.9 4 4 0 0 1 7.5-2 4 4 0 0 1 6.5 3 4 4 0 0 1-1 8.9"/>',
        "pez": '<path d="M2 12s3.5-5 8.5-5S19 9 22 12c-3 3-6.5 5-11.5 5S2 12 2 12z"/><circle cx="8" cy="11" r=".8" fill="currentColor"/><path d="M22 12l-3.5-3v6L22 12z"/>',
        "ola": '<path d="M2 12c2.5 0 2.5 3 5 3s2.5-3 5-3 2.5 3 5 3 2.5-3 5-3M2 6c2.5 0 2.5 3 5 3s2.5-3 5-3 2.5 3 5 3 2.5-3 5-3M2 18c2.5 0 2.5 3 5 3s2.5-3 5-3 2.5 3 5 3 2.5-3 5-3"/>',
        "check": '<path d="M20 6L9 17l-5-5"/>',
        "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-5M12 8h.01"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/>',
        "calendario": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
        "usuarios": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
        "copa": '<path d="M8 22h8M12 15v7M5 3h14l-1.5 6a5.5 5.5 0 0 1-11 0L5 3z"/>',
        "anillos": '<circle cx="9" cy="14" r="6"/><circle cx="15" cy="14" r="6"/>',
        "bolsa": '<path d="M6 2l-2 5v13a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7l-2-5z"/><path d="M4 7h16M16 11a4 4 0 0 1-8 0"/>',
        "fb": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
        "ig": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
        "x": '<path d="M4 4l16 16M20 4L4 20"/>',
        "menu-doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    }
    p = d.get(nombre, "")
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % (s, s, p))


# ---------------------------------------------------------------------------
# Navegacion
# ---------------------------------------------------------------------------
NAV = [
    ("index.html", "Inicio", "01"),
    ("menu.html", "Menú", "02"),
    ("sucursales.html", "Sucursales", "03"),
    ("eventos.html", "Eventos", "04"),
    ("nosotros.html", "Nosotros", "05"),
    ("blog.html", "Blog", "06"),
]


def wa_link(raw, texto="Hola, quisiera información sobre Restaurante SAVE."):
    return "https://wa.me/%s?text=%s" % (raw, texto.replace(" ", "%20").replace("¿", "%C2%BF"))


# ---------------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------------
def _horas():
    if not HORARIO:
        return None
    return [{"@type": "OpeningHoursSpecification",
             "dayOfWeek": d.split(","), "opens": a, "closes": c} for d, a, c in HORARIO]


def sucursal_ld(s, completo=True):
    n = {
        "@type": "Restaurant",
        "@id": "%s/sucursales.html#%s" % (SITIO, s["id"]),
        "name": "Restaurante SAVE %s" % s["nombre"],
        "url": "%s/sucursales.html#%s" % (SITIO, s["id"]),
        "image": "%s/img/social/salon.jpg" % SITIO,
        "servesCuisine": ["Mariscos", "Cocina sinaloense", "Cocina mexicana"],
        "priceRange": "$$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": s["calle"],
            "addressLocality": s["ciudad"],
            "addressRegion": s["estado"],
            "postalCode": s["cp"],
            "addressCountry": "MX",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": s["lat"], "longitude": s["lng"]},
        "hasMap": s["maps"],
        "acceptsReservations": RESERVAS,
        "parentOrganization": {"@id": "%s/#organizacion" % SITIO},
    }
    if s["tel_raw"]:
        n["telephone"] = s["tel_raw"]
    h = _horas()
    if h:
        n["openingHoursSpecification"] = h
    if completo:
        n["menu"] = "%s/menu.html" % SITIO
        n["hasMenu"] = {"@id": "%s/menu.html#carta" % SITIO}
        n["amenityFeature"] = [
            {"@type": "LocationFeatureSpecification", "name": t, "value": True}
            for t in ("Estacionamiento propio", "Valet parking gratuito", "Área de niños",
                      "Transmisión de eventos deportivos", "Área de fumadores")
        ]
    return n


def organizacion_ld():
    return {
        "@type": "Organization",
        "@id": "%s/#organizacion" % SITIO,
        "name": MARCA,
        "alternateName": "SAVE Restaurante",
        "url": SITIO + "/",
        "logo": {"@type": "ImageObject", "url": "%s/img/logoinicio.png" % SITIO,
                 "width": 256, "height": 130},
        "image": "%s/img/og-save.jpg" % SITIO,
        "description": ("Restaurante de pescados y mariscos de estilo sinaloense, nombrado en "
                        "honor a Guasave, Sinaloa. Producto del Mar de Cortés con calidad de "
                        "exportación, en seis sucursales de Jalisco, Querétaro y Nuevo León."),
        "sameAs": [REDES["facebook"], REDES["instagram"], REDES["twitter"]],
        "areaServed": [{"@type": "State", "name": n} for n in ("Jalisco", "Querétaro", "Nuevo León")],
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": "Distintivo H",
             "credentialCategory": "Certificación de manejo higiénico de alimentos (Secretaría de Turismo)"},
            {"@type": "EducationalOccupationalCredential", "name": "Empresa Socialmente Responsable (ESR)"},
        ],
    }


def website_ld():
    return {
        "@type": "WebSite",
        "@id": "%s/#sitio" % SITIO,
        "url": SITIO + "/",
        "name": MARCA,
        "inLanguage": "es-MX",
        "publisher": {"@id": "%s/#organizacion" % SITIO},
    }


def menu_ld():
    secciones = []
    for sec in CARTA:
        secciones.append({
            "@type": "MenuSection",
            "name": sec["nombre"],
            "description": sec["desc"] or None,
            "hasMenuItem": [
                {"@type": "MenuItem", "name": n, "description": d or None}
                for n, d in sec["platos"]
            ],
        })
    return {
        "@type": "Menu",
        "@id": "%s/menu.html#carta" % SITIO,
        "name": "Carta de Restaurante SAVE",
        "url": "%s/menu.html" % SITIO,
        "inLanguage": "es-MX",
        "hasMenuSection": secciones,
    }


def faq_ld(pares):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pares
        ],
    }


def migas_ld(items):
    """items = [(nombre, url_relativa|None)]"""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": ("%s/%s" % (SITIO, u)) if u else None}
            for i, (n, u) in enumerate(items)
        ],
    }


def _limpia(o):
    if isinstance(o, dict):
        return {k: _limpia(v) for k, v in o.items() if v is not None}
    if isinstance(o, list):
        return [_limpia(v) for v in o]
    return o


def jsonld(nodos):
    g = {"@context": "https://schema.org", "@graph": _limpia(nodos)}
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(g, ensure_ascii=False, separators=(",", ":")))


# ---------------------------------------------------------------------------
# HEAD
# ---------------------------------------------------------------------------
def head(titulo, descripcion, ruta, og_img="img/og-save.jpg", tipo="website",
         extra="", precarga=None, keywords=""):
    canonical = "%s/%s" % (SITIO, "" if ruta == "index.html" else ruta)
    pre = ""
    if precarga:
        pre = '\n  <link rel="preload" as="image" href="%s" fetchpriority="high">' % precarga
    return """<!DOCTYPE html>
<html lang="es-MX">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>%(t)s</title>
  <meta name="description" content="%(d)s">
  %(kw)s<link rel="canonical" href="%(c)s">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="author" content="%(m)s">
  <meta name="geo.region" content="MX-JAL">
  <meta name="geo.placename" content="Guadalajara, Zapopan, Querétaro, Monterrey, San Pedro Garza García">
  <meta name="theme-color" content="#04202B">

  <meta property="og:type" content="%(tipo)s">
  <meta property="og:site_name" content="%(m)s">
  <meta property="og:locale" content="es_MX">
  <meta property="og:title" content="%(t)s">
  <meta property="og:description" content="%(d)s">
  <meta property="og:url" content="%(c)s">
  <meta property="og:image" content="%(s)s/%(og)s">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Mesa de pescados y mariscos de Restaurante SAVE">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@savedemar">
  <meta name="twitter:title" content="%(t)s">
  <meta name="twitter:description" content="%(d)s">
  <meta name="twitter:image" content="%(s)s/%(og)s">

  <link rel="icon" href="img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="img/logoinicio.png">
  <link rel="manifest" href="site.webmanifest">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700&family=Manrope:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="css/save.css">%(pre)s
%(extra)s</head>
""" % {"t": titulo, "d": descripcion, "c": canonical, "m": MARCA, "s": SITIO,
       "og": og_img, "tipo": tipo, "extra": extra, "pre": pre,
       "kw": ('<meta name="keywords" content="%s">\n  ' % keywords) if keywords else ""}


# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
def header(activa):
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if u == activa else "", n)
        for u, n, _ in NAV)
    movil = "".join(
        '<a class="mm" href="%s"%s>%s<em>%s</em></a>' % (u, ' aria-current="page"' if u == activa else "", n, num)
        for u, n, num in NAV)
    wa = wa_link(SUCURSALES[0]["wa_raw"])
    return """<a class="saltar" href="#principal">Saltar al contenido</a>
<div class="grano" aria-hidden="true"></div>

<div class="topbar">
  <div class="contenedor topbar__in">
    <p class="topbar__left">%(pez)s <span>Pescados y mariscos del Mar de Cortés<span class="op"> · 6 sucursales en México</span></span></p>
    <div class="topbar__right">
      <a href="sucursales.html">Encuentra tu sucursal</a>
      <a href="%(wa)s" target="_blank" rel="noopener">WhatsApp</a>
      <div class="topbar__redes">
        <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram de Restaurante SAVE">%(i_ig)s</a>
        <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook de Restaurante SAVE">%(i_fb)s</a>
        <a href="%(tw)s" target="_blank" rel="noopener" aria-label="X (Twitter) de Restaurante SAVE">%(i_x)s</a>
      </div>
    </div>
  </div>
</div>

<header class="header">
  <div class="contenedor header__in">
    <a class="marca" href="index.html" aria-label="Restaurante SAVE, inicio">
      <img src="img/logoinicio.png" alt="Restaurante SAVE — Guasave, Sinaloa" width="256" height="130">
    </a>
    <nav class="nav" aria-label="Navegación principal">%(nav)s</nav>
    <div class="header__cta">
      <a class="btn btn--linea btn--sm" href="menu.html">Ver la carta</a>
      <a class="btn btn--sm" href="reservar.html">Reservar mesa</a>
      <button class="hamb" type="button" aria-expanded="false" aria-controls="menu-movil" aria-label="Abrir menú">
        <span></span>
      </button>
    </div>
  </div>
</header>

<div class="menu-movil" id="menu-movil">
  %(movil)s
  <div class="menu-movil__pie">
    <a class="btn btn--full" href="reservar.html">Reservar mesa</a>
    <a class="btn btn--linea-claro btn--full" href="%(wa)s" target="_blank" rel="noopener">Escribir por WhatsApp</a>
  </div>
</div>
""" % {"nav": nav, "movil": movil, "wa": wa, "pez": ico("pez", 15),
       "ig": REDES["instagram"], "fb": REDES["facebook"], "tw": REDES["twitter"],
       "i_ig": ico("ig", 15), "i_fb": ico("fb", 15), "i_x": ico("x", 15)}


# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
def footer():
    sucs = "".join('<li><a href="sucursales.html#%s">%s <span style="opacity:.5">· %s</span></a></li>'
                   % (s["id"], s["nombre"], s["ciudad"]) for s in SUCURSALES)
    apps = "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, n)
                   for n, u, _ in DELIVERY)
    return """<footer class="footer">
  <div class="contenedor">
    <div class="footer__top">
      <div>
        <img class="logo" src="img/logoinicio.png" alt="Restaurante SAVE" width="256" height="130" loading="lazy">
        <p class="footer__desc">Pescados y mariscos de Guasave, Sinaloa. Producto del Mar de Cortés con calidad de exportación, servido en Jalisco, Querétaro y Nuevo León.</p>
        <div class="footer__redes">
          <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram">%(i_ig)s</a>
          <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook">%(i_fb)s</a>
          <a href="%(tw)s" target="_blank" rel="noopener" aria-label="X (Twitter)">%(i_x)s</a>
        </div>
      </div>
      <div>
        <h3>Sucursales</h3>
        <ul>%(sucs)s</ul>
      </div>
      <div>
        <h3>Explora</h3>
        <ul>
          <li><a href="menu.html">La carta completa</a></li>
          <li><a href="%(pdf)s" target="_blank" rel="noopener">Menú en PDF</a></li>
          <li><a href="reservar.html">Reservar mesa</a></li>
          <li><a href="eventos.html">Eventos y banquetes</a></li>
          <li><a href="nosotros.html">Nuestra historia</a></li>
          <li><a href="blog.html">Blog</a></li>
        </ul>
        <h3 style="margin-top:26px">A domicilio</h3>
        <ul>%(apps)s</ul>
      </div>
      <div>
        <h3>Novedades SAVE</h3>
        <p style="color:rgba(232,241,243,.6);line-height:1.6">Temporadas de pesca, platillos nuevos y promociones. Sin spam.</p>
        <form class="news" novalidate>
          <label class="solo-lectores" for="news-mail">Correo electrónico</label>
          <input id="news-mail" type="email" name="email" placeholder="tu@correo.com" required autocomplete="email">
          <button type="submit">Suscribirme</button>
        </form>
        <p class="news__ok">¡Listo! Te escribiremos pronto.</p>
      </div>
    </div>
    <div class="footer__bajo">
      <p>© <span data-anio>2026</span> Restaurante SAVE. Todos los derechos reservados.</p>
      <nav aria-label="Enlaces legales">
        <a href="aviso-de-privacidad.html">Aviso de privacidad</a>
        <a href="sucursales.html">Contacto</a>
        <a href="sitemap.xml">Mapa del sitio</a>
      </nav>
    </div>
  </div>
</footer>
<script src="js/save.js" defer></script>
</body>
</html>
""" % {"sucs": sucs, "apps": apps, "pdf": MENU_PDF,
       "ig": REDES["instagram"], "fb": REDES["facebook"], "tw": REDES["twitter"],
       "i_ig": ico("ig", 17), "i_fb": ico("fb", 17), "i_x": ico("x", 17)}


def migas_html(items):
    out = []
    for i, (n, u) in enumerate(items):
        if u:
            out.append('<a href="%s">%s</a>' % (u, n))
        else:
            out.append('<span aria-current="page">%s</span>' % n)
        if i < len(items) - 1:
            out.append(ico("flecha-d", 13))
    return '<nav class="migas" aria-label="Ruta de navegación">%s</nav>' % "".join(out)


def cta_final(titulo, texto, img="img/w/hero-palapa.webp"):
    return """<section class="cta">
  <img src="%(img)s" alt="" loading="lazy" width="1920" height="1072">
  <div class="contenedor cta__in">
    <h2 class="rv">%(t)s</h2>
    <p class="rv rv-d1">%(x)s</p>
    <div class="cta__acciones rv rv-d2">
      <a class="btn" href="reservar.html">Reservar mesa %(f)s</a>
      <a class="btn btn--linea-claro" href="menu.html">Ver la carta</a>
    </div>
  </div>
</section>
""" % {"t": titulo, "x": texto, "img": img, "f": ico("flecha", 17)}


def faq_html(pares, titulo="Preguntas frecuentes", intro=""):
    items = []
    for i, (q, a) in enumerate(pares):
        items.append("""<div class="faq__item" data-abierto="false">
        <h3><button class="faq__q" type="button" aria-expanded="false" aria-controls="faq-r%(i)d" id="faq-p%(i)d">
          <span>%(q)s</span><span class="faq__ico" aria-hidden="true"></span>
        </button></h3>
        <div class="faq__a" id="faq-r%(i)d" role="region" aria-labelledby="faq-p%(i)d"><div><p>%(a)s</p></div></div>
      </div>""" % {"i": i, "q": q, "a": a})
    return """<section class="seccion" id="preguntas">
  <div class="contenedor faq">
    <div class="rv">
      <p class="eyebrow">Resolvemos dudas</p>
      <h2 class="titulo">%(t)s</h2>
      %(intro)s
    </div>
    <div class="faq__lista rv rv-d1">%(items)s</div>
  </div>
</section>
""" % {"t": titulo, "items": "".join(items),
       "intro": ('<p class="bajada" style="margin-top:20px">%s</p>' % intro) if intro else ""}
