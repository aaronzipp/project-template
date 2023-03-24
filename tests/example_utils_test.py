from hypothesis import given
from hypothesis.strategies import integers

from src.example_utils import sum


@given(integers(), integers())
def test_sum_hypothesis(a, b):
    """Docstring for test_sum_hypothesis function."""
    assert sum(a, b) == a + b


def test_sum():
    """Docstring for test_sum function."""
    assert sum(1, 2) == 3
