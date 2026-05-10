"""Mettre à jour une ligne SQLite."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	with sqlite3.connect(DB_PATH) as connection:
		cursor = connection.execute(
			"UPDATE users SET email = ? WHERE name = ?",
			("alice.updated@example.com", "Alice"),
		)

	print(f"Lignes mises à jour : {cursor.rowcount}")


if __name__ == "__main__":
	main()
