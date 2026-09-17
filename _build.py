# -*- coding: utf-8 -*-
"""Generador del sitio de Restaurante SAVE."""
import io, os
from _data import (SITIO, MARCA, SUCURSALES, DESTACADOS, CARTA, FAQ_HOME,
                   SERVICIOS, DELIVERY, REDES, RESERVAS, MENU_PDF,
                   HORARIO_TXT)
from _shell import (head, header, footer, ico, jsonld, organizacion_ld, website_ld,
                    sucursal_ld, menu_ld, faq_ld, migas_ld, migas_html, cta_final,
                    faq_html, wa_link)

BASE = os.path.dirname(os.path.abspath(__file__))


def escribe(nombre, html):
    with io.open(os.path.join(BASE, nombre), "w", encoding="utf-8") as f:
        f.write(html)
    print("  %-40s %6.1f KB" % (nombre, len(html.encode("utf-8")) / 1024.0))


# ===========================================================================
# Bloques reutilizables
# ===========================================================================
def bloque_sucursales(oscuro=True, limite=None):
    tarjetas = []
    for s in (SUCURSALES[:limite] if limite else SUCURSALES):
        tels = []
        if s["tel_raw"]:
            tels.append('<a href="tel:%s">%s Tel. %s</a>' % (s["tel_raw"], ico("tel", 15), s["tel"]))
        if s["wa_raw"]:
            tels.append('<a href="%s" target="_blank" rel="noopener">%s WhatsApp %s</a>'
                        % (wa_link(s["wa_raw"], "Hola, quisiera reservar en SAVE %s." % s["nombre"]),
                           ico("wa", 15), s["wa"]))
        if not tels:
            tels.append('<a href="%s" target="_blank" rel="noopener">%s Ver ubicación y contacto</a>' % (s["maps"], ico("pin", 15)))
        tarjetas.append("""<article class="sucursal rv" id="card-%(id)s">
        <p class="sucursal__ciudad">%(ciudad)s · %(estado)s</p>
        <h3>%(nombre)s</h3>
        <address>%(dir)s</address>
        <div class="sucursal__tels">%(tels)s</div>
        <div class="sucursal__acc">
          <a class="btn btn--sm btn--%(estilo)s" href="sucursales.html#%(id)s">Detalle</a>
          <a class="btn btn--sm btn--%(estilo)s" href="%(maps)s" target="_blank" rel="noopener">Cómo llegar</a>
        </div>
      </article>""" % dict(s, tels="".join(tels), estilo="linea-claro" if oscuro else "linea"))
    return "".join(tarjetas)


def bloque_destacados(items=None):
    items = items or DESTACADOS
    out = []
    for i, (img, nombre, desc, tag) in enumerate(items):
        out.append("""<article class="platillo rv%(d)s">
        <span class="platillo__tag">%(tag)s</span>
        <img src="img/w/%(img)s.webp" alt="%(nombre)s — Restaurante SAVE" width="900" height="1125" loading="%(lz)s" decoding="async">
        <div class="platillo__txt"><h3>%(nombre)s</h3><p>%(desc)s</p></div>
      </article>""" % {"img": img, "nombre": nombre, "desc": desc, "tag": tag,
                       "d": " rv-d%d" % ((i % 4) + 1) if i % 4 else "",
                       "lz": "eager" if i < 2 else "lazy"})
    return "".join(out)


def bloque_servicios():
    return "".join("""<div class="servicio rv rv-d%(i)d">%(ico)s<h3>%(t)s</h3><p>%(d)s</p></div>"""
                   % {"i": (i % 4) + 1, "ico": ico(k, 26), "t": t, "d": d}
                   for i, (t, d, k) in enumerate(SERVICIOS))


EXPERIENCIAS = [
    ("Restaurante", "img/w/salon.webp",
     "Comedor amplio, servicio atento y el ambiente de palapa que trajimos de la costa. "
     "Para la comida de todos los días y para la de los domingos.", "sucursales.html", "01"),
    ("Eventos y banquetes", "img/w/eventos.webp",
     "Comidas de empresa, cumpleaños, bautizos y cenas navideñas. Menús cerrados y "
     "áreas privadas en cada sucursal.", "eventos.html", "02"),
    ("Bar y coctelería", "img/w/bar-coctel.webp",
     "Micheladas preparadas, clamatos con camarón, cervezas bien frías y una carta de "
     "vinos pensada para acompañar mariscos.", "eventos.html#bar", "03"),
    ("Bodas", "img/w/bodas.webp",
     "Montaje, menú y coordinación para recepciones. Un banquete de mariscos que tus "
     "invitados no van a olvidar.", "eventos.html#bodas", "04"),
]


def bloque_experiencias():
    return "".join("""<article class="exp__item rv rv-d%(d)d">
      <img src="%(img)s" alt="%(t)s en Restaurante SAVE" width="1400" height="933" loading="lazy" decoding="async">
      <span class="exp__num">%(n)s</span>
      <h3>%(t)s</h3>
      <p>%(x)s</p>
      <a class="enlace" href="%(u)s">Saber más %(f)s</a>
    </article>""" % {"t": t, "img": img, "x": x, "u": u, "n": n, "d": i + 1, "f": ico("flecha", 15)}
        for i, (t, img, x, u, n) in enumerate(EXPERIENCIAS))


def bloque_certificaciones():
    return """<div class="cert rv">
      <img src="img/w/cert-h.webp" alt="Distintivo H otorgado por la Secretaría de Turismo" width="300" height="309" loading="lazy">
      <div>
        <h3>Distintivo H</h3>
        <p>Reconocimiento de la Secretaría de Turismo a los establecimientos que cumplen los estándares de manejo higiénico de alimentos.</p>
      </div>
    </div>
    <div class="cert rv rv-d1">
      <img src="img/w/cert-esr.webp" alt="Distintivo Empresa Socialmente Responsable" width="340" height="111" loading="lazy">
      <div>
        <h3>Empresa Socialmente Responsable</h3>
        <p>Distintivo ESR por nuestro compromiso con el equipo, la comunidad y el aprovechamiento responsable del producto del mar.</p>
      </div>
    </div>"""


def bloque_domicilio(fondo="seccion--arena"):
    apps = "".join('<a class="app-card" href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" width="90" height="24" loading="lazy">Pedir en %s</a>'
                   % (u, logo, n, n) for n, u, logo in DELIVERY)
    return """<section class="seccion %(fondo)s" id="domicilio">
  <div class="contenedor domicilio">
    <div class="rv">
      <p class="eyebrow">Servicio a domicilio</p>
      <h2 class="titulo">También <em>llega a tu casa</em></h2>
      <p class="bajada" style="margin-top:20px">Los aguachiles, los camarones y los filetes salen de la misma cocina y se empacan para que lleguen en su punto. Pide por app o llama a tu sucursal para ordenar para llevar.</p>
      <div class="domicilio__apps">%(apps)s</div>
      <p style="margin-top:22px;font-size:.88rem;color:var(--tinta-40)">La disponibilidad y la cobertura varían según la sucursal y la plataforma.</p>
    </div>
    <div class="domicilio__media rv rv-d1">
      <img src="img/w/domicilio.webp" alt="Pedido de mariscos de Restaurante SAVE listo para entrega a domicilio" width="1200" height="800" loading="lazy">
    </div>
  </div>
</section>
"""  % {"apps": apps, "fondo": fondo}


