"""Lire du JSON depuis un fichier."""

import json
from pathlib import Path


def main() -> None:
	file_path = Path(__file__).with_name("demo_read.json")
	file_path.write_text('{"name": "David", "city": "Lyon"}', encoding="utf-8")

	data = json.loads(file_path.read_text(encoding="utf-8"))
	print(data)
	print(data["city"])


if __name__ == "__main__":
	main()
