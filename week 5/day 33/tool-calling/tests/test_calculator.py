import pytest

from app.tools.calculator import calculator


def test_addition():
    result = calculator(10, 5, "add")

    assert result == 15


def test_subtraction():
    result = calculator(10, 5, "subtract")

    assert result == 5


def test_multiplication():
    result = calculator(10, 5, "multiply")

    assert result == 50


def test_division():
    result = calculator(10, 5, "divide")

    assert result == 2


def test_decimal_multiplication():
    result = calculator(2.5, 4, "multiply")

    assert result == 10


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculator(10, 0, "divide")


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculator(10, 5, "power")