<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Lokale Kopie aus dem Starterkit-Repo, wird bei Updates
     überschrieben. Eigene Regeln gehören in deine CLAUDE.md.
     Kit-Version 0.12.0 | Stand 2026-10-28
     ═══════════════════════════════════════════════════════════════ -->

# Support und Fehlerbehandlung

Wenn etwas nicht funktioniert, ist das erste Ziel **nicht** eine Support-Mail,
sondern eine saubere Diagnose. Die meisten Probleme liegen an Zugängen,
Eingaben oder Bedienung und sind in einer Minute gelöst. Erst wenn klar bei
Start & Connect etwas hakt, meldet der Nutzer es über „Fehler melden“.

Arbeite diese drei Schritte der Reihe nach ab, ruhig und ohne zu raten.

## Schritt 1: Die Fehlermeldung genau lesen

Rate nie, was schiefging. Lies die echte Meldung. Bei einem Aufruf über den
Connector oder ein Produkt sagt dir der HTTP-Status fast immer, wo das Problem
sitzt:

| Status | Bedeutung | Wo das Problem meist liegt |
| --- | --- | --- |
| 401 / 403 | nicht angemeldet / keine Berechtigung | **Nutzer:** Schlüssel fehlt, ist falsch oder abgelaufen |
| 404 | Pfad oder Ressource nicht gefunden | **Du:** falscher Endpunkt, erst den Weg suchen lassen |
| 400 / 422 | Eingabe ungültig | **Du:** ein Feld, Format oder Enum stimmt nicht |
| 428 | Bestätigung nötig | **kein Fehler:** by design, z.B. Quitt vor dem Festschreiben |
| 429 | zu viele Anfragen | kurz warten, dann erneut |
| 500 / 502 / 503 | Serverfehler | **Start & Connect:** die Software hakt |
| Timeout / nicht erreichbar | keine Verbindung | Netz des Nutzers oder Server unten |

Zwei Stolpersteine, an denen schon Diagnosen falsch abgebogen sind:

- **Kommt statt einer API-Antwort eine Webseite zurück**, liegt unter dieser
  Adresse keine Schnittstelle. Der Pfad stimmt nicht. Das ist keine Sperre und
  keine fehlende Berechtigung.
- **Ein 404 bei einem Pfad, der richtig aussieht**, kommt oft von einem
  unsichtbaren Zeichen am Ende, etwa einem geschützten Leerzeichen aus Word,
  Outlook oder Teams. Tipp den Pfad neu, statt ihn zu kopieren.

## Schritt 2: Liegt es beim Nutzer oder bei der Software?

Das ist die entscheidende Frage. Prüf sie mit ein paar gezielten Handgriffen,
statt zu vermuten:

- **Tritt es reproduzierbar auf** oder war es einmalig? Einmalige Aussetzer
  sind oft ein Schluckauf, nach einem erneuten Versuch weg.
- **Was hat sich zuletzt geändert?** Ein neuer Schlüssel, ein Update, eine neue
  Datei. Das ist meist die Ursache.
- **Ist der Connector erreichbar?** Lass dir über den Connector die
  Verbindungen auflisten. Kommt eine Liste, steht er. Fehlt das Werkzeug ganz
  oder meldet es einen Anmeldefehler, bitte den Nutzer, `/mcp` zu tippen: Dort
  sieht er, ob `connector` verbunden ist, und kann sich neu anmelden.
- **Ist das Produkt selbst erreichbar?** Ruf seinen Info-Endpunkt auf (z.B.
  `GET /api/ai/info`). Antwortet er mit gültigem Schlüssel nicht, liegt es an
  der Software, nicht am Nutzer.
- **Ist nur ein Programm betroffen oder alle?** Nur eines deutet auf dieses
  Produkt, alle deuten auf Connector oder Netz.

**Typisch Nutzer-Seite** (das kannst du meist selbst lösen):
Anmeldung am Connector abgelaufen, Schlüssel im Connector fehlt oder ist
abgelaufen, im falschen Ordner gestartet (dann fehlt die Verbindung
`connector`), Produkt noch nicht verbunden, ein Tippfehler in der Eingabe.

**Typisch Software-Seite** (das gehört zu Start & Connect):
Ein 500er trotz gültigem Zugang, ein Produkt-Endpunkt reagiert nicht obwohl der
Schlüssel stimmt, ein dokumentierter Endpunkt existiert nicht oder verhält sich
falsch, die Selbst-Doku widerspricht der Realität, ein reproduzierbarer Fehler.

## Schritt 3: Was du selbst zuerst versuchst

Bevor irgendeine Nachricht rausgeht:

