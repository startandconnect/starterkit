<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.12.0 | Stand 2026-10-28
     ═══════════════════════════════════════════════════════════════ -->

# Der CLAUDE.md-Baustein

Anleitung an dich, Claude. Diesen Baustein schreibst du bei der Einrichtung
(`SETUP.md`, Schritt 4) und beim Umstieg von einer älteren Version
(`MIGRATION.md`) in die `CLAUDE.md` im Arbeitsordner.

Die `CLAUDE.md` gehört dem Nutzer. Gibt es schon eine, ergänzt du den Baustein
am Ende und löschst nichts. Halte sie kurz, sie wird bei jedem Chat geladen.

Passe Sprache und Ansprache an das an, was er in Schritt 0 gesagt hat. Bei
Sie-Form oder Englisch schreibst du den Baustein entsprechend um. Abschnitte in
eckigen Klammern füllst du aus oder lässt sie weg, wenn sie nicht zutreffen.

## Vorlage

```markdown
# Wer ich bin

[Aus dem Interview: Name, Tätigkeit, woran ich gerade am meisten arbeite]

# Wie dieser Ordner aufgebaut ist

- `projects/` meine Arbeit, ein Ordner pro Projekt
- `starterkit/` von Start & Connect verwaltet, bitte nicht bearbeiten

# Wie du mit mir arbeitest

- Sprich mit mir [Deutsch, per du]. Kurze Sätze, Fachbegriffe übersetzen.
- Lies nie den ganzen Ordner auf einmal, nur was zur Aufgabe gehört.
- Ohne meine ausdrückliche Zustimmung nie: etwas versenden, veröffentlichen,
  bezahlen, löschen, was du nicht selbst angelegt hast, oder etwas außerhalb
  dieses Ordners ändern. Frag jedes Mal einzeln.
- Bist du unsicher, frag nach, statt etwas Plausibles zu erfinden.

# Software von Start & Connect

- Übersicht: `starterkit/TOOLS.md`, je Produkt `starterkit/tools/<produkt>.md`.
  Lies die Anleitung, bevor du mit einem Produkt arbeitest.
- Klemmt etwas: `starterkit/SUPPORT.md`.
- [Nur mit Connector:] Meine Programme erreichst du über den Connector, er ist
  als MCP-Server `connector` in `.mcp.json` eingetragen. Vor dem ersten Aufruf
  immer erst den passenden Weg suchen lassen, nie Pfade raten.
- [Ohne Connector, mit direkt angebundenem Produkt:] Der Schlüssel für
  [Produkt] liegt in `.env`. Diese Datei nie vorlesen und ihren Inhalt nie
  weitergeben.
- Eingerichtet: [die Produkte, die ich tatsächlich habe]
- [Nur mit Atlas:] Mein Wissen und meine Aufgaben liegen in Atlas. Notizen ins
  Atlas-Wiki, Aufgaben als Aufgaben, nichts davon in lokale Dateien. Steige
  ich in die Arbeit ein, hol zuerst die heutigen Aufgaben aus Atlas.

# Updates des Starterkits

Frage ich nach Neuerungen, oder wirkt eine Anleitung in `starterkit/` veraltet:
`git -C starterkit fetch`, dann `git -C starterkit status`. Ist eine neuere
Version da, frag mich, ob du `git -C starterkit pull` ausführen sollst. Danach
lies `starterkit/MIGRATION.md`, falls dort ein Schritt für meine Version steht.
```

## Was du dabei beachtest

- **Nur ein Abschnitt pro Thema.** Steht bei einem Umstieg schon ein alter
  Abschnitt „Zugang zu meinen Programmen“ oder ein Verweis auf
  `starterkit/CONVENTIONS.md`, `starterkit/DESIGN.md` oder
  `starterkit/scripts/`, ersetzt du ihn durch den neuen Text, statt beides
  stehen zu lassen. Was der Nutzer selbst geschrieben hat, bleibt.
- **Keine Zugangsdaten in die `CLAUDE.md`.** Dort steht nur, wo etwas liegt,
  nie der Schlüssel selbst.
