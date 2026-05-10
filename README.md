# Cookbook Python pour un développeur PHP

Ce dépôt est un cookbook rapide pour écrire en Python sans devoir
rechercher la syntaxe de base toutes les cinq minutes.

Objectif :
- des snippets courts et exécutables
- des exemples pratiques en priorité
- une passerelle mentale entre les habitudes PHP et les idiomes Python

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer un exemple

```bash
python3 01_python_base/functions.py
python3 02_json/write_json.py
python3 03_requests/get.py
```

## Sections actuelles

- `01_python_base` : la syntaxe Python dont tu as besoin tout le temps
- `02_json` : lire et écrire du JSON rapidement
- `03_requests` : appeler des API avec `requests`
- `08_utils` : variables d'environnement, logging, arguments CLI, timers

## Philosophie

- Préférer la bibliothèque standard quand elle suffit.
- Garder chaque fichier centré sur une seule tâche.
- Proposer des exemples faciles à copier dans de vrais projets.
- Montrer la manière Python, pas une copie de PHP.

## Ordre de lecture conseillé

1. `01_python_base`
2. `02_json`
3. `03_requests`
4. `08_utils`
5. `05_fastapi`
6. `06_database`

## Notes pour un développeur PHP

- `dict` est l'équivalent le plus proche d'un tableau associatif au quotidien.
- `None` est l'équivalent de `null`.
- L'indentation fait partie de la syntaxe.
- Les context managers avec `with` remplacent beaucoup de gestion manuelle des ressources.
- Les exceptions sont préférables à une gestion des erreurs par codes de retour.
