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

Ab Version 1.0 enthält das Kit **keinen ausführbaren Code von uns**: keine
Skripte, keine Hooks, keine lokalen MCP-Server, keine längeren Shell- oder
Python-Blöcke zum Abtippen. Grund ist der Cyber Resilience Act. Laut Anwalt
sind Text, Prompts und Konfiguration, kurze Standardbefehle wie `git pull` und
ein MCP-Eintrag auf unseren Remote-Connector mit OAuth nicht erfasst. Wer
etwas Ausführbares hinzufügen will, klärt das vorher mit Ben.

**Einzige Ausnahme, von Ben beauftragt (T-5049, freigegeben mit T-4500 am
28.10.2026):** Das Kit bietet den Mod cache-context an. Sein Code liegt nicht im
Kit, sondern im eigenen öffentlichen Repo `startandconnect/claude-tools` (MIT).
Das Kit enthält nur die Anleitung, ihn mit `--scope local` für den Arbeitsordner
zu installieren, und der Kunde stimmt vorher zu. Ob das für den CRA genauso
unkritisch ist, ist beim Anwalt noch nicht bestätigt.

## Struktur

| Datei | Zweck |
| --- | --- |
| `INSTALL-PROMPT.md` | Der Text, den der Kunde von der Downloadseite kopiert |
| `SETUP.md` | Der Dirigent. Claude liest das zuerst und arbeitet es ab |
| `CLAUDE-BAUSTEIN.md` | Vorlage für die `CLAUDE.md` des Kunden, mit kurzer Arbeitsweise |
| `TOOLS.md` | Übersicht aller Produkte, Empfehlungsregeln, Einrichten eines Produkts |
| `CACHE-CONTEXT.md` | Installiert auf Wunsch den Mod cache-context aus `startandconnect/claude-tools`, nur für den Arbeitsordner |
| `tools/<tool>.md` | Eine Anleitung pro Produkt, wird bei Bedarf gelesen |
| `SUPPORT.md` | Fehlerdiagnose und der Weg über „Fehler melden“ im Produkt |
| `MIGRATION.md` | Umstieg von 0.11 und älter: Hook raus, Connector als MCP, `CLAUDE.md` anpassen |
| `UNINSTALL.md` | Vollständiger Rückbau |
| `CONVENTIONS.md` | Nur noch ein Wegweiser für alte `CLAUDE.md`-Verweise auf `MIGRATION.md` |
| `VERSION` | Kit-Version, für Support und Updates |

## Was beim Kunden entsteht

```
~/Documents/claude/          Der eine Ordner, jeder Chat startet hier
├── CLAUDE.md                Gehört dem Kunden, wir schreiben nur den Baustein
├── .mcp.json                Nur mit Connector: Eintrag "connector", URL ohne Schlüssel
├── .claude/                 Nur mit Mod: settings.local.json mit cache-context
├── projects/                Echte Arbeit, oft eigene Repos
└── starterkit/              Diese verwaltete Kopie
```

## Updates

Es gibt keinen automatischen Update-Check mehr. Der `CLAUDE.md`-Baustein weist
Claude an, auf Nachfrage `git -C starterkit fetch` und `status` zu prüfen und
den `pull` erst nach Zustimmung auszuführen.

Altkunden (0.11 und älter) bekommen keine Mail, das Supportende für 0.11.x gilt
ab sofort (Ben, 24.10.2026). Sie erreichen den Umstieg in zwei Stufen:

1. **0.12.0, Migrationsversion.** Alle Texte wie 1.0, dazu als einziges Skript
   noch `scripts/session-start.py`. Es gibt nur den festen Hinweis „Bitte
   migrieren“ aus, ohne git, ohne Netz, ohne Schreibzugriff. So läuft der alte
   Hook weiter, ohne Fehler, bis `MIGRATION.md` ihn entfernt. Der alte
   Update-Check bietet den Pull auf 0.12.0 von selbst an.
2. **1.0.0.** Entfernt auch dieses Skript. Wer dann noch den alten Hook hat,
   sieht beim Start einen Hook-Fehler, und `CONVENTIONS.md` führt Claude zu
   `MIGRATION.md`.

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
