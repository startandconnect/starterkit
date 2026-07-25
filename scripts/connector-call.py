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

Verwaltet von Start & Connect. Kit-Version 0.4.0
"""

import json
import os
import sys
import urllib.error
import urllib.request


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
        payload = {
            "integrationId": argv[1],
            "method": argv[2].upper(),
            "path": argv[3],
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
