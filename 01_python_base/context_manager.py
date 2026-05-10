"""Context manager personnalisé avec contextlib."""

from contextlib import contextmanager
from pathlib import Path


@contextmanager
def open_temp_file(file_path: Path):
	print("Ouverture du fichier")
	handle = file_path.open("w", encoding="utf-8")
	try:
		yield handle
	finally:
		handle.close()
		print("Fichier fermé")


def main() -> None:
	file_path = Path(__file__).with_name("demo_context_manager.txt")

	with open_temp_file(file_path) as handle:
		handle.write("ligne 1\n")
		handle.write("ligne 2\n")

	print(file_path.read_text(encoding="utf-8"))
	file_path.unlink(missing_ok=True)


if __name__ == "__main__":
	main()