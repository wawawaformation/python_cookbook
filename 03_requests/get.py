"""Requête GET simple avec requests."""

import requests


def main() -> None:
	response = requests.get("https://httpbin.org/get", timeout=10)
	response.raise_for_status()

	print(response.status_code)
	print(response.json()["url"])


if __name__ == "__main__":
	main()
