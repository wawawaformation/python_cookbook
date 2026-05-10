# 09_tests

Snippets courts pour tester du code Python avec la bibliothèque standard
et avec `pytest`.

## Fichiers

- `math_utils.py` : mini module à tester
- `api_client.py` : dépendance externe simulée pour apprendre les mocks
- `unittest_basic.py` : assertions avec `unittest.TestCase`
- `unittest_mock.py` : mock d'un appel HTTP avec `unittest.mock.patch`
- `pytest_basic.py` : style `pytest` avec fonctions simples et paramétrage
- `pytest_mock.py` : remplacement d'une fonction avec `monkeypatch`

## Lancer les exemples

```bash
cd 09_tests
python3 unittest_basic.py
python3 unittest_mock.py
pytest -q pytest_basic.py
pytest -q pytest_mock.py
```

## À retenir

- `unittest` est inclus dans Python et fonctionne bien sans dépendance externe.
- `pytest` offre une syntaxe plus légère et des outils pratiques comme `raises` et `parametrize`.
- Un mock remplace une dépendance externe pendant le test pour éviter un vrai appel réseau, disque ou base de données.