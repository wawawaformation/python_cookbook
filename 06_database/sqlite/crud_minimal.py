"""Exemple CRUD complet SQLite dans un seul script."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	with sqlite3.connect(DB_PATH) as connection:
		connection.row_factory = sqlite3.Row
		connection.execute("DROP TABLE IF EXISTS users")
		connection.execute(
			"""
			CREATE TABLE users (
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
		user_id = cursor.lastrowid

		connection.execute(
			"UPDATE users SET email = ? WHERE id = ?",
			("alice.updated@example.com", user_id),
		)

		row = connection.execute(
			"SELECT id, name, email FROM users WHERE id = ?",
			(user_id,),
		).fetchone()
		print("Après update:", dict(row) if row else None)

		connection.execute("DELETE FROM users WHERE id = ?", (user_id,))

		remaining = connection.execute("SELECT COUNT(*) FROM users").fetchone()[0]
		print(f"Utilisateurs restants : {remaining}")


if __name__ == "__main__":
	main()
