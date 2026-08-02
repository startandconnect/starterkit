#!/usr/bin/env python3
"""report-issue - schickt eine Support-Anfrage an Start & Connect.

NUR nach ausdruecklicher Freigabe des Nutzers aufrufen. Du (Claude) zeigst ihm
vorher den vollstaendigen Inhalt (Titel, Text, Schwere) und holst sein Okay.
Ohne Freigabe wird nichts gesendet.

Reine Standardbibliothek, laeuft auf Mac und Windows.

Verwendung:
  report-issue.py --title "..." --body "..." [--category FUNCTION]
                  [--severity NORMAL] [--email ...] [--name ...] [--product ...]

  category: DISPLAY | FUNCTION | PERFORMANCE | LOGIN | DATA | OTHER
  severity: LOW | NORMAL | HIGH | CRITICAL  (Standard NORMAL)

Der Titel wird als "[Kategorie] Titel" gesendet, damit Start & Connect filtern
kann. Kit-Version und Plattform werden automatisch als Metadaten mitgeschickt.

Verwaltet von Start & Connect. Kit-Version 0.8.1
"""

import argparse
import json
import os
import platform
import re
import sys
import urllib.error
import urllib.request

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

    if not a.email:
        print("Hinweis: keine E-Mail (--email) mitgegeben. Start & Connect kann "
              "dann nicht antworten. Sende trotzdem, aber besser mit E-Mail.",
              file=sys.stderr)

    title = scrub(a.title.strip())[:190]
    body = scrub(a.body.strip())

    payload = {
        "title": f"[{category}] {title}",
        "body": body or None,
        "reporterEmail": a.email,
        "reporterName": a.name,
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
