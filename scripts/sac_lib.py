"""Geteilte Helfer fuer die Starterkit-Hooks.

Reine Standardbibliothek. Alle Funktionen sind fehlertolerant: im Zweifel
liefern sie einen sicheren Default zurueck, statt zu werfen. Ein Hook darf
niemals wegen dieser Datei abstuerzen.

Verwaltet von Start & Connect.
"""

import json
import os


def work_root():
    """Der Arbeitsordner des Nutzers. Feste Struktur: scripts/ -> starterkit/ -> root."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(here))


def starterkit_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(root=None):
    """Liest die .env im Arbeitsordner in ein dict. Leeres dict, wenn keine da ist."""
    root = root or work_root()
    env = {}
    p = os.path.join(root, ".env")
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                if k.startswith("export "):
                    k = k[len("export "):].strip()
                env[k] = v.strip().strip("\"'")
    except Exception:
        pass
    return env


def load_mode(root=None):
    """Wo das secondbrain liegt. Default local, falls die Flag-Datei fehlt.

    local: {"mode": "local", "path": "secondbrain"}
    atlas: {"mode": "atlas", "integration": "atlas-<instanz>", "space": "secondbrain"}
    """
    root = root or work_root()
    default = {"mode": "local", "path": "secondbrain"}
    try:
        with open(os.path.join(root, ".secondbrain.json"), encoding="utf-8") as f:
            d = json.load(f)
            if isinstance(d, dict) and d.get("mode") in ("local", "atlas"):
                return d
    except Exception:
        pass
    return default