# ===========================================================================
# 1. INDEX
# ===========================================================================
def pagina_index():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        {"@type": "WebPage", "@id": SITIO + "/#pagina", "url": SITIO + "/",
         "name": "Restaurante SAVE — Mariscos de Guasave, Sinaloa",
         "isPartOf": {"@id": SITIO + "/#sitio"},
         "about": {"@id": SITIO + "/#organizacion"},
         "inLanguage": "es-MX"},
    ] + [sucursal_ld(s) for s in SUCURSALES] + [faq_ld(FAQ_HOME)])

    marquesina_items = ["Aguachile tatemado", "Camarones SAVE", "Pulpo a las brasas",
                        "Cóctel Guasaveño", "Chilitaco", "Pescado zarandeado",
                        "Callo de hacha", "Camarones Philadelphia", "Tostada de atún"]
    grupo = "".join('<span>%s</span><i></i>' % t for t in marquesina_items)

    html = head(
        "Restaurante SAVE | Mariscos sinaloenses en GDL, Querétaro y Monterrey",
        "Pescados y mariscos del Mar de Cortés con recetas de Guasave, Sinaloa. Aguachiles, "
        "camarones y pescado zarandeado en 6 sucursales. Reserva tu mesa en línea.",
        "index.html", precarga="img/w/hero-plato.webp", extra="  " + ld + "\n",
        keywords="restaurante de mariscos, mariscos Guadalajara, aguachile, pescados y mariscos, "
                 "restaurante sinaloense, mariscos Querétaro, mariscos Monterrey, SAVE")

    html += "<body>\n" + header("index.html")

    html += """<main id="principal">

<!-- ================= HERO ================= -->
<section class="hero">
  <div class="hero__panel">
    <div class="hero__panel-in">
      <p class="eyebrow">Guasave · Sinaloa · desde la playa Las Glorias</p>
      <h1>Mariscos que saben<br><em>a la costa</em></h1>
      <p class="hero__sub">Pescados y mariscos del Mar de Cortés con calidad de exportación, preparados con las recetas tradicionales de Sinaloa y creaciones que solo existen aquí.</p>
      <div class="hero__acciones">
        <a class="btn" href="reservar.html">Reservar mesa %(f)s</a>
        <a class="btn btn--linea-claro" href="menu.html">Ver la carta</a>
      </div>
      <div class="hero__sellos">
        <span class="chip chip--claro">%(i_pin)s 6 sucursales en México</span>
        <span class="chip chip--claro">%(i_check)s Distintivo H</span>
        <span class="chip chip--claro">%(i_estrella)s Empresa Socialmente Responsable</span>
      </div>
    </div>
  </div>
  <figure class="hero__foto">
    <img src="img/w/hero-plato.webp" alt="Camarones SAVE: camarones capeados bañados en aderezo oriental con ajonjolí, cebollín y crujiente de betabel" width="1800" height="1201" fetchpriority="high" decoding="async">
    <figcaption class="hero__pie">
      <strong>Camarones SAVE</strong>
      <span>Capeados en aderezo oriental con un toque de picante. El platillo de la casa.</span>
    </figcaption>
  </figure>
</section>

<div class="marquesina" aria-hidden="true">
  <div class="marquesina__pista">
    <div class="marquesina__grupo">%(grupo)s</div>
    <div class="marquesina__grupo">%(grupo)s</div>
  </div>
</div>

<!-- ================= ORIGEN ================= -->
<section class="seccion" id="origen">
  <div class="contenedor split">
    <div class="rv">
      <p class="eyebrow">Nuestro origen</p>
      <h2 class="titulo">El sabor de la <em>palapa</em>, con el servicio de la ciudad</h2>
      <p class="bajada" style="margin-top:24px">Nos llamamos SAVE en honor a <strong>Guasave, Sinaloa</strong>. De ahí traemos las recetas de la playa Las Glorias y la forma de tratar el producto: sin adornos, con limón, chile y fuego.</p>
      <p class="bajada" style="margin-top:16px">Nuestros pescados y mariscos vienen directamente del <strong>Mar de Cortés</strong>, de donde salen las mejores variedades de México. Calidad de exportación, servida para consumo nacional.</p>
      <dl class="datos">
        <div><dt>6</dt><dd>Sucursales en Jalisco, Querétaro y Nuevo León</dd></div>
        <div><dt>+100</dt><dd>Platillos entre fríos, calientes y a las brasas</dd></div>
        <div><dt>H</dt><dd>Distintivo de manejo higiénico de alimentos</dd></div>
      </dl>
      <p style="margin-top:32px"><a class="enlace" href="nosotros.html">Conoce nuestra historia %(f15)s</a></p>
    </div>
    <div class="split__media rv rv-d1">
      <img src="img/w/pescador.webp" alt="Pescador sostiene un pescado recién capturado en el Mar de Cortés" width="1100" height="1366" loading="lazy">
      <div class="split__badge"><strong>100%%</strong><span>Producto del Mar de Cortés, calidad de exportación</span></div>
    </div>
  </div>
</section>

<!-- ================= PLATILLOS ================= -->
<section class="seccion seccion--osc" id="especialidades">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Lo que la gente pide</p>
        <h2 class="titulo">Especialidades <em>de la casa</em></h2>
        <p class="bajada" style="margin-top:20px">Doce platillos que explican de qué se trata SAVE. La carta completa tiene más de cien.</p>
      </div>
      <a class="btn btn--linea-claro rv rv-d1" href="menu.html">Ver la carta completa %(f)s</a>
    </div>
    <div class="platillos">%(dest)s</div>
  </div>
</section>

<!-- ================= EXPERIENCIAS ================= -->
<section class="seccion" id="experiencias">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Cuatro formas de vivirlo</p>
        <h2 class="titulo">Más que una <em>comida</em></h2>
      </div>
    </div>
    <div class="exp">%(exp)s</div>
  </div>
</section>

<!-- ================= SUCURSALES ================= -->
<section class="seccion seccion--osc" id="sucursales">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Dónde encontrarnos</p>
        <h2 class="titulo">Seis sucursales, <em>una misma cocina</em></h2>
        <p class="bajada" style="margin-top:20px">Tres en la Zona Metropolitana de Guadalajara, una en Santiago de Querétaro y dos en Nuevo León.</p>
      </div>
      <a class="btn btn--linea-claro rv rv-d1" href="sucursales.html">Ver todas con mapa %(f)s</a>
    </div>
    <div class="sucursales">%(sucs)s</div>

    <div style="margin-top:clamp(40px,6vw,72px)">
      <h3 class="rv" style="font-family:var(--texto);font-size:.78rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--coral-txt);margin-bottom:22px">En todas las sucursales</h3>
      <div class="servicios">%(serv)s</div>
    </div>
  </div>
</section>

%(dom)s

<!-- ================= CERTIFICACIONES ================= -->
<section class="seccion" id="certificaciones" style="padding-block:clamp(56px,7vw,90px)">
  <div class="contenedor certs">%(certs)s</div>
</section>

%(faq)s

%(cta)s
</main>
""" % {"f": ico("flecha", 17), "f15": ico("flecha", 15),
       "i_pin": ico("pin", 15), "i_check": ico("check", 15), "i_estrella": ico("estrella", 15),
       "grupo": grupo, "dest": bloque_destacados(), "exp": bloque_experiencias(),
       "sucs": bloque_sucursales(True), "serv": bloque_servicios(),
       "dom": bloque_domicilio(), "certs": bloque_certificaciones(),
       "faq": faq_html(FAQ_HOME, "Preguntas frecuentes sobre SAVE",
                       "Lo que más nos preguntan por teléfono, por WhatsApp y en redes."),
       "cta": cta_final("Tu mesa <em>ya casi está lista</em>",
                        "Reserva en línea en menos de un minuto, o escríbenos por WhatsApp a la sucursal que te queda más cerca.")}

    html += footer()
    escribe("index.html", html)


# ===========================================================================
# 2. MENU
# ===========================================================================
def pagina_menu():
    ld = jsonld([
        organizacion_ld(), website_ld(), menu_ld(),
        migas_ld([("Inicio", ""), ("Menú", "menu.html")]),
        {"@type": "WebPage", "@id": SITIO + "/menu.html#pagina",
         "url": SITIO + "/menu.html", "name": "Carta de Restaurante SAVE",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX",
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITIO + "/img/social/hielo-mariscos.jpg"}},
        faq_ld([
            ("¿Cuántos platillos tiene la carta de SAVE?",
             "La carta reúne más de 100 preparaciones repartidas en once secciones: entremeses, "
             "tostadas y ceviches, variedades del taco, camarón estilo SAVE, zarandeados y a las "
             "brasas, filetes y especialidades, pulpo, opciones light, cortes finos, guarniciones "
             "y postres."),
            ("¿SAVE tiene opciones ligeras o sin capear?",
             "Sí. La sección Light incluye taco de lechuga con camarón, filete empapelado al vapor, "
             "filete Soto Light y las ensaladas Michelle, que pueden pedirse con pollo, pescado, "
             "res o camarón."),
            ("¿Hay platillos para compartir?",
             "Sí. El Molcajete Guasaveño está pensado para dos personas y la Mariscada SAVE para "
             "tres. También hay órdenes de ostiones de 6 y 12 piezas y piezas enteras de pescado "
             "que se sirven por kilo."),
            ("¿Los precios están publicados en línea?",
             "Los precios cambian con la temporada de pesca, sobre todo en las piezas que se "
             "cotizan por kilo como el huachinango, la totoaba y la langosta. Consulta la carta "
             "vigente en el restaurante o pregunta por WhatsApp a tu sucursal."),
        ]),
    ])

    nav = "".join('<a href="#%s">%s</a>' % (s["id"], s["nombre"]) for s in CARTA)

    secciones = []
    for i, sec in enumerate(CARTA):
        platos = []
        for n, d in sec["platos"]:
            platos.append('<div class="plato"><h3>%s</h3>%s</div>'
                          % (n, ('<p>%s</p>' % d) if d else ""))
        secciones.append("""<section class="carta-seccion" id="%(id)s">
    <div class="contenedor">
      <div class="carta-seccion__cab rv">
        <span class="carta-seccion__num">%(num)02d — %(total)d platillos</span>
        <h2>%(nombre)s</h2>
        %(desc)s
      </div>
      <div class="carta-grid rv rv-d1">%(platos)s</div>
    </div>
  </section>""" % {"id": sec["id"], "nombre": sec["nombre"], "num": i + 1,
                   "total": len(sec["platos"]), "platos": "".join(platos),
                   "desc": ('<p class="carta-seccion__desc">%s</p>' % sec["desc"]) if sec["desc"] else ""})

    total = sum(len(s["platos"]) for s in CARTA)

    html = head(
        "Menú de Restaurante SAVE | Aguachiles, camarones y pescados",
        "La carta completa de SAVE: %d platillos de mariscos sinaloenses. Aguachiles, tostadas, "
        "tacos, camarón, zarandeados a las brasas, cortes finos y postres." % total,
        "menu.html", extra="  " + ld + "\n",
        keywords="menú mariscos, carta restaurante mariscos, aguachile, camarones, pescado zarandeado, pulpo a las brasas")

    html += "<body>\n" + header("menu.html")

    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/hielo-mariscos.webp" alt="" width="1400" height="933" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>La carta <em>completa</em></h1>
    <p>%(total)d platillos organizados en once secciones. Todo lo frío se cura al momento; todo lo que va al fuego sale de la parrilla de carbón. Lo que se cotiza por kilo depende de la pesca del día.</p>
    <div class="pagina-cab__chips">
      <a class="chip chip--claro" href="%(pdf)s" target="_blank" rel="noopener">%(i_doc)s Descargar menú en PDF</a>
      <a class="chip chip--claro" href="reservar.html">%(i_cal)s Reservar mesa</a>
    </div>
  </div>
