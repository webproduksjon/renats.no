# Webproduksjon.no — rebuild plan

## Product and deployment

Rebuild the existing static Norwegian website in `webproduksjon/renats.no`, keeping GitHub Pages at `https://webproduksjon.github.io/renats.no/` fully usable as the **testing site**. Do not redirect GitHub Pages to the separately hosted `webproduksjon.no`; the owner will upload there only after testing. Internal links and assets must be relative and work both under `/renats.no/` and at a domain root. Page URLs, canonical/OG URLs and the sitemap are generated with a single `SITE_ORIGIN` setting, defaulting to the GitHub Pages origin for this stage; regeneration with `SITE_ORIGIN=https://webproduksjon.no` is part of the eventual hosting handoff. Never infer a canonical from the local development host. GitHub Pages static HTML is the production format, with no server or database dependency.

The visitor is a Norwegian small-business owner searching for terms such as “nettside for små bedrifter,” “lage nettside til bedrift,” “enkel nettside,” “landingsside,” and “hva koster en nettside.” The home page makes the offer and next step obvious; service and pricing pages answer purchase intent, a real case study supplies bounded proof, industry pages address genuine differences, and helpful resources cover planning questions. Avoid duplicate keyword-stuffed doorway pages, invented clients or reviews, rankings, lead numbers or delivery guarantees. Keep the one genuine ABC Bygg example and explicitly label conceptual demos. Do not market Renat as Norway-based: he serves Norwegian customers remotely. Explain that Manus AI helps produce the site, with human direction/review and no promise that AI itself makes a site rank.

Offer/pricing follows the source site unless the owner changes it: landing page from 4 990 kr and small multi-page site from 7 990 kr, no VAT charged while the business is not VAT-registered, usual 2–4 weeks subject to agreed inputs, one revision, 50/50 payment, hosting/domain separately. Do not assert unverified business performance or a location in Bergen. Contact is written-first, with a short form via the site's existing FormSubmit destination and a direct email fallback; no phone call required. The form's return destination uses the GitHub Pages staging URL now, configurable for later hosting. Clearly disclose external form processing and verify activation/delivery with the owner before accepting real inquiries.

## Design

- **Movement:** Nordic editorial utility, rather than a generic SaaS landing page.
- **Principles:** sharp information hierarchy; transparent specifics over social-proof theater; roomy asymmetry; deliberate restraint on decoration.
- **Color:** deep pine ink and warm bone paper suggest competence and approachability, with an ownable acid-lime highlight for actions and annotations. Color is not the only interaction signal.
- **Layout:** off-center headline and staggered editorial bands, a large real-project viewport in the hero, and narrow reading columns for long-form guides; avoid stacks of identical cards.
- **Signature motifs:** numbered section labels, thin rules with small accent blocks, and a compact browser-frame showing the one real client project.
- **Interactions:** obvious written CTAs, accessible disclosure FAQs, keyboard-friendly mobile navigation, no auto-playing motion. Small hover lifts/underlines and reveal-free essential content; reduced-motion support.
- **Typography:** self-hosted geometric sans for display and body, system mono for overlines/numbers; unusually large, tight display headlines, comfortable prose size and line length.
- **Brand essence:** affordable, considered websites for small Norwegian companies from a single accountable maker; direct, calm, honest.
- **Voice:** specific, conversational Norwegian, not agency plural or inflated promises. Examples: “En nettside som forklarer det du gjør. Og gjør det lett å ta kontakt.” “Send noen linjer. Du slipper å ringe.”
- **Wordmark:** a custom `w/` ligature-like mark in a dark rounded square, paired with the spaced `webproduksjon.no` name; not a default typed logo.
- **Signature brand color:** electric chartreuse `#D9F076`.

## Structure and implementation

- `scripts/build.py`: deterministic static generator; page wrappers, route-specific metadata, relative navigation, JSON-LD, sitemap, robots, route manifest, URL validation; leaves original long-form page bodies in place for legacy pages and replaces primary pages with authored fragments.
- `_content/*.html`: newly written core page body fragments for home, services, price, contact, process, about, project, industries and resource hub.
- Root and nested `*.html`: generated, content-bearing static responses suitable for crawling without JavaScript. Existing useful article URLs and industry pages remain reachable and receive the shared new shell; no unnecessary URL loss.
- `styles.css`, `menu.js`, `favicon.svg`, `social-preview.png`, `assets/`: visual system, minimal interactive menu, brand assets and real project/portrait imagery.
- `robots.txt`, `sitemap.xml`, `manus-routes.json`: built from the route inventory. `404.html` is a real 404 on GitHub Pages, marked noindex.
- `.htaccess`: relevant only to later Apache hosting; never loaded by GitHub Pages. It must not send GitHub traffic to the domain.
- `README.md`: local preview, GitHub Pages staging, FormSubmit verification and eventual domain migration instructions.

Do not promise search rankings or instant organic traffic. Publishing to the existing GitHub repository updates the GitHub Pages test site, not the separate hosted domain.
