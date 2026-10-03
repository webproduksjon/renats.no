#!/usr/bin/env python3
"""Rebuild static pages in place. Default output is the GitHub Pages staging site.

Set SITE_ORIGIN=https://webproduksjon.no only when preparing files for the final host.
The origin includes the project path on GitHub Pages, but not on the final host.
"""
from __future__ import annotations

import html
import json
import os
import posixpath
import re
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = os.environ.get("SITE_ORIGIN", "https://webproduksjon.github.io/renats.no").rstrip("/")
assert ORIGIN.startswith("https://") and not ORIGIN.endswith("/renats.no/")
CONTENT = ROOT / "_content"

# A distinct search task and description for each primary route.
PAGES: dict[str, tuple[str, str, str, str]] = {
    "index.html": ("Nettsider for små bedrifter fra 4 990 kr | Renat", "Enkle, profesjonelle nettsider for små bedrifter. Se priser fra 4 990 kr, ett ekte prosjekt og en skriftlig vei til et konkret forslag.", "nettsider for små bedrifter, enkel nettside bedrift, lage nettside bedrift, rimelig nettside", "index.html"),
    "tjenester/index.html": ("Nettsider for bedrifter | Landingsside eller firmaside", "Velg landingsside fra 4 990 kr eller en liten bedriftsnettside fra 7 990 kr. Ryddig innhold, mobilvennlig design og tydelig kontakt.", "nettside bedrift, landingsside bedrift, enkel firmaside, webdesign småbedrifter", "tjenester.html"),
    "tjenester/landingsside.html": ("Landingsside for bedrift fra 4 990 kr | Renat", "En fokusert landingsside for én tjeneste eller ett tilbud. Se hva som inngår, når løsningen passer og hva den koster.", "landingsside bedrift, lage landingsside, landingsside pris, nettside for tjeneste", "landingsside.html"),
    "tjenester/enkel-nettside.html": ("Enkel nettside for bedrift fra 7 990 kr | Renat", "En enkel bedriftsnettside med tydelige tjenester, mobiltilpasset design og enkel kontaktvei. Se innhold, pris og prosess.", "enkel nettside bedrift, hjemmeside liten bedrift, rimelig firmaside, nettside pris", "enkel-nettside.html"),
    "tjenester/nettside-for-sma-bedrifter.html": ("Nettside for små bedrifter | Innhold og pris", "En nettside for små bedrifter med relevante tjenestesider, god struktur og tydelig kontakt. Fra 7 990 kr for en liten flersidig løsning.", "nettside for små bedrifter, hjemmesider småbedrifter, nettside tjenester, søkemotoroptimalisering bedrift", "nettside-for-sma-bedrifter.html"),
    "priser.html": ("Hva koster en nettside for bedrift? Se priser", "Landingsside fra 4 990 kr og liten bedriftsnettside fra 7 990 kr. Les hva som inngår, tillegg, levering, betaling og eierskap.", "nettside pris bedrift, hjemmeside pris, billig nettside bedrift, landingsside pris", "priser.html"),
    "prosess.html": ("Lage nettside for bedrift | Slik jobber jeg", "Se hvordan en liten bedriftsnettside blir til: fra skriftlig forespørsel og prisforslag til design, tilbakemelding og levering.", "lage nettside bedrift, nettside prosess, webdesigner samarbeid, bestille nettside", "prosess.html"),
    "om.html": ("Om Renat | Nettsider for små bedrifter", "Møt Renat bak webproduksjon.no. Jeg bruker Manus AI som verktøy, jobber digitalt med norske bedrifter og viser ett ekte kundeprosjekt.", "Renat webproduksjon, webdesigner småbedrifter, nettsider med AI, norsk nettside", "om.html"),
    "kontakt.html": ("Kontakt | Få forslag til nettside for bedriften", "Fortell kort om bedriften og få et skriftlig forslag til en enkel nettside. Du trenger ikke ringe eller ha en ferdig prosjektbeskrivelse.", "kontakt webdesigner, tilbud nettside bedrift, prisforespørsel nettside, bestille hjemmeside", "kontakt.html"),
    "prosjekter/index.html": ("Nettside for ABC Bygg AS | Ett ekte prosjekt", "Se en faktisk nettside laget for ABC Bygg AS: struktur, design og kontaktvei. Ett dokumentert kundeprosjekt, ingen oppdiktede resultater.", "nettside byggbedrift, webdesign prosjekt, ABC Bygg nettside, nettside for håndverker", "prosjekter.html"),
    "bransjer/index.html": ("Nettsider for håndverkere og små bedrifter", "Slik kan nettsider tilpasses elektrikere, snekkere, rørleggere, malere og konsulenter. Bransjeeksempler, ikke oppdiktede kundeprosjekter.", "nettside håndverker, nettside elektriker, nettside snekker, nettside rørlegger", "bransjer.html"),
    "ressurser/index.html": ("Guider om nettsider for små bedrifter | Renat", "Få svar om pris, antall sider, innhold og domene før du bestiller nettside til bedriften. Praktiske guider og eksempler.", "hva koster nettside, antall sider bedrift, første nettside bedrift, domene webhotell", "ressurser.html"),
    "demos/index.html": ("Konseptdemoer for nettsider | Fiktive eksempler", "Se tydelig merkede konseptdemoer for elektriker, snekker og rørlegger. Eksemplene er fiktive, ikke kundeprosjekter.", "nettside konseptdemo, elektriker nettside eksempel, snekker nettside eksempel", "demos.html"),
    "gratis-nettsidekonsept.html": ("Få forslag til nettside for bedriften | Renat", "Få en uforpliktende vurdering av passende omfang og pris for bedriftens nettside. Designarbeid avtales før oppstart.", "forslag nettside, nettside tilbud, enkel firmaside pris", "gratis-nettsidekonsept.html"),
    "personvern.html": ("Personvern og kontaktskjema | Webproduksjon.no", "Les hvordan webproduksjon.no behandler henvendelser, e-post og opplysninger sendt gjennom FormSubmit.", "personvern kontaktskjema, webproduksjon personvern, FormSubmit", "personvern.html"),
    "takk.html": ("Takk for meldingen | Webproduksjon.no", "Informasjon etter innsending av en forespørsel om nettside.", "kontakt bekreftelse, melding sendt, webproduksjon", "takk.html"),
    "404.html": ("Fant ikke siden | Webproduksjon.no", "Denne adressen finnes ikke. Gå til forsiden eller se tjenestene våre.", "side finnes ikke, nettside 404, webproduksjon", "404.html"),
}

