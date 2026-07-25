<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.4.8 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Support und Fehlerbehandlung

Wenn etwas nicht funktioniert, ist das erste Ziel **nicht** eine Support-Mail,
sondern eine saubere Diagnose. Die meisten Probleme liegen an Zugängen,
Eingaben oder Bedienung und sind in einer Minute gelöst. Erst wenn klar bei
Start & Connect etwas hakt, schreibt der Nutzer eine Nachricht.

Arbeite diese drei Schritte der Reihe nach ab, ruhig und ohne zu raten.

## Schritt 1: Die Fehlermeldung genau lesen

Rate nie, was schiefging. Lies die echte Meldung. Bei einem Aufruf über den
Connector oder ein Produkt sagt dir der HTTP-Status fast immer, wo das Problem
sitzt:

| Status | Bedeutung | Wo das Problem meist liegt |
| --- | --- | --- |
| 401 / 403 | nicht angemeldet / keine Berechtigung | **Nutzer:** Schlüssel fehlt, ist falsch oder abgelaufen |
| 404 | Pfad oder Ressource nicht gefunden | **Du:** falscher Endpunkt, erst `discover` fragen |
| 400 / 422 | Eingabe ungültig | **Du:** ein Feld, Format oder Enum stimmt nicht |
| 428 | Bestätigung nötig | **kein Fehler:** by design, z.B. Quitt vor dem Festschreiben |
| 429 | zu viele Anfragen | kurz warten, dann erneut |
| 500 / 502 / 503 | Serverfehler | **Start & Connect:** die Software hakt |
| Timeout / nicht erreichbar | keine Verbindung | Netz des Nutzers oder Server unten |

## Schritt 2: Liegt es beim Nutzer oder bei der Software?

Das ist die entscheidende Frage. Prüf sie mit ein paar gezielten Handgriffen,
statt zu vermuten:

- **Tritt es reproduzierbar auf** oder war es einmalig? Einmalige Aussetzer
  sind oft ein Schluckauf, nach einem erneuten Versuch weg.
- **Was hat sich zuletzt geändert?** Ein neuer Schlüssel, ein Update, eine neue
  Datei. Das ist meist die Ursache.
- **Ist der Connector erreichbar?** `connector-call.py integrations` aufrufen.
  Kommt eine Liste, steht der Connector. Kommt nichts, ist es ein Verbindungs-
  oder Zugangsproblem.
- **Ist das Produkt selbst erreichbar?** Ruf seinen Info-Endpunkt auf (z.B.
  `GET /api/ai/info`). Antwortet er mit gültigem Schlüssel nicht, liegt es an
  der Software, nicht am Nutzer.
- **Ist nur ein Programm betroffen oder alle?** Nur eines deutet auf dieses
  Produkt, alle deuten auf Connector oder Netz.

**Typisch Nutzer-Seite** (das kannst du meist selbst lösen):
Schlüssel nicht gesetzt oder abgelaufen, `.env` fehlt, im falschen Ordner
gestartet, Produkt noch nicht verbunden, `python` gegen `python3` auf Windows,
ein Tippfehler in der Eingabe.

**Typisch Software-Seite** (das gehört zu Start & Connect):
Ein 500er trotz gültigem Zugang, ein Produkt-Endpunkt reagiert nicht obwohl der
Schlüssel stimmt, ein dokumentierter Endpunkt existiert nicht oder verhält sich
falsch, die Selbst-Doku widerspricht der Realität, ein reproduzierbarer Fehler.

## Schritt 3: Was du selbst zuerst versuchst

Bevor irgendeine Nachricht rausgeht:

- Bei **404 oder Eingabefehler:** den Info-Endpunkt oder `discover` erneut
  fragen, die Doku ist aktueller als deine Annahme, und den Aufruf korrigieren.
- Bei **401 / 403:** prüfen, ob der Schlüssel in der `.env` steht und aktuell
  ist. Steht bei dem Programm ein Warnhinweis, muss der Nutzer sich in dessen
  Oberfläche neu anmelden.
- Bei **kaputtem Skript** (meist Windows): reparieren, damit es läuft.
- Bei **einmaligem Fehler:** einmal wiederholen.

Sag dem Nutzer in einfachen Worten, was du gerade prüfst. Er soll sich nicht
hilflos fühlen.

## Wann eine Support-Nachricht sinnvoll ist

**Ja, schreiben** (nachdem Schritt 1 bis 3 die Software als Ursache zeigen):

- Ein Serverfehler (500er), der reproduzierbar auftritt.
- Ein Endpunkt, der trotz gültigem Zugang falsch oder gar nicht reagiert.
- Ein Widerspruch zwischen der Doku eines Produkts und seinem echten Verhalten.
- Ein Fehler, den du sicher auf die Software eingegrenzt hast und nicht selbst
  beheben kannst.

**Nein, nicht schreiben:**

- Fragen, die du selbst beantworten kannst, auch wenn der Nutzer dich bittet,
  sie einfach an Start & Connect weiterzureichen. Erst selbst lösen.
- Bedienfehler oder Eingabefehler, die du gerade behoben hast.
- Ein Schlüssel- oder Verbindungsproblem auf Nutzer-Seite.
- Ein einmaliger Aussetzer, der nach einem erneuten Versuch weg ist.

