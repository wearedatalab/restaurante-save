# -*- coding: utf-8 -*-
"""Imagenes de ambiente/costa para el rediseno de Restaurante SAVE (fal.ai FLUX)."""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

OUT = r"C:\Users\donju\Desktop\Webs\restaurante-save\img\gen"
KEY = os.environ.get("FAL_KEY")
if not KEY:
    sys.exit("FAL_KEY no encontrada")

NEG = ("no text, no letters, no words, no numbers, no logos, no watermarks, "
       "no signage, no menus, no captions, no ui elements")

PHOTO = ("editorial photography, natural light, cinematic color grading, "
         "shallow depth of field, crisp realistic detail, shot on full frame, " + NEG)

IMAGES = [
    # ---------- HERO ----------
    ("hero-mar", "21:9",
     "cinematic wide aerial view of the Sea of Cortez at golden sunrise, turquoise "
     "and deep teal water, a small traditional mexican fishing panga boat leaving a "
     "white wake, warm orange light on the horizon, distant Sinaloa coastline and "
     "dunes, dramatic atmospheric haze, dark water in the lower half leaving room "
     "for text, " + PHOTO),
    ("hero-palapa", "16:9",
     "warm inviting interior of an upscale modern mexican seafood restaurant at "
     "dusk, high palm thatch palapa ceiling, woven rattan pendant lamps glowing "
     "amber, dark blue painted walls, natural wood tables, lush tropical plants, "
     "soft bokeh of guests in the background, coastal elegant atmosphere, " + PHOTO),

    # ---------- PRODUCTO / ORIGEN ----------
    ("camaron-hielo", "1:1",
     "extreme close up macro of fresh raw blue mexican shrimp on crushed ice with "
     "lime wedges and sea salt, glistening wet shells, cold blue tones with warm "
     "highlights, dark slate background, overhead, " + PHOTO),
    ("pescador", "4:5",
     "weathered mexican fisherman hands holding a large fresh silver snapper just "
     "out of the water on a wooden panga boat at sunrise, salt water drops, rope "
     "and nets, warm backlight over the Sea of Cortez, documentary portrait of the "
     "hands and fish only, " + PHOTO),
    ("hielo-mariscos", "3:2",
     "overhead display of fresh mexican seafood on crushed ice at a coastal market, "
     "octopus, scallops, blue shrimp, whole snapper, limes, cilantro, cold blue "
     "light, moody dark background, " + PHOTO),
    ("chef-aguachile", "4:5",
     "close up of chef hands in a professional kitchen pouring bright red chiltepin "
     "aguachile sauce over raw shrimp arranged on a dark ceramic plate with thin "
     "cucumber and red onion slices, dramatic side light, steam of freshness, "
     "dark moody background, " + PHOTO),
    ("playa-glorias", "16:9",
     "empty rustic palm thatch palapa on the sand at Las Glorias beach Sinaloa "
     "Mexico at golden hour, calm ocean, long shadows, wooden poles, warm nostalgic "
     "coastal mood, wide cinematic, " + PHOTO),

    # ---------- ESPACIOS ----------
    ("salon", "3:2",
     "elegant modern mexican seafood restaurant dining room, warm wood tables set "
     "with white linen, blue leather banquettes, large windows with tropical "
     "greenery outside, woven light fixtures, empty and beautifully lit in the "
     "afternoon, architectural interior photography, " + PHOTO),
    ("terraza", "3:2",
     "beautiful covered outdoor terrace of an upscale coastal mexican restaurant at "
     "blue hour, string lights, rattan chairs, palms, fire pit glow, wooden deck, "
     "warm ambient light, no people, " + PHOTO),
    ("area-ninos", "4:3",
     "bright cheerful childrens play area inside a family friendly mexican "
     "restaurant, colorful soft play structure, nautical decor, plants, warm "
     "afternoon light through windows, no people, " + PHOTO),
    ("deportes", "4:3",
     "stylish restaurant bar corner with large screens showing a soccer match, "
     "warm amber lighting, bottles backlit behind the bar, dark wood and brass, "
     "blurred silhouettes of guests watching, " + PHOTO),

    # ---------- EXPERIENCIAS ----------
    ("eventos", "3:2",
     "long banquet table beautifully set for a private celebration in a coastal "
     "mexican restaurant, white linen, blue and amber floral centerpieces, candles, "
     "palm thatch ceiling, warm golden light, empty and ready, " + PHOTO),
    ("bodas", "3:2",
     "elegant wedding reception dinner setup by the ocean at sunset, round tables "
     "with white linen and tropical flowers, string lights overhead, palms, warm "
     "golden and teal tones, romantic and luxurious, no people, " + PHOTO),
    ("bar-coctel", "4:5",
     "moody close up of a michelada with a shrimp and lime garnish in a frosted "
     "salt rimmed glass on a dark wooden bar, red clamato tones, condensation, "
     "warm amber backlight, bottles bokeh behind, " + PHOTO),
    ("domicilio", "3:2",
     "kraft paper takeout bag and sealed containers of mexican seafood on a dark "
     "wooden counter near a restaurant entrance at dusk, warm interior light behind, "
     "fresh limes beside, clean minimal composition, " + PHOTO),

    # ---------- SOCIAL / OG ----------
    ("og", "16:9",
     "overhead flat lay of a generous mexican seafood spread on a dark rustic wooden "
     "table, aguachile, shrimp cocktail in tall glass, grilled octopus, tostadas, "
     "limes, ice cold beer, deep teal linen napkin, dramatic warm side light, "
     "abundant and appetizing, " + PHOTO),
    ("textura-agua", "21:9",
     "abstract close up of dark deep teal ocean water surface with subtle golden "
     "sunset reflections and gentle ripples, minimal, moody, very dark, " + PHOTO),
]


def gen(item):
    name, ar, prompt = item
    dest = os.path.join(OUT, name + ".jpg")
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        return name, "ya existe"
    body = json.dumps({
        "prompt": prompt,
        "aspect_ratio": ar,
        "num_images": 1,
        "enable_safety_checker": True,
        "safety_tolerance": "5",
        "output_format": "jpeg",
        "raw": False,
    }).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                "https://fal.run/fal-ai/flux-pro/v1.1-ultra", data=body,
                headers={"Authorization": "Key " + KEY,
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.loads(r.read())
            url = data["images"][0]["url"]
            with urllib.request.urlopen(url, timeout=180) as r, open(dest, "wb") as f:
                f.write(r.read())
            return name, "ok %d KB" % (os.path.getsize(dest) // 1024)
        except Exception as e:
            if attempt == 2:
                return name, "ERROR: %r" % e
            time.sleep(4 * (attempt + 1))


with ThreadPoolExecutor(max_workers=5) as ex:
    futs = [ex.submit(gen, it) for it in IMAGES]
    for fu in as_completed(futs):
        n, st = fu.result()
        print("[%s] %s" % (n, st), flush=True)
print("LISTO")