</header>

<nav class="carta-nav" aria-label="Secciones de la carta">
  <div class="contenedor carta-nav__in">%(nav)s</div>
</nav>

<div id="carta">
%(secciones)s
</div>

<section class="seccion" style="padding-top:0">
  <div class="contenedor">
    <div class="carta-aviso rv">
      %(i_info)s
      <p><strong>Sobre precios y disponibilidad.</strong> La carta cambia con la temporada de pesca. Las piezas enteras —huachinango, pargo, róbalo, totoaba y langosta— se cotizan por kilo según el producto que llegó ese día. Si tienes alguna alergia o restricción alimentaria, dilo al hacer tu pedido: ajustamos la preparación siempre que sea posible.</p>
    </div>
  </div>
</section>

%(faq)s
%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Menú", None)]),
       "total": total, "nav": nav, "secciones": "\n".join(secciones), "pdf": MENU_PDF,
       "i_doc": ico("menu-doc", 15), "i_cal": ico("calendario", 15), "i_info": ico("info", 24),
       "faq": faq_html([
           ("¿SAVE tiene opciones ligeras o sin capear?",
            "Sí. La sección Light incluye taco de lechuga con camarón, jícama y zanahoria al mojo de ajo, "
            "filete empapelado al vapor de 350 g, filete Soto Light relleno de camarón y vegetales, y las "
            "ensaladas Michelle, que pueden pedirse con pollo, pescado, res o camarón."),
           ("¿Qué platillos son para compartir?",
            "El Molcajete Guasaveño está pensado para dos personas y la Mariscada SAVE para tres. También "
            "hay órdenes de ostiones de 6 y 12 piezas, y piezas enteras de pescado que se sirven por kilo."),
           ("¿Cuál es el platillo más pedido?",
            "Los Camarones SAVE —capeados en aderezo oriental con un toque de picante— y el aguachile, "
            "en sus versiones verde, rojo, negro y tatemado. El Chilitaco y el pulpo a las brasas los "
            "siguen de cerca."),
           ("¿Hay algo para quien no come mariscos?",
            "Sí. La sección de cortes finos incluye Rib Eye de 370 g, vacío y arrachera de 320 g, además "
            "del molcajete mar y tierra con arrachera y camarón gratinado."),
       ], "Sobre la carta"),
       "cta": cta_final("¿Ya sabes <em>qué vas a pedir</em>?",
                        "Aparta tu mesa y llega directo a sentarte. Reservar toma menos de un minuto.",
                        "img/w/terraza.webp")}

    html += footer()
    escribe("menu.html", html)


# ===========================================================================
# 3. SUCURSALES
# ===========================================================================
def pagina_sucursales():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Sucursales", "sucursales.html")]),
        {"@type": "CollectionPage", "@id": SITIO + "/sucursales.html#pagina",
         "url": SITIO + "/sucursales.html", "name": "Sucursales de Restaurante SAVE",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX",
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(SUCURSALES),
                        "itemListElement": [
                            {"@type": "ListItem", "position": i + 1,
                             "item": {"@id": "%s/sucursales.html#%s" % (SITIO, s["id"])}}
                            for i, s in enumerate(SUCURSALES)]}},
    ] + [sucursal_ld(s) for s in SUCURSALES])

    indice = "".join('<a class="chip" href="#%s">%s <span style="opacity:.55;font-weight:600">%s</span></a>'
                     % (s["id"], s["nombre"], s["ciudad"]) for s in SUCURSALES)

    bloques = []
    for s in SUCURSALES:
        filas = ['<dt>Dirección</dt><dd>%s</dd>' % s["dir"]]
        if s["tel"]:
            filas.append('<dt>Teléfono</dt><dd><a href="tel:%s">%s</a></dd>' % (s["tel_raw"], s["tel"]))
        if s["wa"]:
            filas.append('<dt>WhatsApp</dt><dd><a href="%s" target="_blank" rel="noopener">%s</a></dd>'
                         % (wa_link(s["wa_raw"], "Hola, quisiera reservar en SAVE %s." % s["nombre"]), s["wa"]))
        filas.append('<dt>Horario</dt><dd>%s</dd>' % (
            HORARIO_TXT if HORARIO_TXT else
            'Consulta el horario del día llamando a la sucursal o por WhatsApp.'))
        acciones = ['<a class="btn btn--sm" href="reservar.html?sucursal=%s">Reservar aquí</a>' % s["id"],
                    '<a class="btn btn--sm btn--linea" href="%s" target="_blank" rel="noopener">Abrir en Google Maps</a>' % s["maps"]]
        if s["tel_raw"]:
            acciones.append('<a class="btn btn--sm btn--linea" href="tel:%s">Llamar</a>' % s["tel_raw"])

        mapa = ("https://www.google.com/maps?q=%s&output=embed"
                % ("Restaurante+Save+" + s["dir"]).replace(" ", "+").replace(",", "%2C").replace("°", ""))

        bloques.append("""<article class="suc-detalle rv" id="%(id)s">
      <div class="suc-detalle__info">
        <p class="sucursal__ciudad">%(ciudad)s · %(estado)s</p>
        <h2>SAVE %(nombre)s</h2>
        <dl class="dl">%(filas)s</dl>
        <div class="tags">
          <span class="chip">%(i_auto)s Estacionamiento</span>
          <span class="chip">%(i_llave)s Valet gratis</span>
          <span class="chip">%(i_nino)s Área de niños</span>
          <span class="chip">%(i_tv)s Eventos deportivos</span>
        </div>
        <div class="sucursal__acc" style="border:0;padding-top:6px;gap:10px">%(acc)s</div>
      </div>
      <div class="suc-detalle__mapa">
        <iframe src="%(mapa)s" title="Mapa de Restaurante SAVE %(nombre)s" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </article>""" % dict(s, filas="".join(filas), acc="".join(acciones), mapa=mapa,
                         i_auto=ico("auto", 14), i_llave=ico("llave", 14),
                         i_nino=ico("nino", 14), i_tv=ico("tv", 14)))

    html = head(
        "Sucursales SAVE | Guadalajara, Zapopan, Querétaro y Monterrey",
        "Direcciones, teléfonos, WhatsApp y mapas de las 6 sucursales de mariscos SAVE en "
        "Zapopan, Guadalajara, Querétaro, San Pedro Garza García y Monterrey.",
        "sucursales.html", extra="  " + ld + "\n",
        keywords="mariscos Guadalajara, mariscos Zapopan, mariscos Chapalita, mariscos Querétaro, "
                 "mariscos San Pedro Garza García, mariscos Carretera Nacional Monterrey")

    html += "<body>\n" + header("sucursales.html")

    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/terraza.webp" alt="" width="1400" height="933" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Encuentra tu <em>SAVE</em></h1>
    <p>Seis restaurantes en tres estados. La misma carta, el mismo producto del Mar de Cortés y, en todos, estacionamiento propio, valet parking gratuito y área de niños.</p>
    <div class="pagina-cab__chips">%(indice)s</div>
  </div>
</header>

<section class="seccion" style="padding-top:clamp(48px,6vw,80px)">
  <div class="contenedor">%(bloques)s</div>
</section>

<section class="seccion seccion--osc" style="padding-block:clamp(56px,7vw,90px)">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Lo que encuentras en todas</p>
        <h2 class="titulo">Servicios <em>en sucursal</em></h2>
      </div>
    </div>
    <div class="servicios">%(serv)s</div>
  </div>
</section>

%(faq)s
%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Sucursales", None)]),
       "indice": indice, "bloques": "".join(bloques), "serv": bloque_servicios(),
       "faq": faq_html([
           ("¿Cuál es la sucursal de SAVE más cercana al centro de Guadalajara?",
            "La sucursal de Av. México 3388, en la colonia Monraz, es la más próxima al centro de "
            "Guadalajara. Las de Av. Guadalupe (Chapalita) y Av. Patria (Jardines de Guadalupe, Zapopan) "
            "quedan hacia el poniente de la ciudad."),
           ("¿Hay SAVE en Monterrey?",
            "Sí, en Nuevo León hay dos: una en Calle Valle Sol 101, colonia La Diana, San Pedro Garza "
            "García; y otra sobre Carretera Nacional km 973 n.º 4500, colonia Valle Alto, en Monterrey."),
           ("¿Todas las sucursales tienen estacionamiento?",
            "Sí. Las seis sucursales cuentan con estacionamiento propio y valet parking privado sin costo "
            "para los comensales."),
           ("¿Puedo llegar con niños?",
            "Sí. Todas las sucursales tienen área de niños y un ambiente pensado para ir en familia, "
            "además de áreas separadas de fumadores y no fumadores."),
       ], "Sobre nuestras sucursales"),
       "cta": cta_final("Elige tu sucursal <em>y nos vemos</em>",
                        "Reserva en línea indicando la sucursal, la fecha y el número de personas.",
                        "img/w/salon.webp")}

    html += footer()
    escribe("sucursales.html", html)


