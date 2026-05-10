"""Lambda, sorted, map et filter sur des cas simples."""


def main() -> None:
	prices = [19.99, 5.0, 12.5, 99.0]
	sorted_prices = sorted(prices, reverse=True)
	print(sorted_prices)

	users = [
		{"name": "Alice", "age": 32},
		{"name": "Bob", "age": 24},
		{"name": "Chloe", "age": 29},
	]
	sorted_users = sorted(users, key=lambda user: user["age"])
	print(sorted_users)

	numbers = [1, 2, 3, 4, 5, 6]
	doubled = list(map(lambda value: value * 2, numbers))
	even_numbers = list(filter(lambda value: value % 2 == 0, numbers))
	print(doubled)
	print(even_numbers)


if __name__ == "__main__":
	main()