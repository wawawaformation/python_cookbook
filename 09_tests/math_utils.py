"""Fonctions simples pour illustrer des tests."""


def add(a: int, b: int) -> int:
	return a + b


def divide(a: float, b: float) -> float:
	if b == 0:
		raise ValueError("b ne doit pas valoir 0")
	return a / b


def is_adult(age: int) -> bool:
	return age >= 18