LEGACY_TITLES = {
    "ressurser/elektriker-akutt-og-planlagt.html": "Elektriker: akutt eller planlagt arbeid på nettsiden",
    "ressurser/hva-koster-en-nettside-for-en-liten-bedrift.html": "Hva koster en nettside for en liten bedrift?",
    "ressurser/rorlegger-akutt-planlagt.html": "Rørlegger: akutt eller planlagt arbeid på nettsiden",
    "ressurser/snekker-for-tilbud.html": "Snekker: hva bør nettsiden vise før et tilbud?",
    "ressurser/hvor-mange-sider-trenger-liten-bedrift.html": "Denne guiden er flyttet | Webproduksjon.no",
}

NOINDEX = {"404.html", "takk.html", "personvern.html", "blogg/index.html", "konsept-kontakt.html", "gratis-nettsidekonsept.html", "demos/index.html", "demos/elektriker/index.html", "demos/snekker/index.html", "demos/rorlegger/index.html", "ressurser/hvor-mange-sider-trenger-liten-bedrift.html", "ressurser/nettside-for-elektriker/index.html", "ressurser/nettside-for-snekker/index.html"}
ALTERNATE = {"blogg/index.html": "ressurser/index.html", "konsept-kontakt.html": "kontakt.html", "ressurser/hvor-mange-sider-trenger-liten-bedrift.html": "ressurser/hvor-mange-sider-trenger-en-liten-bedrift/index.html", "ressurser/nettside-for-elektriker/index.html": "bransjer/elektriker/index.html", "ressurser/nettside-for-snekker/index.html": "bransjer/snekker/index.html"}
LABELS = {"index.html": "Forside", "tjenester/index.html": "Tjenester", "bransjer/index.html": "Bransjer", "ressurser/index.html": "Ressurser", "prosjekter/index.html": "Prosjekt", "priser.html": "Priser", "prosess.html": "Arbeidsmåte", "om.html": "Om Renat", "kontakt.html": "Kontakt", "personvern.html": "Personvern"}


def route(path: str) -> str:
    if path == "index.html":
        return "/"
    if path.endswith("/index.html"):
        return "/" + path[:-10]
    return "/" + path


def href(source: str, target: str) -> str:
    """Relative URL between two files, preserving directory-style routes."""
    start = posixpath.dirname(source) or "."
    if target.endswith("/"):
        result = posixpath.relpath(target.rstrip("/"), start)
        return ("./" if result == "." else result + "/")
    result = posixpath.relpath(target, start)
    return result if result != "index.html" or source != "index.html" else "./"


def canonical(path: str) -> str:
    return ORIGIN + route(path)


def tokens(text: str, path: str) -> str:
    text = text.replace("{{origin}}", html.escape(ORIGIN, quote=True))
    def replace(match: re.Match[str]) -> str:
        kind, target = match.group(1), match.group(2)
        assert kind in {"link", "asset"}
        return html.escape(href(path, target), quote=True)
    return re.sub(r"\{\{(link|asset):([^}]+)\}\}", replace, text)


