"""Zip, enumerate et itertools sur un exemple concret."""

from itertools import pairwise


def main() -> None:
	products = ["stylo", "cahier", "souris"]
	prices = [1.5, 3.2, 24.9]

	for index, product in enumerate(products, start=1):
		print(index, product)

	for product, price in zip(products, prices, strict=True):
		print(f"{product}: {price} EUR")

	temperatures = [18, 20, 19, 23]
	deltas = [current - previous for previous, current in pairwise(temperatures)]
	print(deltas)


if __name__ == "__main__":
	main()