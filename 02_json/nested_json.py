"""Accéder à des données JSON imbriquées simplement."""

import json


def main() -> None:
	payload = {
		"user": {
			"name": "David",
			"address": {"city": "Paris", "zip": "75000"},
		},
		"orders": [
			{"id": 1, "total": 29.9},
			{"id": 2, "total": 49.9},
		],
	}

	print(json.dumps(payload, indent=2, ensure_ascii=False))
	print(payload["user"]["address"]["city"])
	print(payload["orders"][0]["total"])


if __name__ == "__main__":
	main()
