"""Écrire un dict Python au format JSON."""

import json
from pathlib import Path


def main() -> None:
	payload = {
		"name": "David",
		"stack": ["php", "python", "postgresql"],
		"available": True,
	}

	file_path = Path(__file__).with_name("demo_write.json")
	file_path.write_text(
		json.dumps(payload, indent=2, ensure_ascii=False),
		encoding="utf-8",
	)

	print(file_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
	main()
