"""Imports depuis la bibliothèque standard."""

from datetime import datetime
from pathlib import Path


def main() -> None:
	now = datetime.now()
	current_dir = Path(__file__).resolve().parent

	print(now.strftime("%Y-%m-%d %H:%M:%S"))
	print(current_dir)


if __name__ == "__main__":
	main()