- Bei **404 oder Eingabefehler:** den Info-Endpunkt fragen oder den Connector
  den Weg erneut suchen lassen, die Doku ist aktueller als deine Annahme, und den Aufruf korrigieren.
- Bei **401 / 403:** prüfen, ob die Anmeldung am Connector noch gilt (`/mcp`)
  und ob der Schlüssel des Programms im Connector aktuell ist. Ohne Connector:
  ob er in der `.env` steht. Steht bei dem Programm ein Warnhinweis, muss der
  Nutzer sich in dessen Oberfläche neu anmelden.
- Bei **einmaligem Fehler:** einmal wiederholen.

Sag dem Nutzer in einfachen Worten, was du gerade prüfst. Er soll sich nicht
hilflos fühlen.

## Wann eine Meldung sinnvoll ist

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
Fehlereingrenzung ist mehr wert als eine schnelle, vage Nachricht, und eine
Meldung ist der letzte Schritt, nicht der erste.

## Wie eine Meldung rausgeht

Fehler werden immer **asynchron mit KI-Hilfe** behoben. Ein Telefonat oder ein
Loom-Video bringt dabei weder dem Nutzer noch Start & Connect etwas, es hilft
nur eine **präzise, schriftliche Fehlerbeschreibung**. Biete also keine Calls
und keine Bildschirmvideos an, sondern erstelle mit dem Nutzer eine gute
Beschreibung.

### Der Weg: „Fehler melden“ im jeweiligen Produkt

Die Produkte von Start & Connect haben einen Bereich **„Fehler melden“**. Darüber
gehen die Meldungen raus. Ausnahmen stehen in der Anleitung des Produkts, zum
Beispiel bei Orbit. Er hängt Adresse, Version, Browser und Fehlerspuren
von selbst an, die Start & Connect zur Diagnose braucht.

1. Formuliere die Meldung mit ihm: was er tun wollte, was passiert ist, die
   genaue Fehlermeldung, wie es sich wiederholen lässt.
2. Lotse ihn in das Produkt, in dem der Fehler sitzt, zu „Fehler melden“.
3. **Er schickt die Meldung selbst ab.** Du sendest nichts für ihn.

**Der Fehler sitzt im Starterkit oder in der Einrichtung mit Claude Code?** Dann
meldet er ihn über „Fehler melden“ in einem Produkt, das er nutzt, und
schreibt dazu, dass es ums Starterkit geht.

### Die letzte Option: E-Mail

Nur wenn er „Fehler melden“ nicht erreicht, weil das Produkt gar nicht startet
oder er nicht hineinkommt, wenn das Produkt keinen solchen Bereich hat, wenn
nach dem Absenden eine Fehlermeldung statt einer Bestätigung kommt, oder wenn
er kein Produkt von Start & Connect hat,
schreibt er an **hallo@startandconnect.com**. Den Text formulierst du mit ihm,
abschicken tut er.

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

**Niemals in eine Meldung:** Schlüssel, Passwörter oder Zugangsdaten. Steht im
Fehlertext ein Schlüssel, nimm ihn heraus, bevor der Nutzer die Meldung
abschickt. Prüf das bei jeder Meldung, es gibt kein Netz, das ihn noch
abfängt.

## Wenn der Nutzer frustriert ist

Das passiert selten, aber es passiert. Der Nutzer verliert die Geduld, wird
patzig oder ist überzeugt, dass ein Produkt kaputt ist.

- **Bleib ruhig und sachlich.** Geh nicht in die Defensive, spiegle den Ton
  nicht, nimm nichts persönlich.
- **Nimm den Frust einmal kurz und echt an.** „Ich verstehe, dass das gerade
  nervt, lass es uns zusammen lösen“ reicht.
- **Handeln beruhigt mehr als Erklären.** Mach den nächsten konkreten Schritt
  selbst.
- **Frust ist keine Diagnose.** Übersetz ihn in eine Frage: was genau hast du
  gemacht, was hast du erwartet, was kam? Dann arbeite die Schritte oben ab.
- **Glaub nicht die Schuldzuweisung, prüf die Ursache.** „Spotlight ist
  kaputt“ heißt nicht, dass es an Spotlight liegt.
- **Gemeldet wird erst mit echtem Befund**, und dann sachlich, nicht die
  wütende Version.

## Der Ton

Bleib ruhig und lösungsorientiert. Ein Problem ist kein Drama, sondern eine
Aufgabe. Sag klar, was los ist, was du versuchst, und was der nächste Schritt
ist. Wenn es wirklich an der Software liegt, ist das kein Versagen des Nutzers,
sag ihm das auch.
