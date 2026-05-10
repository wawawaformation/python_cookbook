"""Envoyer un token Bearer avec requests."""

import os

import requests


def main() -> None:
	token = os.getenv("API_TOKEN", "replace-me")
	response = requests.get(
		"https://httpbin.org/bearer",
		headers={"Authorization": f"Bearer {token}"},
		timeout=10,
	)
	print(response.status_code)
	print(response.json())


if __name__ == "__main__":
	main()
