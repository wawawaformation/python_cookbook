"""Plusieurs threads avec ThreadPoolExecutor."""

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def download_file(name: str) -> str:
	print(f"Telechargement de {name}")
	sleep(1)
	return f"{name} termine"


def main() -> None:
	with ThreadPoolExecutor(max_workers=3) as executor:
		results = list(executor.map(download_file, ["a.jpg", "b.jpg", "c.jpg"]))

	print(results)


if __name__ == "__main__":
	main()