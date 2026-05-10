"""Lire des lignes dans MySQL."""

import os

from dotenv import load_dotenv

try:
	import pymysql
	from pymysql.cursors import DictCursor
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
		cursorclass=DictCursor,
	)

	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT id, name, email FROM users ORDER BY id")
			for row in cursor.fetchall():
				print(row)
	finally:
		connection.close()


if __name__ == "__main__":
	main()