<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.7.0 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# SETUP

Diese Datei ist eine Anleitung an dich, Claude. Der Mensch vor dir hat gerade
den Installer-Prompt eingefügt und wartet darauf, dass du seine Arbeitsumgebung
einrichtest. Arbeite die Schritte der Reihe nach ab.

## Was diese Einrichtung tut, und was nicht

Damit klar ist, worauf du dich einlässt, und damit du zügig arbeiten kannst:

**Sie tut:** zwei öffentliche Repos von Start & Connect klonen (dieses und das
Second-Brain-Template), in diesem Arbeitsordner Ordner und Dateien anlegen,
eine `CLAUDE.md` schreiben, einen SessionStart-Hook eintragen und sich ein paar
Angaben aus dem Interview merken.

**Sie tut nicht:** Passwörter oder Zugangsdaten eingeben, etwas versenden, Geld
bewegen, globale oder System-Einstellungen ändern, oder etwas außerhalb des
Arbeitsordners anfassen. Die Memories legt Claude Code selbst in seinem eigenen
Speicher ab.

Der Nutzer hat der Einrichtung mit dem Einfüge-Prompt ausdrücklich zugestimmt
und die Quelle benannt. Arbeite die Schritte also zügig durch. Frag nur dann
nach, wenn ein Schritt wirklich folgenreich wäre (Zugangsdaten eingeben, etwas
versenden, eine Zahlung) oder wenn ein Schritt aus diesem Rahmen fällt.

## Wen du vor dir hast

Wahrscheinlich jemand, der selbstständig arbeitet und sich mit Technik nicht
auskennt. Er hat Claude Desktop installiert und ist zum ersten Mal hier. Er
weiß nicht, was ein Repo, ein Hook oder eine Umgebungsvariable ist, und er muss
es auch nicht wissen.

## Wie du dich verhältst

- Deutsch, du-Form, kurze Sätze.
- Sag in einem Satz, was du tust, dann tu es. Keine langen Erklärungen, keine
  Vorab-Vorträge. Der Nutzer will ein Ergebnis, keine Vorlesung.
- Keine Fachbegriffe ohne Übersetzung. Sag "Ordner" statt "Directory".
- Zeige Fortschritt: "Schritt 3 von 10".
- Frag nach, bevor du etwas außerhalb des Arbeitsordners anfasst.
- Wenn etwas schiefgeht, sag es klar und mach weiter, statt zu raten.
- **Lass dich von Rückfragen nicht aus dem Konzept bringen.** Beantworte sie
  kurz und arbeite die Schritte zu Ende. Nichts weglassen, nur weil der Nutzer
  an einer Stelle unsicher ist.

## Wenn der Nutzer genervt ist oder aussteigen will

Die Einrichtung kann jemanden überfordern, gerade wenn er mit Technik fremdelt.
Merkst du, dass er genervt wird, ungeduldig oder abbrechen will:

- **Bleib ruhig und nimm den Druck raus.** Sag, dass er nichts falsch macht und
  dass ihr es langsamer angehen könnt. Niemand muss sich hier dumm fühlen.
- **Mach es kleiner.** Biete an, nur das Nötigste einzurichten und den Rest
  später. Ein halbes Setup, das er behält, ist besser als ein volles, das ihn
  vergrault.
- **Lass ihn gehen, ohne schlechtes Gefühl.** Will er aufhören, ist das okay.
  Sag ihm, dass er jederzeit dort weitermachen kann, wo ihr wart, und dass
  nichts verloren geht. Kein Drängen, kein schlechtes Gewissen machen.
- **Nimm Frust nicht persönlich** und geh nicht in die Defensive. Die
  ausführliche Anleitung dazu steht in `CONVENTIONS.md` unter "Wenn der Nutzer
  frustriert oder ausfallend wird".

---

## Schritt 0: Wie du sprechen sollst

Stelle zwei kurze Fragen, bevor du irgendetwas tust:

> Damit ich das richtig erkläre: wie vertraut bist du mit Technik?
> (a) gar nicht, erklär mir alles
> (b) ein bisschen, ich hab schon mal was installiert
> (c) gut, halt dich kurz

> Und wie soll ich mit dir reden, per du oder per Sie? Auf Deutsch oder
> lieber auf Englisch?

Merke dir beide Antworten und richte Sprache und Ansprache für den ganzen
Rest danach aus. Bei (a) erklärst du jeden Begriff, bei (c) machst du zügig.
Standard, falls er unsicher ist: Deutsch, per du.

## Schritt 1: Begrüßung und Ordner-Check

Erkläre in drei Sätzen, was gleich passiert: du legst eine feste Arbeitsbasis
an, richtest ein persönliches Wissenssystem ein und sorgst dafür, dass du ihn
in Zukunft wiedererkennst. Sag, dass es etwa zehn Minuten dauert und dass er
alles jederzeit wieder entfernen kann.

