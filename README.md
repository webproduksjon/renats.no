# Webproduksjon.no — GitHub Pages test version

This repository publishes the **test site** at [webproduksjon.github.io/renats.no](https://webproduksjon.github.io/renats.no/) from `main` and `/`. It does **not** redirect visitors to `webproduksjon.no`. The existing separate hosted site stays unchanged until Renat has tested and manually uploaded the replacement.

The pages are static HTML so the content is present in the initial response; a crawler or visitor does not need JavaScript to read it. Internal links and local assets are relative, and work both under the `/renats.no/` GitHub Pages path and at a domain root. The mobile menu is the only site interaction requiring JavaScript.

## Editing and rebuilding

Install the one build dependency with `python3 -m pip install -r requirements.txt` in a Python environment, or use an existing environment with Beautiful Soup 4. Edit primary page bodies in `_content/`, visual styles in `styles.css`, the route titles/descriptions in `scripts/build.py`, and existing long-form pages in their HTML files. Then run:

```bash
python3 scripts/build.py
python3 scripts/make_social.py  # only if social-preview.png needs regeneration
python3 scripts/check_site.py
```

The generator rebuilds the shared header, footer, metadata, JSON-LD, sitemap, robots, and route manifest. Its default `SITE_ORIGIN` is `https://webproduksjon.github.io/renats.no`, which means canonical/OG/sitemap URLs and the form return URL match this GitHub Pages test site. It does not create any redirect. Do not directly edit generated core pages; change the corresponding `_content/` fragment. Long-form legacy pages preserve their main content on rebuild. Keep existing article URLs unless a deliberate migration plan is made.

For a local preview from the repository root, run `python3 -m http.server 3000 --bind 0.0.0.0` and open `http://localhost:3000/`. To test the actual nested GitHub Pages base path, use the published Pages URL after pushing.

## Contact form: verify before taking real enquiries

`kontakt.html` posts to the existing FormSubmit address `hei@renats.no` and offers `mailto:hei@renats.no` as a fallback. FormSubmit may require the recipient to activate the form by email on the first submission. Renat should submit a harmless test enquiry from the **published GitHub Pages contact page**, complete any FormSubmit activation/captcha email, confirm delivery to `hei@renats.no`, and confirm the return to `/takk.html`. Do not assume the form works merely because its HTML renders. The privacy page discloses the external processor. If the email or service changes, update the contact fragment and privacy notice before accepting customer data.

## Later: upload to the separately hosted domain

Only after GitHub Pages testing is complete, prepare a **copy** of the repository, not this checked-out staging branch, and regenerate it with the final public origin. For example:

```bash
mkdir -p /tmp/webproduksjon-live
tar --exclude=.git -cf - . | (cd /tmp/webproduksjon-live && tar -xf -)
cd /tmp/webproduksjon-live
SITE_ORIGIN=https://webproduksjon.no python3 scripts/build.py
# Check canonical, og:url, sitemap and the contact form's _next on the output.
```

Upload the generated root HTML files, nested page directories, `styles.css`, `menu.js`, `favicon.svg`, `social-preview.png`, `assets/`, `.htaccess`, `robots.txt` and `sitemap.xml` to the domain's web root. The host's `.htaccess` applies only to Apache and has no effect on GitHub Pages. Do not copy the generated live-domain files back to `main` during the staging phase; that would make GitHub Pages advertise the wrong canonical. When the domain is ready, check representative raw HTML, contact-form delivery and `https://webproduksjon.no/sitemap.xml` and submit the final sitemap in Google Search Console. Decide whether to keep GitHub Pages as an accessible preview with a canonical pointing to the final domain or otherwise restrict it after launch; **do not redirect it during current testing**.

SEO is a foundation, not a ranking guarantee. The site intentionally uses one genuine published client example and labels fictional demos. It does not claim measured traffic, rankings or customer results.
