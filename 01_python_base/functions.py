"""Fonctions, valeurs par défaut et déballage de tuple."""


def greet(name: str, prefix: str = "Hello") -> str:
	return f"{prefix} {name}"


def prices_with_tax(price_ht: float, tax_rate: float = 0.2) -> tuple[float, float]:
	tax_amount = price_ht * tax_rate
	total_ttc = price_ht + tax_amount
	return tax_amount, total_ttc


def main() -> None:
	print(greet("David"))
	print(greet("David", prefix="Welcome"))

	tax_amount, total_ttc = prices_with_tax(100)
	print(f"tax={tax_amount:.2f} total={total_ttc:.2f}")


if __name__ == "__main__":
	main()
