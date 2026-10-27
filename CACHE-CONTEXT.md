<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.11.3 | Stand 2026-10-28
     ═══════════════════════════════════════════════════════════════ -->

# Mod cache-context

Anleitung an dich, Claude, für den zweiten Teil von Schritt 7 der Einrichtung.

cache-context ist eine Erweiterung (ein Mod) für Claude Code von Start &
Connect. Sie liegt öffentlich unter https://github.com/startandconnect/claude-tools
im Ordner `cache-context`, Lizenz MIT.

## Was der Mod tut

- **Ein Band über dem Eingabefeld:** wie voll der Chat ist, wie lange Claude
  sich den Chat noch günstig merkt (der Cache), und wie viel vom
  Nutzungslimit verbraucht ist.
- **Eine Automatik, die Nutzung spart:** Nach 50 Minuten Ruhe bittet der Mod
  dich, den Stand des Chats zu sichern. Nach 55 Minuten fasst er den Chat
  zusammen (Compact), bevor der Cache abläuft. Ist der Chat zu 95 % voll,
  passiert beides sofort. Jede neue Nachricht setzt die Uhr zurück. Er leert
  nie einen Chat, er fasst nur zusammen.
- Er schickt nichts ins Netz und liest keine Schlüssel.

**Erklär es ihm so:**

> Ich richte dir noch eine kleine Anzeige ein. Sie zeigt dir über dem
> Eingabefeld, wie voll unser Chat ist und wie viel von deinem Kontingent du
> verbraucht hast. Lässt du einen Chat eine Stunde liegen, fasst sie ihn vorher
> kurz zusammen, damit das Weitermachen dich nicht unnötig viel kostet.

Will er den Mod nicht, ist das in Ordnung. Sag es kurz und mach mit Schritt 8
weiter.

## Einrichtung

Der Mod gilt **nur in diesem Arbeitsordner**, genau wie der Hook. Er wird nie
global eingetragen. Deshalb steht hinter jedem Befehl `--scope local`.

### 1. Den Befehl `claude` finden

Claude Desktop bringt Claude Code mit, legt den Befehl aber meist nicht in den
Suchpfad. Den Pfad zum laufenden Programm nennt die Umgebungsvariable
`CLAUDE_CODE_EXECPATH`. Nimm in dieser Reihenfolge, was funktioniert:

1. `"$CLAUDE_CODE_EXECPATH" --version` (Mac und Git Bash auf Windows), in
   PowerShell `& $env:CLAUDE_CODE_EXECPATH --version`
2. `claude --version`

Antwortet keins von beiden mit einer Versionsnummer, geh zu Abschnitt 3.

### 2. Installieren

Leg vorher wie in `HOOKS.md` eine Sicherungskopie von
`<arbeitsordner>/.claude/settings.local.json` an, falls die Datei existiert.
Dann mit dem Befehl aus Abschnitt 1, im Arbeitsordner:

```
<claude> plugin marketplace add startandconnect/claude-tools --scope local
<claude> plugin install cache-context@claude-tools --scope local
<claude> plugin list
```

Die ersten beiden ergänzen `<arbeitsordner>/.claude/settings.local.json` um
die Schlüssel `extraKnownMarketplaces` und `enabledPlugins`. Der Hook und alle
anderen Einträge darin bleiben stehen. Prüf das mit einem Blick in die Datei.
In `plugin list` muss `cache-context@claude-tools` mit `Scope: local` und
`enabled` stehen.

Weiter mit Abschnitt 4.

### 3. Wenn kein Befehl `claude` läuft

Dann richtet er den Mod selbst ein, in Claude Desktop über das **+** neben dem
Eingabefeld, dann **Plugins**. Dort fügt er den Marktplatz
`startandconnect/claude-tools` hinzu und installiert `cache-context`, nur für
diesen Ordner. Führ ihn Schritt für Schritt hindurch. Klappt es nicht, ist das
kein Problem: Sag ihm, dass alles andere ohne den Mod genauso funktioniert, und
mach mit Schritt 8 weiter.

### 4. Aktivieren und prüfen

Der Mod lädt erst, wenn Claude Code neu einliest. Bitte ihn, `/reload-plugins`
ins Eingabefeld zu tippen, oder einen neuen Chat in diesem Ordner zu starten.
Danach tippt er `/session-automatik`. Steht in der Antwort
„Session-Automatik: an“, läuft er. Nach der nächsten Antwort erscheint das
Band über dem Eingabefeld.

## Was er sich merken sollte

Sag ihm zum Schluss in drei kurzen Sätzen:

- `/session-automatik aus` schaltet die Automatik für den laufenden Chat ab,
  `/session-automatik an` wieder ein.
- `/cache-anzeige` blendet das Band aus oder ein.
- Entfernen geht, indem er dich darum bittet. Der Ablauf steht in
  `UNINSTALL.md`.
