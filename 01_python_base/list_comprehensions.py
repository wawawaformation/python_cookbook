"""Compréhensions de listes, sets et dictionnaires."""


def main() -> None:
	numbers = [1, 2, 3, 4, 5, 6]

	# Remplace souvent une boucle + append.
	squares = [number * number for number in numbers]
	even_squares = [number * number for number in numbers if number % 2 == 0]
	unique_lengths = {len(word) for word in ["chat", "chien", "chat", "python"]}
	users_by_id = {user["id"]: user["name"] for user in [
		{"id": 1, "name": "Alice"},
		{"id": 2, "name": "Bob"},
	]}

	print(squares)
	print(even_squares)
	print(unique_lengths)
	print(users_by_id)


if __name__ == "__main__":
	main()