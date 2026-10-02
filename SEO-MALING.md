# SEO-måling for webproduksjon.no

## Formål

Målet er ikke å maksimere total trafikk. Målet er å finne ut hvilke relevante søk og sider som gir en realistisk vei til en forespørsel.

Følg denne rekken:

1. relevante visninger
2. klikk fra relevante søk
3. besøk på tjeneste- eller prisside
4. innsending av kontaktform
5. hvilken side besøket startet på

## 1. Koble nettstedet til Google Search Console

Nettstedet har allerede en tilgjengelig sitemap og robots-fil:

- Eiendom: `https://webproduksjon.github.io/renats.no/`
- Sitemap: `https://webproduksjon.github.io/renats.no/sitemap.xml`
- Robots: `https://webproduksjon.github.io/renats.no/robots.txt`

Gjør dette i Search Console:

1. Opprett eller velg en **URL-prefix property** for `https://webproduksjon.github.io/renats.no/`.
2. Velg en verifiseringsmetode Google tilbyr for GitHub Pages. HTML-tag eller HTML-fil er normalt enklest når DNS ikke kan endres.
3. Send inn sitemap-URL-en: `https://webproduksjon.github.io/renats.no/sitemap.xml`.
4. Bruk URL Inspection på de viktigste URL-ene under.
5. Be om indeksering av de viktigste nye eller endrede sidene etter at de er publisert.

**Begrensning:** Search Console-data og verifisering krever tilgang til Google-kontoen. Det finnes ingen Search Console-kode eller verifiseringstoken i repositoryet nå, så token skal ikke oppfinnes eller legges inn uten at Google leverer det.

## 2. Inspiser disse URL-ene først

Prioriter sider som både kan få relevante søk og lede til en forespørsel:

1. `https://webproduksjon.github.io/renats.no/`
2. `https://webproduksjon.github.io/renats.no/tjenester/`
3. `https://webproduksjon.github.io/renats.no/tjenester/enkel-nettside.html`
4. `https://webproduksjon.github.io/renats.no/tjenester/landingsside.html`
5. `https://webproduksjon.github.io/renats.no/tjenester/nettside-for-sma-bedrifter.html`
6. `https://webproduksjon.github.io/renats.no/priser.html`
7. `https://webproduksjon.github.io/renats.no/kontakt.html`
8. `https://webproduksjon.github.io/renats.no/ressurser/hva-koster-en-nettside-for-en-liten-bedrift.html`
9. `https://webproduksjon.github.io/renats.no/bransjer/elektriker/`
10. `https://webproduksjon.github.io/renats.no/bransjer/snekker/`
11. `https://webproduksjon.github.io/renats.no/bransjer/rorlegger/`

Kontroller for hver URL:

- Google kan hente siden
- canonical peker til riktig URL
- siden er kvalifisert for indeksering
- mobilversjonen fungerer
- den nye teksten og CTA-en faktisk er offentlig

## 3. Månedlig rapport

Eksporter eller noter Search Console-data for de siste 28 dagene og sammenlign med forrige periode.

| Målepunkt | Hva som skal noteres | Hva det betyr |
|---|---|---|
| Relevante søk | søk, visninger, posisjon | om siden matcher behovet |
| Klikk | søk, side, klikk, CTR | om søkeresultatet får riktig person til å klikke |
| Tjenestebesøk | landingsside og videreklikk | om innholdet leder mot kjøpssiden |
| Kontakt | antall innsendinger | om interesse blir til henvendelse |
| Startside | første organiske side | hvilke artikler eller sider som skaper inngangen |

Følg særlig disse søkegruppene:

- `nettside for små bedrifter`
- `nettside til bedrift`
- `hjemmeside til bedrift`
- `enkel nettside for bedrift`
- `landingsside for bedrift`
- `hva koster en nettside`
- `nettside for elektrikere`
- `nettside for snekkere`
- `nettside for rørleggere`

## 4. Beslutningsregler

### Mange visninger + lav CTR

Forbedre først:

- SEO-tittel
- metabeskrivelse
- samsvar mellom søket og første del av siden

Ikke endre URL eller lage en ny side før den eksisterende siden er forbedret og målt på nytt.

### Mange klikk + ingen kontakt

Kontroller:

- om pris eller fra-pris er synlig
- om leveringstid og betaling er forklart
- om første CTA sier **Få et konkret forslag**
- om siden leder til riktig tjeneste
- om kontaktformen er lett å forstå

### Artikkelvisninger + ingen tjenesteklikk

Forbedre den relevante CTA-boksen etter første hoveddel. Den skal ha:

- én relevant tjenestelenke
- én tydelig kontaktlenke
- en konkret forklaring på hva kunden får videre

### Bransjesidevisninger + lav kontakt

Sammenlign søket med første skjerm. Den skal raskt vise:

- hva bransjen trenger å forklare
- hva nettsiden kan strukturere
- pris- eller leveringsvei
- **Få et konkret forslag**

### Søk uten god landingsside

Velg én eksisterende side eller opprett én ny side med én tydelig søkeintensjon. Ikke lag fem nesten like sider for samme søk.

## 5. Enkel månedlig arbeidsøkt

1. Åpne Performance → Search results.
2. Velg siste 28 dager og sammenlign med forrige periode.
3. Filtrer på Queries og Pages.
4. Noter de fem mest relevante søkene, ikke bare de største søkene.
5. Finn én side med høy visning/lav CTR eller høy klikkmengde/lav kontakt.
6. Gjør én konkret endring.
7. Skriv ned dato, endring og forventet effekt.
8. Vent på nok data før neste store endring.

## Endringslogg

| Dato | Side | Observasjon | Endring | Neste kontroll |
|---|---|---|---|---|
| 2026-10-02 | Hele nettstedet | Search Console er ikke koblet i repositoryet | Sitemap, canonical-URL-er, CTA-er og kontaktform er kontrollert | Etter verifisering og første dataperiode |

## Teknisk status ved oppsett

- `robots.txt` peker til sitemap: **bestått**
- `sitemap.xml` er gyldig XML: **bestått**
- viktige sider har canonical: **bestått**
- interne lenker er kontrollert: **bestått**
- JSON-LD er kontrollert: **bestått**
- kontaktform har målrettet CTA og valgfritt omfangsfelt: **bestått**
- ekstern analyseplattform: **ikke installert**
- Search Console-verifisering: **krever Google-kontotilgang**
