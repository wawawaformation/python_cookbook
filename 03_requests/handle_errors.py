"""Intercepter proprement les erreurs HTTP et réseau."""

import requests


def main() -> None:
	try:
		response = requests.get("https://httpbin.org/status/404", timeout=10)
		response.raise_for_status()
	except requests.HTTPError as exc:
		print(f"HTTP error: {exc}")
	except requests.RequestException as exc:
		print(f"Network error: {exc}")


if __name__ == "__main__":
	main()
