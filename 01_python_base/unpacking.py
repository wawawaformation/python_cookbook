"""Unpacking pratique avec listes, tuples et dictionnaires."""


def format_user(name: str, age: int, city: str) -> str:
	return f"{name} a {age} ans et habite {city}"


def main() -> None:
	first, second, *rest = [10, 20, 30, 40, 50]
	print(first)
	print(second)
	print(rest)

	coordinates = (48.8566, 2.3522)
	latitude, longitude = coordinates
	print(latitude, longitude)

	user_data = {"name": "David", "age": 35, "city": "Lyon"}
	print(format_user(**user_data))

	base_config = {"host": "localhost", "port": 8000}
	extra_config = {"debug": True}
	merged_config = {**base_config, **extra_config}
	print(merged_config)


if __name__ == "__main__":
	main()