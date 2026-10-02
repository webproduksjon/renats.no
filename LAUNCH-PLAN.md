# webproduksjon.no — launch-readiness plan

**Prepared:** 2026-10-02  
**Target:** Publish on the real `webproduksjon.no` domain today  
**Current source:** `webproduksjon/renats.no`, branch `main`  
**Current public preview:** `https://webproduksjon.github.io/renats.no/`

## Launch decision

The site should launch as a **focused service website with one real portfolio project**, not as a large agency site pretending to have a large body of work.

The launch promise is:

> Renat builds clear, mobile-friendly and movable websites for small businesses, with one real published client website and clearly labelled concept demos—not invented case studies or reviews.

The launch version should keep the strongest service, pricing, process, trust and contact pages; expose the finished ABC Bygg AS website as the first real portfolio item; and remove or delist every page that currently looks like an unfinished promise.

## Current audit findings

- The core conversion path is already present: home → service choice → prices → contact.
- Pricing, delivery, payment, ownership, VAT status and the absence of a fixed monthly agreement are already explained consistently.
- ABC Bygg AS is live at `https://abcbyggas.no/` and links back to `https://webproduksjon.no/` in its footer.
- The ABC Bygg website publicly identifies the business as **ABC BYGG AS**, org. no. **934 398 831**, serving Bergen and nearby areas, with a named daily leader and real services, recommendations and project imagery.
- The current `/prosjekter/` page is a future archive rather than a finished portfolio page and is marked `noindex`.
- `/blogg/` says “Kommer senere”; it is also `noindex` and should not be exposed as a primary navigation destination at launch.
- The following are public stub pages with only a heading and should not remain discoverable:
  - `/bransjer/konsulent/`
  - `/bransjer/maler/`
  - `/ressurser/hvor-mange-sider-trenger-en-liten-bedrift/`
  - `/ressurser/nettside-for-elektriker/`
  - `/ressurser/nettside-for-snekker/`
- Existing concept demos are useful, but must remain visibly labelled as fictional concept demos and never be counted as portfolio work.
- The repository currently has no broken internal links, but the sitemap contains future-facing content that should be reduced to the launch set.

## Stage 0 — freeze the truth set before editing

**Goal:** establish what can safely be claimed on a public website.

1. Confirm that the public ABC Bygg website may be shown as a portfolio project.
2. Confirm whether ABC Bygg AS permits:
   - the company name and logo/brand to appear on webproduksjon.no;
   - screenshots or cropped images from the finished website;
   - a short project description;
   - a link to `abcbyggas.no`;
   - public mention that webproduksjon.no built the site.
3. Use only facts visible on the public ABC Bygg site or facts explicitly supplied by the client. Do not infer project price, conversion results, traffic, delivery time, technical stack, or business performance.
4. Do not copy ABC Bygg customer recommendations onto webproduksjon.no as if they were testimonials for Renat. They are testimonials for ABC Bygg.
5. Keep the existing business facts for webproduksjon.no unchanged:
   - webproduksjon.no is operated under Bogdanovs Webproduksjon;
   - org. no. 932 091 992;
   - prices are stated without VAT because the business is not VAT-registered;
   - no fixed monthly agreement is included.

**Exit condition:** there is a written yes/no decision for the portfolio use of ABC Bygg and a short approved fact list.

## Stage 1 — define the launch information architecture

**Goal:** make every public page intentional.

### Keep public and conversion-relevant

- `/`
- `/tjenester/`
- `/tjenester/landingsside.html`
- `/tjenester/enkel-nettside.html`
- `/tjenester/nettside-for-sma-bedrifter.html`
- `/priser.html`
- `/prosess.html`
- `/om.html`
- `/kontakt.html`
- `/takk.html`
- `/personvern.html`
- `/prosjekter/` — convert from empty archive to the ABC Bygg portfolio page
- `/ressurser/` and the completed, useful resource articles that support purchase decisions
- `/demos/` and its three demo pages — keep, but label as concept demos everywhere
- `/bransjer/` and the three completed industry pages — keep as educational/service pages, not portfolio evidence

### Remove from the public launch set

- `/blogg/` from footer and sitemap until there is at least one genuinely useful article and a real editorial reason to maintain it.
- The two empty industry stubs:
  - `/bransjer/konsulent/`
  - `/bransjer/maler/`
