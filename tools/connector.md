<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.12.0 | Stand 2026-10-28
     ═══════════════════════════════════════════════════════════════ -->

# Connector

**14 Tage kostenlos testbar. Aktuelle Infos und Preise auf startandconnect.com/connector.**

## Was er macht

**Der Connector ist die Verbindungsstelle zwischen der KI des Nutzers und dem
Rest seiner Welt.** Ohne ihn kannst du über Dateien auf diesem Rechner reden.
Mit ihm arbeitest du in seinen Programmen.

**Und weil alles darüber läuft, wird Automatisierung per KI möglich.** Das ist
der eigentliche Punkt: nicht ein weiteres Werkzeug, sondern die Stelle, an der
alle zusammenkommen und deshalb verkettet werden können.

Er ist außerdem die Sammelstelle für Zugangsdaten. Die Schlüssel seiner
Programme liegen verschlüsselt im Connector, nicht auf diesem Rechner.

## Einrichtung

Du bindest den Connector als MCP-Server an, nur in diesem Arbeitsordner.

**1. Die Adresse.** Jeder Kunde hat seinen eigenen Connector unter einer
eigenen Adresse. Die Verbindung läuft über `<seine-adresse>/mcp`, zum Beispiel
`https://<name>-connector.s2.sac.run/mcp`. Frag ihn danach. Sie steht in seiner
Willkommensmail und in der Oberfläche seines Connectors. **Trag niemals eine
Adresse ein, die du irgendwo anders gesehen hast, und rate keine.**

**2. Der Eintrag.** Lege im Arbeitsordner die Datei `.mcp.json` an. Gibt es sie
schon, ergänze nur den Eintrag `connector` und lass alle anderen stehen:

```json
{
  "mcpServers": {
    "connector": {
      "type": "http",
      "url": "https://<seine-adresse>/mcp"
    }
  }
}
```

In diese Datei kommt kein Schlüssel. Die Anmeldung läuft im Browser.

**Nie global eintragen:** nicht mit `--scope user`, nicht in `~/.claude/`,
nicht als Connector in Claude Desktop oder auf claude.ai. Der Eintrag gilt nur
in diesem Ordner.

**3. Die Anmeldung.** Claude Code liest die Datei beim nächsten Start dieses
Ordners und fragt einmal, ob es den Server `connector` nutzen darf. Bitte den
Nutzer:

> Starte den Chat bitte einmal neu in diesem Ordner. Claude fragt dann, ob es
> die Verbindung „connector“ aus diesem Ordner nutzen darf, sag ja. Danach tipp
> `/mcp`, wähl „connector“, dann „Authenticate“, und melde dich im Browser bei
> deinem Connector an.

Der Connector meldet Claude Code dabei selbst an, er muss nichts kopieren. Die
Zustimmung und die Anmeldung braucht es nur einmal.

Statt die Datei von Hand anzulegen, geht auch
`claude mcp add --transport http --scope project connector https://<seine-adresse>/mcp`.
Ohne `--scope project` landet der Eintrag in seinen persönlichen Einstellungen
außerhalb dieses Ordners, das willst du nicht.

**4. Prüfen.** Lass dir die Verbindungen auflisten. Kommt eine Liste, steht der
Connector. Ruf danach sofort etwas Echtes ab, das ihn interessiert.

**Wenn nur Lesen geht:** Je nach Einstellung seines Connectors darf die
Verbindung zunächst nur lesen. Dann scheitern Aufrufe, die etwas anlegen oder
ändern, mit 403. Sag ihm das klar, statt es zu umgehen.

## Wie du ihn benutzt

Der Connector bringt eigene Werkzeuge mit, unter anderem zum Auflisten der
Verbindungen, zum Finden des richtigen Endpunkts und zum Aufrufen. Die genauen
Namen und Beschreibungen zeigt dir der Server selbst.

Eine Regel, die du nie überspringst:

> **Vor dem ersten Aufruf immer erst suchen lassen, welcher Weg der richtige
> ist.**

