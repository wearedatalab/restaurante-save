# -*- coding: utf-8 -*-
"""Datos reales de Restaurante SAVE (extraidos del sitio original restaurante-save.mx)."""

# URL base para canonical, Open Graph, sitemap y JSON-LD.
# Demo publicada; al pasar a producción cambia a "https://restaurante-save.mx"
# y vuelve a ejecutar `python _build.py`.
SITIO = "https://wearedatalab.github.io/restaurante-save"
MARCA = "Restaurante SAVE"

# ---------------------------------------------------------------------------
# PENDIENTE DE CONFIRMAR CON EL CLIENTE
# El sitio original no publica horarios. Cuando los tengas, llena HORARIO con
# una lista de tuplas de schema.org, p. ej.:
#   HORARIO = [("Mo,Tu,We,Th", "12:00", "21:00"), ("Fr,Sa", "12:00", "23:00"),
#              ("Su", "12:00", "19:00")]
# y HORARIO_TXT con el texto visible. Mientras esten vacios el sitio invita a
# consultar por WhatsApp y el JSON-LD omite openingHours (no se inventan datos).
# ---------------------------------------------------------------------------
HORARIO = []
HORARIO_TXT = ""

RESERVAS = "https://www.covermanager.com/reservation/module_group/save-group/spanish"
MENU_PDF = "https://restaurante-save.mx/wp-content/uploads/2020/12/MenuSaveWeb.pdf"

REDES = {
    "facebook": "https://www.facebook.com/saveresta",
    "instagram": "https://www.instagram.com/saverestaurant/",
    "twitter": "https://twitter.com/savedemar",
}

DELIVERY = [
    ("Uber Eats", "https://www.ubereats.com/mx/search?q=Restaurante%20Save", "img/ubereats.png"),
    ("Rappi", "https://www.rappi.com.mx/restaurantes/busqueda?q=Restaurante%20Save", "img/rappi.png"),
]

SERVICIOS = [
    ("Estacionamiento propio", "Cajones exclusivos para comensales en todas las sucursales.", "auto"),
    ("Valet parking gratis", "Servicio de valet privado sin costo adicional.", "llave"),
    ("Área de niños", "Zona de juegos vigilada para que la sobremesa dure lo que tenga que durar.", "nino"),
    ("Eventos deportivos", "Transmisión de los partidos en pantallas dentro del restaurante.", "tv"),
    ("Fumadores y no fumadores", "Áreas separadas y ventiladas para cada preferencia.", "aire"),
]

