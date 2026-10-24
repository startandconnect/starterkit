#!/usr/bin/env python3
"""Alter SessionStart-Hook des Starterkits, nur noch als Hinweis.

Ab Version 0.12 richtet das Starterkit keinen Hook mehr ein. Diese Datei gibt
es nur, damit Installationen aus Version 0.11 und älter beim Start keinen
Fehler sehen, sondern den Hinweis zum Umstieg. Sie liest nichts, schreibt
nichts, ruft nichts auf und verbindet sich mit nichts. Mit Version 1.0 entfällt
sie.

Verwaltet von Start & Connect. Kit-Version 0.12.0
"""

print(
    "Hinweis an Claude (Starterkit): Bitte migrieren. Dieses Starterkit wurde "
    "auf eine neue Version aktualisiert, die ohne Hook und ohne Skripte "
    "auskommt. Lies starterkit/MIGRATION.md und biete dem Nutzer den Umstieg "
    "an. Der alte Zugang ueber connector-call.py besteht nicht mehr."
)
