"""Connexion PostgreSQL minimale."""

import os

from dotenv import load_dotenv

try:
	import psycopg
except ImportError as error:
	raise SystemExit("Installe psycopg avec: pip install 'psycopg[binary]' ") from error


def main() -> None:
	load_dotenv()

	connection = psycopg.connect(
		host=os.getenv("PGHOST", "127.0.0.1"),
		port=os.getenv("PGPORT", "5432"),
		dbname=os.getenv("PGDATABASE", "cookbook"),
		user=os.getenv("PGUSER", "cookbook"),
		password=os.getenv("PGPASSWORD", "cookbook"),
	)

	try:
		print("Connexion PostgreSQL OK")
	finally:
		connection.close()


if __name__ == "__main__":
	main()
