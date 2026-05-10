"""Lire les arguments de ligne de commande avec argparse."""

import argparse


def main() -> None:
	parser = argparse.ArgumentParser(description="Minimal CLI example")
	parser.add_argument("name", help="User name")
	parser.add_argument("--admin", action="store_true", help="Flag admin mode")
	args = parser.parse_args()

	print({"name": args.name, "admin": args.admin})


if __name__ == "__main__":
	main()