# ---------------------------------------------------------------------------
# Sucursales
# ---------------------------------------------------------------------------
SUCURSALES = [
    {
        "id": "av-patria",
        "nombre": "Av. Patria",
        "ciudad": "Zapopan",
        "estado": "Jalisco",
        "region": "JAL",
        "cp": "44030",
        "calle": "Av. Patria 574, Jardines de Guadalupe",
        "dir": "Av. Patria 574, Jardines de Guadalupe, 44030 Zapopan, Jal.",
        "tel": "33 3629 3124",
        "tel_raw": "+523336293124",
        "wa": "33 1736 2644",
        "wa_raw": "5213317362644",
        "maps": "https://goo.gl/maps/N9isY32A4s3GsAvD6",
        "lat": "20.6690",
        "lng": "-103.4059",
    },
    {
        "id": "av-mexico",
        "nombre": "Av. México",
        "ciudad": "Guadalajara",
        "estado": "Jalisco",
        "region": "JAL",
        "cp": "44670",
        "calle": "Av. México 3388, Monraz",
        "dir": "Av. México 3388, Monraz, 44670 Guadalajara, Jal.",
        "tel": "33 3813 1194",
        "tel_raw": "+523338131194",
        "wa": "33 2595 7625",
        "wa_raw": "5213325957625",
        "maps": "https://goo.gl/maps/rPba4MKgwLKqvvm68",
        "lat": "20.7003",
        "lng": "-103.3923",
    },
    {
        "id": "av-guadalupe",
        "nombre": "Av. Guadalupe",
        "ciudad": "Guadalajara",
        "estado": "Jalisco",
        "region": "JAL",
        "cp": "45030",
        "calle": "Av. Guadalupe 721, Chapalita",
        "dir": "Av. Guadalupe 721, Chapalita, Guadalajara, Jal.",
        "tel": "33 3629 3124",
        "tel_raw": "+523336293124",
        "wa": "33 3006 5241",
        "wa_raw": "5213330065241",
        "maps": "https://goo.gl/maps/2ZLKDVBbvnP1jzgB6",
        "lat": "20.6672",
        "lng": "-103.4009",
    },
    {
        "id": "queretaro",
        "nombre": "Querétaro",
        "ciudad": "Santiago de Querétaro",
        "estado": "Querétaro",
        "region": "QUE",
        "cp": "76127",
        "calle": "Paseo de la República 10874",
        "dir": "Paseo de la República 10874, 76127 Santiago de Querétaro, Qro.",
        "tel": "442 325 0787",
        "tel_raw": "+524423250787",
        "wa": "",
        "wa_raw": "",
        "maps": "https://goo.gl/maps/VBXj2CXnRjreW3hb9",
        "lat": "20.6296",
        "lng": "-100.4059",
    },
    {
        "id": "san-pedro",
        "nombre": "San Pedro",
        "ciudad": "San Pedro Garza García",
        "estado": "Nuevo León",
        "region": "NLE",
        "cp": "66266",
        "calle": "Calle Valle Sol 101, La Diana",
        "dir": "Calle Valle Sol 101, La Diana, San Pedro Garza García, N.L.",
        "tel": "81 8363 5971",
        "tel_raw": "+528183635971",
        "wa": "",
        "wa_raw": "",
        "maps": "https://goo.gl/maps/wApzQX82nJNasvdC6",
        "lat": "25.6540",
        "lng": "-100.3580",
    },
    {
        "id": "carretera-nacional",
        "nombre": "Carretera Nacional",
        "ciudad": "Monterrey",
        "estado": "Nuevo León",
        "region": "NLE",
        "cp": "64988",
        "calle": "Carr. Nacional km 973 N.º 4500, Col. Valle Alto, Nivel 3",
        "dir": "Carr. Nacional km 973 N.º 4500, Col. Valle Alto, Nivel 3, Monterrey, N.L.",
        "tel": "",
        "tel_raw": "",
        "wa": "",
        "wa_raw": "",
        "maps": "https://maps.app.goo.gl/W44DLbDmJpAECDQM6",
        "lat": "25.5556",
        "lng": "-100.2545",
    },
]

# ---------------------------------------------------------------------------
# Platillos destacados (fotografia real del cliente)
# ---------------------------------------------------------------------------
DESTACADOS = [
    ("p-camarones-save-1", "Camarones SAVE", "Capeados en aderezo oriental con un toque de picante.", "El clásico"),
    ("p-aguachile-rojo-1", "Aguachile rojo", "Camarón curtido al momento en limón, chile y pepino.", "Crudo"),
    ("p-pulpo-brasas-1", "Pulpo a las brasas", "240 g de pulpo sellado al carbón, suave por dentro.", "A las brasas"),
    ("p-coctel-grande-1", "Cóctel SAVE especial", "Callo de hacha, camarón, pulpo, caracol y callo de almeja.", "Frío"),
    ("p-chilitaco-1", "Chilitaco", "Tortilla de harina con camarón o marlín, queso y tocino.", "De la casa"),
    ("p-aguachile-tatemado-close-1", "Aguachile tatemado", "Chiles tatemados al comal para un ahumado profundo.", "Crudo"),
    ("p-camarones-philadelphia-1", "Camarones Philadelphia", "Rellenos de queso, empanizados con coco y ajonjolí.", "Caliente"),
    ("p-atun-citrico2-1", "Atún cítrico", "Atún fresco importado en salsa cremosa de cítricos.", "Importado"),
    ("p-chicharron-de-pescado-1", "Chicharrón de pescado", "Trozos de pescado crujientes recién salidos del aceite.", "Para compartir"),
    ("p-camarones-a-las-brasas-1", "Camarones a las brasas", "Con cabeza, 260 g la orden, directo de la parrilla.", "A las brasas"),
    ("p-camarones-aguacate-1-1", "Camarones aguacate", "Sobre guacamole, bañados en salsa de vino blanco y ajo.", "Caliente"),
    ("p-agua-kiwi-fresa-1", "Agua de kiwi con fresa", "Aguas frescas preparadas al momento, sin concentrados.", "Bebida"),
]

