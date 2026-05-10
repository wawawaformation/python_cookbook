"""Insérer une ligne dans SQLite."""

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

		cursor = connection.execute(
			"INSERT INTO users (name, email) VALUES (?, ?)",
			("Alice", "alice@example.com"),
		)

	print(f"Utilisateur inséré avec l'id {cursor.lastrowid}")


if __name__ == "__main__":
	main()
