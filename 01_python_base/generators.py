"""Générateurs pour produire des valeurs à la demande."""


def fibonacci(limit: int):
	a, b = 0, 1
	count = 0
	while count < limit:
		yield a
		a, b = b, a + b
		count += 1


def main() -> None:
	values = list(fibonacci(7))
	print(values)
	print(sum(fibonacci(7)))


if __name__ == "__main__":
	main()