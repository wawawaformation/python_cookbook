"""Mesurer un temps d'exécution."""

from time import perf_counter, sleep


def main() -> None:
	start = perf_counter()
	sleep(0.2)
	duration = perf_counter() - start
	print(f"Duration: {duration:.3f}s")


if __name__ == "__main__":
	main()