# ---------------------------------------------------------------------------
# Carta completa
# ---------------------------------------------------------------------------
CARTA = [
    {
        "id": "entremeses",
        "nombre": "Entremeses",
        "desc": "Para abrir la mesa. Mariscos fríos, molcajetes para compartir y los caldos que despiertan el apetito.",
        "platos": [
            ("Cóctel SAVE especial", "Callo de hacha, callo lobina, camarones ahogados, camarón natural, pulpo, caracol y callo de almeja."),
            ("Molcajete Guasaveño", "Para 2 personas. Callo de hacha, callo lobina, camarones ahogados, camarón natural, pulpo, caracol y callo de almeja."),
            ("Mariscada SAVE", "Para 3 personas. Callo de hacha, camarón natural, pulpo, caracol y aguachile verde y rojo."),
            ("Camarón grande para pelar", ""),
            ("Camarones cucaracha", "Con cáscara o pelados."),
            ("Camarón frito en salsas negras", ""),
            ("Camarón natural", ""),
            ("Pulpo natural", ""),
            ("Cóctel", "Ostión, pulpo o camarón."),
            ("Almeja natural o en ceviche", ""),
            ("Ostiones en su concha", "Órdenes de 6 o 12 piezas."),
            ("Chiles torito", "Chiles güeros rellenos de machaca de camarón o marlín en salsas negras."),
            ("Leche de tigre", "Consomé con camarón picado, cebolla y pepino."),
            ("Leche de tigre Santa Julia", "Consomé con camarón, pulpo, caracol, cebolla, pepino y cilantro."),
            ("Callo de hacha Jayalai", "En salsas negras con tomate y pepino."),
            ("Callo de hacha SAVE especial", "Clamato, cebolla, pepino y chile de árbol."),
        ],
    },
    {
        "id": "tostadas-ceviches",
        "nombre": "Tostadas y ceviches",
        "desc": "El corazón crudo de la costa sinaloense: limón, chile y producto que llegó fresco esa mañana.",
        "platos": [
            ("Aguachile verde, rojo, negro o tatemado", "Camarón curtido al momento. El tatemado lleva chiles asados al comal."),
            ("Aguachile de mango", ""),
            ("Tostada de pescado", "Trozos de pescado curtidos en limón."),
            ("Tostada de camarón", "Camarón curtido en limón."),
            ("Tostada de camarón cocido", ""),
            ("Campechano", "Pescado curtido en limón, camarón y pulpo cocido."),
            ("SAVE peruano", "Callo de hacha, camarón y pescado en salsa cremosa de jalapeño."),
            ("SAVE especial de camarón o pulpo", "Clamato, cebolla, pepino y chile de árbol."),
            ("Tropical", "Camarón cocido, mango, fresa y un toque agridulce."),
            ("Primavera", "Camarón curtido en limón, cebolla, cilantro, pepino y un toque de habanero."),
            ("Camarón tempura", "Montados sobre tostadita crocante en cama de aguacate oriental."),
            ("Tostada de marlín", ""),
            ("Lomo de atún", "Machaca de atún importado."),
            ("Jaiba natural", ""),
            ("Casaleña especial", "Pulpa de jaiba, camarón, pulpo, callo de almeja, callo de hacha y caracol."),
            ("Crocante de atún", "Con vinagreta de aceite de ajonjolí, aguacate y cebolla curtida."),
            ("Atún cítricos", "Atún fresco importado en salsa de cítricos, coronado con poro frito y mayonesa."),
        ],
    },
    {
        "id": "tacos",
        "nombre": "Variedades del taco",
        "desc": "De la tortilla de harina del norte al vampiro y la costra de queso. Los que se piden de dos en dos.",
        "platos": [
            ("Chilitaco", "En tortilla de harina relleno de camarón o marlín con queso y envuelto en tocino."),
            ("Taco Mochomito Don Manuel", "Machaca de camarón o pescado mochomito sobre costra de queso, aguacate y aderezo chipotle."),
            ("Gober", "Machaca de camarón con queso a la plancha."),
            ("Gober 300", "Machaca de camarón con queso adobado a las brasas, con salsa chipotle."),
            ("Pescado al pastor", ""),
            ("Pescado capeado", ""),
            ("Vampiro de pescado al pastor", ""),
            ("Lorenza de pescado al pastor", ""),
            ("Taco de atún", "Machaca de atún con queso a las brasas."),
            ("Taco de salmón", "Frito en cama de guacamole con un toque de salsa Gus."),
            ("Taco de marlín", "Machaca de marlín con queso a las brasas o plancha."),
            ("Pulpo Campeche", ""),
            ("Pulpo premium", "Pulpo a las brasas con queso dorado y champiñones al ajillo."),
            ("Mexicano", "Camarón, pulpo o pescado en tortilla de harina con aderezos y salsa mexicana."),
            ("Camarón capeado", ""),
            ("Vallarta", "En tortilla de harina relleno de jaiba y queso, bañado en salsa chipotle."),
        ],
    },
    {
        "id": "camaron",
        "nombre": "Camarón estilo SAVE",
        "desc": "Quince maneras de entender el mismo camarón azul del Mar de Cortés. Aquí viven los clásicos de la casa.",
        "platos": [
            ("Camarones SAVE", "Capeados en aderezo oriental con un toque de picante."),
            ("Camarones Philadelphia", "Rellenos de queso philadelphia, empanizados con coco y ajonjolí, con salsa de mango."),
            ("Camarones Doña Pelancha", "Con tocino, cebolla, champiñones y espinacas a la crema."),
            ("Camarones Puerto Rico", "Empanizados con coco en salsa de mango."),
            ("Camarones Manta", "Rellenos de queso philadelphia y jamón, empanizados con pistache."),
            ("Camarones Danny", "A la crema con chile poblano, horneados al gratín."),
            ("Camarones enchipotlados", "Horneados al gratín con salsa de chile guajillo, chipotle y champiñón."),
            ("Camarones almendrados", "Costra de almendras, relleno de philadelphia, con dúo de salsas oriental y almendras."),
            ("Camarones aguacate", "Montados en base de guacamole, bañados en salsa de vino blanco y ajo."),
            ("Camarones Guanajuato", "Rellenos de queso y envueltos en tocino."),
            ("Camarones rellenos", "Rellenos de marlín y queso, envueltos en tocino."),
            ("Camarones mantequilla o mojo de ajo", ""),
            ("Camarones a la diabla", ""),
            ("Camarones empanizados", ""),
            ("Camarones al ajillo", ""),
        ],
    },
    {
        "id": "brasas",
        "nombre": "Zarandeados y a las brasas",
        "desc": "El fuego de la palapa. Piezas enteras, lonjas y langostinos que se cotizan por kilo según la pesca del día.",
        "platos": [
            ("Lonja a las brasas", "340 g."),
            ("Lonja Pelancha Michelle", "A las brasas, bañada en salsa cremosa con tocino, espinaca y champiñón."),
            ("Volcán marino", "Lonja a las brasas con banderillas de camarón en salsa de ajo."),
            ("Filete a las brasas", "240 g."),
            ("Camarones con cabeza a las brasas", "260 g la orden."),
            ("Pulpo a las brasas", "240 g."),
            ("Ostiones a las brasas", "8 piezas."),
            ("Langostinos especial a las brasas", "700 g."),
            ("Huachinango, pargo o róbalo", "A las brasas o frito. Por kilo."),
            ("Totoaba", "Zarandeada o frita. Por kilo."),
            ("Salmón a las brasas o plancha", "280 g en salsa de mango, tamarindo o mantequilla."),
            ("Salmón Martell especial", "280 g con banderillas de camarón y pulpo, bañado en salsa de manzana."),
            ("Cola de langosta Termidor o Puerto Nuevo", "Por kilo."),
        ],
    },
    {
        "id": "filetes",
        "nombre": "Filetes y especialidades",
        "desc": "Rellenos, gratinados y bañados. La cocina caliente de SAVE en su versión más ambiciosa.",
        "platos": [
            ("Filete Rey", "260 g horneado, relleno de tocino, champiñón y camarón al gratín con un toque de picante."),
            ("Filete Tamazula", "260 g relleno de camarón, pulpo, queso philadelphia y salsa bechamel al gratín."),
            ("Filete Doña Olivia", "260 g relleno de camarón, philadelphia, champiñón y espinacas en salsa bechamel al gratín."),
            ("Filete Caribeño", "260 g horneado al gratín, relleno de camarón, pulpo y marlín."),
            ("Filete Tres Ilusiones", "300 g relleno de camarón, espinaca, champiñones, nuez y philadelphia, bañado en salsa de tres quesos."),
            ("Filete relleno a la diabla", "300 g relleno de queso cheddar con pimiento y espinaca, bañado en salsa diabla."),
            ("Filete Doña Aída", "280 g a la plancha con tocino y camarón al gratín."),
            ("Filete relleno", "260 g relleno de camarón, pulpo y marlín, capeado y bañado en aderezo Aurora."),
            ("Filete agridulce", "En costra de almendra, bañado con salsa oriental y montado sobre puré."),
            ("Atún de dos gotas de agua", "Medallón a las brasas o sellado, gratinado, bañado en salsa de vino blanco y ajo."),
            ("Atún cítrico", "Medallón a las brasas o sellado, bañado en salsa cremosa de cítricos."),
            ("Salmón al portobello", "A la plancha sobre guiso de portobello con pimientos, bañado en crema de camarón al cognac."),
            ("Filete a la diabla", ""),
            ("Filete de pescado", ""),
            ("Filete empanizado", ""),
        ],
    },
    {
        "id": "pulpo",
        "nombre": "Pulpo estilo SAVE",
        "desc": "Pulpo suave, guisado o al fuego, con tres personalidades distintas.",
        "platos": [
            ("Pulpo Rey Loco", "Guisado con marlín ahumado, camarón y salsa de soya."),
            ("Pulpo a la diabla", ""),
            ("Pulpo al mojo o mantequilla", ""),
        ],
    },
    {
        "id": "light",
        "nombre": "Light",
        "desc": "Al vapor, a la plancha y en ensalada: la misma materia prima, sin capeado ni crema.",
        "platos": [
            ("Taco de lechuga", "Camarón, jícama y zanahoria guisados con mojo de ajo."),
            ("Filete Soto Light", "300 g relleno de camarón y vegetales, bañado en salsa light."),
            ("Filete empapelado", "350 g de filete al vapor con camarón, pulpo y vegetales."),
            ("Ensalada Michelle", ""),
            ("Ensalada Michelle especial", "Con pollo, pescado, res o camarón."),
        ],
    },
    {
        "id": "cortes",
        "nombre": "Cortes finos",
        "desc": "Porque no toda la mesa viene por mariscos.",
        "platos": [
            ("Rib Eye", "370 g."),
            ("Vacío", "320 g."),
            ("Arrachera", "320 g."),
            ("Molcajete mar y tierra", "Arrachera y camarón gratinado."),
        ],
    },
    {
        "id": "extras",
        "nombre": "Guarniciones",
        "desc": "",
        "platos": [
            ("Papa SAVE famosa", ""),
            ("Pan con ajo", "5 piezas."),
            ("Orden de arroz", ""),
            ("Orden de frijoles", ""),
            ("Orden de aguacate", ""),
            ("Orden de guacamole", ""),
            ("Puré de papa", ""),
            ("Papas fritas", ""),
            ("Ensalada fresca", ""),
            ("Ensalada americana", ""),
        ],
    },
    {
        "id": "postres",
        "nombre": "Postres",
        "desc": "",
        "platos": [
            ("Pastel de tres leches", ""),
            ("Volcán de chocolate o dulce de leche", ""),
            ("Pastel de queso con zarzamora", ""),
            ("Crème brûlée", ""),
            ("Jericalla", ""),
            ("Flan napolitano", ""),
            ("Pay de guayaba", ""),
            ("Pay de plátano", ""),
            ("Pastel de chocolate", ""),
            ("Arroz con leche", ""),
            ("Pastel de elote", "Endulzado con Splenda."),
            ("Helados", "Vainilla, chocolate, fresa, coco o limón."),
        ],
    },
]