# ===========================================================================
# 4. NOSOTROS
# ===========================================================================
def pagina_nosotros():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Nosotros", "nosotros.html")]),
        {"@type": "AboutPage", "@id": SITIO + "/nosotros.html#pagina",
         "url": SITIO + "/nosotros.html", "name": "Historia de Restaurante SAVE",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX",
         "about": {"@id": SITIO + "/#organizacion"}},
        faq_ld([
            ("¿Por qué el restaurante se llama SAVE?",
             "El nombre es un homenaje a Guasave, Sinaloa, el municipio del norte del estado de donde "
             "provienen las recetas y la forma de trabajar el producto que distingue al restaurante."),
            ("¿Qué es la playa Las Glorias?",
             "Las Glorias es la playa de Guasave, en el norte de Sinaloa, sobre el Golfo de California. "
             "De su cocina de palapa vienen las recetas tradicionales que SAVE trajo a Guadalajara."),
        ]),
    ])

    html = head(
        "Nosotros | Restaurante SAVE, de Guasave a tu mesa",
        "SAVE nació como homenaje a Guasave, Sinaloa: recetas de la playa Las Glorias y producto "
        "del Mar de Cortés con calidad de exportación.",
        "nosotros.html", extra="  " + ld + "\n")

    html += "<body>\n" + header("nosotros.html")

    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/playa-glorias.webp" alt="" width="1600" height="893" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Nacimos en la costa, <em>crecimos en la ciudad</em></h1>
    <p>Restaurante SAVE lleva ese nombre en honor a Guasave, Sinaloa. Todo lo demás —las recetas, el producto, el modo de servir— viene del mismo lugar.</p>
  </div>
</header>

<section class="seccion">
  <div class="contenedor split">
    <div class="rv">
      <p class="eyebrow">La propuesta</p>
      <h2 class="titulo">Un sabor <em>diferente</em></h2>
      <p class="bajada" style="margin-top:24px">Ofrecemos una propuesta de sabor distinta, con recetas tradicionales de la <strong>playa Las Glorias</strong> y creaciones gastronómicas originales y exclusivas, tanto en platillos fríos como calientes, pensadas para satisfacer a los paladares más exigentes.</p>
      <p class="bajada" style="margin-top:16px">Nuestros pescados y mariscos son traídos directamente desde el <strong>Mar de Cortés</strong>, lugar donde se obtienen las mejores variedades de México. Calidad de exportación para consumo nacional.</p>
      <p style="margin-top:32px"><a class="enlace" href="menu.html">Explora la carta %(f)s</a></p>
    </div>
    <div class="split__media rv rv-d1">
      <img src="img/w/chef-aguachile.webp" alt="Preparación de aguachile rojo sobre camarón fresco en la cocina de SAVE" width="1100" height="1366" loading="lazy">
      <div class="split__badge"><strong>Las Glorias</strong><span>La playa de Guasave, origen de nuestras recetas</span></div>
    </div>
  </div>
</section>

<section class="seccion seccion--osc">
  <div class="contenedor split">
    <div class="split__media rv">
      <img src="img/w/hero-palapa.webp" alt="Comedor de Restaurante SAVE con techo de palapa y luz cálida" width="1920" height="1072" loading="lazy" style="aspect-ratio:4/5">
    </div>
    <div class="rv rv-d1">
      <p class="eyebrow">El ambiente</p>
      <h2 class="titulo">La palapa, <em>sin perder nada</em></h2>
      <p class="bajada" style="margin-top:24px">Un sabor único, ambiente de playa, la alegría y la hospitalidad de la gente de la región costera del norte de Sinaloa: esos son los factores que quisimos traer a Guadalajara.</p>
      <p class="bajada" style="margin-top:16px">Lo hicimos en un restaurante con todas las comodidades y una atención de primer nivel, con un ambiente 100%% familiar y lo último en tecnología de audio y video, pero sin perder la identidad y el sabor de la palapa.</p>
      <dl class="datos datos--claro">
        <div><dt>6</dt><dd>Sucursales en Jalisco, Querétaro y Nuevo León</dd></div>
        <div><dt>H</dt><dd>Distintivo de manejo higiénico de alimentos</dd></div>
        <div><dt>ESR</dt><dd>Empresa Socialmente Responsable</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Cómo trabajamos</p>
        <h2 class="titulo">Cuatro cosas que <em>no negociamos</em></h2>
      </div>
    </div>
    <div class="exp">
      <article class="exp__item rv rv-d1" style="min-height:360px">
        <img src="img/w/camaron-hielo.webp" alt="Camarón azul fresco sobre hielo" width="1000" height="1000" loading="lazy">
        <span class="exp__num">01</span>
        <h3>El producto manda</h3>
        <p>Si la pesca del día no llega como debe, el platillo no sale. Las piezas enteras se cotizan por kilo justamente por eso.</p>
      </article>
      <article class="exp__item rv rv-d2" style="min-height:360px">
        <img src="img/w/chef-aguachile.webp" alt="Chef preparando aguachile" width="1100" height="1366" loading="lazy">
        <span class="exp__num">02</span>
        <h3>Se cura al momento</h3>
        <p>Los aguachiles, ceviches y tostadas se preparan cuando se ordenan. El limón hace su trabajo en la mesa, no en la cámara.</p>
      </article>
      <article class="exp__item rv rv-d3" style="min-height:360px">
        <img src="img/w/area-ninos.webp" alt="Área de niños en Restaurante SAVE" width="1100" height="832" loading="lazy">
        <span class="exp__num">03</span>
        <h3>Mesa para todos</h3>
        <p>Área de niños, estacionamiento, valet gratis y los partidos en pantalla. Que nadie tenga un motivo para irse temprano.</p>
      </article>
      <article class="exp__item rv rv-d4" style="min-height:360px">
        <img src="img/w/hielo-mariscos.webp" alt="Mariscos frescos sobre hielo" width="1400" height="933" loading="lazy">
        <span class="exp__num">04</span>
        <h3>Calidad de exportación</h3>
        <p>El mismo estándar que se exige para salir del país, servido aquí. Con Distintivo H que lo respalda.</p>
      </article>
    </div>
  </div>
</section>

<section class="seccion seccion--arena" style="padding-block:clamp(56px,7vw,90px)">
  <div class="contenedor certs">%(certs)s</div>
</section>

%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Nosotros", None)]),
       "f": ico("flecha", 15), "certs": bloque_certificaciones(),
       "cta": cta_final("Ven a probar <em>de dónde venimos</em>",
                        "Reserva tu mesa en cualquiera de nuestras seis sucursales.",
                        "img/w/playa-glorias.webp")}

    html += footer()
    escribe("nosotros.html", html)


# ===========================================================================
# 5. EVENTOS
# ===========================================================================
def pagina_eventos():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Eventos", "eventos.html")]),
        {"@type": "WebPage", "@id": SITIO + "/eventos.html#pagina",
         "url": SITIO + "/eventos.html", "name": "Eventos y banquetes en Restaurante SAVE",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX"},
        {"@type": "Service", "name": "Eventos y banquetes en Restaurante SAVE",
         "serviceType": "Banquetes y eventos privados",
         "provider": {"@id": SITIO + "/#organizacion"},
         "areaServed": [{"@type": "City", "name": n} for n in
                        ("Guadalajara", "Zapopan", "Santiago de Querétaro",
                         "San Pedro Garza García", "Monterrey")],
         "hasOfferCatalog": {
             "@type": "OfferCatalog", "name": "Tipos de evento",
             "itemListElement": [
                 {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
                 for n in ("Comidas y cenas de empresa", "Cena navideña de empresa",
                           "Celebraciones familiares", "Bodas y recepciones",
                           "Barra de bar y coctelería")]}},
        faq_ld([
            ("¿SAVE organiza comidas de empresa?",
             "Sí. Atendemos comidas y cenas de empresa con menú cerrado, áreas reservadas dentro del "
             "restaurante y facturación. Se recomienda apartar con anticipación en temporada alta "
             "(noviembre y diciembre)."),
            ("¿Cuántas personas caben en un evento privado?",
             "Depende de la sucursal y del montaje. Escríbenos por WhatsApp con la fecha, el número "
             "aproximado de personas y la ciudad, y te confirmamos qué sucursal se acomoda mejor."),
            ("¿SAVE hace banquetes de boda?",
             "Sí. Ofrecemos menú de banquete de mariscos, montaje y coordinación del servicio para "
             "recepciones de boda."),
        ]),
    ])

    wa = wa_link(SUCURSALES[0]["wa_raw"], "Hola, quisiera cotizar un evento en SAVE.")

    html = head(
        "Eventos y banquetes | Restaurante SAVE",
        "Comidas de empresa, cenas navideñas, celebraciones y bodas con menú de mariscos. "
        "Áreas reservadas en las 6 sucursales de SAVE.",
        "eventos.html", extra="  " + ld + "\n",
        keywords="comida de empresa Guadalajara, cena navideña empresa, banquete de mariscos, "
                 "boda mariscos, eventos privados restaurante")

    html += "<body>\n" + header("eventos.html")

    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/eventos.webp" alt="" width="1400" height="933" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Eventos que se recuerdan <em>por lo que se comió</em></h1>
    <p>Comidas de empresa, cenas navideñas, cumpleaños, bautizos y bodas. Ponemos la cocina, el espacio y el equipo; tú pones el motivo.</p>
    <div class="pagina-cab__chips">
      <a class="chip chip--claro" href="%(wa)s" target="_blank" rel="noopener">%(i_wa)s Cotizar por WhatsApp</a>
      <a class="chip chip--claro" href="#tipos">%(i_flecha)s Ver tipos de evento</a>
    </div>
  </div>
