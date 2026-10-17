#!/usr/bin/env python3
"""report-issue - schickt eine Support-Anfrage an Start & Connect.

NUR nach ausdruecklicher Freigabe des Nutzers aufrufen. Du (Claude) zeigst ihm
vorher den vollstaendigen Inhalt (Titel, Text, Schwere) und holst sein Okay.
Ohne Freigabe wird nichts gesendet.

Reine Standardbibliothek, laeuft auf Mac und Windows.

Verwendung:
  report-issue.py --title "..." --body "..." --email "seine@mail.de"
                  [--category FUNCTION] [--severity NORMAL] [--name ...] [--product ...]

  category: DISPLAY | FUNCTION | PERFORMANCE | LOGIN | DATA | OTHER
  severity: LOW | NORMAL | HIGH | CRITICAL  (Standard NORMAL)

Der Titel wird als "[Kategorie] Titel" gesendet, damit Start & Connect filtern
kann. Kit-Version und Plattform werden automatisch als Metadaten mitgeschickt.

Die E-Mail des Nutzers ist Pflicht. Ohne sie kann Start & Connect weder eine
Eingangs- noch eine Abschlussbestaetigung schicken - die Meldung verschwindet
aus Sicht des Nutzers spurlos. Statt --email kann SUPPORT_EMAIL in der .env
stehen, dann muss niemand jedes Mal danach gefragt werden.

Verwaltet von Start & Connect. Kit-Version 0.11.1
"""

import argparse
import json
import os
import platform
import re
import sys
import urllib.error
import urllib.request

# Ausgabe fest auf UTF-8. Auf Windows steht die Konsole sonst auf cp1252, und ein einzelnes
# Zeichen ausserhalb dieser Tabelle - im Text einer Fehlermeldung keine Seltenheit - laesst
# das Skript abbrechen, bevor die Meldung raus ist. Siehe SUP-0163.
for _strom in (sys.stdout, sys.stderr):
    try:
        _strom.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# Inbound-Ticket-Webhook des Starterkits. Der Token ist ein
# Rate-Limit-Bezeichner, kein Datenzugang. Bei Missbrauch serverseitig
# rotierbar.
WEBHOOK = "https://atlas.sac.sh/api/tickets/inbound/tk_mliQKf20jFsaqOzj4gYcXdeOy3m7mqQl"

CATEGORIES = {"DISPLAY", "FUNCTION", "PERFORMANCE", "LOGIN", "DATA", "OTHER"}
SEVERITIES = {"LOW", "NORMAL", "HIGH", "CRITICAL"}

# Bekannte Schluessel-Muster, die niemals in ein Ticket gehoeren. Sicherheitsnetz,
# falls doch mal ein Schluessel im Text landet.
KEY_PATTERNS = [
    r"\b(sk|pk|cnk|atl|qit|spk|nx)_[A-Za-z0-9_\-]{8,}\b",
    r"Bearer\s+[A-Za-z0-9._\-]{12,}",
    r"tk_[A-Za-z0-9_\-]{8,}",
]


def scrub(text):
    if not text:
        return text
    for pat in KEY_PATTERNS:
        text = re.sub(pat, "[ENTFERNT]", text)
    return text