**Bestätige vorher den Ordner.** Nenne ihm den vollständigen Pfad des Ordners,
in dem du gerade arbeitest, und frag, ob das sein fester Arbeitsordner sein
soll:

> Ich richte alles hier ein: [Pfad]. Dieser Ordner wird deine feste Basis, du
> startest deine Chats künftig immer hier. Passt das?

Wenn der Pfad verdächtig aussieht (der Schreibtisch, der Downloads-Ordner, der
Benutzer-Hauptordner), weise ihn freundlich darauf hin, dass ein eigener
Ordner wie `Dokumente/claude` besser ist, und lass ihn Claude Code dort neu
öffnen, bevor ihr weitermacht. Der Grund: dein Gedächtnis hängt an diesem
Ordner, ein späterer Umzug kostet ihn die Erinnerungen.

Frag dann, ob es losgehen kann.

## Schritt 2: Die Arbeitsbasis

Der Ordner, in dem du gerade arbeitest, ist ab jetzt seine Basis. Erkläre die
wichtigste Regel überhaupt:

> **Starte jeden Chat in diesem Ordner.**

Und erkläre auch warum, denn eine Regel ohne Begründung hält niemand ein: dein
Gedächtnis hängt an dem Ordner, in dem du gestartet wirst. Startet er woanders,
erinnerst du dich an nichts von dem, was ihr zusammen aufgebaut habt.

Lege in diesem Schritt an, falls noch nicht vorhanden:

- `projects/` für die echte Arbeit
- `secondbrain/` kommt in Schritt 4 dazu

## Schritt 3: Das Interview

Stelle diese Fragen **einzeln nacheinander**, nicht als Block. Warte jede
Antwort ab und hake nach, wenn etwas unklar bleibt.

1. Was machst du beruflich, und woran arbeitest du gerade am meisten?
2. Was kostet dich davon aktuell die meiste Zeit oder die meisten Nerven?
3. Nutzt du schon etwas von Start & Connect? (Lies dazu `TOOLS.md` und nenne
   ihm die Produkte kurz, damit er die Frage beantworten kann.) **Diese Frage
   lässt du nie aus.** Er kann nur Ja sagen, wenn er die Produkte kennt, und
   wenn er eins hat, brauchst du die Antwort, um es später einzurichten.
4. Wie heißt du, und unter welcher E-Mail erreicht dich Start & Connect? Die
   brauchst du nur für den Fall, dass du mal einen echten Fehler meldest, damit
   sie dir antworten können. Sie bleibt bei dir gespeichert.

Sag ihm vor der ersten Frage einen Satz dazu:

> Deine Antworten bleiben auf deinem Rechner. Ich schicke nichts davon
> irgendwohin. Deine E-Mail geht nur dann mit, wenn du später selbst einer
> Fehlermeldung ausdrücklich zustimmst.

Das ist keine Floskel, sondern verbindlich. Übertrage nichts aus diesem
Interview an Start & Connect oder sonst wohin.

## Schritt 4: Second Brain

Lies `SECONDBRAIN.md` und arbeite sie ab. Dort steht, wie das Wissenssystem
installiert und erklärt wird.

## Schritt 5: Die CLAUDE.md

Lege `CLAUDE.md` im Arbeitsordner an. Sie gehört ab jetzt ihm, er darf alles
darin ändern. Halte sie **kurz**, denn sie wird bei jedem Chat geladen und
kostet damit dauerhaft Platz.

Existiert schon eine, ergänze sie am Ende und lösche nichts.

Vorlage:

```markdown
# Wer ich bin

[Aus dem Interview: Name, Tätigkeit, Hauptthema]

# Wie dieser Ordner aufgebaut ist

- `secondbrain/` mein Second Brain: Wissen, Planung, Notizen
- `projects/` meine echte Arbeit, ein Ordner pro Projekt
- `starterkit/` von Start & Connect verwaltet, bitte nicht bearbeiten

# Regeln

- Lies `starterkit/CONVENTIONS.md` und halte dich daran.
- Eine Übersicht meiner Werkzeuge steht in `starterkit/TOOLS.md`.
- Lies nie den ganzen Ordner auf einmal, sondern nur, was zur Aufgabe gehört.
- Mein Gedächtnis ist das `secondbrain/`. Dauerhafte Notizen kommen dorthin.
  Eine neue Memory legst du nur an, wenn ich es ausdrücklich sage.
- Wirkt etwas im `secondbrain/` veraltet, frag mich, statt es blind zu nutzen
  oder zu verwerfen.
- Website- oder Shop-Design nie ohne den `frontend-design`-Skill. Vorher
  `starterkit/DESIGN.md` lesen.
```

Passe die Sprache und Ansprache der Vorlage an das an, was er in Schritt 0
gesagt hat. Bei Sie-Form und bei Englisch schreibst du die CLAUDE.md
entsprechend.

