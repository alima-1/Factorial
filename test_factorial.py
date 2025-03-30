import pytest
from factorial import factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(4) == 24
    assert factorial(5) == 120


def test_factorial_neg():
    with pytest.raises(ValueError):
        factorial(-5)


def test_factorial_str():
    with pytest.raises(TypeError):
        factorial("Lima")
