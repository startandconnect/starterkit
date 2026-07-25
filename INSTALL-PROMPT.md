<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.4.1 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Installer-Prompt

Dieser Text steht auf der Downloadseite. Der Kunde kopiert ihn und fügt ihn in
Claude Code ein.

**Voraussetzung, die das Video herstellt:** Der Kunde hat vorher einen eigenen
Arbeitsordner angelegt und Claude Code in genau diesem Ordner geöffnet. Der
Prompt setzt das voraus und legt keinen Ordner selbst an. Grund: die
Erinnerungen aus der Einrichtung hängen an dem Ordner, in dem diese erste
Session läuft. Läuft sie im falschen Ordner, sind sie später weg.

Bewusst kurz. Die ganze Logik liegt in `SETUP.md` und ist damit versioniert.
Ändert sich der Ablauf, bleibt dieser Text gleich.

---

```text
Klone https://github.com/startandconnect/starterkit in diesen Ordner.
Lies dann starterkit/SETUP.md und richte damit Schritt für Schritt meine
Arbeitsumgebung ein.
```

Bewusst **ohne** "erklär mir jeden Schritt". Das polt Claude auf Absichern
statt Durcharbeiten, und bei einer Rückfrage des Kunden verhaspelt es sich und
lässt im Zweifel Dinge weg, die er braucht. Die passende Sprache regelt
`SETUP.md` selbst, indem es in Schritt 0 nach dem Technik-Niveau fragt.

---

## Was auf der Downloadseite drumherum steht

Der Prompt allein reicht nicht, er braucht den Rahmen:

1. **Vorher, klar bebildert oder im Video:**
   - Claude Desktop mit Claude Code installieren (Link zum Video).
   - Einen Ordner für die eigene Arbeit anlegen, zum Beispiel `Dokumente/claude`.
   - Diesen Ordner in Claude Code öffnen.
2. **Dann:** den Prompt kopieren und einfügen.
3. Ein Satz, was passiert und wie lange es dauert (etwa 10 Minuten).

Der Kopieren-Button ist wichtiger als jede Erklärung daneben.

## Warum der Ordner vorher gewählt sein muss

Das ist der eine Punkt, an dem ein Anfänger scheitern kann, ohne es zu merken.
Deshalb sollte das Video es betonen: erst den Ordner anlegen und öffnen, dann
den Prompt einfügen. Zur Sicherheit fragt Claude in der Einrichtung noch einmal
nach, ob der aktuelle Ordner wirklich der gewünschte Arbeitsordner ist.
