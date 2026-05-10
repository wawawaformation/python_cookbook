"""Cookbook minimal avec unittest."""

import unittest

from math_utils import add, divide, is_adult


class TestMathUtils(unittest.TestCase):
	def test_add(self) -> None:
		self.assertEqual(add(2, 3), 5)

	def test_divide(self) -> None:
		self.assertEqual(divide(10, 2), 5)

	def test_divide_by_zero(self) -> None:
		with self.assertRaises(ValueError):
			divide(10, 0)

	def test_is_adult(self) -> None:
		self.assertTrue(is_adult(18))
		self.assertFalse(is_adult(17))


if __name__ == "__main__":
	unittest.main()