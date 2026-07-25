<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.4.7 | Stand 2026-07-25
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
fertige Rezepte und 41 Bereiche mit je eigenem Info-Endpunkt. Arbeite die
Schritte in der Reihenfolge ab und lies pro Schritt den angegebenen
Info-Endpunkt, bevor du loslegst.

Die Pflichtschritte sind Firmendaten, Branding, Produkte, Seiten, Rechtsseiten
und Steuern. Theme und Zusatzfunktionen sind optional.

**Fertige Rezepte**, die dir Arbeit abnehmen, unter anderem:

- `first-product-live`, von null zu einem öffentlich kaufbaren Produkt
- `first-subscription-live`, dasselbe für ein Abo
- `legal-pages-and-company-data`, Rechtsseiten plus Stammdaten
- `shipping-ready`, Versand einrichten
- `modern-homepage-and-theme`, Startseite und Erscheinungsbild

Für `first-product-live` gilt: das ist exakt dein Weg zum ersten Erfolg. Folge
dem Rezept, statt dir einen eigenen auszudenken.

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
