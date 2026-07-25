<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.4.1 | Stand 2026-07-25
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

- Fragen, die du selbst beantworten kannst.
- Bedienfehler oder Eingabefehler, die du gerade behoben hast.
- Ein Schlüssel- oder Verbindungsproblem auf Nutzer-Seite.
- Ein einmaliger Aussetzer, der nach einem erneuten Versuch weg ist.

Im Zweifel gilt: erst weiter diagnostizieren. Eine gute Fehlereingrenzung ist
mehr wert als eine schnelle, vage Nachricht.

## Die drei Support-Wege

Es gibt keine Telefonate, keine Rückrufe und keine Bildschirmfreigaben, biete
das auch nicht an. Es gibt drei Wege, je nachdem, wo der Fehler sitzt.

### 1. Fehler in einem Produkt: die "Fehler melden"-Funktion im Produkt

Ist der Fehler in einem Produkt selbst (Quitt, Nexus, Spotlight, Atlas,
Connector), ist der beste Weg die **"Fehler melden"-Funktion**, die in jedem
Produkt prominent eingebaut ist. Sie hängt den technischen Kontext automatisch
an und landet direkt im richtigen Postfach. Lotse den Nutzer dorthin.

### 2. Du sendest ein Ticket, mit ausdrücklicher Freigabe

Für Einrichtungs- und Kit-Probleme, oder wenn der Nutzer möchte, dass du es
übernimmst, kannst du selbst eine Support-Anfrage an Start & Connect schicken.
**Nur mit seiner ausdrücklichen Freigabe.**

Der Ablauf ist verbindlich:

1. Formuliere Titel, Text und Schwere.
2. **Zeig ihm den vollständigen Inhalt** und frag, ob du das so senden darfst.
3. Erst bei einem klaren Ja sendest du mit:

   ```
   python3 starterkit/scripts/report-issue.py --title "..." --body "..." \
     --category FUNCTION --severity NORMAL --product quitt
   ```

   Kategorie: `DISPLAY`, `FUNCTION`, `PERFORMANCE`, `LOGIN`, `DATA`, `OTHER`.
   Schwere: `LOW`, `NORMAL`, `HIGH`, `CRITICAL`. Kit-Version und Plattform
   hängt das Skript selbst an.

Ohne Freigabe wird nichts gesendet. Sag ihm die Ticket-Nummer, die
zurückkommt.

### 3. E-Mail

Der Nutzer kann jederzeit selbst schreiben, an **support@startandconnect.com**.
Nutze das, wenn er lieber selbst formuliert oder etwas Persönliches klären will.

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
