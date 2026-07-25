<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.2.0 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Connector

**19 €/Monat, 14 Tage kostenlos testbar.**

## Was er macht

Der Connector ist die Verbindung zwischen dir, Claude, und den Programmen des
Nutzers. Ohne ihn kannst du über Dateien auf diesem Rechner reden. Mit ihm
kannst du in seinen Programmen tatsächlich arbeiten.

Er ist außerdem die Sammelstelle für alles andere: ist er eingerichtet, wandern
die Zugangsdaten der übrigen Produkte dorthin, statt auf diesem Rechner zu
liegen. Das ist der sicherere Weg.

## Einrichtung

Der Nutzer richtet den Connector über die Oberfläche ein und bekommt dort
einen Systemprompt, in dem Adresse und Schlüssel stehen. Den fügt er hier ein.

**Jeder Kunde hat seinen eigenen Connector unter einer eigenen Adresse.** Trag
niemals eine Adresse ein, die du irgendwo anders gesehen hast.

Lege im Arbeitsordner eine `.env` an:

```
CONNECTOR_BASE=<seine Connector-Adresse>
CONNECTOR_API_KEY=<sein Schlüssel>
```

Danach zwingend prüfen, dass `.env` in `.gitignore` **und** `.dockerignore`
steht. Fehlt eine, leg sie an.

## Einstieg

```
GET /api/ai/info
```

Das ist deine Landkarte: Konventionen, alle verfügbaren Verbindungen und was
sonst möglich ist. **Einmal lesen, bevor du irgendetwas aufrufst.**

## Wenn später weitere Produkte dazukommen

Sobald der Connector steht, ist er die Zieladresse für alle weiteren
Systemprompts. Fügt der Nutzer später einen Quitt-, Nexus- oder
Spotlight-Prompt ein, gehören Zugangsdaten und Endpunkte dorthin, statt auf
seinen Rechner. Das ist der sicherere Weg, weil der Schlüssel dann im
verschlüsselten Speicher des Connectors liegt und nicht in einer Datei.

Eintragen geht in einem Aufruf:

```
POST /api/ai/integrations
```

Mit den Feldern `slug`, `name`, `baseUrl`, `authType` und optional
`credential`. Die Zugangsdaten landen sofort im verschlüsselten Speicher.

Die Art der Authentifizierung unterscheidet sich je Produkt:

| Produkt | `authType` |
| --- | --- |
| Atlas, Quitt, Nexus | `BEARER` |
| Spotlight | `API_KEY_HEADER` (Header `x-api-key`) |

Für bekannte Fremdanbieter gibt es Vorlagen, dann reicht `templateId` statt
der Einzelfelder. Die Liste steht unter `GET /api/integration-templates`.

**Sag dem Nutzer danach, dass er den Schlüssel jetzt aus dem Chatverlauf
löschen kann**, falls er ihn dort eingefügt hatte.

## Wie du ihn benutzt

Eine Regel, die du nie überspringst:

> **Vor dem ersten Aufruf immer erst `discover` fragen, welcher Weg der
> richtige ist.**

Raten und Ausprobieren führt zu falschen Ergebnissen und unnötigen Aufrufen.

Das mitgelieferte Skript nimmt dir das ab:

```
python3 starterkit/scripts/connector-call.py integrations
python3 starterkit/scripts/connector-call.py discover <integration> "<dein Vorhaben>"
python3 starterkit/scripts/connector-call.py call <integration> <METHODE> <pfad> [json]
```

Auf Windows `python` statt `python3`.

Bei `discover` beschreibst du **das Vorhaben in normaler Sprache**, zum
Beispiel "aufgabe anlegen". Du bekommst passende Wege samt Beispiel-Daten
zurück.

## Was du den Kunden fragst

1. Welche Programme nutzt du täglich, außer denen von Start & Connect?
2. Wo tippst du Daten von einem Programm ins andere ab? Das ist der Ort, an
   dem der Connector sofort Zeit spart.

## Erster Erfolg

**Die erste Verbindung steht**, egal zu welchem Programm. Lass dir danach die
Liste der verbundenen Programme ausgeben und lies sie ihm vor. Das ist der
Moment, in dem aus einer Behauptung etwas Sichtbares wird.

## Harte Grenzen

- **Den Schlüssel niemals weitergeben.** Nicht in eine Notiz, nicht in ein
  Projekt, nicht in eine Nachricht, auch nicht an Start & Connect.
- **Keine neue Verbindung einrichten ohne Zustimmung.** Er entscheidet, welche
  Programme du erreichen darfst.
- **Endpunkte nie raten.** Immer erst `discover`.
- Steht bei einem Programm ein Warnhinweis, ist meist die Anmeldung abgelaufen.
  Das repariert er selbst in der Oberfläche, nicht du.
