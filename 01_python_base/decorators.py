"""Décorateurs simples pour enrichir une fonction."""

from functools import wraps
from time import perf_counter
from typing import Callable


def log_call(func: Callable) -> Callable:
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f"Appel de {func.__name__} args={args} kwargs={kwargs}")
		return func(*args, **kwargs)

	return wrapper


def measure_time(func: Callable) -> Callable:
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		elapsed = perf_counter() - start
		print(f"{func.__name__} exécutée en {elapsed:.6f}s")
		return result

	return wrapper


@log_call
@measure_time
def build_message(name: str) -> str:
	return f"Bonjour {name}"


def main() -> None:
	print(build_message("David"))


if __name__ == "__main__":
	main()