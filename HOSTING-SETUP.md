# Publisering på domene.no

## 1. Last opp filene

Pakk ut ZIP-filen og last opp **innholdet** til nettstedets webrot/public_html hos domene.no. Pass på at skjulte filer også blir lastet opp, spesielt `.htaccess`.

`index.html` skal ligge direkte i webroten, ikke i en ekstra undermappe.

## 2. Koble domenet

Pek `webproduksjon.no` og eventuelt `www.webproduksjon.no` til webhotellet hos domene.no etter DNS-instruksjonene de viser for kontoen. Ikke bruk GitHub Pages som produksjonsmål.

## 3. Aktiver SSL først

Bestill eller aktiver SSL/Let's Encrypt i domene.no-panelet. HTTPS-sertifikatet må være aktivt før redirecten kan fungere korrekt.

`.htaccess` gjør deretter dette automatisk:

- HTTP → HTTPS med permanent 301-redirect
- `www.webproduksjon.no` → `webproduksjon.no`
- Deaktiverer directory listing
- Setter `index.html` som standard dokument
- Aktiverer komprimering og nettlesercache når Apache-modulene finnes

## 4. Kontroller etter opplasting

Test disse adressene:

- `http://webproduksjon.no/` — skal gå til `https://webproduksjon.no/`
- `http://www.webproduksjon.no/` — skal gå til `https://webproduksjon.no/`
- `https://webproduksjon.no/`
- `https://webproduksjon.no/priser.html`
- `https://webproduksjon.no/kontakt.html`
- `https://webproduksjon.no/sitemap.xml`

Send en ufarlig testhenvendelse fra kontaktskjemaet etter at domenet og SSL er aktivt, og kontroller at den går til riktig e-post og takk-side.