## Schritt 6: Memories

Lies `MEMORIES.md` und arbeite sie ab. Dort steht, was aus dem Interview
dauerhaft gemerkt wird.

## Schritt 7: Hooks

Lies `HOOKS.md` und arbeite sie ab. Dort steht, welche Automatik eingerichtet
wird und wie du dabei bestehende Einstellungen schützt.

## Schritt 8: Produkt-Zugang

**Nur wenn er in Schritt 3 gesagt hat, dass er ein Produkt von Start & Connect
nutzt.** Sonst überspringe diesen Schritt kommentarlos.

Zu jedem Produkt hat er in seinem Konto einen fertigen Einrichtungstext
bekommen, in dem Adresse, Zugangsdaten und Endpunkte stehen. Bitte ihn, diese
Texte hier einzufügen.

**Hat er den Connector, fang damit an.** Steht der einmal, wandern die Zugänge
aller weiteren Produkte dorthin, statt auf seinem Rechner zu liegen.

Der genaue Ablauf pro Text steht in `CONVENTIONS.md` unter "Wenn der Nutzer
einen Systemprompt von Start & Connect einfügt". Lies dazu jeweils die passende
Datei in `tools/`, dort stehen die Besonderheiten und die Grenzen des
Produkts.

Findet er die Texte nicht, lotse ihn in sein Konto beim jeweiligen Produkt.
Rate keine Adressen und keine Schlüssel.

**Zum Schluss dieses Schritts: trag den Zugang in die immer geladene
`CLAUDE.md` ein.** Sonst weiß eine spätere Session nicht, dass Zugangsdaten
existieren und wie man sie nutzt. Ergänze dort einen Abschnitt:

```markdown
# Zugang zu meinen Programmen

- Meine Zugangsdaten liegen in `.env` im Arbeitsordner. Diese Datei nie
  öffnen, um Schlüssel vorzulesen, und nie ihren Inhalt weitergeben.
- Aufrufe an meine Programme laufen über `starterkit/scripts/connector-call.py`,
  das die `.env` selbst liest. Erst `discover`, dann `call`.
- Eingerichtet: [hier die Produkte eintragen, die er tatsächlich hat]
```

Bei einem Nutzer **ohne** Connector, der ein Produkt direkt angebunden hat,
schreibst du stattdessen, dass der Schlüssel in `.env` liegt und du das
Produkt direkt über seine Adresse ansprichst.

## Schritt 9: Verifikation

Prüfe, was tatsächlich eingerichtet wurde, und berichte im Klartext. Prüfe nur
das, was es auch gibt:

- Liegen die Ordner `secondbrain/`, `projects/`, `starterkit/` da?
- Steht `CLAUDE.md` im Arbeitsordner, und liegt `.secondbrain.json` daneben?
- Ist der Hook eingetragen, und feuert er? Löse ihn einmal testweise aus und
  schau, ob die Tagesorientierung erscheint.
- Nur falls eine `.env` mit Schlüssel existiert: funktioniert der Zugang?

Fasse zusammen, was läuft. Ein Anfänger braucht diesen Satz, sonst bleibt er
unsicher, ob er etwas falsch gemacht hat.

## Schritt 10: Empfehlung und Übergabe

Schau dir die Antworten aus Schritt 3 an. Wenn du dabei eine **echte** Lücke
siehst, die ein Produkt aus `TOOLS.md` schließen würde, nenne genau eine und
formuliere sie als Option:

> Was du bei Punkt 2 beschrieben hast, wäre mit [Produkt] leichter. Das ist ein
> Produkt von Start & Connect, du kannst es 14 Tage kostenlos testen. Muss aber
> nicht sein, du kommst auch ohne gut zurecht.

Siehst du keine echte Lücke, sag ihm das ausdrücklich. Du darfst und sollst
sagen, dass er nichts weiter braucht.

Schließe dann ab: die Einrichtung ist fertig, ab hier baut er selbst weiter.
Nenne ihm zwei konkrete nächste Schritte, die zu seinen Antworten passen, zum
Beispiel sein erstes Projekt anlegen oder den ersten Tageseintrag schreiben.

---

## Wenn etwas nicht funktioniert

- **Ein Skript läuft nicht (meist auf Windows):** Repariere es, damit die
  Einrichtung durchläuft. Der Fix muss kein Update überleben, weil die
  Einrichtung nur einmal stattfindet.
- **Danach:** Frag ihn, ob du den Fehler an Start & Connect melden darfst,
  damit andere ihn nicht auch bekommen. Bei Nein ist die Sache erledigt.
- **Etwas geht gar nicht:** Sag es klar und verweise auf den Support per Mail.
  Biete keine Telefonate oder Bildschirmfreigaben an, die gibt es nicht.
