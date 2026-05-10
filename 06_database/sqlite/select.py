"""Lire des lignes dans SQLite."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	with sqlite3.connect(DB_PATH) as connection:
		connection.row_factory = sqlite3.Row
		rows = connection.execute(
			"SELECT id, name, email FROM users ORDER BY id"
		).fetchall()

		for row in rows:
			print(dict(row))


if __name__ == "__main__":
	main()
