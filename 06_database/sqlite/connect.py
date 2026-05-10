"""Connexion SQLite minimale."""

from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("sqlite_demo.db")


def main() -> None:
	connection = sqlite3.connect(DB_PATH)
	try:
		print("Connexion SQLite OK")
		print(f"Fichier : {DB_PATH}")
	finally:
		connection.close()


if __name__ == "__main__":
	main()
