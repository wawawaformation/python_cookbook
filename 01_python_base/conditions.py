"""if, elif, else et vérifications de vérité."""


def shipping_price(country: str, total: float) -> float:
	if total >= 100:
		return 0.0
	if country == "FR":
		return 4.90
	if country in {"BE", "DE", "ES"}:
		return 8.90
	return 14.90


def main() -> None:
	cart = ["keyboard", "mouse"]
	if cart:
		print("Cart is not empty")

	print(shipping_price("FR", 50))
	print(shipping_price("DE", 20))
	print(shipping_price("FR", 120))


if __name__ == "__main__":
	main()
