# 05_fastapi

Exemples courts pour demarrer avec FastAPI.

## Fichiers

- `minimal_api.py` : application minimale avec deux routes GET
- `get_route.py` : route GET qui retourne une liste
- `post_route.py` : route POST simple avec payload JSON
- `path_params.py` : parametres dans l'URL
- `query_params.py` : query string et pagination simple
- `pydantic_model.py` : validation d'entree avec Pydantic
- `error_response.py` : erreur HTTP 404 avec `HTTPException`
- `run_uvicorn.md` : commande pour lancer Uvicorn

## Lancer un exemple

```bash
uvicorn 05_fastapi.minimal_api:app --reload
```

## Documentation automatique

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc