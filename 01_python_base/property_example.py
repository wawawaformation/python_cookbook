"""Proprietes avec validation via @property."""


class Product:
	def __init__(self, name: str, price: float) -> None:
		self.name = name
		self.price = price

	@property
	def price(self) -> float:
		return self._price

	@price.setter
	def price(self, value: float) -> None:
		if value < 0:
			raise ValueError("Le prix ne peut pas etre negatif")
		self._price = round(value, 2)

	@property
	def price_with_tax(self) -> float:
		return round(self.price * 1.2, 2)


def main() -> None:
	product = Product("Clavier", 49.999)
	print(product.price)
	print(product.price_with_tax)

	product.price = 59.5
	print(product.price)

	try:
		product.price = -10
	except ValueError as error:
		print(f"Erreur: {error}")


if __name__ == "__main__":
	main()