</header>

<section class="seccion" id="tipos">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Qué organizamos</p>
        <h2 class="titulo">Cuatro formatos, <em>una sola cocina</em></h2>
        <p class="bajada" style="margin-top:20px">Cada evento se arma sobre la carta real de SAVE. Nada de menús paralelos: lo que sirve el restaurante es lo que llega a tu mesa.</p>
      </div>
    </div>
    <div class="exp">
      <article class="exp__item rv rv-d1" id="empresa">
        <img src="img/w/eventos.webp" alt="Mesa larga montada para una comida de empresa" width="1400" height="933" loading="lazy">
        <span class="exp__num">01</span>
        <h3>Comidas de empresa</h3>
        <p>Menú cerrado, tiempos definidos y factura. Ideal para cierres de año, juntas de equipo y comidas con clientes.</p>
      </article>
      <article class="exp__item rv rv-d2" id="navidad">
        <img src="img/w/salon.webp" alt="Comedor privado del restaurante" width="1400" height="933" loading="lazy">
        <span class="exp__num">02</span>
        <h3>Cena navideña</h3>
        <p>Diciembre se llena rápido. Aparta con anticipación tu área reservada y define el menú con semanas de margen.</p>
      </article>
      <article class="exp__item rv rv-d3" id="bar">
        <img src="img/w/bar-coctel.webp" alt="Michelada preparada en la barra de SAVE" width="1000" height="1241" loading="lazy">
        <span class="exp__num">03</span>
        <h3>Bar y coctelería</h3>
        <p>Micheladas preparadas, clamatos con camarón, cerveza bien fría y vinos elegidos para acompañar mariscos.</p>
      </article>
      <article class="exp__item rv rv-d4" id="bodas">
        <img src="img/w/bodas.webp" alt="Montaje de recepción de boda junto al mar" width="1400" height="933" loading="lazy">
        <span class="exp__num">04</span>
        <h3>Bodas y recepciones</h3>
        <p>Banquete de mariscos, montaje y coordinación del servicio. Un menú que tus invitados van a comentar por meses.</p>
      </article>
    </div>
  </div>
</section>

<section class="seccion seccion--osc">
  <div class="contenedor split">
    <div class="rv">
      <p class="eyebrow">Cómo se arma</p>
      <h2 class="titulo">De la idea al <em>montaje</em></h2>
      <p class="bajada" style="margin-top:24px">No hay formularios interminables. Un mensaje de WhatsApp con cuatro datos basta para empezar.</p>
      <div class="pasos">
        <div class="paso"><span class="paso__n">1</span><div><h3>Cuéntanos lo básico</h3><p>Ciudad, fecha tentativa, número aproximado de personas y tipo de evento.</p></div></div>
        <div class="paso"><span class="paso__n">2</span><div><h3>Elegimos la sucursal</h3><p>Te decimos cuál se acomoda mejor por capacidad, área reservada y accesos.</p></div></div>
        <div class="paso"><span class="paso__n">3</span><div><h3>Armamos el menú</h3><p>Sobre la carta real: entremeses, fuertes y postre, o barra de mariscos para servicio de pie.</p></div></div>
        <div class="paso"><span class="paso__n">4</span><div><h3>Confirmamos y montamos</h3><p>Cerramos fecha, montaje y tiempos de servicio. El día del evento solo llegas.</p></div></div>
      </div>
      <div style="margin-top:34px;display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn" href="%(wa)s" target="_blank" rel="noopener">Cotizar mi evento %(i_flecha)s</a>
        <a class="btn btn--linea-claro" href="sucursales.html">Ver sucursales</a>
      </div>
    </div>
    <div class="split__media rv rv-d1">
      <img src="img/w/bodas.webp" alt="Recepción montada con mesas y luces cálidas" width="1400" height="933" loading="lazy">
      <div class="split__badge"><strong>6</strong><span>Sucursales disponibles para eventos privados</span></div>
    </div>
  </div>
</section>

<section class="seccion seccion--arena">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">Contacto directo</p>
        <h2 class="titulo">Habla con <em>tu sucursal</em></h2>
        <p class="bajada" style="margin-top:20px">Cada sucursal coordina sus propios eventos. Escribe o llama a la que te queda más cerca.</p>
      </div>
    </div>
    <div class="sucursales">%(sucs)s</div>
  </div>
</section>

%(faq)s
%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Eventos", None)]),
       "wa": wa, "i_wa": ico("wa", 14), "i_flecha": ico("flecha", 15),
       "sucs": bloque_sucursales(False),
       "faq": faq_html([
           ("¿Con cuánta anticipación debo reservar un evento?",
            "Para comidas de grupo, una semana suele bastar. Para cenas navideñas de empresa y bodas "
            "recomendamos contactarnos con uno o dos meses de anticipación, porque noviembre y diciembre "
            "se saturan."),
           ("¿Puedo reservar un área privada?",
            "Sí. Cada sucursal tiene áreas que pueden reservarse para grupos. La capacidad varía según el "
            "restaurante y el montaje; te lo confirmamos al cotizar."),
           ("¿El menú del evento es distinto al del restaurante?",
            "No. Los menús de evento se arman con platillos de la carta real de SAVE, en formato cerrado "
            "de entremés, fuerte y postre, o como barra de mariscos para servicio de pie."),
           ("¿Emiten factura?",
            "Sí, emitimos factura para eventos y consumos de empresa. Solicítala al cerrar la cotización."),
       ], "Sobre eventos en SAVE"),
       "cta": cta_final("Cuéntanos <em>qué estás celebrando</em>",
                        "Un mensaje basta para empezar a armar tu evento.",
                        "img/w/eventos.webp")}

    html += footer()
    escribe("eventos.html", html)


# ===========================================================================
# 6. RESERVAR
# ===========================================================================
def pagina_reservar():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Reservar", "reservar.html")]),
        {"@type": "WebPage", "@id": SITIO + "/reservar.html#pagina",
         "url": SITIO + "/reservar.html", "name": "Reservar mesa en Restaurante SAVE",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX",
         "potentialAction": {"@type": "ReserveAction",
                             "target": {"@type": "EntryPoint", "urlTemplate": RESERVAS,
                                        "inLanguage": "es-MX",
                                        "actionPlatform": ["http://schema.org/DesktopWebPlatform",
                                                           "http://schema.org/MobileWebPlatform"]},
                             "result": {"@type": "FoodEstablishmentReservation",
                                        "name": "Reservación en Restaurante SAVE"}}},
    ])

    opciones = "".join(
        '<option value="%s" data-id="%s"%s>SAVE %s — %s</option>'
        % (s["nombre"], s["id"],
           (' data-wa="%s"' % s["wa_raw"]) if s["wa_raw"] else "",
           s["nombre"], s["ciudad"])
        for s in SUCURSALES)
    wa_default = SUCURSALES[0]["wa_raw"]

    html = head(
        "Reservar mesa | Restaurante SAVE",
        "Reserva tu mesa en SAVE en línea o por WhatsApp. Elige sucursal, fecha, hora y número "
        "de personas en Guadalajara, Querétaro o Monterrey.",
        "reservar.html", extra="  " + ld + "\n")

    html += "<body>\n" + header("reservar.html")

    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/salon.webp" alt="" width="1400" height="933" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Aparta tu <em>mesa</em></h1>
    <p>Reserva en línea las 24 horas o mándanos los datos por WhatsApp. En fines de semana y días festivos conviene apartar con anticipación.</p>
  </div>
</header>

<section class="seccion">
  <div class="contenedor reserva">
    <div class="rv">
      <p class="eyebrow">Dos maneras de hacerlo</p>
      <h2 class="titulo">Rápido, <em>sin llamadas</em></h2>
      <p class="bajada" style="margin-top:22px">Usa el sistema de reservas en línea para confirmar al instante, o llena el formulario y te contestamos por WhatsApp.</p>
      <div class="pasos">
        <div class="paso"><span class="paso__n">1</span><div><h3>Elige sucursal y fecha</h3><p>Tenemos seis restaurantes entre Jalisco, Querétaro y Nuevo León.</p></div></div>
        <div class="paso"><span class="paso__n">2</span><div><h3>Indica cuántos van</h3><p>Si son más de diez personas, escríbenos: es un evento y lo coordinamos aparte.</p></div></div>
        <div class="paso"><span class="paso__n">3</span><div><h3>Confirma</h3><p>Recibes la confirmación y solo tienes que llegar.</p></div></div>
      </div>
      <div style="margin-top:34px;display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn" href="%(res)s" target="_blank" rel="noopener">Reservar en línea %(f)s</a>
        <a class="btn btn--linea" href="eventos.html">¿Es un evento?</a>
      </div>
      <p class="aviso-form" style="margin-top:20px">El sistema de reservas en línea es operado por CoverManager. Se abre en una ventana nueva.</p>
    </div>

    <div class="reserva__panel rv rv-d1">
      <h2 style="font-size:1.5rem;margin-bottom:6px">O mándanos los datos</h2>
      <p style="font-size:.92rem;color:var(--tinta-60);margin-bottom:26px">Se abrirá WhatsApp con tu solicitud lista para enviar.</p>
      <form id="form-reserva" data-wa="%(wa)s">
        <div class="campo">
          <label for="r-sucursal">Sucursal</label>
          <select id="r-sucursal" name="sucursal" required>%(opts)s</select>
        </div>
        <div class="campo-fila">
          <div class="campo"><label for="r-fecha">Fecha</label><input id="r-fecha" name="fecha" type="date" required></div>
          <div class="campo"><label for="r-hora">Hora</label><input id="r-hora" name="hora" type="time" required></div>
        </div>
        <div class="campo-fila">
          <div class="campo"><label for="r-personas">Personas</label><input id="r-personas" name="personas" type="number" min="1" max="20" value="2" required></div>
          <div class="campo"><label for="r-telefono">Teléfono</label><input id="r-telefono" name="telefono" type="tel" autocomplete="tel" placeholder="33 1234 5678" required></div>
        </div>
        <div class="campo"><label for="r-nombre">Nombre</label><input id="r-nombre" name="nombre" type="text" autocomplete="name" placeholder="A nombre de quién" required></div>
        <div class="campo"><label for="r-notas">Notas (opcional)</label><textarea id="r-notas" name="notas" rows="3" placeholder="Silla para bebé, alergias, mesa en terraza…"></textarea></div>
        <button class="btn btn--full" type="submit">Enviar por WhatsApp %(f)s</button>
        <p class="aviso-form">Al enviar aceptas nuestro <a href="aviso-de-privacidad.html" style="color:var(--coral-txt);font-weight:700">aviso de privacidad</a>. No guardamos tus datos en este sitio: el mensaje viaja directo a WhatsApp.</p>
      </form>
    </div>
  </div>
</section>

<section class="seccion seccion--osc" style="padding-block:clamp(56px,7vw,90px)">
  <div class="contenedor">
    <div class="cab">
      <div class="cab__txt rv">
        <p class="eyebrow">O llama directo</p>
        <h2 class="titulo">Teléfonos <em>por sucursal</em></h2>
      </div>
    </div>
    <div class="sucursales">%(sucs)s</div>
  </div>
</section>

%(faq)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Reservar", None)]),
       "res": RESERVAS, "wa": wa_default, "opts": opciones, "f": ico("flecha", 16),
       "sucs": bloque_sucursales(True),
       "faq": faq_html([
           ("¿Es obligatorio reservar en SAVE?",
            "No, aceptamos comensales sin reservación. Pero en fines de semana, puentes y días festivos "
            "la espera puede alargarse, así que reservar es la forma segura de sentarte a la hora que "
            "quieres."),
           ("¿Puedo reservar para un grupo grande?",
            "Para grupos de más de diez personas lo manejamos como evento: escríbenos por WhatsApp o "
            "revisa la página de eventos para coordinar menú y área reservada."),
           ("¿Cómo cancelo o cambio mi reservación?",
            "Si reservaste en línea, usa el enlace de confirmación que recibiste. Si la hiciste por "
            "WhatsApp o teléfono, avisa directamente a la sucursal."),
           ("¿Cuál es el horario del restaurante?",
            "El horario puede variar por sucursal y por temporada. Confírmalo llamando o escribiendo por "
            "WhatsApp a la sucursal donde quieres comer."),
       ], "Sobre las reservaciones")}

    html += footer()
    escribe("reservar.html", html)


# ===========================================================================
# 7. BLOG + POST
# ===========================================================================
POSTS = [
    {
        "slug": "blog-la-marea-regresa-con-fuerza.html",
        "titulo": "La marea regresa con fuerza",
        "fecha": "2026-08-25",
        "fecha_txt": "25 de agosto de 2026",
        "autor": "Emiliano Nájera",
        "img": "img/w/textura-agua.webp",
        "img_w": 1920, "img_h": 823,
        "resumen": ("Si alguna vez has estado en la playa durante la bajamar, habrás notado cómo el "
                    "océano parece rendirse. Lo que viene después explica bastante sobre la vida."),
    },
    {
        "slug": "blog-cena-navidena-de-empresa.html",
        "titulo": "¿Tienes cena navideña de empresa?",
        "fecha": "2025-11-14",
        "fecha_txt": "14 de noviembre de 2025",
        "autor": "Equipo SAVE",
        "img": "img/w/eventos.webp",
        "img_w": 1400, "img_h": 933,
        "resumen": ("Diciembre se llena rápido. Esto es lo que conviene tener resuelto antes de "
                    "apartar la cena de fin de año de tu equipo."),
    },
]


def pagina_blog():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Blog", "blog.html")]),
        {"@type": "Blog", "@id": SITIO + "/blog.html#blog",
         "url": SITIO + "/blog.html", "name": "Blog de Restaurante SAVE",
         "inLanguage": "es-MX", "publisher": {"@id": SITIO + "/#organizacion"},
         "blogPost": [{"@type": "BlogPosting", "headline": p["titulo"],
                       "url": "%s/%s" % (SITIO, p["slug"]), "datePublished": p["fecha"],
                       "author": {"@type": "Person", "name": p["autor"]}} for p in POSTS]},
    ])

    tarjetas = "".join("""<article class="post rv rv-d%(i)d">
      <a href="%(slug)s" class="post__img"><img src="%(img)s" alt="%(titulo)s" width="%(w)d" height="%(h)d" loading="lazy"></a>
      <p class="post__meta">%(fecha)s · %(autor)s</p>
      <h2><a href="%(slug)s">%(titulo)s</a></h2>
      <p>%(resumen)s</p>
      <p><a class="enlace" href="%(slug)s">Seguir leyendo %(f)s</a></p>
    </article>""" % dict(p, i=i + 1, fecha=p["fecha_txt"], w=p["img_w"], h=p["img_h"], f=ico("flecha", 15))
        for i, p in enumerate(POSTS))

    html = head(
        "Blog | Restaurante SAVE",
        "Historias del mar, temporadas de pesca y consejos para organizar comidas de grupo. "
        "El blog de Restaurante SAVE.",
        "blog.html", extra="  " + ld + "\n")

    html += "<body>\n" + header("blog.html")
    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/textura-agua.webp" alt="" width="1920" height="823">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Historias <em>del mar</em></h1>
    <p>Lo que pasa antes de que el producto llegue a la mesa, y algunas cosas que hemos aprendido sirviendo mariscos.</p>
  </div>
</header>

<section class="seccion">
  <div class="contenedor">
    <div class="posts">%(posts)s</div>
  </div>
</section>

%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Blog", None)]), "posts": tarjetas,
       "cta": cta_final("Mejor <em>en persona</em>",
                        "Leer sobre mariscos abre el apetito. Reserva tu mesa.",
                        "img/w/hero-palapa.webp")}
    html += footer()
    escribe("blog.html", html)


def pagina_post_marea():
    p = POSTS[0]
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Blog", "blog.html"), (p["titulo"], p["slug"])]),
        {"@type": "BlogPosting", "@id": "%s/%s#post" % (SITIO, p["slug"]),
         "headline": p["titulo"], "url": "%s/%s" % (SITIO, p["slug"]),
         "datePublished": p["fecha"], "dateModified": p["fecha"],
         "inLanguage": "es-MX",
         "author": {"@type": "Person", "name": p["autor"]},
         "publisher": {"@id": SITIO + "/#organizacion"},
         "image": SITIO + "/img/social/textura-agua.jpg",
         "description": p["resumen"],
         "mainEntityOfPage": {"@id": "%s/%s" % (SITIO, p["slug"])}},
    ])
    html = head(p["titulo"] + " | Blog de Restaurante SAVE", p["resumen"], p["slug"],
                tipo="article", extra="  " + ld + "\n")
    html += "<body>\n" + header("blog.html")
    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/hero-mar.webp" alt="" width="2400" height="1029" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <p class="post__meta" style="color:var(--coral-claro);margin-bottom:14px">%(fecha)s · %(autor)s</p>
    <h1>%(titulo)s</h1>
  </div>
</header>

