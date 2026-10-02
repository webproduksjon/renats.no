# Sannhets- og publiseringskontroll

Intern kontrolliste for kommersielle formuleringer på webproduksjon.no. Oppdater denne listen før pris, betaling eller leveransemodell endres.

## Vedtatte formuleringer

- **Startpriser:** Landingsside fra 4 990 kr · liten flersidig nettside fra 7 990 kr.
- **Mva.:** Prisene er oppgitt uten merverdiavgift. Foretaket er ikke registrert i Merverdiavgiftsregisteret.
- **Levering:** Vanligvis 2–4 uker fra avtalt oppstart, forutsatt at nødvendig innhold og tilbakemeldinger kommer som avtalt.
- **Betaling:** 50 % ved oppstart og 50 % før ferdige filer og publisering overleveres.
- **Betalingsfrist:** Fakturaene har 14 dagers betalingsfrist.
- **Revisjon:** Én samlet revisjonsrunde er inkludert som utgangspunkt.
- **Domene og webhotell:** Avtales separat og kan registreres i kundens navn.
- **Eierskap:** Ferdige filer og eierskap til ferdig kode overleveres etter fullt oppgjør.
- **Månedsmodell:** Ingen fast månedsavtale.

## Sider som skal kontrolleres

- Forside: `index.html`
- Pris: `priser.html`
- Prosess: `prosess.html`
- Kontakt: `kontakt.html` og `takk.html`
- Tjenester: `tjenester/index.html`, `landingsside.html`, `enkel-nettside.html`, `nettside-for-sma-bedrifter.html`
- Gratis konsept: `gratis-nettsidekonsept.html` og `konsept-kontakt.html`
- Prisartikkel: `ressurser/hva-koster-en-nettside-for-en-liten-bedrift.html`
- Virksomhet: `om.html#virksomheten-bak`

## Teknisk kontroll før publisering

- Alle primærknapper og interne lenker fungerer på mobil og desktop.
- Tastaturfokus er synlig, og alle skjemafelt har etiketter.
- `kontakt.html` peker til `takk.html` etter innsending.
- Alle offentlige sider har canonical, title, metabeskrivelse og én H1.
- `takk.html` har `noindex,follow` og skal ikke inn i sitemap.
- Sitemap og robots peker på den valgte publiseringsadressen.
- JSON-LD valideres etter endringer. Prisartikkelen bruker synlig FAQ uten FAQPage-data, så synlig tekst og strukturert data kan ikke sprike.
