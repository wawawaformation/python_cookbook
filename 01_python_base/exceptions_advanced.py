"""Exceptions avancées avec exception chaining."""


def parse_port(value: str) -> int:
	try:
		port = int(value)
	except ValueError as error:
		raise ValueError(f"Port invalide: {value}") from error

	if port <= 0:
		raise ValueError("Le port doit etre positif")

	return port


def main() -> None:
	for value in ["8000", "abc", "-1"]:
		try:
			print(parse_port(value))
		except ValueError as error:
			print(f"Erreur: {error}")
			if error.__cause__ is not None:
				print(f"Cause initiale: {error.__cause__}")


if __name__ == "__main__":
	main()