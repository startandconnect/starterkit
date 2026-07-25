# Starterkit

Das Claude Code Starter Kit von Start & Connect. Diese Datei richtet sich an
uns, nicht an Kunden. Kunden sehen nur den Installer-Prompt von der
Downloadseite und danach das, was Claude ihnen erzählt.

## Was das Kit tut

Ein Kunde hat Claude Code über Claude Desktop laufen und sonst nichts. Er fügt
einen Prompt ein, und Claude richtet ihm daraufhin eine saubere Arbeitsbasis
ein: einen festen Ordner, ein Second Brain, Konventionen, Memories, einen
Update-Hook und, falls er ein Produkt von uns hat, den Zugang dazu.

**Das Kit ist ausschließlich für die Einrichtung da.** Danach gehört die
Umgebung dem Kunden und er baut sie selbst weiter aus. Wir übernehmen keine
Verantwortung für seine Konfiguration und pflegen sie nicht.

## Struktur

| Datei | Zweck |
| --- | --- |
| `INSTALL-PROMPT.md` | Der Text, den der Kunde von der Downloadseite kopiert |
| `SETUP.md` | Der Dirigent. Claude liest das zuerst und arbeitet es ab |
| `CONVENTIONS.md` | Verhaltensregeln, die dauerhaft gelten |
| `TOOLS.md` | Übersicht aller SAC-Produkte |
| `RECHERCHE.md` | Valide Primärquellen für Fachrecherche |
| `SUPPORT.md` | Fehlerdiagnose und wann eine Support-Mail sinnvoll ist |
| `SECONDBRAIN.md` | Erklärt und installiert das Second Brain |
| `MEMORIES.md` | Was Claude sich dauerhaft merken soll |
| `HOOKS.md` | Welche Hooks gesetzt werden und wie |
| `UNINSTALL.md` | Vollständiger Rückbau |
| `tools/<tool>.md` | Ein File pro Produkt, wird bei Bedarf gelesen |
| `scripts/` | Helfer, die mitgeliefert werden |
| `VERSION` | Kit-Version, für Support und Update-Check |

## Zwei Repos, bewusst getrennt

- **Dieses Repo** ist eine verwaltete Kopie. Es landet beim Kunden unter
  `starterkit/` und wird bei jedem Update überschrieben. Jede Datei trägt oben
  einen Header, der das sagt.
- **Das Second-Brain-Repo** ist Saatgut. Es wird einmal ausgepackt und danach
  nie wieder angefasst, weil dort die echten Notizen des Kunden liegen.

Diese Trennung ist der Grund, warum ein Update niemals Kundendaten zerstören
kann. Sie darf nicht aufgeweicht werden.

## Was beim Kunden entsteht

```
~/Documents/claude/          Der eine Ordner, jeder Chat startet hier
├── CLAUDE.md                Gehört dem Kunden, wir ergänzen nur Pointer
├── .claude/                 settings.local.json + hooks
├── secondbrain/                   Second Brain, eigenes Repo
├── projects/                Echte Arbeit, oft eigene Repos
└── starterkit/              Diese verwaltete Kopie
```

## Grundregeln beim Weiterentwickeln

1. **Niemals global schreiben.** Weder `~/.claude/CLAUDE.md` noch globale
   Settings. Alles liegt auf Projekt-Ebene im Ordner des Kunden, damit die
   Deinstallation ein gelöschter Ordner ist.
2. **Niemals überschreiben, immer mergen.** Besonders bei
   `.claude/settings.local.json`. Dort können Permissions des Kunden liegen,
   die ein naiver Schreibvorgang vernichtet.
3. **Empfehlen statt verkaufen.** Claude darf ausdrücklich sagen, dass der
   Kunde nichts von uns braucht. Ohne diese Erlaubnis wirkt jede Empfehlung
   wie ein Verkaufsgespräch.
4. **Interview-Antworten bleiben lokal.** Nichts wird ohne ausdrückliche
   Zustimmung an uns übertragen.
5. **Mac und Windows.** Claude Desktop läuft auf beidem, Linux ist kein Ziel.
   Skripte in Python-Standardbibliothek halten, keine Shell-Eigenheiten.
6. **Niemals Preise hardcoden.** Das Kit liegt als Kopie beim Kunden und
   veraltet, Preise ändern sich. Immer nur auf die Produktseite verweisen,
   `startandconnect.com/<produkt>` (z.B. /quitt, /atlas). Der Trial-Hinweis
   ("14 Tage kostenlos testbar") ist erlaubt, das ist ein Angebot, kein Preis.

## Zielgruppe

Solo-Selbstständige, Schwerpunkt 25 bis 40, ohne Technikwissen. Alles im Kit
muss so geschrieben sein, dass es jemand versteht, der zum ersten Mal ein
Terminal-Werkzeug bedient.
