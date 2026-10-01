# webproduksjon.no

Design-neutral foundation for a Norwegian website studio offering simple static websites for new and small businesses.

## Current phase

This repository intentionally contains **structure before design**. The HTML is semantic and crawlable, but it does not attempt to look finished yet. Each page is a separate static document so it can be copied to ordinary hosting without WordPress or a server-side runtime.

## Positioning

- Simple websites for new and small companies
- One-page landing pages and small multi-page company websites
- Clear online presence, not a promise of rankings, leads, or ongoing SEO
- Norwegian-first content, with room for future language versions

## Information architecture

```text
/
├── tjenester/
│   ├── index.html
│   ├── enkel-nettside.html
│   ├── landingsside.html
│   └── nettside-for-sma-bedrifter.html
├── bransjer/
│   └── index.html
├── prosess.html
├── priser.html
├── om.html
├── kontakt.html
├── ressurser/
│   └── index.html
├── blogg/
│   └── index.html
├── personvern.html
├── 404.html
├── robots.txt
└── sitemap.xml
```

### Why this structure

1. **Tjenester** is the commercial cluster. Every future service page should answer a distinct customer question and link back to the most relevant parent page.
2. **Bransjer** is reserved for genuinely useful, manually written examples. Do not create dozens of near-identical industry pages just to target keywords.
3. **Prosess, priser, om and kontakt** reduce uncertainty and support conversion without pretending to be SEO content.
4. **Ressurser and blogg** are separate future editorial areas. A resource should solve a practical problem; a blog post should have a real point of view or answer a specific question.
5. **Personvern** is a trust/legal route and should not be treated as a marketing landing page.

## URL and content rules for future work

- Use Norwegian, lowercase, hyphen-separated slugs.
- Give every indexable URL one primary search intent and one genuinely useful page purpose.
- Avoid city/industry permutations with only swapped words. That creates thin doorway-like pages.
- Do not publish placeholder copy as indexable content. Keep unfinished routes out of `sitemap.xml` until they are useful.
- Every page should have a unique title, meta description, H1, introduction, canonical URL, and internal-link role.
- Add the page to `sitemap.xml` only after it has been reviewed as complete.
- Keep claims precise: a static website can improve a company's online presence, but it does not guarantee rankings, traffic, or customers.
- Keep the final contact details and legal text accurate before publishing.

## Technical notes

- Pages are plain HTML and can be hosted on ordinary static hosting.
- No framework, CMS, build step, JavaScript, or design system is required at this stage.
- `robots.txt` and `sitemap.xml` use `https://webproduksjon.no` as the intended public origin. Change this everywhere if the canonical domain changes.
- The current pages include meaningful structural content rather than an empty client-rendered shell.
- When adding a page, update navigation, breadcrumbs, relevant cross-links, `sitemap.xml`, and this route map together.

## Next recommended phase

Work through the pages one at a time. Start with the home page, the main services page, the service detail pages, and the contact page. For each page, define the audience, search intent, promise, proof, objections, call to action, and links to the next useful page before adding visual design.
