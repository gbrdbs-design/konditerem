#!/usr/bin/env python3
"""Összeállítja a 4 HTML oldalt a közös részekből (fejléc, lábléc, referenciák, GYIK, kapcsolat, 3D).
Futtatás: python3 src/build.py  (a html-proto mappából vagy bárhonnan)"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent

CHECK = '<svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true"><circle cx="14" cy="14" r="14" fill="#009247"/><path d="M8 14.5l4 4 8-9" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CLIP = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11.5l-8.6 8.6a5.5 5.5 0 01-7.8-7.8l8.6-8.6a3.7 3.7 0 015.2 5.2l-8.6 8.6a1.8 1.8 0 01-2.6-2.6l7.9-7.9" fill="none" stroke="#23262d" stroke-width="1.8" stroke-linecap="round"/></svg>'
CHEV = '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="#171717" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_L = '<svg width="36" height="18" viewBox="0 0 36 18" aria-hidden="true"><path d="M35 9H2M9 1L1 9l8 8" fill="none" stroke="#545454" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_R = '<svg width="36" height="18" viewBox="0 0 36 18" aria-hidden="true"><path d="M1 9h33M27 1l8 8-8 8" fill="none" stroke="#545454" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PAGE_L = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PAGE_R = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def menu_links(current=""):
    items = [("Rólunk", "index.html#rolunk", ""), ("Termékek", "kategoria.html", "termekek"),
             ("Referenciák", "index.html#referenciak", ""), ("Kapcsolat", "#kapcsolat", "")]
    lis = []
    for label, href, key in items:
        cur = ' aria-current="page"' if key and key == current else ""
        lis.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return '<ul class="nav__links">' + "".join(lis) + "</ul>"


def header(mode, current="", contact_href="#kapcsolat"):
    links = menu_links(current).replace('href="#kapcsolat"', f'href="{contact_href}"')
    return f'''<header class="site-header site-header--{mode}">
  <div class="container">
    <nav class="nav" aria-label="Fő navigáció">
      <a class="nav__logo" href="index.html" aria-label="konditeremberendezesek.hu – főoldal"><img src="img/logo.png" alt="konditeremberendezesek.hu by VitalForce" width="201" height="81"></a>
      <button class="nav__toggle" type="button" aria-label="Menü" aria-expanded="false"><span></span></button>
      <div class="nav__menu">
        {links}
        <a class="btn" href="{contact_href}">Személyre szabott ajánlatot kérek</a>
      </div>
    </nav>
  </div>
</header>'''


def footer(contact_href="#kapcsolat"):
    links = menu_links().replace('href="#kapcsolat"', f'href="{contact_href}"')
    return f'''<footer class="footer">
  <div class="footer__top">
    <a href="index.html"><img src="img/logo.png" alt="konditeremberendezesek.hu by VitalForce" width="201" height="81"></a>
    <div class="nav__menu">
      {links}
      <a class="btn" href="{contact_href}">Személyre szabott ajánlatot kérek</a>
    </div>
  </div>
  <hr class="footer__rule">
  <p class="footer__copy">A weboldal teljes képi és szöveges tartalma jogvédelem alatt áll! Ezek felhasználása a jogtulajdonos írásos engedélye nélkül tilos!<br>Copyright ©2026 Fitness-Vital Trade Kft.</p>
</footer>'''


def page(title, desc, body, head_mode, current="", contact_href="#kapcsolat"):
    return f'''<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Mulish:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{header(head_mode, current, contact_href)}
{body}
{footer(contact_href)}
<script src="js/main.js"></script>
</body>
</html>
'''


REF_CARD = '''<article class="ref">
  <img src="img/reference.jpg" alt="Modern edzőterem belső tere" loading="lazy" width="590" height="297">
  <dl>
    <div><dt>Projekt:</dt><dd>[referencia neve]</dd></div>
    <div><dt>Helyszín:</dt><dd>[település]</dd></div>
    <div><dt>Típus:</dt><dd>[edzőterem]</dd></div>
    <div><dt>Tartalom:</dt><dd>[tervezés, géppark, szállítás, telepítés]</dd></div>
    <div><dt>Cél:</dt><dd>[teljes géppark csere]</dd></div>
  </dl>
  <a class="btn btn--solid" href="#kapcsolat">Hasonló megoldást szeretnék</a>
</article>'''

REFS = f'''<section id="referenciak" class="container">
  <div class="section-title narrow">
    <p class="eyebrow">Referenciák</p><hr class="rule">
    <h2 class="h2">Korábbi fitneszterem projektjeink</h2>
    <p class="lead">Edzőtermek, szállodák, sportközpontok, stúdiók és intézményi fitneszterek kialakításában egyaránt közreműködtünk. Tekintse meg, milyen megoldásokat valósítottunk meg különböző méretű és célú terekben!</p>
  </div>
  <div class="refs carousel-m" data-carousel="refs-dots">{REF_CARD * 3}</div>
  <div class="dots" id="refs-dots"></div>
</section>'''

FAQS = [
    ("Mennyibe kerül egy komplett edzőterem berendezése?", "A beruházás összege függ a terem méretétől, a gépek számától és kategóriájától, a várható terheléstől, valamint a szállítási és telepítési igényektől. Ezért minden projekthez személyre szabott ajánlatot készítünk."),
    ("Milyen információkra van szükség az ajánlatadáshoz?", "A terem alapterülete és alaprajza, a tervezett felhasználás (edzőterem, hotel, iskola stb.), a várható napi forgalom, a kívánt gépkategóriák és a költségkeret alapján tudunk pontos ajánlatot adni. [Prototípus szöveg]"),
    ("Meglévő helyiséget vagy működő edzőtermet is újraterveznek?", "Igen. Meglévő termek gépparkjának korszerűsítését, bővítését és átrendezését is vállaljuk, a működés zavarását minimalizáló ütemezéssel. [Prototípus szöveg]"),
    ("Alaprajz alapján is készíthető 3D látványterv?", "Igen, a helyiség alaprajza és a főbb méretek alapján elkészítjük a 3D látványtervet, amelyen a gépek elrendezése és a zónák is jól áttekinthetők. [Prototípus szöveg]"),
]


def faq():
    items = []
    for i, (q, a) in enumerate(FAQS):
        open_ = i == 0
        items.append(f'''<div class="faq__item{' is-open' if open_ else ''}">
      <h3><button class="faq__q" type="button" aria-expanded="{str(open_).lower()}" aria-controls="faq-{i}">{q}<span class="faq__icon" aria-hidden="true"></span></button></h3>
      <div class="faq__a" id="faq-{i}"><div><p>{a}</p></div></div>
    </div>''')
    return f'''<section id="gyik" class="container">
  <div class="narrow">
    <div class="section-title"><p class="eyebrow">Gyakori kérdések</p><hr class="rule"><h2 class="h2">Gyakori kérdések a konditerem berendezéséről</h2></div>
    <div class="faq" style="margin-top:20px">
    {"".join(items)}
    </div>
  </div>
</section>'''


CONTACT = f'''<section id="kapcsolat" class="container">
  <div class="contact narrow">
    <div class="contact__info">
      <p class="eyebrow">Ajánlatkérés</p><hr class="rule">
      <h2 class="h2">Tervezze meg velünk leendő edzőtermét!</h2>
      <p class="lead" style="color:#23262d">Küldje el elképzelését, a helyiség alaprajzát vagy a projekt legfontosabb adatait! Kollégáink felveszik Önnel a kapcsolatot, és egy rövid igényfelmérést követően javaslatot készítenek a megfelelő gépparkra és a következő lépésekre.</p>
      <dl class="contact__facts">
        <div><dt>Vevőszolgálat:</dt><dd>Munkanapokon: 9:00 - 16:00</dd></div>
        <div><dt>Telefon:</dt><dd><a href="tel:+36305555555">+36 30 555 5555</a></dd></div>
        <div><dt>E-mail:</dt><dd><a href="mailto:info@konditeremberendezes.hu">info@konditeremberendezes.hu</a></dd></div>
      </dl>
    </div>
    <div class="contact__divider" aria-hidden="true"></div>
    <form class="form" novalidate>
      <div class="field"><label for="f-name">Név</label><input id="f-name" name="name" placeholder="Teljes név" required autocomplete="name"><span class="error">Kérjük, adja meg a nevét.</span></div>
      <div class="field"><label for="f-company">Cégnév</label><input id="f-company" name="company" placeholder="Cégnév" autocomplete="organization"></div>
      <div class="field"><label for="f-email">Email cím</label><input id="f-email" name="email" type="email" placeholder="pl. minta@gmail.com" required autocomplete="email"><span class="error">Kérjük, érvényes e-mail címet adjon meg.</span></div>
      <div class="field"><label for="f-phone">Telefonszám</label><input id="f-phone" name="phone" type="tel" placeholder="+36 30 555 5555" autocomplete="tel"></div>
      <div class="field"><span class="label">Fájl csatolása (alaprajz vagy dokumentum feltöltése)</span>
        <label class="file">{CLIP}<span>Feltöltés a számítógépről</span><input type="file" name="file" accept=".pdf,.jpg,.jpeg,.png,.dwg,.doc,.docx"></label>
        <span class="file-name" aria-live="polite"></span></div>
      <div class="field"><label for="f-msg">Üzenet</label><textarea id="f-msg" name="message" rows="1" placeholder="Rövid üzenet a projektről"></textarea></div>
      <button class="btn btn--solid" type="submit">Üzenet elküldése</button>
      <p class="form__success" role="status">Köszönjük! Üzenetét megkaptuk, kollégánk hamarosan felveszi Önnel a kapcsolatot. (Prototípus – az űrlap nem küld adatot.)</p>
    </form>
  </div>
</section>'''

PLAN3D = '''<section id="3d-tervezes" class="container">
  <div class="plan3d">
    <div class="plan3d__media"><img src="img/3d.jpg" alt="Edzőterem 3D látványterve" loading="lazy" width="797" height="726"></div>
    <div class="plan3d__text">
      <p class="eyebrow">3D tervezés</p><hr class="rule">
      <h2 class="h2">Nézze meg leendő edzőtermét még a megvalósítás előtt!</h2>
      <p class="lead">A megfelelő gépek kiválasztása mellett azok elhelyezése is meghatározó. A 3D látványterv segítségével előre megtervezhetők a különböző edzészónák, a gépek közötti távolságok és a biztonságos közlekedési útvonalak.</p>
      <div class="lead">
        <p><strong>A tervezés során figyelembe vesszük:</strong></p>
        <ul class="plan3d__list" style="margin:var(--body-lh) 0">
          <li>a helyiség méretét és alaprajzát</li>
          <li>az ajtók, ablakok és egyéb építészeti elemek helyét</li>
          <li>a gépek méretét és használatához szükséges mozgásteret</li>
          <li>a kardió-, erősítő- és funkcionális zónák elhelyezését</li>
          <li>a biztonságos és kényelmes teremhasználatot</li>
        </ul>
        <p>Így a telepítéskor a gépek már az előre meghatározott helyükre kerülhetnek, és még a megrendelés előtt módosítható a terem elrendezése.</p>
      </div>
      <a class="btn btn--solid" href="{CONTACT_HREF}">3D látványtervet kérek</a>
    </div>
  </div>
</section>'''

# ---------------- Főoldal ----------------
AREAS = [
    ("ic-weightlifting", "Professzionális edzőtermek", "Nagy terhelésre tervezett kardió és erősítőgépek, teljes gépcsaládok és egységes teremkoncepció újonnan nyíló vagy megújuló edzőtermek számára."),
    ("ic-studio", "Személyi edző és funkcionális stúdiók", "Helytakarékos, többfunkciós megoldások kisebb alapterületre, az edzéskoncepcióhoz és a vendégkörhöz igazítva."),
    ("ic-hotel", "Hotelek, szállodák és apartmanházak", "Esztétikus, egyszerűen kezelhető és megbízható géppark, amely illeszkedik a szálláshely színvonalához és várható vendégforgalmához."),
    ("ic-team", "Vállalati fitnesztermek", "Könnyen használható, változatos edzést biztosító gépek és kiegészítők munkahelyi sport és egészségprogramokhoz."),
    ("ic-school", "Iskolák, közintézmények és sportegyesületek", "Strapabíró, biztonságos és költséghatékony eszközök az intézmény céljaihoz és rendelkezésre álló költségkeretéhez igazítva."),
    ("ic-hospital", "Rehabilitációs és egészségügyi intézmények", "A speciális felhasználási szempontok és az intézmény szakmai elvárásai alapján összeállított kardió és mozgást támogató eszközök."),
]
WHY = [
    ("2006 óta a fitneszpiacon", "Több évtizedes értékesítési, teremkialakítási és üzemeltetési tapasztalatra építjük javaslatainkat."),
    ("Nem katalógusból választunk", "A gépparkot a terem céljához, méretéhez, várható forgalmához és költségkeretéhez igazítjuk."),
    ("Több márka, széles termékkínálat", "Különböző műszaki és pénzügyi igényekre is tudunk megoldást javasolni."),
    ("3D látványtervezés", "Már a megvalósítás előtt áttekinthető a gépek elrendezése és a terem várható megjelenése."),
    ("Országos szervizháttér", "Garanciális és garancián túli javítással, alkatrészellátással és karbantartással támogatjuk partnereinket."),
]
STEPS = [
    ("Igényfelmérés", "Átbeszéljük a terem célját, méretét, célcsoportját, költségkeretét és tervezett nyitási időpontját."),
    ("Szakmai koncepció", "Javaslatot készítünk a géppark összetételére, a termékkategóriákra és a tér funkcionális felosztására."),
    ("Tervezés és ajánlat", "Elkészítjük a javasolt elrendezést, igény szerint a 3D látványtervet, valamint a részletes, személyre szabott árajánlatot."),
    ("Szállítás és telepítés", "A jóváhagyott gépparkot a megállapodás szerinti ütemezéssel leszállítjuk, összeszereljük és elhelyezzük."),
    ("Szerviz és karbantartás", "A gépek átadását követően országos szervizháttérrel és karbantartási szolgáltatással támogatjuk a működést."),
]


def why_card(t, d):
    return f'<div class="why-card"><h3>{CHECK}{t}</h3><p>{d}</p></div>'


FIG = '<img class="why__fig" src="img/vf-fig.png" alt="" width="23" height="86">'


def home():
    areas = "".join(f'<article class="area"><img src="img/{i}.png" alt="" width="80" height="80"><h3>{t}</h3><p>{d}</p></article>' for i, t, d in AREAS)
    steps = "".join(f'<li class="step"><span class="step__num">{n}</span><div class="step__body"><h3>{t}</h3><p>{d}</p></div></li>' for n, (t, d) in enumerate(STEPS, 1))
    more = '<span class="tile__more">Megnézem</span>'
    SM, BR = ' tile__title--sm', '<br>'
    bh = "".join(f'<a class="tile tile--bh" href="kategoria.html"><img src="img/bh-{i}.jpg" alt="" loading="lazy" width="450" height="450"><span class="tile__circle" aria-hidden="true"></span><span class="tile__label"><span class="tile__title{SM * (BR in n)}">{n}</span>{more}</span></a>' for i, n in enumerate(["Cardio", "Funkcionális<br>edzés", "Indoor<br>cycling", "Erősítés"], 1))
    ff = "".join(f'<a class="tile tile--ff" href="kategoria.html"><img src="img/ffittech-{i}.jpg" alt="" loading="lazy" width="340" height="510"><span class="tile__circle"><span class="tile__title">{n}</span></span></a>' for i, n in enumerate(["Erősítés", "Cardio", "Multifunkció"], 1))
    flow = "".join(f'<a class="tile tile--flow" href="kategoria.html"><span class="tile__circle"><span class="tile__title">{n}</span>{more}</span><img src="img/flow-{i}.webp" alt="" loading="lazy" width="400" height="400"></a>' for i, n in enumerate(["Indoor cycles", "Speed Bikes", "Elliptical", "Treadmills"], 1))
    virtu_txt = {
        "Cardio": "Futópadok, szobakerékpárok és elliptikus trénerek hotelek, irodák és kisebb stúdiók mérsékelt terheléséhez.",
        "Fitness": "Súlyzók, rudak, tárcsák, szőnyegek és SMR-eszközök, amelyekkel bármely terem kiegészíthető.",
        "Beltér": "Helytakarékos otthoni és beltéri gépek, amelyek kis alapterületen is teljes értékű edzést adnak.",
    }
    virtu = "".join(f'<a class="tile tile--virtu" href="kategoria.html"><span class="tile__media"><img src="img/virtu-{i}.jpg" alt="" loading="lazy" width="640" height="690"></span><span class="tile__label"><span class="tile__title">{n}</span><span class="tile__rule" aria-hidden="true"></span><span class="tile__desc">{virtu_txt[n]}</span><span class="btn tile__btn">Megnézem</span></span></a>' for i, n in enumerate(["Cardio", "Fitness", "Beltér"], 1))
    body = f'''<section class="hero" aria-label="Bemutatkozás">
  <div class="hero__content">
    <div>
      <h1>Konditerem berendezés<br> a tervezéstől a beüzemelésig</h1>
      <p class="hero__lead">Új edzőtermet nyitna, meglévő gépparkját korszerűsítené, vagy szállodai, vállalati, intézményi fitneszteret alakítana ki? Csapatunk az igényfelméréstől és a 3D látványtervezéstől a megfelelő géppark összeállításán és telepítésén keresztül egészen a szervizelésig támogatja projektjét.</p>
    </div>
    <ul class="hero__tags"><li>Edzőterem</li><li>Hotel</li><li>Közintézmény</li><li>Iskola</li></ul>
    <a class="btn" href="#kapcsolat">Személyre szabott ajánlatot kérek</a>
  </div>
</section>
<main class="stack" style="padding-top:30px">
<section id="rolunk" class="container">
  <div class="about">
    <div class="about__text">
      <div class="section-title left"><p class="eyebrow">Ismerj meg minket</p><hr class="rule"><h2 class="h2">Nem egyszerűen gépeket szállítunk. Jól működő edzőteret tervezünk.</h2></div>
      <div class="lead"><p>Egy fitneszterem sikere nem kizárólag a kiválasztott gépek számán vagy márkáján múlik. Fontos a kardió és erősítőgépek megfelelő aránya, a biztonságos közlekedési útvonalak kialakítása, a rendelkezésre álló terület optimális kihasználása és a várható igénybevételhez megfelelő gépkategória kiválasztása.</p><p style="margin-top:var(--body-lh)"><strong>Csapatunk abban segít, hogy ne egymástól független termékeket vásároljon, hanem átgondolt, egységes és hosszú távon is fenntartható gépparkot alakítson ki.</strong></p></div>
    </div>
    <div class="about__media"><img src="img/about.jpg" alt="Edző sportoló súlytárcsával az edzőteremben" width="1140" height="620"></div>
  </div>
</section>
<section class="container">
  <div class="narrow">
    <div class="section-title"><p class="eyebrow">Felhasználási területek</p><hr class="rule"><h2 class="h2">Milyen fitnesztermek berendezésében segítünk?</h2></div>
    <div class="areas">{areas}</div>
  </div>
</section>
<section id="markak" class="container brands">
  <div class="section-title" style="width:100%">
    <p class="eyebrow">Márkák</p><hr class="rule">
    <h2 class="brands__band">A megfelelő márka a megfelelő felhasználási területhez!</h2>
    <p class="lead"><strong>Nem egyetlen márkát próbálunk minden projektre alkalmazni.</strong><br>A gépeket a várható terhelés, a terem mérete, a célcsoport és a rendelkezésre álló költségkeret alapján választjuk ki.</p>
  </div>
  <div class="brand">
    <div class="brand__head"><img class="brand__logo" src="img/bh-logo.png" alt="BH Fitness" width="348" height="63"><hr class="rule"><p class="lead">Széles körű professzionális kardió, erősítő és funkcionális gépkínálat komplett fitnesztermek kialakításához. Megoldásai nagyobb edzőtermekben, szállodákban, vállalati fitneszterekben és intézményi környezetben egyaránt alkalmazhatók.</p></div>
    <div class="bh-grid">{bh}</div>
    <a class="btn" href="kategoria.html">Megnézem a BH Fitness termékeket</a>
  </div>
  <div class="ffit">
    <div class="ffit__text">
      <img class="ffit__logo" src="img/ffittech-logo.png" alt="FFittech" width="258" height="47"><hr class="rule">
      <p class="lead">Nagy terhelésű, professzionális edzőtermekhez tervezett erősítőgépek, edzőpadok, erőkeretek, többállásos tornyok és kardióberendezések. Masszív kialakításának és kedvező ár-érték arányának köszönhetően komplett gépparkok létrehozásához és meglévő termek korszerűsítéséhez is jó választás.</p>
      <a class="btn" href="kategoria.html">Megnézem a FFittech termékeket</a>
    </div>
    <div class="ffit__mobile">
      <div class="ffit__tiles carousel-m" data-carousel="ff-dots">{ff}</div>
      <div class="dots" id="ff-dots"></div>
      <div class="ffit__mobile-btn" style="margin-top:24px"><a class="btn" href="kategoria.html" style="width:100%">Megnézem a FFittech termékeket</a></div>
    </div>
  </div>
  <div class="brand">
    <div class="brand__head"><img class="brand__logo" src="img/flow-logo.png" alt="Flow Fitness" width="402" height="63"><hr class="rule"><p class="lead">Modern kialakítású professzionális és félprofesszionális kardiógépek, amelyek intenzív használat mellett is kényelmes edzésélményt biztosítanak. Elsősorban kisebb edzőtermekbe, személyi edzőstúdiókba, hotelekbe, vállalati és intézményi fitneszterekbe kínálnak jól alkalmazható megoldást.</p></div>
    <div class="flow-grid">{flow}</div>
    <a class="btn" href="kategoria.html">Megnézem a FlowFitness termékeket</a>
  </div>
  <div class="brand">
    <div class="brand__head"><img class="brand__logo" src="img/virtu-logo.png" alt="VirtuFit" width="402" height="63"><hr class="rule"><p class="lead">Jó ár-érték arányú kardió és erősítőeszközök, valamint súlyzók, rudak, tárcsák és egyéb fitneszkiegészítők széles választéka. Elsősorban kisebb személyi edzőstúdiók, hotelek, iskolák, közintézmények és mérsékeltebb terhelésű fitneszterek gépparkjának kialakításához vagy kiegészítéséhez ajánlott.</p></div>
    <div style="width:100%"><div class="virtu-grid carousel-m" data-carousel="virtu-dots">{virtu}</div><div class="dots" id="virtu-dots"></div></div>
    <a class="btn" href="kategoria.html">Megnézem a VirtuFit termékeket</a>
  </div>
  <p class="lead brands__note">A konkrét márkát és géptípust minden esetben a terem funkciójához, várható forgalmához és az eszközök terhelhetőségéhez igazítjuk. Ennek köszönhetően egy projekten belül akár több márka termékei is kombinálhatók, így műszaki és pénzügyi szempontból egyaránt optimális géppark alakítható ki.</p>
</section>
<section class="why" aria-labelledby="why-title">
  <img class="why__logo" src="img/vf-logo.png" alt="VitalForce – Fitness-Wellness szaküzlet és szerviz" width="253" height="51">
  <div class="why__title"><p>Miért a VitalForce?</p><h2 id="why-title">Tapasztalat a tervezéstől az üzemeltetésig</h2></div>
  <div class="why__row">{why_card(*WHY[0])}{FIG}{why_card(*WHY[1])}{FIG}{why_card(*WHY[2])}</div>
  <div class="why__row">{why_card(*WHY[3])}{FIG}{why_card(*WHY[4])}</div>
</section>
{PLAN3D.replace("{CONTACT_HREF}", "#kapcsolat")}
<section class="container">
  <h2 class="h2" style="text-align:center">Hogyan valósul meg egy edzőterem berendezése?</h2>
  <ol class="steps">{steps}</ol>
</section>
{REFS}
{faq()}
{CONTACT}
</main>'''
    return page("Konditeremberendezések prototípus",
                "Edzőtermek, hotelek, közintézmények és iskolák fitnesztermeinek tervezése, gépparkja, telepítése és szervize.",
                body, "overlay")


def flow_head(title_tag):
    return f'''<div class="brand-head container">
  <img class="brand__logo" src="img/flow-logo.png" alt="Flow Fitness" width="402" height="63"><hr class="rule">
  {title_tag}
</div>'''


def category():
    tiles = "".join('<a class="cat-tile" href="termeklista.html"><img src="img/category-tile.jpg" alt="" loading="lazy" width="635" height="438"><span>Indoor Cycles</span></a>' for _ in range(8))
    body = f'''<main class="stack">
<section>
  {flow_head('<p class="lead narrow">Modern kialakítású professzionális és félprofesszionális kardiógépek, amelyek intenzív használat mellett is kényelmes edzésélményt biztosítanak. Elsősorban kisebb edzőtermekbe, személyi edzőstúdiókba, hotelekbe, vállalati és intézményi fitneszterekbe kínálnak jól alkalmazható megoldást.</p>')}
  <div class="container" style="margin-top:60px"><div class="cat-grid">{tiles}</div></div>
</section>
{REFS}
{faq()}
{CONTACT}
</main>'''
    return page("Flow Fitness kategóriák | konditeremberendezesek.hu", "Flow Fitness termékkategóriák: indoor cycles, speed bikes, elliptical, treadmills.", body, "bar", "termekek")


def product_list():
    card = f'''<article class="product">
  <a href="termek.html"><img src="img/product.jpg" alt="Flow Fitness Perform S2i indoor bike" loading="lazy" width="258" height="258"></a>
  <h2><a href="termek.html">Flow Fitness Perform S2i – félprofesszionális indoor bike szobabicikli</a></h2>
  <div class="badges"><span class="badge badge--green">készleten</span><span class="badge badge--purple">ingyenes szállítás</span></div>
  <p>Indoor bike félprofesszionális használatra.</p>
  <a class="btn" href="termek.html">Részletek</a>
</article>'''
    body = f'''<main class="stack">
<section class="container stack" style="gap:60px">
  <div class="brand-head list-head"><img class="brand__logo" src="img/flow-logo.png" alt="Flow Fitness" width="402" height="63"><hr class="rule"><h1>Indoor Cycles</h1></div>
  <div class="toolbar">
    <p><strong>Összesen:</strong> 12 termék</p>
    <label class="sort"><strong>Rendezés:</strong><select id="sort" aria-label="Rendezés"><option>Ár szerint növekvő</option><option>Ár szerint csökkenő</option><option>Név szerint (A–Z)</option><option>Legújabb elöl</option></select>{CHEV}</label>
  </div>
  <div class="products">{card * 11}</div>
  <nav class="pager" aria-label="Lapozás">
    <button class="pager__arrow pager__arrow--prev" type="button" aria-label="Előző oldal">{PAGE_L}</button>
    <ul class="pager__pages"><li><button type="button" aria-current="page">1</button></li><li><button type="button">2</button></li><li><button type="button">3</button></li><li><span>...</span></li><li><button type="button">12</button></li></ul>
    <button class="pager__arrow pager__arrow--next" type="button" aria-label="Következő oldal">{PAGE_R}</button>
  </nav>
</section>
</main>'''
    return page("Indoor Cycles – Flow Fitness | konditeremberendezesek.hu", "Flow Fitness indoor bike termékek listája.", body, "bar", "termekek", "index.html#kapcsolat")


def product():
    body = f'''<section class="pd-hero">
  <div class="pd-hero__media"><img src="img/product-hero.jpg" alt="Flow Fitness Perform S2i használat közben" width="945" height="690"></div>
  <div class="pd-hero__text">
    <h1>Flow Fitness Perform S2i</h1>
    <div class="pd-hero__body">
      <p class="warranty">3 év garancia!</p>
      <p><strong>Félprofesszionális indoor bike szobabicikli</strong></p>
      <p>A Flow Fitness Perform S2i indoor bike tökéletes választás, ha edzőtermi szintű kardió élményt szeretnél otthon.</p>
    </div>
  </div>
</section>
<main class="stack" style="padding-top:60px">
<div>
  <div class="gallery container">
    <button class="gallery__arrow gallery__arrow--prev" type="button" aria-label="Előző kép">{ARROW_L}</button>
    <div class="gallery__track" data-carousel="gal-dots">
      <img src="img/gallery-1.jpg" alt="Optimális kényelem – ergonomikus kialakítás" width="425" height="425">
      <img src="img/gallery-2.jpg" alt="Flow Fitness Perform S2i oldalnézet" width="425" height="425">
      <img src="img/gallery-3.jpg" alt="Fejlett TFT kijelző és programok" width="425" height="425">
    </div>
    <button class="gallery__arrow gallery__arrow--next" type="button" aria-label="Következő kép">{ARROW_R}</button>
  </div>
  <div class="dots" id="gal-dots"></div>
</div>
<div class="center container"><a class="btn" href="index.html#kapcsolat">Személyre szabott ajánlatot kérek</a></div>
<p class="pd-desc container">A Flow Fitness Perform S2i indoor bike tökéletes választás, ha edzőtermi szintű kardió élményt szeretnél otthon. A masszív kialakítás és a sima hajtás garantálja a stabil és kényelmes edzést, míg az állítható ellenállás lehetővé teszi a személyre szabott terhelést. Az ergonomikus ülés- és kormányállítás biztosítja az ideális testhelyzetet, a csendes működés pedig zavartalan használatot tesz lehetővé. Ideális zsírégetéshez, állóképesség-fejlesztéshez és intenzív edzésekhez is. Ha megbízható, tartós és hatékony szobabiciklit keresel, ez a modell kiváló választás.</p>
<div class="container">
  <section class="tech" aria-labelledby="tech-title">
    <h2 id="tech-title">Technikai adatok</h2>
    <ul>
      <li>Motor teljesítménye: 1,75LE / 1,28KW folyamatos teljesítmény (Digital Drive)</li>
      <li>Johnson Drive system</li>
      <li>Futófelület: 135x42cm</li>
      <li>Futószalag: 1,6mm</li>
      <li>Sebesség: 0,8-15km/h</li>
      <li>Dőlésszög: 0-10%</li>
      <li>Ízületkímélő rendszer: Ideal Zone – VRC (Variable Response Cushioning) ízületkímélő rendszer – Bővebben itt olvashat róla: <a href="http://www.vital-force.hu/futopad-info/horizon-fitness-futopad-izuletkimelo-rendszerek/" target="_blank" rel="noopener">Ízületkímélő</a></li>
    </ul>
    <h3>Kijelző tulajdonságai:</h3>
    <ul><li>3 ablakos LED kijelző</li><li>LED kijelző</li><li>Színes jól megkülönböztethető nyomógombok</li><li>Program direktválasztási lehetőség</li><li>Sebesség gyorsgombok – 4, 8, 12km/h</li><li>Dőlésszög gyorsgombok – 3, 6, 9%</li><li>Energiatakarékos üzemmód</li></ul>
    <h3>Kijelzőn található programok:</h3>
    <ul><li>Összes edzési program: 4 + 23 programvariáns + manuális program</li><li>Kalória cél program</li><li>Testsúlycsökkentő program</li><li>Láb tonizáló program</li><li>10K lépés program</li></ul>
    <h3>Konzolon beállítható adatok:</h3>
    <ul><li>idő</li><li>távolság</li><li>kalória</li><li>pulzus</li><li>profil</li><li>felhasználói adatok</li></ul>
  </section>
</div>
<div class="center container"><a class="btn" href="index.html#kapcsolat">Személyre szabott ajánlatot kérek</a></div>
{PLAN3D.replace("{CONTACT_HREF}", "index.html#kapcsolat")}
</main>'''
    return page("Flow Fitness Perform S2i | konditeremberendezesek.hu", "Flow Fitness Perform S2i félprofesszionális indoor bike szobabicikli – technikai adatok.", body, "bar", "termekek", "index.html#kapcsolat")


if __name__ == "__main__":
    for name, fn in [("index.html", home), ("kategoria.html", category), ("termeklista.html", product_list), ("termek.html", product)]:
        html = fn().replace("carousel-m", "carousel-m")
        (OUT / name).write_text(html, encoding="utf-8")
        print("írva:", OUT / name)