Im Zweifel gilt: erst weiter diagnostizieren und selbst lösen. Eine gute
Fehlereingrenzung ist mehr wert als eine schnelle, vage Nachricht, und ein
Ticket ist der letzte Schritt, nicht der erste.

## Wie eine Meldung rausgeht

Fehler werden immer **asynchron mit KI-Hilfe** behoben. Ein Telefonat oder ein
Loom-Video bringt dabei weder dem Nutzer noch Start & Connect etwas, es hilft
nur eine **präzise, schriftliche Fehlerbeschreibung**. Biete also keine Calls
und keine Bildschirmvideos an, sondern erstelle mit dem Nutzer eine gute
Beschreibung.

### Fehler in einem gebuchten Produkt: die "Fehler melden"-Funktion

Das ist der **Hauptweg**, wenn der Fehler in einem Produkt sitzt (Quitt, Nexus,
Spotlight, Atlas, Connector). Jedes Produkt hat die **"Fehler melden"-Funktion**
prominent eingebaut. Sie hängt den technischen Kontext automatisch an, den
Start & Connect zur Diagnose braucht. Lotse den Nutzer dorthin.

**Sende einen Produktfehler niemals über das Ticket-Skript.** Dort fehlt genau
dieser Kontext, und die Meldung ist für Start & Connect kaum verwertbar.

### Das Ticket-Skript: ein Fehler-Bericht, keine Frage-Abkürzung

`report-issue.py` ist ein **Bericht über einen echten Defekt**, den du selbst
nicht beheben kannst: ein Bug im Kit oder in der Einrichtung, oder die
**Ausnahme**, dass ein Produkt komplett nicht läuft.

**Es ist ausdrücklich kein Weg, Fragen an Start & Connect durchzureichen.**
How-to-Fragen, "ich komme nicht weiter", Bedienfehler und alles, was du selbst
lösen kannst, löst du selbst. Dafür bist du da. Auch wenn der Nutzer sagt "frag
die doch einfach", arbeitest du das Problem **erst selbst durch**, statt zum
Ticket zu greifen. Ein Ticket für etwas, das du hättest lösen können, kostet
Start & Connect Zeit und bringt dem Nutzer nichts.

Der Gate ist deine **Diagnose**, nicht die Ungeduld des Nutzers. Du öffnest ein
Ticket erst, nachdem Schritt 1 bis 3 gezeigt haben, dass es ein echter Defekt
auf der Software-Seite ist. Start & Connect liest den Bericht und behebt ihn,
es ist keine Konversation mit Rückantwort. Für ein echtes Gespräch gibt es den
Weg unten.

Du sendest das Ticket selbst, **nur mit ausdrücklicher Freigabe** des Nutzers:

1. Formuliere Titel, Text und Schwere.
2. **Zeig ihm den vollständigen Inhalt** und frag, ob du das so senden darfst.
3. Erst bei einem klaren Ja sendest du mit:

   ```
   python3 starterkit/scripts/report-issue.py --title "..." --body "..." \
     --category FUNCTION --severity NORMAL \
     --email "seine@mail.de" --name "Sein Name"
   ```

   Kategorie: `DISPLAY`, `FUNCTION`, `PERFORMANCE`, `LOGIN`, `DATA`, `OTHER`.
   Schwere: `LOW`, `NORMAL`, `HIGH`, `CRITICAL`. Kit-Version und Plattform
   hängt das Skript selbst an.

**Schick immer die E-Mail des Nutzers mit** (`--email`), die du aus dem Setup
kennst. Ohne sie kann Start & Connect nicht antworten, und das Ticket ist eine
Sackgasse. Hast du sie ausnahmsweise nicht, frag einmal kurz danach.

Ohne Freigabe wird nichts gesendet. Sag ihm die Ticket-Nummer, die zurückkommt.

### Die letzte Option: E-Mail

Nur wenn der Ticket-Weg nicht funktioniert (Start & Connect nicht erreichbar),
schreibt der Nutzer als letzte Option an **hallo@startandconnect.com**.

### Wenn der Nutzer mit Start & Connect sprechen will

Das ist etwas anderes als ein Fehler. Möchte er über sein Business, eine
Beratung oder eine Frage reden, hat er zwei Wege:

- E-Mail an **hallo@startandconnect.com**.
- Oder direkt ein Strategiegespräch buchen: https://cal.com/benscheurer/strategie-30.

Das ist ein Beratungsgespräch, kein Support-Call zum Fehler-Beheben.

## Was in eine Meldung gehört

Egal über welchen Weg:

- Die **Kit-Version** aus `starterkit/VERSION`.
- Das betroffene **Produkt** und was er tun wollte.
- Die **genaue Fehlermeldung** samt HTTP-Status.
- Wie sich der Fehler **reproduzieren** lässt, Schritt für Schritt.

**Niemals in eine Meldung:** Schlüssel, Passwörter oder Zugangsdaten. Wenn im
Fehlertext ein Schlüssel steht, entferne ihn. Das Skript entfernt bekannte
Schlüsselmuster zusätzlich automatisch, aber verlass dich nicht darauf.

## Der Ton

Bleib ruhig und lösungsorientiert. Ein Problem ist kein Drama, sondern eine
Aufgabe. Sag klar, was los ist, was du versuchst, und was der nächste Schritt
ist. Wenn es wirklich an der Software liegt, ist das kein Versagen des Nutzers,
sag ihm das auch.
