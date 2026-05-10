"""En-têtes HTTP personnalisés."""

import requests


def main() -> None:
	headers = {
		"Accept": "application/json",
		"User-Agent": "python-cookbook/1.0",
		"X-App": "cookbook-python",
	}

	response = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)
	response.raise_for_status()
	print(response.json()["headers"])


if __name__ == "__main__":
	main()