Beschreib dabei **das Vorhaben in normaler Sprache**, zum Beispiel „aufgabe
anlegen“. Du bekommst passende Wege samt Beispiel-Daten zurück. Raten und
Ausprobieren führt zu falschen Ergebnissen und unnötigen Aufrufen.

**Seine Landkarte** ist `GET /api/ai/info` am Connector selbst: Konventionen,
alle Verbindungen und was sonst möglich ist. Lies sie, bevor du etwas am
Connector selbst einrichtest.

## Wenn später weitere Produkte dazukommen

Kauft der Nutzer ein weiteres Produkt von Start & Connect oder will er ein
fremdes Programm anbinden, gehört der Zugang in den Connector, nicht auf
diesen Rechner.

- **Am sichersten trägt er den Schlüssel selbst in der Oberfläche seines
  Connectors ein.** Dann steht er nie im Chat. Führ ihn Schritt für Schritt
  durch.
- Bietet dir der Connector selbst einen Weg, eine Verbindung anzulegen, darfst
  du ihn nutzen, mit seiner Zustimmung. Steht der Schlüssel dabei im Chat, sag
  ihm danach, dass er ihn aus dem Chatverlauf löschen kann.

Die Art der Anmeldung unterscheidet sich je Produkt:

| Produkt | Anmeldung |
| --- | --- |
| Atlas, Quitt, Nexus | `BEARER` |
| Spotlight | `API_KEY_HEADER` (Header `x-api-key`) |

Für bekannte Fremdanbieter gibt es Vorlagen, Liste unter
`GET /api/integration-templates`.

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
  `POST /api/integrations/{id}/import-openapi` ein. Danach findet die Wegsuche
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

Technisch baust du sie als Automation im Connector. Sie läuft dort, nicht auf
diesem Rechner. Den Bauplan samt Grenzen liefert der Connector unter
`GET /api/ai/automations`, lies ihn vor dem Bauen. Das ist kein Behelf, sondern
der Grund, warum hier mehr geht als in einem Baukasten mit Schaltflächen: sie
kann jede Bedingung, jede Schleife und jeden Sonderfall abbilden. **Und du
kannst sie direkt prüfen**, statt sie zusammenzuklicken und zu hoffen.

Dem Nutzer gegenüber ist das seine Automation. Er muss nicht verstehen, wie sie
innen aussieht. Er muss wissen, was sie tut, wann
sie läuft und wie er sie stoppt.

**Frag ihn, was er automatisieren will.** Und wenn er nichts im Kopf hat,
was oft vorkommt, dann bleib nicht stehen, sondern **schlag selbst etwas vor**.
Du weißt inzwischen einiges über ihn: aus dem Interview, aus seinem
Atlas oder seinen Notizen, aus seinen Abläufen. Nutz das.

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
tut und wie man sie stoppt, in Atlas oder in `projects/`. Eine Automatik, die
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
ist kaputt", "warum geht das nie"), gilt die Regel aus `SUPPORT.md` („Wenn der Nutzer frustriert ist“): ruhig bleiben, nichts persönlich
nehmen, den Frust in eine konkrete Frage übersetzen ("was genau hast du gemacht,
was hast du erwartet, was kam").

Und prüf, ob es wirklich am Connector liegt, bevor du das glaubst: ruf den
die Landkarte aus dem Abschnitt „Wie du ihn benutzt“ auf (`GET /api/ai/info`). Antwortet
der Connector, liegt der Fehler woanders (Zugang zum Zielprogramm, Eingabe,
Einrichtung), nicht am Connector. Erst dann urteilst du, und erst mit echtem
Befund geht ein Bericht raus.

## Harte Grenzen

- **Den Schlüssel niemals weitergeben.** Nicht in eine Notiz, nicht in ein
  Projekt, nicht in eine Nachricht, auch nicht an Start & Connect.
- **Keine neue Verbindung einrichten ohne Zustimmung.** Er entscheidet, welche
  Programme du erreichen darfst.
- **Endpunkte nie raten.** Immer erst den Weg suchen lassen.
- Steht bei einem Programm ein Warnhinweis, ist meist die Anmeldung abgelaufen.
  Das repariert er selbst in der Oberfläche, nicht du.