- The three empty resource stubs:
  - `/ressurser/hvor-mange-sider-trenger-en-liten-bedrift/`
  - `/ressurser/nettside-for-elektriker/`
  - `/ressurser/nettside-for-snekker/`

Delete these unfinished stub files from the published branch rather than leaving thin pages with `noindex`. Git history preserves them for future rewriting. If a future URL has already acquired meaningful external links, replace it with a deliberate redirect strategy before deletion; do not create redirects for the current empty stubs without evidence that they are needed.

**Exit condition:** sitemap, footer links, resource index, industry index and project navigation expose only pages that are complete and useful today.

## Stage 2 — build the first real portfolio case

**Goal:** turn `/prosjekter/` into credible proof without overstating the work.

1. Replace the future-archive copy with a finished case page for **ABC Bygg AS**.
2. Use a clear title such as `Nettside for ABC Bygg AS`.
3. Include these sections:
   - **The client:** ABC Bygg AS, with the public business name and link to `abcbyggas.no`.
   - **The brief:** a concise description based on the actual site, e.g. helping a building company explain its services, local coverage and contact route.
   - **What was built:** explain the actual deliverable only—structure, responsive presentation, service overview, recommendations, gallery and enquiry route if those are part of the finished site.
   - **The customer journey:** show how a visitor can move from understanding the offer to seeing services, recommendations/gallery and contacting the company.
   - **Screenshots or selected visuals:** use only with permission, with descriptive alt text and captions.
   - **Result statement:** use a factual statement such as `The website is live at abcbyggas.no.` Do not claim more leads, sales, rankings or conversion without measured evidence.
   - **External link:** `Visit abcbyggas.no` opening in a normal, clearly labelled link.
4. Add a visible disclosure: `This is a real website project. Business facts and recommendations belong to ABC Bygg AS; they are not testimonials for webproduksjon.no.`
5. Add a second, separate block for the concept demos: `Concept demos — fictional examples, not client projects.`
6. Link the home page to the real project with one strong, honest CTA such as `See the ABC Bygg project`.
7. Keep `/prosjekter/` indexable only after the page contains the real case. Update its title, description, canonical URL, Open Graph metadata and structured data accordingly.

**Exit condition:** a visitor can tell, in under 10 seconds, which work is real, which work is fictional, what Renat contributed and what is not being claimed.

## Stage 3 — strengthen credibility without inventing social proof

**Goal:** make the site persuasive even with one portfolio project and no reviews for webproduksjon.no.

1. Use the ABC Bygg case as **proof of capability**, not proof of business results.
2. Add a compact “What you can verify” trust block near the main CTA:
   - one real published website;
   - direct contact with Renat;
   - legal business name and organization number;
   - transparent starting prices and VAT wording;
   - clear delivery, payment and ownership terms;
   - no forced monthly platform subscription.
3. Make the founder identity consistent across home, Om and Kontakt: first-person voice where Renat speaks directly; avoid switching between “I” and “we” unless a real team exists.
4. Keep the honest limitations prominent: no guarantee of rankings, traffic or customers; advanced features are scoped separately.
5. Add a simple “How projects become portfolio pieces” explanation on the portfolio page or process page:
   - client approval before publication;
   - factual project description;
   - link to the live site;
   - no invented metrics.
6. Do not add star ratings, invented review counts, “trusted by” logos, years-of-experience claims, awards, or client-result numbers unless documented.
7. Ensure every primary CTA answers one action only: request a concrete proposal or ask for a concept—not several competing actions in the same visual block.

**Exit condition:** the site feels credible because it is specific and verifiable, not because it imitates a larger agency.

## Stage 4 — domain and publication preparation

**Goal:** move from the GitHub Pages preview to the real domain without leaving preview URLs in public metadata.

1. Decide whether `webproduksjon.no` remains on GitHub Pages or is deployed to another host. Do not change hosting and DNS simultaneously without a rollback plan.
2. If GitHub Pages remains the host:
   - configure the repository Pages custom domain for `webproduksjon.no`;
   - add the required `CNAME` file only after the DNS target is ready;
   - configure the apex and/or `www` DNS records according to the selected host;
   - choose one canonical host (`https://webproduksjon.no/` or `https://www.webproduksjon.no/`) and redirect the other;
   - enable HTTPS and wait for certificate issuance.
