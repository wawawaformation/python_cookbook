"""Lire des variables d'environnement depuis .env."""

import os
from pathlib import Path

from dotenv import load_dotenv


def main() -> None:
	env_path = Path(__file__).resolve().parents[1] / ".env"
	load_dotenv(env_path)

	config = {
		"APP_NAME": os.getenv("APP_NAME", "python-cookbook"),
		"APP_ENV": os.getenv("APP_ENV", "dev"),
		"APP_DEBUG": os.getenv("APP_DEBUG", "false"),
	}
	print(config)


if __name__ == "__main__":
	main()
