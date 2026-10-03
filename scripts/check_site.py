#!/usr/bin/env python3
"""Check generated pages without executing JavaScript."""
from __future__ import annotations
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://webproduksjon.github.io/renats.no"
PAGES = sorted(p for p in ROOT.rglob("*.html") if "_content" not in p.parts and ".git" not in p.parts and "site" not in p.parts)
errors: list[str] = []
noindex: set[str] = set()

def route(p: Path) -> str:
    name = p.relative_to(ROOT).as_posix()
    return "/" if name == "index.html" else "/" + (name[:-10] if name.endswith("/index.html") else name)

for page in PAGES:
    rel = page.relative_to(ROOT).as_posix()
    doc = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
    if not doc.main or not doc.main.get_text(" ", strip=True):
        errors.append(f"{rel}: missing visible main content")
    if len(doc.select("h1")) != 1:
        errors.append(f"{rel}: expected exactly one H1, got {len(doc.select('h1'))}")
    for selector in ("title", 'meta[name="description"]', 'link[rel="canonical"]', 'meta[property="og:url"]', 'meta[property="og:image"]'):
        if not doc.select_one(selector): errors.append(f"{rel}: missing {selector}")
    canonical = doc.select_one('link[rel="canonical"]')
    if canonical and not canonical.get("href", "").startswith(ORIGIN + "/"):
        errors.append(f"{rel}: wrong canonical origin: {canonical.get('href')}")
    robots = doc.select_one('meta[name="robots"]')
    if robots and "noindex" in robots.get("content", ""):
        noindex.add(rel)
    for el in doc.select("[href], [src]"):
        attr = "href" if el.has_attr("href") else "src"
        value = el.get(attr)
        if not value or value.startswith(("#", "mailto:", "tel:", "data:", "javascript:")): continue
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc: continue
        target = (page.parent / unquote(parsed.path)).resolve()
        if target.is_dir(): target = target / "index.html"
        if not target.is_file(): errors.append(f"{rel}: broken {attr}={value} -> {target}")
    for token in ("{{link:", "{{asset:", "?preview="):
        if token in page.read_text(encoding="utf-8"):
            errors.append(f"{rel}: leaked token {token}")

routes = json.loads((ROOT / "manus-routes.json").read_text())["routes"]
expected = {route(p) for p in PAGES if p.name != "404.html"}
actual = {r["path"] for r in routes}
if expected != actual:
    errors.append(f"manifest route mismatch missing={expected-actual}, extra={actual-expected}")
xml = ET.parse(ROOT / "sitemap.xml")
listed = {el.text for el in xml.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
expected_urls = {ORIGIN + route(p) for p in PAGES if p.relative_to(ROOT).as_posix() not in noindex and p.name != "404.html"}
if listed != expected_urls:
    errors.append(f"sitemap mismatch missing={expected_urls-listed}, extra={listed-expected_urls}")
contact = BeautifulSoup((ROOT / "kontakt.html").read_text(), "html.parser")
form = contact.select_one("form.enquiry-form")
if not form or form.get("action") != "https://formsubmit.co/hei@renats.no":
    errors.append("contact: missing expected form destination")
if not form or not form.select_one('input[name="_next"][value="https://webproduksjon.github.io/renats.no/takk.html"]'):
    errors.append("contact: wrong GitHub Pages return URL")
print(f"Checked {len(PAGES)} pages, {len(listed)} indexable routes, {len(noindex)} noindex routes")
for error in errors: print("ERROR:", error)
sys.exit(bool(errors))
