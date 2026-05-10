"""Lire des lignes dans PostgreSQL."""

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
			cursor.execute("SELECT id, name, email FROM users ORDER BY id")
			for row in cursor.fetchall():
				print(row)


if __name__ == "__main__":
	main()
