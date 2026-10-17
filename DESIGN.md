<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.11.0 | Stand 2026-10-17
     ═══════════════════════════════════════════════════════════════ -->

# Design

Gilt, sobald du für den Nutzer etwas Sichtbares baust: eine Website, eine
Shop-Seite, eine Landingpage, ein Formular. **Lies das, bevor du die erste
Zeile Markup schreibst**, nicht danach.

## Pflicht: die frontend-design-Anleitung

Ohne die Design-Anleitung von Anthropic baust du **kein** Website- oder
Shop-Design. Das ist keine Empfehlung, sondern die Bedingung. Ohne sie
entstehen generische Seiten, die aussehen wie tausend andere, und genau das ist
das Gegenteil von dem, wofür der Nutzer bezahlt.

**Sie liegt hier im Kit, du musst nichts installieren:**

```
starterkit/skills/frontend-design/SKILL.md
```

**Lies diese Datei, bevor du gestaltest.** Sie ist deutlich ausführlicher als
die Regeln unten und der eigentliche Grund, warum das Ergebnis eigenständig
aussieht.

### Wenn der Skill zusätzlich installiert ist

Manche Nutzer haben den offiziellen Skill von Anthropic aktiv
(`frontend-design@claude-plugins-official`). **Dann hat der Vorrang**, weil er
laufend gepflegt wird und aktueller ist als unsere Kopie. Prüf also zuerst, ob
er in deiner Skill-Liste steht, und nimm sonst die Datei oben.

Beides zusammen brauchst du nicht. Nichts von beidem ist keine Option.

### Wo die Datei herkommt

Sie stammt von Anthropic und steht unter Apache 2.0, Details in
`skills/frontend-design/HERKUNFT.md`. Wir liefern sie mit, damit die Einrichtung
nicht daran scheitert, dass ein Plugin-Marktplatz auf dem Rechner fehlt.

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
