# Final technical SEO and experience audit

## Scope

This audit covers the complete static repository after Stage 5:

- 45 HTML files
- 32 intended indexable URLs
- 13 intentionally `noindex,follow` URLs
- 32 URLs in `sitemap.xml`
- 3 service pages
- 3 researched industry pages
- 17 resource articles plus the resource hub
- 3 clearly labelled concept demos
- Contact form and public business information

The audit was performed against the repository structure intended for publication at `https://webproduksjon.no/`.

## Final result

**Technical status: ready for hosting upload.**

The site is technically coherent for a static deployment. The remaining items intentionally outside this stage are evidence-based growth assets: real client projects, testimonials, reviews, permission-based before/after examples, real case studies, and genuine local relevance.

## Completed checks and fixes

### Crawlability and indexation

- All intended indexable HTML pages have a meaningful initial HTML body.
- All indexable pages have one H1.
- All indexable pages have a canonical URL on `webproduksjon.no`.
- All indexable pages have a route-specific title and meta description.
- `robots.txt` allows crawling and points to the canonical sitemap.
- The sitemap contains exactly the 32 intended indexable routes.
- No sitemap URL points to a known `noindex` page.
- The 13 unfinished, demo, portfolio-shell, privacy, and error routes remain `noindex,follow` and are excluded from the sitemap.
- The local static server returns a real `404` for an unknown route.

### Internal architecture

- Relative internal links work from root and nested routes.
- Breadcrumbs were checked across the page hierarchy.
- Resource articles link naturally to relevant services and contact paths.
- Industry pages link to their relevant resources and concept demos.
- Concept demos remain clearly labelled as fictional and are not presented as client projects.

### Metadata and structured data

- Norwegian pages use `lang="nb"`.
- Titles were shortened where they exceeded the preferred search-result range.
- The overlong electrician description was shortened below 160 characters.
- Indexable resource articles include Article JSON-LD with author, publisher, language, and canonical main entity.
- Existing Organization, Person, BreadcrumbList, and relevant page structured data were preserved.
- Open Graph and Twitter Card metadata were checked on indexable pages.
- Social preview metadata points to the public `social-preview.png` asset.

### Images and performance

The three tall concept-demo screenshots were converted from PNG to WebP and downscaled from approximately 1440px wide to 900px wide while preserving their aspect ratio:

| Asset | New dimensions | New size |
|---|---:|---:|
| `assets/demos/elektriker.webp` | 900 × 1808 | 98.9 KB |
| `assets/demos/snekker.webp` | 900 × 1888 | 95.4 KB |
| `assets/demos/rorlegger.webp` | 900 × 1813 | 89.9 KB |

The original PNG screenshot assets were removed from the active repository after all references were updated. Founder images and the social preview remain appropriately sized for their use.

### Accessibility and experience

- Skip links target `#main-content`.
- The contact form has labels associated with all three visible controls.
- Keyboard focus is visible through the global focus ring and explicit form focus-visible styling.
- Key text/background combinations were checked against WCAG contrast thresholds.
- Image alt text was checked; the active HTML image references contain non-empty alternatives.
- Mobile and desktop checks passed with no horizontal overflow.
- 64 page/viewport render checks passed across the indexable site at 390px and 1440px widths.
- No unnecessary scripts, iframes, video embeds, or third-party page widgets were found in the active content system.

## Intentionally postponed evidence

These are not technical SEO defects and should not be invented:

- Real client portfolio pages
- Testimonials and client reviews
- Before-and-after claims about real businesses
- Performance, traffic, ranking, or lead-generation results
- Client logos
- Permission-based screenshots
- Real case studies
- Location pages without genuine local relevance

## Deployment notes

Before final public launch, verify the deployed host itself—not only the repository copy—for:

1. `https://webproduksjon.no/robots.txt`
2. `https://webproduksjon.no/sitemap.xml`
3. The contact form flow and its FormSubmit confirmation redirect
4. HTTPS and the canonical domain
5. Search Console ownership and sitemap submission
6. A real mobile visit on the production host

The contact form was structurally checked but not submitted during this audit.

## Conclusion

The repository is now a technically clean, crawlable, responsive static content system suitable for hosting upload. Its future SEO growth should come from adding genuinely useful, experience-based content and evidence—not from multiplying near-identical pages or making unsupported claims.
