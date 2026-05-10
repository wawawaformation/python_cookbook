"""Configuration minimale du logging."""

import logging


def main() -> None:
	logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

	logging.info("Application started")
	logging.warning("This is only a cookbook example")


if __name__ == "__main__":
	main()
