"""Gérer un dépassement de délai."""

import requests


def main() -> None:
	try:
		requests.get("https://httpbin.org/delay/3", timeout=1)
	except requests.Timeout:
		print("Request timed out")


if __name__ == "__main__":
	main()
