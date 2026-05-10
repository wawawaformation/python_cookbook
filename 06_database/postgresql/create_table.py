"""Créer une table PostgreSQL."""

import os

from dotenv import load_dotenv

try:
	import psycopg
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
	) as connection:
		with connection.cursor() as cursor:
			cursor.execute(
				"""
				CREATE TABLE IF NOT EXISTS users (
					id SERIAL PRIMARY KEY,
					name VARCHAR(100) NOT NULL,
					email VARCHAR(255) NOT NULL UNIQUE
				)
				"""
			)

	print("Table users créée ou déjà présente")


if __name__ == "__main__":
	main()
