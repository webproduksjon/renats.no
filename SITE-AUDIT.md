# webproduksjon.no website audit

Audit completed after the Stage 3 proof-system implementation and final health pass.

## Current score

**88/100 overall for the current development site.**

This is a strong, crawlable foundation, but a genuine 100/100 is not possible before real-world proof and production verification exist. It would be misleading to award points for clients, results, identity, legal accuracy, or hosting behavior that has not been supplied or verified.

| Area | Score | Assessment |
| --- | ---: | --- |
| Design | 90 | Consistent visual system, strong contrast, responsive cards and CTAs. It is intentionally text-first and still lacks real project imagery. |
| Usability | 93 | Clear primary paths, good page hierarchy, visible contact email, suitability guidance, skip link, and no horizontal overflow in browser inspection. |
| Accessibility | 91 | Semantic landmarks, one H1 per page, keyboard skip link, visible focus treatment, descriptive links, and no empty links. A production accessibility review is still needed. |
| Technical SEO | 91 | Static crawlable HTML, canonical URLs, sitemap, robots, metadata, JSON-LD, breadcrumbs, favicon, and social preview. Production status codes and redirects still need verification on the final host. |
| Content quality | 88 | Core offer and first three industry pages are specific and honest. The resource, blog, privacy, and project areas are intentionally unfinished or protected. |
| Credibility | 74 | Claims are careful and transparent, but the site has no founder identity, real projects, testimonials, or measured outcomes yet. |
| Conversion | 86 | Strong email CTAs, clear scope, free concept offer, and suitability filters. A real project/demo would improve confidence substantially. |
| Health/maintainability | 91 | Plain static files, centralized CSS, no JavaScript dependency, validated internal links, clean git state. Hosting headers and deployment behavior remain external checks. |

## Verified in the sandbox

- 24 HTML pages parsed
- One H1 per page
- No broken internal links
- No empty links
- No missing image alt attributes because no content images are published yet
- Canonical tags present
- Open Graph metadata present
- Twitter metadata present
- JSON-LD parses successfully on pages where used
- Favicon and social preview are present
- Sitemap URLs resolve to existing pages
- No `noindex` page is in the sitemap
- Homepage has no horizontal overflow in browser inspection
- Header, main, footer, and navigation landmarks are present
- Unknown local route returns HTTP 404 under the static server

## What prevents 100/100 today

These are not safely inventable by the agent:

1. **Founder identity:** real name, background, location/operating area, and optional photo.
2. **Proof:** real client projects, permission-based before/after work, or clearly labeled concept demos.
3. **Testimonials:** only genuine, permission-based testimonials can be added.
4. **Pricing:** real starting prices or ranges would make the pricing page more concrete.
5. **Privacy:** the privacy page must match actual hosting, email handling, analytics, cookies, and external tools.
6. **Production hosting:** verify HTTPS, canonical-domain redirects, real 404 handling, cache headers, compression, and the served sitemap/robots files on the chosen host.
7. **Measurement:** connect Search Console and measure impressions, enquiries, and qualified leads after launch.

## Final launch gate

Do not remove `noindex` from unfinished routes or add them to the sitemap merely to increase URL count. Add proof only with permission, label concepts clearly, and verify every factual business claim before publishing.
