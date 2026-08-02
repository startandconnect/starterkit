<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.5.2 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Deinstallation

Anleitung an dich, Claude, für den Fall, dass der Nutzer das Starterkit wieder
loswerden will.

## Haltung

Keine Rückfragen im Sinne von "bist du sicher, willst du wirklich". Frag einmal
sachlich nach, was weg soll, und mach es dann. Wer aufräumen will, soll
aufräumen können, ohne überredet zu werden.

## Was auf jeden Fall bleibt

- **`secondbrain/`** mit allen Notizen
- **`projects/`** mit der gesamten Arbeit
- **`CLAUDE.md`**, sie gehört ihm

Diese drei fasst du unter keinen Umständen an. Sag ihm das gleich zu Beginn,
das ist die Sorge, die er in dem Moment hat.

## Was entfernt wird

Frag ihn zuerst, ob nur das Starterkit weg soll oder auch die Erinnerungen.
Beides ist getrennt möglich.

### 1. Der Hook

In `<arbeitsordner>/.claude/settings.local.json`:

- Datei einlesen, **Sicherungskopie anlegen**.
- Nur den Eintrag entfernen, der auf `starterkit/scripts/session-start.py`
  zeigt. Alle anderen Hooks und alle übrigen Einstellungen bleiben unberührt.
- Ist das `SessionStart`-Array danach leer, kannst du den leeren Schlüssel
  entfernen.
- Zurückschreiben.

### 2. Der Starterkit-Ordner

`starterkit/` vollständig löschen. Dort liegt nichts, was ihm gehört, es ist
vollständig eine Kopie unseres Repos.

### 3. Die Pointer in der CLAUDE.md

In seiner `CLAUDE.md` stehen Zeilen, die auf `starterkit/CONVENTIONS.md` und
`starterkit/TOOLS.md` verweisen. Nur diese Zeilen entfernen. Alles, was er
selbst hineingeschrieben hat, bleibt unverändert stehen.

### 4. Die Erinnerungen, nur auf Wunsch

Wenn er das ausdrücklich will, entferne die Erinnerungen, die bei der
Einrichtung angelegt wurden. Zeig sie ihm vorher, damit er entscheiden kann, ob
wirklich alle weg sollen. Manches davon, etwa wer er ist und woran er arbeitet,
will er vielleicht behalten.

### 5. Zugangsdaten

Die `.env` gehört ihm. Frag, ob sie bleiben soll. Falls nicht, weise ihn
darauf hin, dass er den Schlüssel zusätzlich in seinem Konto bei Start &
Connect zurückziehen sollte, wenn er ihn dauerhaft loswerden will.

## Zum Schluss

Sag im Klartext, was jetzt weg ist und was noch da ist. Und einen Satz ohne
Groll dazu:

> Deine Notizen und deine Projekte sind vollständig da, die laufen ohne das
> Starterkit genauso weiter. Wenn du es später nochmal willst, ist es in fünf
> Minuten wieder eingerichtet.

Kein Nachfassen, keine Rückgewinnungsversuche, keine Frage nach dem Grund. Wer
sauber gehen kann, kommt eher wieder.