3. Replace every production-facing absolute URL currently using `https://webproduksjon.github.io/renats.no/` with the selected real-domain URL in:
   - canonical tags;
   - Open Graph and Twitter URLs;
   - JSON-LD;
   - sitemap;
   - robots.txt;
   - FormSubmit `_next` URL;
   - any public “website by webproduksjon.no” links where appropriate.
4. Preserve relative internal links so future host moves do not break navigation.
5. Confirm that the contact form still returns to the real-domain `/takk.html` page and that the privacy page describes the actual form provider.
6. If the new domain is not ready in DNS, keep the GitHub Pages site live and do not publish mixed canonical URLs. The website can be content-ready before the DNS cutover.

**Exit condition:** the chosen canonical domain resolves over HTTPS, all public metadata points to it, and form submissions return to it.

## Stage 5 — launch QA on the real domain

**Goal:** verify the complete visitor journey, not only individual files.

1. Test the home page on a narrow mobile viewport and desktop.
2. Test these journeys:
   - home → ABC Bygg case → live ABC Bygg site → back to webproduksjon.no;
   - home → service choice → prices → contact;
   - home → concept demo → clear return to real services/contact;
   - resource article → relevant service → contact;
   - contact form → form provider → `/takk.html`.
3. Check every header/footer link and every URL in the sitemap.
4. Request representative removed stub URLs and confirm they return the intended 404 experience rather than a thin page.
5. Validate:
   - one H1 per page;
   - valid title and meta description;
   - canonical URL uses the real domain;
   - no preview URL remains in production metadata;
   - no unfinished wording such as “coming later” remains in public pages;
   - no fake reviews or unapproved ABC Bygg claims appear;
   - all images have useful alt text;
   - no horizontal overflow on mobile;
   - form labels, required fields and success page work.
6. Check that the sitemap contains only canonical, launch-ready URLs.
7. Submit the final sitemap in Google Search Console after the real domain is verified.

**Exit condition:** no broken links, no visible unfinished pages, no preview-domain metadata and no ambiguity about real versus fictional work.

## Stage 6 — publish today

**Order of operations:**

1. Approve the ABC Bygg portfolio fact list and usage permission.
2. Implement the information-architecture cleanup and the real ABC Bygg project page.
3. Remove the empty stubs from navigation and sitemap, then delete them from the published branch.
4. Remove Blogg from navigation and sitemap unless an article is ready.
5. Update production URLs and form return URL.
6. Commit as one launch candidate.
7. Run the full QA in Stage 5 against the preview candidate.
8. Configure DNS/custom domain and HTTPS.
9. Re-run the same QA against `https://webproduksjon.no/`.
10. Publish the launch commit and record the exact commit hash, DNS state, canonical host and sitemap URL.
11. Keep the GitHub Pages URL available as a temporary rollback/reference URL, but do not use it in public metadata after cutover.

## Stage 7 — the next few weeks

The site does not need more portfolio work to be credible today. When new projects become available, add them deliberately:

1. Create one case page per real project, using the same fact/disclosure format as ABC Bygg.
2. Ask for written permission before publishing client name, screenshots, logo, quotes or metrics.
3. Add a short testimonial only when the client supplies or approves the exact wording.
4. Add measured outcomes only when there is a defined baseline, measurement period and permission to publish.
5. Publish one useful article only when it answers a real customer question and links naturally to a service.
6. Add new industry pages only when they contain original service logic, real customer questions and a credible reason to exist.
7. Keep the portfolio small and specific rather than filling it with generic mockups.
8. Review Search Console queries, contact-form volume and which project/service pages assist conversions before changing the homepage.

## Final launch standard

The site is ready to launch when:

- the real domain works over HTTPS;
- the homepage explains the offer, pricing starting point and next step without requiring a portfolio;
- ABC Bygg AS is shown as one clearly identified real project;
- concept demos are clearly separated from client work;
- no page says “coming later”, “published when finished” or contains only a heading;
- empty future pages are deleted or excluded from navigation, sitemap and indexing;
- every public price, VAT, delivery, payment, ownership and monthly-model statement is consistent;
- the contact path works and returns to the real domain;
- the site makes no claims that cannot be documented.