# ---------------------------------------------------------------------------
# Preguntas frecuentes (clave para SEO y para respuestas de IA)
# ---------------------------------------------------------------------------
FAQ_HOME = [
    ("¿Dónde están los restaurantes SAVE?",
     "SAVE tiene seis sucursales en México: tres en la Zona Metropolitana de Guadalajara "
     "(Av. Patria en Zapopan, Av. México en Monraz y Av. Guadalupe en Chapalita), una en "
     "Santiago de Querétaro sobre Paseo de la República, y dos en Nuevo León "
     "(San Pedro Garza García y Carretera Nacional en Monterrey)."),
    ("¿Qué tipo de comida sirve SAVE?",
     "SAVE es un restaurante de pescados y mariscos de estilo sinaloense. La carta combina "
     "recetas tradicionales de la playa Las Glorias, en Guasave, con creaciones propias: "
     "aguachiles, cócteles, tostadas, tacos de mariscos, camarones en quince preparaciones, "
     "pescados zarandeados a las brasas y cortes finos."),
    ("¿De dónde vienen los pescados y mariscos?",
     "Llegan directamente del Mar de Cortés, la zona de donde proceden las mejores variedades "
     "de México. Es producto con calidad de exportación que se destina al consumo nacional."),
    ("¿Necesito reservación?",
     "No es obligatoria, pero sí recomendable en fines de semana y días festivos. Puedes "
     "reservar en línea las 24 horas desde este sitio o llamar directamente a la sucursal "
     "que prefieras."),
    ("¿SAVE tiene servicio a domicilio?",
     "Sí. Puedes pedir a domicilio a través de Uber Eats y Rappi en las ciudades donde "
     "operamos, o llamar a tu sucursal para ordenar para llevar."),
    ("¿Es un restaurante para ir en familia?",
     "Sí. Todas las sucursales cuentan con área de niños, estacionamiento propio, valet parking "
     "gratuito, áreas de fumadores y no fumadores, y transmisión de eventos deportivos."),
    ("¿SAVE organiza eventos y comidas de empresa?",
     "Sí. Atendemos comidas de empresa, celebraciones familiares, cenas navideñas, bodas y "
     "banquetes. Escríbenos por WhatsApp a la sucursal de tu elección para armar un menú y "
     "cotizar el espacio."),
    ("¿Qué certificaciones tiene el restaurante?",
     "SAVE cuenta con el Distintivo H, el reconocimiento de la Secretaría de Turismo a los "
     "establecimientos que cumplen los estándares de manejo higiénico de alimentos, y con el "
     "distintivo ESR de Empresa Socialmente Responsable."),
]
