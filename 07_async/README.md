# 07_async

Exemples simples pour comprendre la concurrence en Python.

## Fichiers

- `async_function.py` : une fonction `async` simple
- `gather_tasks.py` : plusieurs taches async en meme temps
- `thread_basic.py` : un thread simple
- `thread_pool.py` : plusieurs threads avec un pool
- `async_to_thread.py` : utiliser un thread depuis `asyncio`

## Idee simple

- `asyncio` : utile quand tu attends souvent, par exemple une API ou un fichier
- `threading` : utile quand une librairie bloque et n'est pas async
- `asyncio.to_thread()` : utile pour melanger les deux

## Lancer les exemples

```bash
python3 07_async/async_function.py
python3 07_async/gather_tasks.py
python3 07_async/thread_basic.py
python3 07_async/thread_pool.py
python3 07_async/async_to_thread.py
```