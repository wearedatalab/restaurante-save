# Restaurante SAVE — rediseño web

Rediseño completo del sitio de **Restaurante SAVE** (mariscos de Guasave, Sinaloa; 6 sucursales
en Jalisco, Querétaro y Nuevo León), partiendo del HTML original de `restaurante-save.mx`.

HTML estático, sin dependencias ni build de JS. Se sube tal cual a cualquier hosting.

**Demo pública:** https://wearedatalab.github.io/restaurante-save/

---

## Qué cambió respecto al sitio original

| Original (WordPress + Visual Composer) | Rediseño |
|---|---|
| Texto de plantilla sin traducir en la home (*"Ristora is a restaurant… Farringdon's Exmouth Market"*) | Sección real de experiencias: Restaurante, Eventos, Bar y coctelería, Bodas |
| Carta solo en PDF y en una página con pestañas | Página `menu.html` con los 126 platillos en HTML, navegable y rastreable |
| Sin datos estructurados | `Organization`, 6 × `Restaurant`, `Menu`, `FAQPage`, `BreadcrumbList`, `BlogPosting`, `Service`, `ReserveAction` |
| Sin `sitemap.xml`, `robots.txt` ni control de rastreadores de IA | Los tres, más `llms.txt` |
| ~40 CSS + ~25 JS de WordPress, imágenes JPG de 1–2 MB | 1 CSS + 1 JS, imágenes WebP; sitio completo **4.8 MB** |
| Sin reserva desde el sitio | Reserva en línea (CoverManager) + formulario que arma el mensaje de WhatsApp de la sucursal elegida |

---

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Home: hero, origen, 12 especialidades, 4 experiencias, 6 sucursales, servicios, domicilio, certificaciones, FAQ |
| `menu.html` | Carta completa: 11 secciones, 126 platillos, navegación sticky con scroll-spy |
| `sucursales.html` | Las 6 sucursales con dirección, teléfono, WhatsApp, servicios y mapa embebido |
| `reservar.html` | Reserva en línea + formulario → WhatsApp (admite `?sucursal=av-patria`) |
| `eventos.html` | Comidas de empresa, cena navideña, bar y coctelería, bodas |
| `nosotros.html` | Historia y origen (texto real del sitio original) |
| `blog.html` + 2 posts | Blog con los artículos existentes reescritos |
| `aviso-de-privacidad.html` | Aviso conforme a la LFPDPPP (noindex) |
| `404.html` | Página de error |

Auxiliares: `sitemap.xml`, `robots.txt`, `llms.txt`, `site.webmanifest`, `img/favicon.svg`.

---

## Pendiente de confirmar con el cliente

**Horarios de atención.** El sitio original no los publica en ninguna página, así que no se
inventaron. Hoy el sitio dice *"Consulta el horario del día llamando a la sucursal o por
WhatsApp"* y el JSON-LD omite `openingHours`.

Para activarlos, edita `_data.py` y vuelve a generar:

```python
HORARIO = [("Mo,Tu,We,Th", "12:00", "21:00"), ("Fr,Sa", "12:00", "23:00"), ("Su", "12:00", "19:00")]
HORARIO_TXT = "Lun a jue 12:00–21:00 · Vie y sáb 12:00–23:00 · Dom 12:00–19:00"
```

Otros puntos a revisar, heredados del sitio original:

- **Av. Guadalupe y Av. Patria comparten el teléfono `33 3629 3124`.** Está así en el sitio
  actual; probablemente sea un error de contenido.
- **Carretera Nacional (Monterrey) no tiene teléfono publicado.**
- **Querétaro, San Pedro y Carretera Nacional no tienen WhatsApp propio**: el formulario de
  reserva cae al número de Av. Patria, indicando la sucursal en el mensaje.
- Los enlaces de Uber Eats y Rappi apuntan a una búsqueda por nombre; conviene cambiarlos por
  las URLs directas de cada tienda.

---

## SEO y GEO

