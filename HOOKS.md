<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.4.5 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Hooks

Anleitung an dich, Claude, für Schritt 7 der Einrichtung.

Ein Hook ist eine Automatik, die bei jedem Start eines Chats losläuft. Wir
richten genau **einen** ein. Jeder weitere Hook ist eine weitere Sache, die
kaputtgehen kann, und der Nutzer könnte sie nicht selbst reparieren.

## Der SessionStart-Hook

Ein Script, `scripts/session-start.py`, das beim Start eines Chats vier kleine
Dinge erledigt. Alle sind fail-open: schlägt eines fehl, läuft die Session
normal weiter.

1. **Update-Check.** Schaut, ob es eine neuere Kit-Version gibt, und bietet sie
   an. Aktualisiert nichts von selbst, fasst `secondbrain/` und `projects/`
   nie an.
2. **Doctor-lite.** Nur wenn eine `.env` mit Connector-Key da ist: prüft, ob
   der Connector erreichbar ist. Ist er es nicht, weist der Hinweis dich darauf
   hin, damit du den Nutzer warnen kannst. Ist alles gut, bleibt er still.
3. **Tagesgerüst.** Legt die heutige Session-Datei im secondbrain an, falls sie
   fehlt (nur im lokalen Modus).
4. **Tagesorientierung.** Zeigt die heutigen Prioritäten aus `TODAY.md` (lokal)
   oder weist dich an, sie aus Atlas zu holen (Atlas-Modus).

Ob lokal oder Atlas, liest der Hook aus der Datei `.secondbrain.json` im
Arbeitsordner. Die legst du in Schritt 4 an, der Atlas-Umschalter ändert sie.

**Erklär es ihm so:**

> Ich richte eine kleine Automatik ein, die beim Start deiner Chats nachschaut,
> ob es Neuigkeiten gibt, ob deine Verbindungen laufen, und die dir zeigt, was
> heute ansteht. Sie fragt dich, bevor sie etwas ändert, und sie fasst deine
> eigenen Dateien nie an.

## Einrichtung

### 1. Interpreter bestimmen

Finde heraus, womit Python auf diesem Rechner läuft. Probiere in dieser
Reihenfolge `python3`, dann `python`, und merke dir, was funktioniert. Auf
Windows ist es meistens `python`, auf dem Mac `python3`. Findest du nichts,
überspringe den Hook, sag es dem Nutzer, und mach mit Schritt 8 weiter. Ohne
diesen Hook funktioniert alles andere trotzdem, nur die Automatik beim Start
fehlt.

### 2. Bestehende Einstellungen einlesen

Die Datei ist `<arbeitsordner>/.claude/settings.local.json`.

**Das ist die gefährlichste Stelle der ganzen Einrichtung.** In dieser Datei
können bereits Einstellungen des Nutzers liegen, zum Beispiel Berechtigungen.
Wenn du sie einfach neu schreibst, ist all das weg, und er versteht nie warum
plötzlich alles anders ist.

Also in dieser Reihenfolge:

1. Existiert die Datei? Wenn ja, **Sicherungskopie anlegen** als
   `settings.local.json.bak-<datum>`.
2. Datei einlesen und als Struktur behandeln, nicht als Text.
3. Deinen Eintrag in das bestehende `SessionStart`-Array **ergänzen**. Gibt es
   den Schlüssel noch nicht, lege ihn an. Gibt es schon andere Hooks, bleiben
   die vollständig stehen.
4. Zurückschreiben.

### 3. Der Eintrag

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "<interpreter> <voller-pfad>/starterkit/scripts/session-start.py"
          }
        ]
      }
    ]
  }
}
```

Der Pfad muss vollständig ausgeschrieben sein, keine Abkürzungen wie `~`.

### 4. Testen

Führe den Befehl einmal von Hand aus, genau so, wie er in der Datei steht.
Läuft er durch, ist alles in Ordnung. Läuft er nicht:

- Repariere das Skript, damit der Hook läuft.
- Weise den Nutzer darauf hin, dass deine Reparatur bei einem Update
  überschrieben werden kann und der Hinweis dann erneut auftaucht.
- Frag danach, ob du den Fehler an Start & Connect melden darfst, damit andere
  ihn nicht auch haben. Bei Nein ist die Sache erledigt.

## Zwei Regeln, die nicht verhandelbar sind

**Der Hook darf niemals blockieren.** Kein Internet, Server nicht erreichbar,
Skript kaputt: in allen Fällen läuft der Chat ganz normal weiter. Ein Hook, der
die Arbeit des Nutzers aufhält, weil bei uns etwas hakt, ist schlimmer als gar
kein Hook.

**Der Hook läuft nur in diesem Ordner.** Er wird auf Projekt-Ebene eingetragen,
niemals in den globalen Einstellungen unter `~/.claude/`. Der Nutzer benutzt
Claude Code möglicherweise auch für anderes, und dort hat unsere Automatik
nichts verloren. Nebeneffekt: die Deinstallation ist dadurch ein gelöschter
Ordner.

## Wenn er keinen Hook will

Vollkommen in Ordnung. Sag ihm, dass er das Kit dann von Hand aktualisiert,
indem er dich einfach darum bittet, und mach weiter. Dränge nicht.
