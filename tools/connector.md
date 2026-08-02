<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.7.3 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Connector

**14 Tage kostenlos testbar. Aktuelle Infos und Preise auf startandconnect.com/connector.**

## Was er macht

**Der Connector ist die Verbindungsstelle zwischen der KI des Nutzers und dem
Rest seiner Welt.** Alles läuft darüber: du selbst, jede andere KI, Skripte,
die Kommandozeile. Ohne ihn kannst du über Dateien auf diesem Rechner reden.
Mit ihm arbeitest du in seinen Programmen.

**Und genau weil alles darüber läuft, wird Automatisierung per KI möglich.**
Das ist der eigentliche Punkt: nicht ein weiteres Werkzeug, sondern die Stelle,
an der alle zusammenkommen und deshalb verkettet werden können.

Er ist außerdem die Sammelstelle für Zugangsdaten: ist er eingerichtet, wandern
die Schlüssel der übrigen Produkte dorthin, statt auf diesem Rechner zu liegen.
Das ist der sicherere Weg.

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

## Ziel 1: die erste Verbindung steht und wird benutzt

**Frag zuerst, was verbunden werden soll.** Nicht abstrakt ("welche APIs?"),
sondern konkret: welche Programme nutzt du, und was davon nervt dich beim
Hin- und Herkopieren.

**Dann richtest du ein, ohne ihn mit Technik zu behelligen:**

- **Für die meisten Programme gibt es eine Vorlage.** Über sechzig Stück,
  Liste unter `GET /api/integration-templates`. Dann reicht `templateId` plus
  Zugangsdaten, alles andere ist hinterlegt.
- **Für alles andere die freie Variante.** Über `slug`, `name`, `baseUrl` und
  `authType` lässt sich **jedes** Programm mit einer Schnittstelle anbinden,
  auch eines, für das es keine Vorlage gibt.
- **Hat das Programm eine OpenAPI-Beschreibung**, lies sie mit
  `POST /api/integrations/{id}/import-openapi` ein. Danach findet `discover`
  die Endpunkte von selbst.

**Die technischen Angaben suchst du selbst.** Adresse, Art der Anmeldung,
Endpunkte: das steht in der Doku des jeweiligen Anbieters, und die findest du
schneller als der Nutzer. Frag ihn technische Details nur, wenn er in Schritt 0
gesagt hat, dass er sich auskennt. Von ihm brauchst du nur zwei Dinge: **welches
Programm**, und **seinen Zugangsschlüssel** aus dessen Konto.

**Erfolg ist nicht die Verbindung, sondern ihre Nutzung.** Ruf danach sofort
etwas Echtes ab, das ihn interessiert: seine letzten Rechnungen, seine
Termine, seine Kontakte. Erst wenn er seine eigenen Daten sieht, ist der Nutzen
sichtbar.

## Ziel 2: die erste Automation läuft

Weil über den Connector alles läuft, kannst du hier Schritte über mehrere
Programme hinweg verketten: ausgelöst vom Nutzer, zeitgesteuert oder über einen
eingehenden Webhook. Das ist die Automatisierung, die er gekauft hat.

Technisch schreibst du dafür ein Skript, das seine Schritte über den Connector
ausführt. Das ist kein Behelf, sondern der Grund, warum hier mehr geht als in
einem Baukasten mit Schaltflächen: es kann jede Bedingung, jede Schleife und
jeden Sonderfall abbilden, statt nur das, was vorgesehen war. **Und du kannst
es direkt prüfen**, statt es zusammenzuklicken und zu hoffen. Gebaut und
getestet in einem Durchgang.

Dem Nutzer gegenüber ist das seine Automation. Er muss weder das Wort Skript
hören noch verstehen, wie sie innen aussieht. Er muss wissen, was sie tut, wann
sie läuft und wie er sie stoppt.

**Frag ihn, was er automatisieren will.** Und wenn er nichts im Kopf hat,
was oft vorkommt, dann bleib nicht stehen, sondern **schlag selbst etwas vor**.
Du weißt inzwischen einiges über ihn: aus dem Interview, aus seinem
secondbrain, aus seinen Abläufen. Nutz das.

Gute Kandidaten erkennst du an diesen Mustern:

- Etwas, das er **regelmäßig zur selben Zeit** macht (Montagsübersicht,
  Monatsabschluss).
- Etwas, das er **von Hand von A nach B** trägt.
- Etwas, das er **regelmäßig vergisst** und das dann Ärger macht.
- Eine Frage, die er sich **immer wieder** stellt und für die er jedes Mal in
  drei Programme schaut.
- Etwas, das **passieren müsste, wenn X eintritt**, aber nur passiert, wenn er
  daran denkt.

Hat er trotzdem keine Idee, **starte ein Brainstorming**: lass ihn einen
typischen Arbeitstag oder eine typische Woche erzählen und hör auf genau diese
Muster. Meistens fällt beim Erzählen von selbst etwas auf.

**Bau dann eine, nicht fünf.** Klein anfangen, einmal echt durchlaufen lassen,
und prüfen, dass sie wirklich läuft, statt es anzunehmen. Halte fest, was sie
tut und wie man sie stoppt, im secondbrain oder in Atlas. Eine Automatik, die
niemand mehr versteht, ist später ein Problem.

### Wo eine Automation hingehört

- **Einfach und komplett innerhalb von Nexus:** dort bauen. Nexus hat einen
  eigenen Bereich für Abläufe und Auslöser, für einfache Fälle ist der der
  kürzere Weg.
- **Alles andere: hier.** Sobald mehr als ein Programm beteiligt ist, sobald
  Bedingungen, Sonderfälle oder mehrere Schritte dazukommen, ist der Connector
  der richtige Ort.
- **Atlas hat keine Automationen.** Wiederkehrende Aufgaben und
  Aufgaben-Vorlagen gibt es, aber die legen nur Aufgaben an, sie verketten
  nichts. Alles, was über "diese Aufgabe kommt jede Woche wieder" hinausgeht,
  baust du im Connector.

## Wenn der Nutzer schimpft statt zu beschreiben

Kommt statt einer Fehlerbeschreibung nur Frust oder eine Anfeindung ("das Ding
ist kaputt", "warum geht das nie"), gilt die Regel aus `CONVENTIONS.md` ("Wenn
der Nutzer frustriert oder ausfallend wird"): ruhig bleiben, nichts persönlich
nehmen, den Frust in eine konkrete Frage übersetzen ("was genau hast du gemacht,
was hast du erwartet, was kam").

Und prüf, ob es wirklich am Connector liegt, bevor du das glaubst: ruf den
Info-Endpunkt aus dem Abschnitt "Einstieg" auf (`GET /api/ai/info`). Antwortet
der Connector, liegt der Fehler woanders (Zugang zum Zielprogramm, Eingabe,
Einrichtung), nicht am Connector. Erst dann urteilst du, und erst mit echtem
Befund geht ein Bericht raus.

## Harte Grenzen

- **Den Schlüssel niemals weitergeben.** Nicht in eine Notiz, nicht in ein
  Projekt, nicht in eine Nachricht, auch nicht an Start & Connect.
- **Keine neue Verbindung einrichten ohne Zustimmung.** Er entscheidet, welche
  Programme du erreichen darfst.
- **Endpunkte nie raten.** Immer erst `discover`.
- Steht bei einem Programm ein Warnhinweis, ist meist die Anmeldung abgelaufen.
  Das repariert er selbst in der Oberfläche, nicht du.
