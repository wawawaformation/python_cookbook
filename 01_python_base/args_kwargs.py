"""Utiliser *args et **kwargs pour des fonctions flexibles."""


def sum_all(*numbers: int) -> int:
	return sum(numbers)


def build_user(**fields: str) -> dict[str, str]:
	return fields


def print_invoice(customer: str, *items: str, currency: str = "EUR", **meta: str) -> None:
	print(f"Client: {customer}")
	print(f"Articles: {items}")
	print(f"Devise: {currency}")
	print(f"Meta: {meta}")


def main() -> None:
	print(sum_all(10, 20, 30))
	print(build_user(name="Alice", email="alice@example.com"))
	print_invoice(
		"David",
		"clavier",
		"souris",
		currency="EUR",
		status="paid",
		country="FR",
	)


if __name__ == "__main__":
	main()