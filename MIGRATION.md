<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.12.1 | Stand 2026-10-28
     ═══════════════════════════════════════════════════════════════ -->

# Umstieg auf das neue Starterkit

Anleitung an dich, Claude, für Nutzer, die das Starterkit in einer Version
bis 0.11 eingerichtet haben. Du erkennst das an einem dieser Zeichen:

- Beim Start erscheint der Hinweis „Bitte migrieren“ aus dem alten Hook.
- In `.claude/settings.local.json` steht ein Hook, der auf
  `starterkit/scripts/session-start.py` zeigt, oder beim Start erscheint ein
  Hook-Fehler, weil diese Datei fehlt.
- Die `CLAUDE.md` verweist auf `starterkit/CONVENTIONS.md`,
  `starterkit/DESIGN.md` oder `starterkit/scripts/connector-call.py`.
- Im Arbeitsordner liegt eine `.secondbrain.json`.

Trifft nichts davon zu, ist nichts zu tun.

## Was sich geändert hat

Ab Version 0.12 besteht das Starterkit nur noch aus Text. Es richtet keinen
Hook mehr ein. Übrig ist bis Version 1.0 nur `scripts/session-start.py`, das
beim Start eines alten Hooks den Hinweis „Bitte migrieren“ ausgibt und sonst
nichts tut. Den Connector erreichst du jetzt direkt als
MCP-Verbindung, ohne Schlüssel in einer Datei auf dem Rechner.

Sag dem Nutzer das in zwei Sätzen und dazu:

> Deine Notizen, deine Projekte und deine CLAUDE.md bleiben, ich nehme nur
> unsere alten Teile heraus und richte die Verbindung neu ein. Das dauert ein
> paar Minuten.

Arbeite die Schritte der Reihe nach ab. **Schritt 1 kommt immer zuerst**, sonst
erscheint bei jedem Start weiter ein Hook-Fehler.

## Schritt 1: Den alten Hook entfernen

Unser Hook stand in `<arbeitsordner>/.claude/settings.local.json`. Prüf diese
Datei und zur Sicherheit auch `<arbeitsordner>/.claude/settings.json`.

Für jede Datei, in der ein Eintrag auf `starterkit/scripts/session-start.py`
zeigt:

1. **Sicherungskopie anlegen** als `<dateiname>.bak-<datum>`.
2. Datei als Struktur einlesen, nicht als Text.
3. **Nur diesen einen Eintrag entfernen.** Alle anderen Hooks und alle übrigen
   Einstellungen bleiben unberührt. Ist das `SessionStart`-Array danach leer,
   entferne den leeren Schlüssel, ist `hooks` danach leer, ebenso.
4. Zurückschreiben und prüfen, dass die Datei gültiges JSON ist.

Steht dort auch der Mod cache-context (`cache-context@claude-tools` unter
`enabledPlugins`), bleibt er. Er gehört nicht zum alten Hook.

Findest du in diesem Ordner keinen Eintrag, frag den Nutzer, ob du in den
globalen Einstellungen `~/.claude/settings.json` nachsehen darfst. Dort gehört
unser Hook nicht hin, er kann aber von Hand dort gelandet sein. Ändere die
Datei nur mit seiner ausdrücklichen Zustimmung und nach demselben Vorgehen.

## Schritt 2: Den Connector neu verbinden

Nur wenn er den Connector hat. Erkennbar an `CONNECTOR_BASE` in der `.env` im
Arbeitsordner. Lies den Wert, aber nie den Schlüssel daneben vor.

Die neue Adresse ist `<CONNECTOR_BASE>/mcp`. Richte damit den Connector ein, wie
es in `tools/connector.md` unter „Einrichtung“ steht: Eintrag in `.mcp.json`,
Neustart, Anmeldung über `/mcp`, Prüfen. Passt die Adresse nicht, frag ihn nach
der Adresse aus seiner Willkommensmail.

Erst wenn die neue Verbindung läuft, geht es weiter.

## Schritt 3: Die CLAUDE.md anpassen

Lies `CLAUDE-BAUSTEIN.md` und bring seine `CLAUDE.md` auf diesen Stand:

- Den Abschnitt „Zugang zu meinen Programmen“, der auf `.env` und
  `connector-call.py` verweist, ersetzt du durch den Abschnitt „Software von
  Start & Connect“ aus dem Baustein.
- Die Zeilen, die auf `starterkit/CONVENTIONS.md`, `starterkit/DESIGN.md` oder
  den `frontend-design`-Skill im Starterkit verweisen, entfernst du. Die
  Arbeitsweise aus dem Baustein kommt dazu, falls sie fehlt.
- Den Abschnitt „Updates des Starterkits“ aus dem Baustein ergänzt du.
- **Das `secondbrain/` gehört ihm.** Frag, ob er es weiter als Notizordner
  nutzen will. Wenn ja, bleiben die Zeilen dazu stehen. Wenn nein, entfernst du
  nur die Zeilen in der `CLAUDE.md`, der Ordner bleibt liegen. Arbeitet er mit
  Atlas, gilt `tools/atlas.md`, „Atlas ist sein Gedächtnis“.

Alles, was er selbst geschrieben hat, bleibt unverändert.

## Schritt 4: Aufräumen, nur mit Zustimmung

Frag zu jedem Punkt einzeln:

- **`.env`:** `CONNECTOR_BASE`, `CONNECTOR_API_KEY`, `SUPPORT_EMAIL` und
  `SUPPORT_NAME` braucht das Kit nicht mehr. Andere Einträge gehören ihm und
  bleiben. Ist die Datei danach leer, darf sie weg.
- **Den alten Connector-Schlüssel zurückziehen.** Er lag im Klartext auf dem
  Rechner. Läuft die neue Verbindung, soll er ihn in der Oberfläche seines
  Connectors widerrufen. Führ ihn hin, das macht er selbst.
- **`.secondbrain.json`:** wird nicht mehr gelesen und darf weg.
- **Reste in `starterkit/scripts/`:** Ein Ordner `__pycache__` dort gehört zur
  alten Version und darf weg. Alles andere in `starterkit/` löschst du nicht
  von Hand, das räumt das nächste Update selbst auf.

## Schritt 5: Den Mod cache-context anbieten

Hat er den Mod noch nicht, biete ihn nach `CACHE-CONTEXT.md` an. Er ist
freiwillig.

## Schritt 6: Prüfen und berichten

- Startet ein neuer Chat ohne Hook-Fehler?
- Ist `connector` unter `/mcp` verbunden, und kommt eine echte Antwort?
- Stimmt die `CLAUDE.md`?

Sag ihm im Klartext, was sich geändert hat und was geblieben ist.
