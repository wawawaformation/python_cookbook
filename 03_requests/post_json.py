"""Envoyer des données JSON en POST."""

import requests


def main() -> None:
	payload = {"title": "Cookbook", "language": "python", "from": "php"}
	response = requests.post("https://httpbin.org/post", json=payload, timeout=10)
	response.raise_for_status()

	print(response.status_code)
	print(response.json()["json"])


if __name__ == "__main__":
	main()
