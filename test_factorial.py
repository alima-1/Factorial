import pytest
from factorial import factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_neg():
    with pytest.raises(ValueError):
        factorial(-5)
