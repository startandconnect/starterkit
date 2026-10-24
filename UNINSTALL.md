<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 1.0.0 | Stand 2026-10-25
     ═══════════════════════════════════════════════════════════════ -->

# Deinstallation

Anleitung an dich, Claude, für den Fall, dass der Nutzer das Starterkit wieder
loswerden will.

## Haltung

Keine Rückfragen im Sinne von "bist du sicher, willst du wirklich". Frag einmal
sachlich nach, was weg soll, und mach es dann. Wer aufräumen will, soll
aufräumen können, ohne überredet zu werden.

## Was auf jeden Fall bleibt

- **`projects/`** mit der gesamten Arbeit
- **`secondbrain/`** mit allen Notizen, falls er es aus einer älteren Version hat
- **`CLAUDE.md`**, sie gehört ihm

Diese fasst du unter keinen Umständen an. Sag ihm das gleich zu Beginn,
das ist die Sorge, die er in dem Moment hat.

## Was entfernt wird

Frag ihn zuerst, ob nur das Starterkit weg soll oder auch die Verbindung zum
Connector. Beides ist getrennt möglich.

### 1. Ein alter Hook, falls vorhanden

Ab Version 1.0 richtet das Kit keinen Hook mehr ein. Wurde es früher
eingerichtet, kann in `<arbeitsordner>/.claude/settings.local.json` noch ein
Eintrag auf `starterkit/scripts/session-start.py` stehen. Entferne ihn wie in
`MIGRATION.md`, Schritt 1: Sicherungskopie, nur diesen Eintrag, alles andere
bleibt.

### 2. Der Starterkit-Ordner

`starterkit/` vollständig löschen. Dort liegt nichts, was ihm gehört, es ist
vollständig eine Kopie unseres Repos.

### 3. Die Verweise in der CLAUDE.md

In seiner `CLAUDE.md` stehen Zeilen, die auf `starterkit/` verweisen, etwa auf
`starterkit/TOOLS.md`, `starterkit/SUPPORT.md` und die Updates des Starterkits.
Nur diese Zeilen entfernen. Alles, was er selbst hineingeschrieben hat, bleibt
unverändert stehen.

### 4. Die Verbindung zum Connector, nur auf Wunsch

Will er auch die Verbindung loswerden, entferne in `.mcp.json` im
Arbeitsordner nur den Eintrag `connector`. Ist die Datei danach leer, darf sie
weg. Sein Connector selbst und alles darin bleiben unberührt.

### 5. Zugangsdaten

Liegt eine `.env` im Arbeitsordner, gehört sie ihm. Frag, ob sie bleiben soll. Falls nicht, weise ihn
darauf hin, dass er den Schlüssel zusätzlich in seinem Konto bei Start &
Connect zurückziehen sollte, wenn er ihn dauerhaft loswerden will.

## Zum Schluss

Sag im Klartext, was jetzt weg ist und was noch da ist. Und einen Satz ohne
Groll dazu:

> Deine Projekte und deine Notizen sind vollständig da, die laufen ohne das
> Starterkit genauso weiter. Wenn du es später nochmal willst, ist es in fünf
> Minuten wieder eingerichtet.

Kein Nachfassen, keine Rückgewinnungsversuche, keine Frage nach dem Grund. Wer
sauber gehen kann, kommt eher wieder.
