"""Créer une table SQLite."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	with sqlite3.connect(DB_PATH) as connection:
		connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS users (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				email TEXT NOT NULL UNIQUE
			)
			"""
		)

	print("Table users créée ou déjà présente")


if __name__ == "__main__":
	main()
