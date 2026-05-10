"""Cookbook minimal avec pytest."""

import pytest

from math_utils import add, divide, is_adult


def test_add() -> None:
	assert add(4, 6) == 10


def test_divide() -> None:
	assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
	with pytest.raises(ValueError, match="0"):
		divide(5, 0)


@pytest.mark.parametrize(
	("age", "expected"),
	[
		(16, False),
		(18, True),
		(30, True),
	],
)
def test_is_adult(age: int, expected: bool) -> None:
	assert is_adult(age) is expected