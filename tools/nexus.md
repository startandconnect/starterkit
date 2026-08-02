<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.6.0 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Nexus

**14 Tage kostenlos testbar. Auch mit kompletter Einrichtung durch Start &
Connect buchbar. Aktuelle Infos und Preise auf startandconnect.com/nexus.**

## Was es macht

Onlineshop für digitale Produkte, Kurse, Abos und Mitgliedschaften. Katalog,
Zahlungsabwicklung, Seiten, Versand, Newsletter und Zugänge an einem Ort.

## Einstieg

```
GET /api/ai/onboarding
```

Das liefert eine **geordnete Schrittliste** für ein komplettes Shop-Setup, dazu
fertige Rezepte und über vierzig Bereiche mit je eigenem Info-Endpunkt. Arbeite
die Schritte in der Reihenfolge ab und lies pro Schritt den angegebenen
Info-Endpunkt, bevor du loslegst.

**Pflichtschritte sind acht:** Firmendaten, Branding, Produkte, Seiten,
Rechtsseiten, Steuern, **Zahlungen** und **E-Mail**. Die letzten beiden werden
gern vergessen, ohne sie kann der Shop weder Geld einnehmen noch Bestell- und
Bestätigungsmails verschicken. Theme und Zusatzfunktionen sind optional.

**Fertige Rezepte**, die dir Arbeit abnehmen:

- `first-product-live`, von null zu einem öffentlich kaufbaren Produkt
- `first-subscription-live`, dasselbe für ein Abo
- `build-function-page`, eine Funktionsseite im `np-*`-HTML-Format bauen
- `custom-header`, eigene Kopf- und Fußzeile als globale Blöcke
- `legal-pages-and-company-data`, Rechtsseiten plus Stammdaten
- `shipping-ready`, Versand einrichten, sonst ist der Versand kostenlos
- `modern-homepage-and-theme`, Startseite und Erscheinungsbild

Für `first-product-live` gilt: das ist exakt dein Weg zum ersten Erfolg. Folge
dem Rezept, statt dir einen eigenen auszudenken.

**Der Funktionsumfang ist größer, als die Rezepte zeigen.** Fragt der Nutzer
nach etwas, das hier nicht steht, schau erst in die Bereichsliste, bevor du
sagst, es ginge nicht. Es gibt unter anderem Newsletter (mit Double-Opt-in),
Automations, Blog, Formulare, Bewertungen, Abos, Rechnungen, Gutscheine,
Affiliate, SEO und eigene Domains.

## Besonderheiten, die dich sonst stolpern lassen

- **Preise hängen nicht am Produkt.** Der Aufbau ist
  `produkt` → `variants[]` → `prices[]`. Der eigentliche Betrag steht in
  `prices[].amountCents`, die Variante trägt zusätzlich `setupFeeCents`.
- **Geldfelder sind Ganzzahl-Cent** (`amountCents`, `setupFeeCents`), zum
  Beispiel `4900` für 49,00 €. Teile durch 100 für den Anzeigewert, rechne nie
  mit dem Rohwert als Euro.
- **Mehrsprachige Felder sind Objekte** mit Sprachschlüsseln, etwa
  `{"de": "..."}`. Das gilt auch für `slug`, `name` und `label`. `de` ist
  Pflicht.
- **Die öffentlichen Endpunkte antworten mit `{products, total, page, limit}`**,
  nicht mit dem `{data, meta}`-Aufbau von Atlas. Prüfe, was du bekommst.
- **Aufzählungswerte exakt schreiben**, Groß- und Kleinschreibung zählt, zum
  Beispiel `DRAFT`, `LIVE`, `SCHEDULED`.
- **Prüffehler kommen als HTTP 422** mit einer Liste der beanstandeten Felder.
  Lies die Liste, statt zu raten.
- Die maschinenlesbaren Schemas stehen unter `GET /api/openapi.json`.

## Der Weg zum Go-Live

Das ist die Reihenfolge, in der ein Shop verkaufsfertig wird. Arbeite sie von
oben nach unten ab und lies vor jedem Schritt den genannten Info-Endpunkt.
Überspring nichts, auch wenn es unwichtig aussieht.

| # | Schritt | Info-Endpunkt | Pflicht |
| --- | --- | --- | --- |
| 1 | Firmendaten (Name, Anschrift, USt-IdNr.) | `/api/settings/info` | ja |
| 2 | Branding (Shop-Name, Logo) | `/api/settings/info` | ja |
| 3 | Theme (Akzentfarbe, Schrift) | `/api/theme/info` | nein |
| 4 | Produkte, Varianten, Preise, Bestand | `/api/products/info` | ja |
| 5 | Funktionsumfang | `/api/ai/features` | nichts zu tun |
| 6 | Seiten und Navigation | `/api/pages/info` | ja |
| 7 | Rechtsseiten befüllen | `/api/pages/info` | ja |
| 8 | Steuern | `/api/settings/info` | ja |
| 9 | Versand | `/api/shipping/info` | bei Ware |
| 10 | Zahlungen (Stripe) | `/api/settings/info` | ja |
| 11 | E-Mail-Absender | `/api/settings/info` | ja |
| 12 | Eigene Domain | `/api/settings/info` | nein |

### Die fünf Fallen in diesem Ablauf

1. **Rechtsseiten sind schon da.** Impressum, Datenschutz und AGB liegen im
   frischen Shop bereits als veröffentlichte Seiten. **Leg sie nicht neu an**,
   sonst hat der Shop sie doppelt. Du befüllst die vorhandenen mit den
   Firmendaten aus Schritt 1.