def aus_env_datei(schluessel):
    """Sucht die .env vom Skript aus aufwaerts - dieselbe Datei wie connector-call.py."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        pfad = os.path.join(d, ".env")
        if os.path.isfile(pfad):
            try:
                with open(pfad, encoding="utf-8") as f:
                    for zeile in f:
                        zeile = zeile.strip()
                        if not zeile or zeile.startswith("#") or "=" not in zeile:
                            continue
                        k, v = zeile.split("=", 1)
                        k = k.strip()
                        if k.startswith("export "):
                            k = k[len("export "):].strip()
                        if k == schluessel:
                            return v.strip().strip("\"'")
            except OSError:
                return None
            return None
        eltern = os.path.dirname(d)
        if eltern == d:
            break
        d = eltern
    return None


def sieht_aus_wie_adresse(wert):
    """Absichtlich grob: erkennt Tippfehler und Platzhalter, nicht jede Feinheit von RFC 5322."""
    if not wert:
        return False
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", wert.strip()) is not None


# Die Adresse ist Pflicht, und zwar aus einem gemessenen Grund.
#
# Atlas schickt dem Melder genau zwei Mails: eine Eingangsbestaetigung und eine Nachricht beim
# Abschluss. Beide haengen an reporterEmail. Fehlt sie, passiert auf seiner Seite NICHTS - kein
# "angekommen", kein "behoben". Er sieht ein Skript, das "gesendet" sagt, und danach Stille.
#
# Bei SUP-0158 und SUP-0163 war das so. Beim ersten schrieb der Melder sogar dazu, er sende
# lieber doppelt, weil er nicht wusste, ob die erste Meldung angekommen war. Genau diese
# Unsicherheit entsteht aus der fehlenden Adresse. Ein Hinweis auf stderr hat nicht gereicht;
# er stand schon in der Anleitung und wurde zweimal ueberlesen.
def ermittle_adresse(vom_aufruf):
    quelle = "--email"
    adresse = vom_aufruf
    if not adresse:
        adresse, quelle = os.environ.get("SUPPORT_EMAIL"), "SUPPORT_EMAIL aus der Umgebung"
    if not adresse:
        adresse, quelle = aus_env_datei("SUPPORT_EMAIL"), "SUPPORT_EMAIL aus der .env"
    if not adresse:
        print(
            "Fehler: Es fehlt die E-Mail des Nutzers, deshalb wurde nichts gesendet.\n"
            "\n"
            "Ohne sie bekommt er weder eine Eingangs- noch eine Abschlussbestaetigung. Die\n"
            "Meldung verschwindet aus seiner Sicht spurlos, und er meldet sie irgendwann ein\n"
            "zweites Mal, weil er nicht weiss, ob die erste ankam.\n"
            "\n"
            "Frag ihn kurz nach seiner E-Mail und ruf erneut auf mit --email \"seine@mail.de\".\n"
            "Damit das nicht jedes Mal noetig ist, kann sie als SUPPORT_EMAIL in der .env stehen.",
            file=sys.stderr,
        )
        sys.exit(1)
    if not sieht_aus_wie_adresse(adresse):
        print(
            f"Fehler: \"{adresse}\" ({quelle}) sieht nicht nach einer E-Mail-Adresse aus, deshalb\n"
            f"wurde nichts gesendet. Eine falsche Adresse ist so gut wie keine - die Antwort\n"
            f"geht ins Leere. Frag beim Nutzer nach und ruf erneut auf.",
            file=sys.stderr,
        )
        sys.exit(1)
    return adresse.strip()


def kit_version():
    try:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(root, "VERSION"), encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return "unbekannt"


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("--title", required=True)
    p.add_argument("--body", default="")
    p.add_argument("--category", default="OTHER")
    p.add_argument("--severity", default="NORMAL")
    p.add_argument("--email", default=None)
    p.add_argument("--name", default=None)
    p.add_argument("--product", default=None)
    a = p.parse_args()

    category = a.category.upper()
    severity = a.severity.upper()
    if category not in CATEGORIES:
        category = "OTHER"
    if severity not in SEVERITIES:
        severity = "NORMAL"

    email = ermittle_adresse(a.email)
    name = a.name or os.environ.get("SUPPORT_NAME") or aus_env_datei("SUPPORT_NAME")

    title = scrub(a.title.strip())[:190]
    body = scrub(a.body.strip())

    payload = {
        "title": f"[{category}] {title}",
        "body": body or None,
        "reporterEmail": email,
        "reporterName": name,
        "severity": severity,
        "metadata": {
            "source": "starterkit",
            "kitVersion": kit_version(),
            "platform": platform.platform(),
            "python": platform.python_version(),
            "product": a.product,
        },
    }

    req = urllib.request.Request(
        WEBHOOK,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode() or "{}")
        num = (data.get("data") or {}).get("number")
        if num:
            print(f"Support-Anfrage gesendet. Ticket-Nummer: {num}")
        else:
            print("Support-Anfrage gesendet.")
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:200]
        print(f"Fehler: Start & Connect hat die Anfrage abgelehnt ({e.code}): {detail}",
              file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Fehler: Start & Connect ist gerade nicht erreichbar ({e.reason}). "
              f"Versuch es spaeter erneut oder schreib als letzte Option an "
              f"hallo@startandconnect.com.",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
