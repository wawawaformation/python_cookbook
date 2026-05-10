# Lancer FastAPI avec Uvicorn

Depuis la racine du projet :

```bash
uvicorn 05_fastapi.minimal_api:app --reload
```

Puis ouvre :

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

Pour lancer un autre fichier du dossier, remplace simplement `minimal_api`
par le nom du module :

```bash
uvicorn 05_fastapi.query_params:app --reload
```