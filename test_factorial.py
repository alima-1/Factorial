import pytest
from factorial import factorial

def test_factorial_neg():
    with pytest.raises(ValueError):
        factorial(-5)