def fix_legacy(soup: BeautifulSoup, path: str) -> str:
    main = soup.select_one("main")
    if not main:
        return "<section class='reading-section'><h1>Siden er flyttet</h1><p>Se <a href='" + href(path, "ressurser/") + "'>ressursene våre</a>.</p></section>"
    for nav in main.select(".breadcrumbs"):
        nav.decompose()
    for link in main.select('a[href*="gratis-nettsidekonsept"]'):
        link["href"] = href(path, "kontakt.html")
        link.string = "Få et skriftlig forslag ↗"
    for callout in main.select(".concept-callout"):
        heading = callout.find("h2")
        if heading:
            heading.string = "Få et forslag til riktig omfang"
        paragraph = callout.find("p", recursive=False)
        if paragraph and not paragraph.get("class"):
            paragraph.string = "Send litt informasjon, så får du en skriftlig vurdering av pris og leveranse. Designarbeid avtales før oppstart."
    for tag in main.find_all(True):
        for attr in ("href", "src"):
            val = tag.get(attr)
            if not isinstance(val, str):
                continue
            parsed = urlparse(val)
            if parsed.netloc in {"webproduksjon.github.io", "webproduksjon.no"}:
                if parsed.netloc == "webproduksjon.github.io" and not parsed.path.startswith("/renats.no/"):
                    continue
                target = parsed.path.removeprefix("/renats.no/").lstrip("/") if parsed.netloc == "webproduksjon.github.io" else parsed.path.lstrip("/")
                target = target or "index.html"
                tag[attr] = href(path, target)
            elif val.startswith("/") and not val.startswith("//") and (ROOT / val.lstrip("/")).exists():
                tag[attr] = href(path, val.lstrip("/"))
        if tag.name == "form" and "formsubmit.co" in tag.get("action", ""):
            for field in tag.select('input[name="_next"]'):
                field["value"] = ORIGIN + "/takk.html"
    return main.decode_contents()


def head(path: str, title: str, description: str, keywords: str, indexed: bool) -> str:
    esc = lambda value: html.escape(value, quote=True)
    actual = ALTERNATE.get(path, path)
    url = canonical(actual)
    image = ORIGIN + "/social-preview.png"
    org = {"@type": "Organization", "@id": ORIGIN + "/#organization", "name": "webproduksjon.no", "legalName": "Bogdanovs Webproduksjon", "url": ORIGIN + "/", "email": "hei@renats.no"}
    website = {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "webproduksjon.no", "url": ORIGIN + "/", "inLanguage": "nb-NO", "publisher": {"@id": org["@id"]}}
    page = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": description, "inLanguage": "nb-NO", "isPartOf": {"@id": website["@id"]}}
    graph = [org, website, page]
    if path != "index.html" and indexed:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Forside", "item": ORIGIN + "/"}, {"@type": "ListItem", "position": 2, "name": LABELS.get(path, title.split("|")[0].strip()), "item": canonical(path)}]})
    metadata = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("<", "\\u003c")
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#142c2a"><title>{esc(title)}</title>
<meta name="description" content="{esc(description)}"><meta name="keywords" content="{esc(keywords)}">
<link rel="canonical" href="{esc(url)}"><link rel="icon" type="image/svg+xml" href="{href(path, 'favicon.svg')}">
<link rel="stylesheet" href="{href(path, 'styles.css')}">
<meta property="og:type" content="website"><meta property="og:site_name" content="webproduksjon.no">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}"><meta property="og:image" content="{esc(image)}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Webproduksjon.no — enkle nettsider for små bedrifter">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{esc(image)}">
{'' if indexed else '<meta name="robots" content="noindex,follow">'}
<script type="application/ld+json">{metadata}</script>'''


def shell(path: str, title: str, body: str, description: str, keywords: str, indexed: bool) -> str:
    link = lambda target: html.escape(href(path, target), quote=True)
    nav = [("Tjenester", "tjenester/"), ("Bransjer", "bransjer/"), ("Priser", "priser.html"), ("Arbeidsmåte", "prosess.html"), ("Om Renat", "om.html")]
    nav_items = "".join(f'<li><a href="{link(p)}"' + (' aria-current="page"' if path == (p + 'index.html' if p.endswith('/') else p) else '') + f'>{label}</a></li>' for label, p in nav)
    html_head = head(path, title, description, keywords, indexed)
    home = path == "index.html"
    return f'''<!doctype html>
