# Projektübersicht

Mit diesem Projekt sollen Grunddaten mittels Verarbeitungen in Python so aufbereitet werden, dass sie unter verschiedenen Aspekten ausgewertet werden können.
Primär geht es darum, Daten über Software-Entwicklungsprojekte auszuwerten, zu denen wir in statistische Angaben erhalten haben.

Siehe .\data\commit_stats_all_terms_031125.csv

Im speziellen möchten wir die Daten pro Projekt und Entwickler konsolidieren.
Leider wurde in der Spalte "Author Name" aber keine eindeutige, konsistente Kennung verwendet.
So ist dort oft ein generischer Name "UBC Student" vermerkt, auch wenn sich aufgrund der eMail-Adresse eruieren lässt, wie eigentlich der spezifische Entwicklername lautet.

## Aufgabe
Erstelle für uns Programmcode in Python, der für uns aus der gesamten Datenbasis eine Zuordnungstabelle von spezifischen Entwicklernamen zu den verwendeten eMail-Adressen erstellt.
Im Resultat sollen "Author Name" und "Author email" aus den Grunddaten enthalten sein, sowie der zugehörige eindeutige Entwicklername, mit einer zusätzlichen Angabe zur Wahrscheinlichkeit, dass diese ermittelte Zuordnung stimmt. Diese Angabe der Wahrscheinlichkeit ist wichtig, weil zur Ermittlung dieser Zuordnung auch Fuzzy Search verwendet werden darf, wenn keine eindeutigen Zuordnungen ermittelt werden können.

Beschreibe im Programmcode und allenfalls in einer zusätzlichen Dokumentation, welche Methoden du zur Lösung der Aufgabe anwendest.

## Ordnerstruktur

- `/src`: Enthält den Quellcode
- `/docs`: Enthält die Dokumentation für das Projekt
- `/data`: Enthält die Grund-/Ausgangsdaten und auch die Ergebnisdaten des Projekts

## Generelle Instruktionen

Die Projektsprache ist Deutsch.

Schreibe Programmcode (Namen von Klassen, Objekten, Variablen, Methoden, Kommentaren, usw.) immer in der Projektsprache.

Formuliere alle deine Anworten immer in der Projektsprache, auch wenn die Prompts in einer anderen Sprache verfasst wurden.
Als Ausnahme kann der(die) Entwickler(in) dich aber für die Übersetzung von Begriffen und Sätzen anfragen, die er(sie) nicht versteht.

## Versionskontrolle

When working on a feature, suggest which branch to use.
When the developer asks questions about tools he uses, switch to a different chat reserved for these questions.

## Github Copilot Modes

When in Agent mode, don't modify any code, unless you did check out to a new Git branch before.
Each prompt shall use the context @workspace automatically.
