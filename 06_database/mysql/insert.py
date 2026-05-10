"""Insérer une ligne dans MySQL."""

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
		autocommit=True,
	)

	try:
		with connection.cursor() as cursor:
			cursor.execute(
				"""
				CREATE TABLE IF NOT EXISTS users (
					id INT AUTO_INCREMENT PRIMARY KEY,
					name VARCHAR(100) NOT NULL,
					email VARCHAR(255) NOT NULL UNIQUE
				)
				"""
			)
			cursor.execute(
				"INSERT INTO users (name, email) VALUES (%s, %s)",
				("Alice", "alice@example.com"),
			)
			print(f"Utilisateur inséré avec l'id {cursor.lastrowid}")
	finally:
		connection.close()


if __name__ == "__main__":
	main()