<html lang="nb"><head>{html_head}</head>
<body class="{'home-page' if home else 'interior-page'}"><a class="skip-link" href="#main-content">Hopp til hovedinnhold</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="{link('index.html')}" aria-label="Webproduksjon.no – til forsiden"><span class="brand-symbol" aria-hidden="true">w<span>/</span></span><span class="brand-type">webproduksjon<span>.no</span></span></a><button class="menu-toggle" type="button" aria-controls="site-navigation" aria-expanded="false">Meny <span aria-hidden="true">☰</span></button><nav id="site-navigation" class="site-nav" aria-label="Hovedmeny"><ul>{nav_items}<li class="nav-contact"><a href="{link('kontakt.html')}"{' aria-current="page"' if path == 'kontakt.html' else ''}>Få forslag <span aria-hidden="true">↗</span></a></li></ul></nav></div></header>
<main id="main-content" class="page-shell {'home-main' if home else ''}">{body}</main>
<footer class="site-footer"><div class="footer-grid"><div class="footer-brand"><a class="brand" href="{link('index.html')}"><span class="brand-symbol" aria-hidden="true">w<span>/</span></span><span class="brand-type">webproduksjon<span>.no</span></span></a><p>Enkle, gjennomtenkte nettsider for små bedrifter i Norge. Laget av Renat, digitalt og personlig.</p><a href="mailto:hei@renats.no">hei@renats.no ↗</a></div><div><span class="footer-heading">UTFORSK</span><a href="{link('tjenester/')}">Tjenester</a><a href="{link('priser.html')}">Priser</a><a href="{link('bransjer/')}">Bransjer</a><a href="{link('prosjekter/')}">Ett ekte prosjekt</a></div><div><span class="footer-heading">LES MER</span><a href="{link('ressurser/')}">Guider og ressurser</a><a href="{link('prosess.html')}">Arbeidsmåte</a><a href="{link('om.html')}">Om Renat</a><a href="{link('kontakt.html')}">Kontakt skriftlig</a></div></div><div class="footer-bottom"><span>© Bogdanovs Webproduksjon · org.nr. 932 091 992</span><a href="{link('personvern.html')}">Personvern</a></div></footer>
<script src="{link('menu.js')}" defer></script></body></html>
'''


def main() -> None:
    pages = sorted(p for p in ROOT.rglob("*.html") if CONTENT not in p.parents and ".git" not in p.parts and "site" not in p.parts)
    routes = []
    indexed_paths = []
    for file in pages:
        path = file.relative_to(ROOT).as_posix()
        original = BeautifulSoup(file.read_text(encoding="utf-8"), "html.parser")
        if path in PAGES:
            title, desc, keywords, fragment = PAGES[path]
            body = tokens((CONTENT / fragment).read_text(encoding="utf-8"), path)
        else:
            title = LEGACY_TITLES.get(path, original.title.get_text(" ", strip=True) if original.title else path.replace("/", " "))
            d = original.find("meta", attrs={"name": "description"})
            desc = d.get("content", "") if d else "Praktiske råd om nettsider for små bedrifter."
            desc = " ".join(desc.split())[:158]
            keywords = "nettside for små bedrifter, hjemmeside bedrift, webdesign, nettside pris"
            body = fix_legacy(original, path)
        if path == "blogg/index.html":
            body = '<section class="page-hero"><p class="eyebrow">GUIDER</p><h1>Du finner guidene våre her.</h1><p class="lead">Artikler og svar om nettsider for små bedrifter er samlet under ressurser.</p><a class="button" href="' + href(path, "ressurser/") + '">Se ressursene ↗</a></section>'
        if path == "konsept-kontakt.html":
            body = '<section class="page-hero"><h1>Send en kort forespørsel</h1><p class="lead">Bruk kontaktsiden for et skriftlig forslag til nettside og pris.</p><a class="button" href="' + href(path, "kontakt.html") + '">Til kontaktsiden ↗</a></section>'
        if path == "ressurser/hvor-mange-sider-trenger-liten-bedrift.html":
            body = '<section class="page-hero"><h1>Hvor mange sider trenger du?</h1><p class="lead">Denne guiden er flyttet til en mer utfyllende versjon.</p><a class="button" href="' + href(path, "ressurser/hvor-mange-sider-trenger-en-liten-bedrift/") + '">Les guiden ↗</a></section>'
        file.write_text(shell(path, title, body, desc, keywords, path not in NOINDEX), encoding="utf-8")
        if path != "404.html":
            routes.append({"path": route(path), "title": title})
        if path not in NOINDEX:
            indexed_paths.append(path)
    (ROOT / "manus-routes.json").write_text(json.dumps({"routes": routes}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{html.escape(canonical(path))}</loc></url>\n" for path in indexed_paths) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n", encoding="utf-8")
    print(f"Built {len(pages)} HTML pages; {len(indexed_paths)} in sitemap for {ORIGIN}")


if __name__ == "__main__":
    main()
