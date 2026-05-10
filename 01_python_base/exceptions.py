"""Lever et intercepter des exceptions."""


def divide(a: float, b: float) -> float:
	if b == 0:
		raise ValueError("b must not be zero")
	return a / b


def main() -> None:
	try:
		print(divide(10, 2))
		print(divide(10, 0))
	except ValueError as exc:
		print(f"Handled error: {exc}")


if __name__ == "__main__":
	main()
