#!/usr/bin/env python3
"""SessionStart-Hook des Starterkits.

Erledigt in einem Lauf, einmal pro Session:
  1. Update-Check   - gibt es eine neuere Kit-Version?
  2. Doctor-lite    - ist der Connector erreichbar? (nur wenn ein Key da ist)
  3. Tagesgeruest   - heutige Session-Datei anlegen (nur local)
  4. Tagesorientierung - die heutigen Prioritaeten zeigen

WICHTIG: Dieses Skript darf eine Session NIEMALS blockieren. Jeder Fehler,
jedes Timeout, jede fehlende Verbindung fuehrt zu einem stillen Exit 0. Lieber
kein Hinweis als ein gestoerter Start.

Die Ausgabe geht als Kontext an Claude, nicht direkt an den Nutzer.

Verwaltet von Start & Connect. Kit-Version 0.5.2
"""

import datetime
import os
import subprocess
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_lib  # noqa: E402

GIT_TIMEOUT = 8
NET_TIMEOUT = 5


def check_update(kit):
    """Meldet, wenn das Starterkit-Repo hinterherhinkt. None sonst."""
    if not os.path.isdir(os.path.join(kit, ".git")):
        return None

    def git(*a):
        try:
            r = subprocess.run(
                ["git", "-C", kit, *a],
                capture_output=True, text=True, timeout=GIT_TIMEOUT,
            )
        except Exception:
            return None
        return r.stdout.strip() if r.returncode == 0 else None

    if git("fetch", "--quiet") is None:
        return None
    behind = git("rev-list", "--count", "HEAD..@{u}")
    if not behind or behind == "0":
        return None
    return (
        f"Fuer das Starterkit gibt es eine neuere Version ({behind} Aenderungen). "
        "Sag dem Nutzer kurz Bescheid und frage, ob du aktualisieren sollst. Bei "
        "Ja: 'git -C starterkit pull'. Fasse dabei weder secondbrain/ noch "
        "projects/ an. Will er nicht, ist das in Ordnung, frag nicht erneut."
    )


def check_connector(env):
    """Warnt, wenn ein Connector-Key da ist, der Connector aber nicht antwortet."""
    base = env.get("CONNECTOR_BASE", "").rstrip("/")
    key = env.get("CONNECTOR_API_KEY", "")
    if not base or not key:
        return None  # kein Connector eingerichtet, nichts zu pruefen
    req = urllib.request.Request(
        f"{base}/api/ai/info",
        headers={"Authorization": f"Bearer {key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=NET_TIMEOUT) as r:
            r.read(1)
        return None  # erreichbar, still bleiben
    except Exception:
        return (
            "Der Connector des Nutzers ist gerade nicht erreichbar. Wenn er in "
            "dieser Session mit seinen Programmen arbeiten will, weise ihn "
            "freundlich darauf hin, dass das gerade nicht geht, und schlag vor, "
            "es spaeter erneut zu versuchen. Lokale Arbeit ist normal moeglich."
        )


def orientation(root, mode):
    """Legt (lokal) die Session-Datei an und liefert die heutige Orientierung."""
    today = datetime.date.today().isoformat()

    if mode.get("mode") == "atlas":
        return (
            "Das secondbrain des Nutzers liegt in Atlas. Hol dir zu Beginn die "
            "heutigen Aufgaben aus Atlas, wenn er in die Arbeit einsteigt, und "
            "halte den Tagesstand am Ende im Atlas-Wiki fest."
        )

    sb = os.path.join(root, mode.get("path", "secondbrain"))

    # Tagesgeruest: heutige Session-Datei anlegen, falls sie fehlt.
    try:
        sessions = os.path.join(sb, "sessions")
        os.makedirs(sessions, exist_ok=True)
        f = os.path.join(sessions, f"{today}.md")
        if not os.path.isfile(f):
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# Session {today}\n\n")
    except Exception:
        pass

    # Tagesorientierung aus TODAY.md.
    try:
        today_md = os.path.join(sb, "planning", "TODAY.md")
        with open(today_md, encoding="utf-8") as fh:
            content = fh.read().strip()
        if content:
            return (
                "Die heutigen Prioritaeten des Nutzers aus "
                "secondbrain/planning/TODAY.md:\n\n" + content[:1000]
            )
    except Exception:
        pass
    return None


def main():
    root = sac_lib.work_root()
    kit = sac_lib.starterkit_dir()
    env = sac_lib.load_env(root)
    mode = sac_lib.load_mode(root)

    parts = []
    for fn in (
        lambda: check_update(kit),
        lambda: check_connector(env),
        lambda: orientation(root, mode),
    ):
        try:
            msg = fn()
        except Exception:
            msg = None
        if msg:
            parts.append(msg)

    if parts:
        print("Hinweis an Claude (Starterkit):\n\n" + "\n\n".join(parts))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # Absolut nie die Session stoeren.
    sys.exit(0)
