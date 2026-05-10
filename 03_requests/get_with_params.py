"""Requête GET avec paramètres de requête."""

import requests


def main() -> None:
	params = {"page": 2, "limit": 10, "search": "python"}
	response = requests.get("https://httpbin.org/get", params=params, timeout=10)
	response.raise_for_status()

	data = response.json()
	print(data["args"])
	print(response.url)


if __name__ == "__main__":
	main()
