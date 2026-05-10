"""Lire et écrire des fichiers avec pathlib."""

from pathlib import Path


def main() -> None:
	file_path = Path(__file__).with_name("notes.txt")
	file_path.write_text("Python is concise.\nPHP devs adapt fast.\n", encoding="utf-8")

	content = file_path.read_text(encoding="utf-8")
	print(content.strip())


if __name__ == "__main__":
	main()
