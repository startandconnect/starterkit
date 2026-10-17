#!/usr/bin/env python3
"""connector-call - Zugriff auf die Programme des Nutzers ueber den Connector.

Nur Standardbibliothek, laeuft auf Mac und Windows ohne Installation.

Verwendung:
  connector-call.py integrations
      Listet alle verbundenen Programme mit ihrem Zustand.

  connector-call.py discover <integration> "<suchbegriff>"
      Findet den richtigen Weg fuer ein Vorhaben. IMMER zuerst aufrufen.

  connector-call.py call <integration> <METHODE> <pfad> [json-body]
      Fuehrt den Aufruf aus.

Beispiel:
  connector-call.py discover atlas "aufgabe anlegen"
  connector-call.py call atlas POST /api/tasks '{"title":"Angebot schreiben"}'

Zugangsdaten kommen aus der .env im Arbeitsordner. Jeder Kunde hat eine
eigene Connector-Adresse, beides steht in seinem Connector-Konto:
  CONNECTOR_BASE=<seine Connector-Adresse>
  CONNECTOR_API_KEY=<sein Schluessel>

Verwaltet von Start & Connect. Kit-Version 0.11.0
"""

import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request

# Ausgabe fest auf UTF-8, unabhaengig vom Betriebssystem.
#
# Windows gibt der Konsole standardmaessig die Zeichentabelle cp1252. Sobald eine Antwort ein
# Zeichen enthaelt, das dort fehlt - ein Pfeil genuegt - bricht das Skript mit einem
# UnicodeEncodeError ab, mitten in einer ansonsten fehlerfreien Antwort. Der Behelf war bisher,
# PYTHONIOENCODING von Hand zu setzen; das muss niemand wissen muessen.
for _strom in (sys.stdout, sys.stderr):
    try:
        _strom.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def load_env():
    """Sucht die .env vom Skript aus aufwaerts und laedt sie in os.environ."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        p = os.path.join(d, ".env")
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    k = k.strip()
                    if k.startswith("export "):
                        k = k[len("export "):].strip()
                    os.environ.setdefault(k, v.strip().strip("\"'"))
            return
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent


# Zeichen, die man nicht sieht, die aber im Pfad landen.
#
# Gemeldet am 27.08.2026: derselbe Aufruf antwortete mit 404, mit einem angehaengten
# Fragezeichen dagegen mit 200. Nachgemessen gegen den Connector:
#
#   /api/tasks          200        /api/tasks<CR>      200
#   /api/tasks<U+00A0>  404        /api/tasks<U+200B>  404
#   /api/tasks?<U+00A0> 200
#
# Der Unterschied liegt daran, WELCHES unsichtbare Zeichen es ist. Leerzeichen, Tabulator und
# Wagenruecklauf entfernt der URL-Parser auf dem Server von selbst. Ein geschuetztes
# Leerzeichen oder eine Breite Null ueberlebt, wird zu %C2%A0 beziehungsweise %E2%80%8B kodiert
# und haengt damit am Pfad - die Route gibt es unter diesem Namen nicht. Mit dem Fragezeichen
# rutscht das Zeichen in den Abfrageteil, wo es niemanden stoert. Daher der Eindruck, das
# Fragezeichen repariere etwas.
#
# Solche Zeichen kommen beim Kopieren aus Word, Outlook oder Teams mit, ohne Spur im Text.
def saeubere_pfad(pfad):
    """Entfernt unsichtbare Zeichen an beiden Enden. Gibt (pfad, entferntes) zurueck."""
    def unsichtbar(z):
        return z.isspace() or unicodedata.category(z) in ("Cc", "Cf", "Zs", "Zl", "Zp")

    sauber = pfad
    weg = []
    while sauber and unsichtbar(sauber[0]):
        weg.append(sauber[0]); sauber = sauber[1:]
    while sauber and unsichtbar(sauber[-1]):
        weg.append(sauber[-1]); sauber = sauber[:-1]
    return sauber, "".join(weg)


def melde_gesaeuberten_pfad(original, sauber, weg):
    """Sagt, dass etwas entfernt wurde - stilles Reparieren verschleiert die Ursache."""
    if not weg:
        return
    namen = ", ".join(f"U+{ord(z):04X} ({unicodedata.name(z, 'ohne Namen')})" for z in weg)
    print(
        f"Hinweis: Im Pfad steckten unsichtbare Zeichen, sie wurden entfernt: {namen}. "
        f"Gesendet wurde \"{sauber}\". Solche Zeichen kommen beim Kopieren aus Word, Outlook "
        f"oder Teams mit.",
        file=sys.stderr,
    )


def die(msg):
    print(f"Fehler: {msg}", file=sys.stderr)
    sys.exit(1)


def request(path, payload=None, method="GET"):
    base = os.environ.get("CONNECTOR_BASE", "").rstrip("/")
    key = os.environ.get("CONNECTOR_API_KEY", "")
    if not base or not key:
        die(
            "Kein Connector-Zugang gefunden. In der .env im Arbeitsordner "
            "muessen CONNECTOR_BASE und CONNECTOR_API_KEY stehen."
        )

    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        f"{base}{path}",
        data=data,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:800]
        # Eine HTML-Seite als Antwort heisst fast immer "diese Adresse gibt es nicht" - und
        # fast nie "du darfst hier nicht". Aus genau dieser Verwechslung ist am 27.08.2026 die
        # Meldung entstanden, das Wiki sei fuer eine Mitarbeiterin gesperrt. Es war nichts
        # gesperrt, der Pfad stimmte nicht.
        if body.lstrip()[:1] == "<":
            die(
                f"Der Connector hat mit {e.code} geantwortet, und zwar mit einer Webseite statt "
                f"einer API-Antwort. Das heisst: unter dieser Adresse liegt keine Schnittstelle. "
                f"Pruefe den Pfad - es ist keine Sperre und keine fehlende Berechtigung."
            )
        die(f"Der Connector hat mit {e.code} geantwortet: {body}")
    except urllib.error.URLError as e:
        die(f"Der Connector ist nicht erreichbar: {e.reason}")


def out(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv):
    load_env()
    if not argv:
        print(__doc__)
        return

    cmd = argv[0]

    if cmd == "integrations":
        out(request("/api/integrations"))

    elif cmd == "discover":
        if len(argv) < 3:
            die('Aufruf: discover <integration> "<suchbegriff>"')
        out(request(
            "/api/discover",
            {"integrationId": argv[1], "intent": argv[2]},
            method="POST",
        ))

    elif cmd == "call":
        if len(argv) < 4:
            die("Aufruf: call <integration> <METHODE> <pfad> [json-body]")
        pfad, entfernt = saeubere_pfad(argv[3])
        melde_gesaeuberten_pfad(argv[3], pfad, entfernt)
        payload = {
            "integrationId": argv[1],
            "method": argv[2].upper(),
            "path": pfad,
        }
        if len(argv) > 4:
            try:
                payload["body"] = json.loads(argv[4])
            except json.JSONDecodeError as e:
                die(f"Der json-body ist kein gueltiges JSON: {e}")
        out(request("/api/playground/request", payload, method="POST"))

    else:
        die(f"Unbekannter Befehl '{cmd}'. Bekannt: integrations, discover, call")


if __name__ == "__main__":
    main(sys.argv[1:])