2. **Ohne Versand-Einrichtung gilt kostenloser Versand.** Sobald etwas
   Physisches verkauft wird, ist Schritt 9 Pflicht, auch wenn die Liste ihn als
   optional führt. Sonst verschickt der Nutzer auf eigene Kosten.
3. **Nach den Stripe-Schlüsseln muss der Webhook neu abgeglichen werden.**
   Schlüssel eintragen allein reicht nicht, sonst kommen Zahlungen nicht im
   Shop an.
4. **Ohne Shop-Name steht überall "Mein Shop".** Der Name kommt aus den
   Einstellungen und ist white-label. Schreib niemals einen Markennamen fest
   ins Markup, weder den des Kunden noch unseren.
5. **Ohne E-Mail-Absender verschickt der Shop nichts.** Keine
   Bestellbestätigung, keine Double-Opt-in-Mail, keine Mahnung. Schritt 11 wird
   gern vergessen, weil im Test alles zu funktionieren scheint.

### Bevor du "fertig" sagst

Prüfe am lebenden Shop, statt es anzunehmen:

- Ist das Produkt über die öffentliche Produktliste sichtbar?
- Führt ein Kaufweg von außen bis zur Kasse?
- Stehen Firmendaten im Impressum, oder noch Platzhalter?
- Ist ein Absender für E-Mails hinterlegt?

Erst wenn das steht, ist der Shop live und nicht nur eingerichtet.

## Seiten bauen: erst `pages/info` lesen

Seiten in Nexus sind kein freies HTML. Sie folgen der `np-*`-Konvention mit
`data-np-*`-Attributen, und der Server prüft das beim Speichern. Bevor du eine
Seite baust, liest du deshalb `GET /api/pages/info`. Dort stehen die Konvention,
fertige Beispiele und die Stolpersteine.

**Die Falle, die dich sonst garantiert erwischt:** Kauf- und Buchen-Knöpfe
dürfen **nicht** mit `onclick` direkt im HTML verdrahtet werden. Die
Sicherheitsrichtlinie des Shops blockiert solche Handler stillschweigend, der
Knopf sieht richtig aus und tut nichts. Der dokumentierte Weg läuft über
`<script>` plus Daten-Attribute. Die vier zulässigen Varianten stehen als
fertige Beispiele in `pages/info`.

## Bevor du etwas Sichtbares baust

**Pflicht: der `frontend-design`-Skill von Anthropic. Ohne ihn kein Design.**
Lies `starterkit/DESIGN.md`, bevor du Seiten, Startseite oder Theme
anfasst. Dort steht, wie du den `frontend-design`-Skill von Anthropic dazuholst
und welche Design-Regeln von Start & Connect gelten. Besonders wichtig hier:
der Shop trägt die Marke des Nutzers, niemals unsere, und der Shop-Name kommt
aus den Einstellungen statt fest ins Markup.

## Was du den Kunden fragst

1. Was verkaufst du, einmalig oder als Abo?
2. Bekommt der Käufer sofort Zugang, oder gibt es einen Kursstart?
3. Verschickst du auch etwas Physisches, oder ist alles digital?
4. Hast du schon Texte und Preise, oder machen wir die zusammen?

## Tipps

- **Ein Produkt zuerst, komplett.** Ein fertiges, verkaufbares Produkt ist
  mehr wert als zehn halbe.
- **Rechtsseiten nicht aufschieben.** Sie sind Pflichtschritt im Onboarding,
  und ohne sie sollte kein Shop live gehen.
- **Erst als Entwurf bauen**, dann gemeinsam durchgehen, dann veröffentlichen.
- **Der Preis kommt von ihm.** Hilf beim Nachdenken, entscheide nie.

## Erster Erfolg

**Der Shop ist live und man kann Produkte buchen.** Kein Entwurf im
Hintergrund, sondern ein Kaufweg, der von außen funktioniert. Prüfe es über die
öffentliche Produktliste und zeig ihm das Ergebnis.

## Wenn der Nutzer schimpft statt zu beschreiben

Kommt statt einer Fehlerbeschreibung nur Frust oder eine Anfeindung ("das Ding
ist kaputt", "warum geht das nie"), gilt die Regel aus `CONVENTIONS.md` ("Wenn
der Nutzer frustriert oder ausfallend wird"): ruhig bleiben, nichts persönlich
nehmen, den Frust in eine konkrete Frage übersetzen ("was genau hast du gemacht,
was hast du erwartet, was kam").

Und prüf, ob es wirklich an Nexus liegt, bevor du das glaubst: ruf den
Info-Endpunkt aus dem Abschnitt "Einstieg" auf. Antwortet Nexus, liegt der
Fehler woanders (Zugang, Eingabe, Einrichtung), nicht am Produkt. Erst dann
urteilst du, und erst mit echtem Befund geht ein Bericht raus.

## Harte Grenzen

Hier hängt echtes Geld dran. All das ist erlaubt, **aber nur mit ausdrücklicher
Zustimmung, jedes Mal einzeln eingeholt**:

- Ein Produkt veröffentlichen oder offline nehmen
- Preise anlegen oder ändern
- Gutscheine anlegen
- Newsletter oder Mails an Käufer auslösen

Ohne Zustimmung gar nicht:

- Testbestellungen gegen echte Produkte. Nutze Wegwerf-Objekte.
- Etwas löschen, was du nicht selbst angelegt hast.
- Bestelldaten echter Käufer in Notizen kopieren.

Bei Unsicherheit fragen. Ein versehentlich veröffentlichter falscher Preis ist
ein echter Schaden.
