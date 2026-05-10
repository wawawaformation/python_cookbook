"""Convertir une chaîne JSON en objets Python."""

import json


def main() -> None:
	payload = '{"name": "David", "skills": ["php", "python"], "active": true}'
	data = json.loads(payload)

	print(data)
	print(data["name"])
	print(data["skills"][1])


if __name__ == "__main__":
	main()