<section class="seccion">
  <div class="contenedor">
    <article class="articulo rv">
      <p>Si alguna vez has estado en la playa durante la bajamar, habrás notado cómo el océano parece rendirse. El agua retrocede decenas, a veces cientos de metros, dejando al descubierto arena mojada, rocas y un paisaje que parece temporalmente desolado.</p>
      <p>En la vida, todos experimentamos nuestras propias mareas bajas. Temporadas en las que lo que antes era abundante se retira. Proyectos que se detienen, relaciones que se enfrían, negocios que dejan de crecer. La tentación es leer ese vacío como un final.</p>
      <blockquote>La marea baja no se lleva el mar. Solo lo mueve de lugar, y siempre vuelve.</blockquote>
      <h2>Lo que queda al descubierto</h2>
      <p>Los pescadores de Las Glorias lo saben mejor que nadie: la bajamar no es un castigo, es información. Cuando el agua se retira, se ve el fondo. Se ven las piedras, los bancos de arena, los sitios donde conviene tirar la red cuando el agua regrese.</p>
      <p>Las temporadas bajas cumplen la misma función. Enseñan qué sostiene realmente una operación cuando se van los clientes de paso, qué parte del equipo se queda, qué recetas siguen pidiendo los de siempre.</p>
      <h2>Y luego regresa</h2>
      <p>La marea siempre vuelve, y vuelve con fuerza. Trae consigo lo que estaba mar adentro. En nuestro caso, trae el camarón azul, el callo de hacha, el pulpo. La diferencia entre quien aprovecha ese regreso y quien lo deja pasar está en lo que hizo mientras el agua estaba baja.</p>
      <figure>
        <img src="img/w/playa-glorias.webp" alt="Palapa vacía en la playa Las Glorias, Guasave, Sinaloa, al atardecer" width="1600" height="893" loading="lazy">
        <figcaption>La playa Las Glorias, en Guasave, Sinaloa: el origen de nuestras recetas.</figcaption>
      </figure>
      <p>En SAVE llevamos años trabajando con ese ritmo. Sabemos que hay meses en los que la pesca es generosa y otros en los que hay que esperar. Por eso nuestras piezas enteras se cotizan por kilo según lo que llegó ese día: porque respetar la marea es parte del oficio.</p>
      <p>Si estás en tu propia bajamar, ordena el fondo. El agua regresa.</p>
    </article>

    <div style="max-width:70ch;margin:48px auto 0;display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="reservar.html">Reservar mesa %(f)s</a>
      <a class="btn btn--linea" href="blog.html">Volver al blog</a>
    </div>
  </div>
</section>

%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Blog", "blog.html"), (p["titulo"], None)]),
       "fecha": p["fecha_txt"], "autor": p["autor"], "titulo": p["titulo"], "f": ico("flecha", 16),
       "cta": cta_final("El mar <em>ya volvió</em>",
                        "Ven a probar lo que trajo la marea de esta semana.",
                        "img/w/hero-mar.webp")}
    html += footer()
    escribe(p["slug"], html)


def pagina_post_navidad():
    p = POSTS[1]
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Blog", "blog.html"), (p["titulo"], p["slug"])]),
        {"@type": "BlogPosting", "@id": "%s/%s#post" % (SITIO, p["slug"]),
         "headline": p["titulo"], "url": "%s/%s" % (SITIO, p["slug"]),
         "datePublished": p["fecha"], "dateModified": p["fecha"], "inLanguage": "es-MX",
         "author": {"@type": "Organization", "@id": SITIO + "/#organizacion"},
         "publisher": {"@id": SITIO + "/#organizacion"},
         "image": SITIO + "/img/social/eventos.jpg", "description": p["resumen"],
         "mainEntityOfPage": {"@id": "%s/%s" % (SITIO, p["slug"])}},
    ])
    wa = wa_link(SUCURSALES[0]["wa_raw"], "Hola, quisiera cotizar una cena navideña de empresa en SAVE.")
    html = head(p["titulo"] + " | Blog de Restaurante SAVE",
                "Guía breve para organizar la cena navideña de empresa: cuándo apartar, cómo elegir "
                "el menú y qué preguntar antes de confirmar.",
                p["slug"], tipo="article", extra="  " + ld + "\n")
    html += "<body>\n" + header("blog.html")
    html += """<main id="principal">
<header class="pagina-cab">
  <img class="fondo" src="img/w/eventos.webp" alt="" width="1400" height="933" fetchpriority="high">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <p class="post__meta" style="color:var(--coral-claro);margin-bottom:14px">%(fecha)s · %(autor)s</p>
    <h1>%(titulo)s</h1>
  </div>
</header>

<section class="seccion">
  <div class="contenedor">
    <article class="articulo rv">
      <p>Cada año pasa lo mismo: alguien en la oficina se acuerda de la cena de fin de año a mediados de diciembre, cuando ya no quedan mesas. Si te tocó organizarla, estos son los cuatro puntos que conviene resolver primero.</p>
      <h2>1. Aparta antes de decidir el menú</h2>
      <p>La fecha es el recurso escaso, no el menú. En noviembre y diciembre las áreas reservadas se ocupan con semanas de anticipación. Aparta el espacio con un número aproximado de personas y ajusta los detalles después.</p>
      <h2>2. Define si es sentado o de pie</h2>
      <p>Una cena sentada con menú cerrado —entremés, fuerte y postre— funciona cuando hay discursos, entrega de reconocimientos o un grupo que se conoce poco. Una barra de mariscos de pie funciona mejor cuando lo que se busca es que la gente circule.</p>
      <blockquote>Un menú cerrado no significa un menú corto: significa que nadie espera cuarenta minutos por su plato.</blockquote>
      <h2>3. Pregunta por las restricciones del equipo</h2>
      <p>Alergias a mariscos, vegetarianos, quien no toma alcohol. Es una pregunta de treinta segundos en el chat del equipo que evita un problema el día del evento. En SAVE siempre hay alternativa: la sección de cortes finos y las opciones light cubren casi todos los casos.</p>
      <h2>4. Confirma la factura desde el principio</h2>
      <p>Si el gasto va a cuenta de la empresa, pide los datos de facturación al cerrar la cotización, no al final de la noche. Ahorra una conversación incómoda en la caja.</p>
      <figure>
        <img src="img/w/salon.webp" alt="Comedor de Restaurante SAVE preparado para un grupo" width="1400" height="933" loading="lazy">
        <figcaption>Áreas reservadas disponibles en las seis sucursales de SAVE.</figcaption>
      </figure>
      <p>Si ya tienes fecha tentativa y número aproximado de personas, escríbenos y lo armamos contigo.</p>
    </article>

    <div style="max-width:70ch;margin:48px auto 0;display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="%(wa)s" target="_blank" rel="noopener">Cotizar la cena %(f)s</a>
      <a class="btn btn--linea" href="eventos.html">Ver eventos</a>
    </div>
  </div>
</section>

%(cta)s
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Blog", "blog.html"), (p["titulo"], None)]),
       "fecha": p["fecha_txt"], "autor": p["autor"], "titulo": p["titulo"],
       "wa": wa, "f": ico("flecha", 16),
       "cta": cta_final("Diciembre <em>se llena rápido</em>",
                        "Aparta la fecha de tu cena de empresa antes de que se acaben las mesas.",
                        "img/w/eventos.webp")}
    html += footer()
    escribe(p["slug"], html)


# ===========================================================================
# 8. AVISO DE PRIVACIDAD
# ===========================================================================
def pagina_aviso():
    ld = jsonld([
        organizacion_ld(), website_ld(),
        migas_ld([("Inicio", ""), ("Aviso de privacidad", "aviso-de-privacidad.html")]),
        {"@type": "WebPage", "@id": SITIO + "/aviso-de-privacidad.html#pagina",
         "url": SITIO + "/aviso-de-privacidad.html", "name": "Aviso de privacidad",
         "isPartOf": {"@id": SITIO + "/#sitio"}, "inLanguage": "es-MX"},
    ])
    html = head("Aviso de privacidad | Restaurante SAVE",
                "Aviso de privacidad de Restaurante SAVE conforme a la Ley Federal de Protección de "
                "Datos Personales en Posesión de los Particulares.",
                "aviso-de-privacidad.html",
                extra='  <meta name="robots" content="noindex,follow">\n  ' + ld + "\n")
    html += "<body>\n" + header("")
    html += """<main id="principal">
<header class="pagina-cab" style="padding-block:clamp(48px,6vw,80px) clamp(40px,5vw,64px)">
  <div class="contenedor pagina-cab__in">
    %(migas)s
    <h1>Aviso de <em>privacidad</em></h1>
  </div>
</header>

