"""Exemple CRUD PostgreSQL dans un seul script."""

import os

from dotenv import load_dotenv

try:
	import psycopg
	from psycopg.rows import dict_row
except ImportError as error:
	raise SystemExit("Installe psycopg avec: pip install 'psycopg[binary]' ") from error


def main() -> None:
	load_dotenv()

	with psycopg.connect(
		host=os.getenv("PGHOST", "127.0.0.1"),
		port=os.getenv("PGPORT", "5432"),
		dbname=os.getenv("PGDATABASE", "cookbook"),
		user=os.getenv("PGUSER", "cookbook"),
		password=os.getenv("PGPASSWORD", "cookbook"),
		row_factory=dict_row,
	) as connection:
		with connection.cursor() as cursor:
			cursor.execute("DROP TABLE IF EXISTS users")
			cursor.execute(
				"""
				CREATE TABLE users (
					id SERIAL PRIMARY KEY,
					name VARCHAR(100) NOT NULL,
					email VARCHAR(255) NOT NULL UNIQUE
				)
				"""
			)

			cursor.execute(
				"INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
				("Alice", "alice@example.com"),
			)
			user_id = cursor.fetchone()[0]

			cursor.execute(
				"UPDATE users SET email = %s WHERE id = %s",
				("alice.updated@example.com", user_id),
			)

			cursor.execute(
				"SELECT id, name, email FROM users WHERE id = %s",
				(user_id,),
			)
			print("Après update:", cursor.fetchone())

			cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
			cursor.execute("SELECT COUNT(*) AS total FROM users")
			print("Utilisateurs restants:", cursor.fetchone()["total"])


if __name__ == "__main__":
	main()
