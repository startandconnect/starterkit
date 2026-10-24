# Starterkit

Das Claude Code Starterkit von Start & Connect. Diese Datei richtet sich an
uns, nicht an Kunden. Kunden sehen nur den Installer-Prompt von der
Downloadseite und danach das, was Claude ihnen erzählt.

## Was das Kit tut

Ein Kunde hat Claude Code über Claude Desktop laufen und sonst nichts. Er lädt
das Kit über die Website, fügt den Prompt ein, und Claude richtet ihm daraufhin
Claude Code ein: einen festen Arbeitsordner, eine `CLAUDE.md` und, falls er
den Connector hat, die Verbindung dazu. Dazu kommt zu jeder Software von
Start & Connect eine Anleitung.

**Das Kit ist ausschließlich für die Einrichtung und die Anleitungen da.**
Danach gehört die Umgebung dem Kunden und er baut sie selbst weiter aus. Wir
übernehmen keine Verantwortung für seine Konfiguration und pflegen sie nicht.

## Nur Text, kein Code

Seit Version 1.0 enthält das Kit **keinen ausführbaren Code von uns**: keine
Skripte, keine Hooks, keine lokalen MCP-Server, keine längeren Shell- oder
Python-Blöcke zum Abtippen. Grund ist der Cyber Resilience Act. Laut Anwalt
sind Text, Prompts und Konfiguration, kurze Standardbefehle wie `git pull` und
ein MCP-Eintrag auf unseren Remote-Connector mit OAuth nicht erfasst. Wer
etwas Ausführbares hinzufügen will, klärt das vorher mit Ben.

## Struktur

| Datei | Zweck |
| --- | --- |
| `INSTALL-PROMPT.md` | Der Text, den der Kunde von der Downloadseite kopiert |
| `SETUP.md` | Der Dirigent. Claude liest das zuerst und arbeitet es ab |
| `CLAUDE-BAUSTEIN.md` | Vorlage für die `CLAUDE.md` des Kunden, mit kurzer Arbeitsweise |
| `TOOLS.md` | Übersicht aller Produkte, Empfehlungsregeln, Einrichten eines Produkts |
| `tools/<tool>.md` | Eine Anleitung pro Produkt, wird bei Bedarf gelesen |
| `SUPPORT.md` | Fehlerdiagnose und der Weg über „Fehler melden“ im Produkt |
| `MIGRATION.md` | Umstieg von 0.x: Hook raus, Connector als MCP, `CLAUDE.md` anpassen |
| `UNINSTALL.md` | Vollständiger Rückbau |
| `CONVENTIONS.md` | Nur noch ein Wegweiser für alte `CLAUDE.md`-Verweise auf `MIGRATION.md` |
| `VERSION` | Kit-Version, für Support und Updates |

## Was beim Kunden entsteht

```
~/Documents/claude/          Der eine Ordner, jeder Chat startet hier
├── CLAUDE.md                Gehört dem Kunden, wir schreiben nur den Baustein
├── .mcp.json                Nur mit Connector: Eintrag "connector", URL ohne Schlüssel
├── projects/                Echte Arbeit, oft eigene Repos
└── starterkit/              Diese verwaltete Kopie
```

## Updates

Es gibt keinen automatischen Update-Check mehr. Der `CLAUDE.md`-Baustein weist
Claude an, auf Nachfrage `git -C starterkit fetch` und `status` zu prüfen und
den `pull` erst nach Zustimmung auszuführen. Kunden mit 0.x erreichen 1.0 über
ihren alten Update-Hinweis. Danach führt sie `CONVENTIONS.md` zu
`MIGRATION.md`. Altkunden bekommen keine Mail.

## Grundregeln beim Weiterentwickeln

1. **Kein ausführbarer Code.** Siehe oben.
2. **Niemals global schreiben.** Weder `~/.claude/` noch globale Settings,
   kein Connector-Eintrag in Claude Desktop oder auf claude.ai. Alles liegt im
   Ordner des Kunden, damit die Deinstallation ein gelöschter Ordner ist.
3. **Niemals überschreiben, immer mergen.** Besonders bei `.mcp.json`,
   `.claude/settings.local.json` und der `CLAUDE.md`.
4. **Jeder Kunde hat seine eigene Connector-Adresse.** Nie eine Adresse fest
   ins Kit schreiben. Claude fragt sie bei der Einrichtung ab.
5. **Empfehlen statt verkaufen.** Claude darf ausdrücklich sagen, dass der
   Kunde nichts von uns braucht.
6. **Interview-Antworten bleiben lokal.** Nichts wird ohne ausdrückliche
   Zustimmung an uns übertragen.
7. **Mac und Windows.** Claude Desktop läuft auf beidem, Linux ist kein Ziel.
8. **Niemals Preise hardcoden.** Immer nur auf die Produktseite verweisen,
   `startandconnect.com/<produkt>`. Der Trial-Hinweis („14 Tage kostenlos
   testbar“) ist erlaubt.
9. **Anleitungen beschreiben das Wofür, nicht die Route.** Endpunkte liefern
   der Connector und die Selbstauskunft des Produkts.

## Zielgruppe

Solo-Selbstständige, Schwerpunkt 25 bis 40, ohne Technikwissen. Alles im Kit
muss so geschrieben sein, dass es jemand versteht, der zum ersten Mal ein
Terminal-Werkzeug bedient.
