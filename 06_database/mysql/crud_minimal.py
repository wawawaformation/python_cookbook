"""Exemple CRUD MySQL dans un seul script."""

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
		autocommit=True,
	)

	try:
		with connection.cursor() as cursor:
			cursor.execute("DROP TABLE IF EXISTS users")
			cursor.execute(
				"""
				CREATE TABLE users (
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
			user_id = cursor.lastrowid

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
	finally:
		connection.close()


if __name__ == "__main__":
	main()