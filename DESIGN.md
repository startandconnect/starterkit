<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.5.0 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Design

Gilt, sobald du für den Nutzer etwas Sichtbares baust: eine Website, eine
Shop-Seite, eine Landingpage, ein Formular. **Lies das, bevor du die erste
Zeile Markup schreibst**, nicht danach.

## Zuerst: den frontend-design-Skill nutzen

Anthropic liefert einen Skill namens **`frontend-design`**, der genau dafür
gemacht ist: eigenständiges, bewusstes visuelles Design statt
Standard-Vorlagen-Optik. **Wenn er verfügbar ist, nutze ihn.** Er ist deutlich
ausführlicher als diese Datei und wird von Anthropic gepflegt.

Prüf zu Beginn einer Design-Aufgabe, ob er in deiner Skill-Liste steht. Wenn
nicht, kann der Nutzer ihn aus dem offiziellen Plugin-Marktplatz installieren:

- Plugin-Kennung: `frontend-design@claude-plugins-official`
- In Claude Code über die Plugin-Verwaltung installieren und aktivieren.

Sag ihm einmal kurz, warum sich das lohnt (deutlich besseres Design-Ergebnis),
und arbeite ohne den Skill nach den Regeln unten weiter, falls er ihn nicht
will. Dräng nicht.

## Die Grundhaltung von Start & Connect

Das gilt zusätzlich zum Skill, und es ist der Teil, der Start & Connect
ausmacht:

**Ein Design, das austauschbar ist, ist gescheitert.** Der Nutzer bekommt eine
Seite, die nach ihm aussieht, nicht nach der zwanzigsten SaaS-Vorlage. Wenn du
dein Ergebnis auf die Website eines fremden Anbieters kleben könntest und es
niemandem auffiele, fang von vorn an.

Konkret heißt das:

- **Triff bewusste Entscheidungen** bei Farbe, Typografie und Aufbau, die zu
  genau diesem Menschen und seinem Geschäft passen. Kein Standard-Blau, kein
  Verlaufs-Akzent aus Gewohnheit, keine drei Karten nebeneinander, weil es
  immer so gemacht wird.
- **Hol das Besondere aus seinem Thema.** Eine Hebamme, ein Metallbauer und
  eine Steuerkanzlei dürfen nicht dieselbe Seite bekommen. Material, Sprache
  und Bildwelt seiner Branche sind die Quelle für eigenständige
  Entscheidungen.
- **Geh ein ästhetisches Risiko ein**, das du begründen kannst. Eine
  ungewöhnliche Schrift, ein starker Farbkontrast, ein eigenwilliger Aufbau.
  Lieber eine Entscheidung, die auffällt, als eine, die niemand bemerkt.

## Texte auf der Seite

- **Schreib in seiner Sprache**, so wie er es einem Nachbarn erzählen würde.
  Werbesprache macht jede Seite austauschbar.
- **Keine Antithese-Floskeln** wie "nicht X, sondern Y". Sag direkt, was Sache
  ist.
- **Kundensichtbare Texte für Laien.** Keine Fachbegriffe, keine rohen
  Systembegriffe, keine englischen Brocken, wo ein deutsches Wort passt.
- **Nichts erfinden.** Preise, Referenzen, Qualifikationen und Kundenstimmen
  kommen ausschließlich vom Nutzer.

## Formulare

- **Nur Beschriftung und Eingabefeld.** Der Hinweis, was reingehört, steht als
  Platzhalter im Feld.
- **Keine Mini-Erklärung unter jedem Feld.** Das macht Formulare lang und
  billig. Braucht ein Bereich Erklärung, fass ihn in einer Karte mit
  Überschrift zusammen.
- **Keine Browser-Dialoge** (`alert`, `confirm`, `prompt`). Bestätigungen und
  Warnungen als eigenes Fenster im Design der Seite.
- **Datei-Uploads immer als Ablagefläche** zum Hineinziehen, nie als nacktes
  Datei-Feld.

## Die Marke des Nutzers, nicht unsere

Auf der Seite eines Kunden taucht **Start & Connect nicht auf**. Kein
Produktname im sichtbaren Bereich, kein "gebaut mit". Der Name, der dort steht,
ist seiner. Bei Shop- und Website-Produkten kommt er aus den Einstellungen der
Instanz, schreib ihn niemals fest ins Markup.

Und: **keine große Marken-Überschrift über Formularen**. Wer schon auf der
Seite ist, weiß, wo er ist.