**SEO técnico**

- `<title>` y meta description propias por página, dentro de límites de truncado.
- Canonical, Open Graph y Twitter Card con imagen 1200×630 (`img/og-save.jpg`).
- Un solo `<h1>` por página, jerarquía de encabezados correcta, `alt` en todas las imágenes.
- `width`/`height` en todas las imágenes (evita CLS), `fetchpriority="high"` en el LCP,
  `loading="lazy"` en el resto, WebP en todo el sitio.
- Sitemap y robots.txt.
- Mapas embebidos con `loading="lazy"`.

**Datos estructurados (JSON-LD, un solo `@graph` por página)**

- `Organization` con `sameAs`, `hasCredential` (Distintivo H, ESR) y `areaServed`.
- Seis nodos `Restaurant` con dirección postal, coordenadas, teléfono, `hasMap`,
  `acceptsReservations`, `servesCuisine` y `amenityFeature`.
- `Menu` completo con las 11 `MenuSection` y sus `MenuItem`.
- `FAQPage` en home, menú, sucursales, eventos, nosotros y reservar.
- `BreadcrumbList`, `BlogPosting`, `Service` y `ReserveAction`.

**GEO (optimización para motores generativos)**

- `llms.txt` con el resumen estructurado del negocio, sucursales y carta.
- `robots.txt` permite explícitamente GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot,
  Claude-User, PerplexityBot, Google-Extended y Applebot-Extended.
- Bloques de respuesta directa y autocontenida: cada respuesta de FAQ es una afirmación
  completa y citable, sin depender del contexto de la página.
- Entidades nombradas de forma explícita en el texto (Guasave, Mar de Cortés, playa Las
  Glorias, Distintivo H, cada colonia y municipio) en lugar de referencias vagas.
- La carta vive en HTML, no solo en PDF, para que sea extraíble.

**Accesibilidad**

- Todo el texto cumple contraste AA. El naranja de marca `#F08920` da 2.4:1 sobre el fondo
  claro, así que el texto naranja usa `--coral-txt: #A35407` (5.3:1) sobre fondos claros y
  `#FFA94D` sobre fondos oscuros; los botones naranjas llevan texto en azul profundo (6.5:1).
- Navegación por teclado, `:focus-visible` visible, skip link, `aria-expanded` en menú y FAQ,
  `prefers-reduced-motion` respetado.

---

## Imágenes

- **Fotografía de platillos:** las 12 fotos reales del cliente, recomprimidas a WebP. El hero
  de la home es la foto real de los **Camarones SAVE** (el platillo de la casa) y el del 404 es
  el aguachile tatemado: la primera imagen del sitio es comida, no mar.
- **Ambiente, costa y producto:** 17 imágenes generadas con **FLUX 1.1 Pro Ultra** (fal.ai).
  No se generó ningún platillo: la comida que se muestra es la real del restaurante.
- Originales sin comprimir en `_originales/` (fuera de lo publicable).

---

## Regenerar el sitio

```bash
python _build.py        # genera los 11 HTML + sitemap, robots, llms.txt, manifest
python _optimiza.py     # reconvierte las imágenes a WebP desde _originales/
python _gen_images.py   # vuelve a generar las imágenes de ambiente (requiere FAL_KEY)
```

`_data.py` concentra todo el contenido (sucursales, carta, FAQ, redes). `_shell.py` tiene el
cascarón común (head, header, footer, JSON-LD). `_build.py` arma cada página.

## Previsualizar

```bash
python -m http.server 8827 --directory restaurante-save
```

## Publicar

Sube todo salvo `_originales/`, `__pycache__/` y los `*.py`.

`SITIO` en `_data.py` apunta hoy a la demo de GitHub Pages, que es lo que usan `canonical`,
Open Graph, el sitemap y el JSON-LD. **Al pasar a producción cámbialo a
`https://restaurante-save.mx` y vuelve a ejecutar `python _build.py`.**