<section class="seccion">
  <div class="contenedor">
    <div class="prosa rv">
      <p><strong>Restaurante SAVE</strong>, con domicilio en Av. Patria 574, Jardines de Guadalupe, 44030 Zapopan, Jalisco, es responsable del tratamiento de tus datos personales conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares.</p>

      <h2>Qué datos recabamos</h2>
      <p>Según el trámite que realices, podemos recabar los siguientes datos:</p>
      <ul>
        <li>Nombre completo y teléfono, cuando solicitas una reservación.</li>
        <li>Correo electrónico, si te suscribes a nuestro boletín de novedades.</li>
        <li>Datos de facturación, cuando lo solicitas para un consumo o evento.</li>
        <li>Preferencias alimentarias o alergias que nos compartes voluntariamente para preparar tu pedido.</li>
      </ul>
      <p>No recabamos datos personales sensibles distintos a los que tú nos proporciones de manera voluntaria para atender tu solicitud.</p>

      <h2>Para qué los usamos</h2>
      <ul>
        <li>Gestionar y confirmar reservaciones de mesa.</li>
        <li>Cotizar, coordinar y ejecutar eventos y banquetes.</li>
        <li>Emitir comprobantes fiscales.</li>
        <li>Enviarte información sobre novedades y promociones, si lo autorizaste.</li>
        <li>Atender dudas, comentarios y quejas.</li>
      </ul>

      <h2>Formulario de reservación de este sitio</h2>
      <p>El formulario de reservación de este sitio <strong>no almacena información en nuestros servidores</strong>: al enviarlo se abre WhatsApp en tu dispositivo con el mensaje precargado, y eres tú quien decide enviarlo. El tratamiento de ese mensaje se rige además por las políticas de WhatsApp.</p>

      <h2>Terceros</h2>
      <p>Utilizamos servicios de terceros que pueden tratar datos por cuenta nuestra o por cuenta propia:</p>
      <ul>
        <li><strong>CoverManager</strong>, para el sistema de reservaciones en línea.</li>
        <li><strong>Uber Eats</strong> y <strong>Rappi</strong>, para pedidos a domicilio.</li>
        <li><strong>Google Maps</strong>, para mostrar la ubicación de las sucursales.</li>
      </ul>
      <p>Cada uno cuenta con sus propios avisos de privacidad, que te sugerimos consultar.</p>

      <h2>Tus derechos ARCO</h2>
      <p>Puedes solicitar en cualquier momento el <strong>acceso, rectificación, cancelación u oposición</strong> al tratamiento de tus datos personales, así como revocar tu consentimiento. Para ejercerlos, escríbenos a la sucursal donde nos proporcionaste tus datos o llama al teléfono publicado en la página de <a href="sucursales.html">sucursales</a>. Responderemos tu solicitud en los plazos que marca la ley.</p>

      <h2>Cambios a este aviso</h2>
      <p>Cualquier modificación a este aviso de privacidad se publicará en esta misma página. Te recomendamos revisarla periódicamente.</p>

      <p style="margin-top:2.5em;color:var(--tinta-40);font-size:.9rem">Última actualización: septiembre de 2026.</p>
    </div>
  </div>
</section>
</main>
""" % {"migas": migas_html([("Inicio", "index.html"), ("Aviso de privacidad", None)])}
    html += footer()
    escribe("aviso-de-privacidad.html", html)


# ===========================================================================
# 9. 404
# ===========================================================================
def pagina_404():
    html = head("Página no encontrada | Restaurante SAVE",
                "La página que buscas no existe. Vuelve al inicio o revisa la carta de SAVE.",
                "404.html", extra='  <meta name="robots" content="noindex,follow">\n')
    html += "<body>\n" + header("")
    html += """<main id="principal">
<section class="hero">
  <div class="hero__panel">
    <div class="hero__panel-in">
      <p class="eyebrow">Error 404</p>
      <h1>Esta página se fue <em>con la marea</em></h1>
      <p class="hero__sub">No encontramos lo que buscabas. Puede que la dirección haya cambiado.</p>
      <div class="hero__acciones">
        <a class="btn" href="index.html">Volver al inicio</a>
        <a class="btn btn--linea-claro" href="menu.html">Ver la carta</a>
        <a class="btn btn--linea-claro" href="sucursales.html">Ver sucursales</a>
      </div>
    </div>
  </div>
  <figure class="hero__foto">
    <img src="img/w/hero-404.webp" alt="Aguachile tatemado de camarón servido en Restaurante SAVE" width="1600" height="1067">
    <figcaption class="hero__pie">
      <strong>Aguachile tatemado</strong>
      <span>Esto sí lo tenemos. Chiles asados al comal para un ahumado profundo.</span>
    </figcaption>
  </figure>
</section>
</main>
"""
    html += footer()
    escribe("404.html", html)


# ===========================================================================
# 10. Archivos auxiliares
# ===========================================================================
def auxiliares():
    paginas = [
        ("", "1.0", "weekly"),
        ("menu.html", "0.9", "monthly"),
        ("sucursales.html", "0.9", "monthly"),
        ("reservar.html", "0.8", "monthly"),
        ("eventos.html", "0.8", "monthly"),
        ("nosotros.html", "0.6", "yearly"),
        ("blog.html", "0.6", "weekly"),
        ("blog-la-marea-regresa-con-fuerza.html", "0.5", "yearly"),
        ("blog-cena-navidena-de-empresa.html", "0.5", "yearly"),
    ]
    urls = "".join(
        "\n  <url><loc>%s/%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>"
        % (SITIO, u, cf, pr) for u, pr, cf in paginas)
    escribe("sitemap.xml",
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s\n</urlset>\n' % urls)

    escribe("robots.txt",
            "User-agent: *\nAllow: /\n\n"
            "# Rastreadores de IA: contenido permitido para citas y respuestas\n"
            "User-agent: GPTBot\nAllow: /\n\n"
            "User-agent: OAI-SearchBot\nAllow: /\n\n"
            "User-agent: ChatGPT-User\nAllow: /\n\n"
            "User-agent: ClaudeBot\nAllow: /\n\n"
            "User-agent: Claude-User\nAllow: /\n\n"
            "User-agent: PerplexityBot\nAllow: /\n\n"
            "User-agent: Google-Extended\nAllow: /\n\n"
            "User-agent: Applebot-Extended\nAllow: /\n\n"
            "Sitemap: %s/sitemap.xml\n" % SITIO)

    # llms.txt — resumen legible por modelos de lenguaje (GEO)
    sucs = "\n".join("- **SAVE %s** — %s%s" % (s["nombre"], s["dir"],
                                               (" · Tel. " + s["tel"]) if s["tel"] else "")
                     for s in SUCURSALES)
    secs = "\n".join("- **%s** (%d platillos): %s" % (c["nombre"], len(c["platos"]),
                                                      c["desc"] or "—") for c in CARTA)
    escribe("llms.txt", """# Restaurante SAVE

> Restaurante de pescados y mariscos de estilo sinaloense, nombrado en honor a Guasave,
> Sinaloa. Sirve recetas tradicionales de la playa Las Glorias y creaciones propias, con
> producto traído directamente del Mar de Cortés con calidad de exportación. Opera seis
> sucursales en Jalisco, Querétaro y Nuevo León (México).

## Datos clave

- **Nombre:** Restaurante SAVE (también "SAVE Restaurante")
- **Tipo de cocina:** pescados y mariscos, cocina sinaloense, cocina mexicana
- **Origen del nombre:** homenaje a Guasave, Sinaloa
- **Origen del producto:** Mar de Cortés (Golfo de California), calidad de exportación
- **Certificaciones:** Distintivo H (Secretaría de Turismo) y Empresa Socialmente Responsable (ESR)
- **Servicios:** restaurante, eventos y banquetes, bar y coctelería, bodas, servicio a domicilio
- **Reservaciones:** en línea vía CoverManager, por teléfono o por WhatsApp
- **A domicilio:** Uber Eats y Rappi
- **En todas las sucursales:** estacionamiento propio, valet parking gratuito, área de niños,
  transmisión de eventos deportivos, áreas de fumadores y no fumadores

## Sucursales

%s

## Secciones de la carta

%s

## Platillos más representativos

Camarones SAVE (capeados en aderezo oriental), aguachile verde/rojo/negro/tatemado,
Chilitaco, Cóctel SAVE especial, pulpo a las brasas, Molcajete Guasaveño (2 personas),
Mariscada SAVE (3 personas), pescado zarandeado, filete Rey, atún cítrico.

## Páginas

- [Inicio](%s/): presentación, especialidades y sucursales
- [Menú](%s/menu.html): carta completa con todas las secciones y descripciones
- [Sucursales](%s/sucursales.html): direcciones, teléfonos, WhatsApp y mapas
- [Reservar](%s/reservar.html): reservación en línea y por WhatsApp
- [Eventos](%s/eventos.html): comidas de empresa, cenas navideñas, bodas y banquetes
- [Nosotros](%s/nosotros.html): historia y origen del restaurante
- [Blog](%s/blog.html)

## Notas

Los precios no se publican en línea porque varían con la temporada de pesca; las piezas
enteras (huachinango, pargo, róbalo, totoaba, langosta) se cotizan por kilo según la pesca
del día.
""" % (sucs, secs, SITIO, SITIO, SITIO, SITIO, SITIO, SITIO, SITIO))

    escribe("site.webmanifest", """{
  "name": "Restaurante SAVE",
  "short_name": "SAVE",
  "description": "Pescados y mariscos de Guasave, Sinaloa. Producto del Mar de Cortés.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FDFAF5",
  "theme_color": "#04202B",
  "lang": "es-MX",
  "icons": [
    {"src": "img/logoinicio.png", "sizes": "256x130", "type": "image/png"}
  ]
}
""")

    escribe("img/favicon.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#04202B"/>
  <path d="M8 34c0-9 9-16 19-16 7 0 13 3 17 8l12-8v32L44 42c-4 5-10 8-17 8C17 50 8 43 8 34z" fill="#F08920"/>
  <circle cx="20" cy="30" r="3" fill="#04202B"/>
</svg>
""")


# ===========================================================================
if __name__ == "__main__":
    print("Generando sitio de Restaurante SAVE…\n")
    pagina_index()
    pagina_menu()
    pagina_sucursales()
    pagina_nosotros()
    pagina_eventos()
    pagina_reservar()
    pagina_blog()
    pagina_post_marea()
    pagina_post_navidad()
    pagina_aviso()
    pagina_404()
    auxiliares()
    print("\nListo.")
