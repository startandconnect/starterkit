<!-- ═══════════════════════════════════════════════════════════════
     VERWALTET VON START & CONNECT - BITTE NICHT BEARBEITEN
     Kit-Version 0.3.1 | Stand 2026-07-25
     ═══════════════════════════════════════════════════════════════ -->

# Spotlight

**14 Tage kostenlos testbar. Auch mit kompletter Einrichtung durch Start &
Connect buchbar. Aktuelle Infos und Preise auf startandconnect.com/spotlight.**

## Was es macht

White-Label-Website-System. Seiten, Medien, Formulare, eigene Domain, SEO.
Für Selbstständige, die eine saubere Seite brauchen, ohne sich mit
Baukästen oder Hosting zu beschäftigen.

## Einstieg

```
GET /api/ai/onboarding    Orientierung, Konventionen, erste Schritte
GET /api/ai/info          alle Bereiche und Endpunkte in einem Aufruf
```

Beide brauchen **keine** Authentifizierung. Lies sie zuerst, sie sind immer
aktueller als diese Datei.

Danach in dieser Reihenfolge: `GET /api/settings` für den aktuellen Zustand,
`GET /api/pages` für die vorhandenen Seiten.

Bereiche sind unter anderem `pages`, `media`, `settings`, `domain`, `forms`
und `credentials`.

## Besonderheiten, die dich sonst stolpern lassen

- **Die Authentifizierung ist anders als bei den übrigen Produkten.** Header
  `x-api-key: spk_...`, kein Bearer-Token.
- **Änderungen brauchen bis zu einer Minute**, bis sie öffentlich sichtbar
  sind. Prüfst du sofort nach dem Speichern, siehst du noch den alten Stand.
  Warte, bevor du dem Nutzer sagst, es habe nicht geklappt.
- **Entwürfe sind nicht öffentlich.** Sichtbar für Admins über
  `/api/pages/admin-preview/:slug`. Veröffentlicht wird mit
  `POST /api/pages/:id/publish`.
- **Zugangsdaten kommen beim Lesen immer maskiert zurück** (••••••••). Das ist
  kein Fehler, sondern Absicht. Versuch nicht, sie im Klartext zu bekommen.
- **Der Antwort-Aufbau ist uneinheitlich.** `ai/*` und `settings` liefern
  `{ data: ... }`, die Ressourcen-Endpunkte antworten direkt. Prüfe, was du
  bekommst, statt es anzunehmen.
- **Beim Umbenennen einer Mediendatei** wird automatisch eine Weiterleitung
  angelegt. Alte Links bleiben also gültig.

## Was du den Kunden fragst

Das ist hier der wichtigste Teil. Eine Website scheitert selten an der
Technik, sondern daran, dass niemand weiß, was draufstehen soll.

1. Wer soll auf der Seite landen, und was soll die Person danach tun?
2. Was machst du, in einem Satz, wie du es einem Nachbarn erzählen würdest?
3. Was unterscheidet dich von anderen, die dasselbe anbieten?
4. Wie sollen Leute dich erreichen, Formular, Mail, Telefon, Termin?
5. Hast du Bilder, Logo, Referenzen, oder fangen wir bei null an?

Nimm die Antwort auf Frage 2 wörtlich. Wie er es dem Nachbarn erzählt, ist
fast immer besser als das, was er für eine Website angemessen findet.

## Tipps

- **Schreib in seiner Sprache.** Werbesprache macht die Seite austauschbar.
- **Eine Seite reicht am Anfang.** Wer erst fünf Unterseiten plant, geht nie
  online.
- **Zeig Entwürfe früh**, statt lange perfekt zu machen.

## Erster Erfolg

**Die erste Website ist online.** Kein Entwurf, sondern eine erreichbare
Adresse, die er weitergeben kann. Warte die Minute ab, ruf sie dann auf und
zeig ihm, dass sie wirklich da ist.

## Harte Grenzen

- **Nichts veröffentlichen ohne ausdrückliche Zustimmung.** Entwürfe zeigen
  ja, `publish` erst nach seinem Okay.
- **Keine Domain-Änderung ohne Zustimmung.** Wenn dabei etwas schiefgeht, ist
  die Seite nicht mehr erreichbar.
- **Keine Angaben erfinden.** Preise, Referenzen, Qualifikationen und
  Kundenstimmen kommen ausschließlich von ihm. Erfundene Referenzen sind ein
  rechtliches Problem, kein Stilfehler.
- Bei allem, was rechtlich aussieht (Impressum, Datenschutz, Widerruf), lieber
  einmal zu viel fragen.
