"""Supprimer une ligne SQLite."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	with sqlite3.connect(DB_PATH) as connection:
		cursor = connection.execute(
			"DELETE FROM users WHERE email = ?",
			("alice.updated@example.com",),
		)

	print(f"Lignes supprimées : {cursor.rowcount}")


if __name__ == "__main__":
	main()
