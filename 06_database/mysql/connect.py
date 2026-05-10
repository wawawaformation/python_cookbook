"""Connexion MySQL minimale."""

import os

from dotenv import load_dotenv

try:
	import pymysql
except ImportError as error:
	raise SystemExit("Installe PyMySQL avec: pip install PyMySQL") from error


def main() -> None:
	load_dotenv()

	connection = pymysql.connect(
		host=os.getenv("MYSQL_HOST", "127.0.0.1"),
		port=int(os.getenv("MYSQL_PORT", "3306")),
		user=os.getenv("MYSQL_USER", "cookbook"),
		password=os.getenv("MYSQL_PASSWORD", "cookbook"),
		database=os.getenv("MYSQL_DATABASE", "cookbook"),
	)

	try:
		print("Connexion MySQL OK")
	finally:
		connection.close()


if __name__ == "__main__":
	main()