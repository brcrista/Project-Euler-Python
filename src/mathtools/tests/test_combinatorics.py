from typing import cast, List

from core.iterable import take
from mathtools.combinatorics import binomial_coefficient, recurrence, triangle_numbers

def test_recurrence() -> None:
    it0 = recurrence(cast(List[int], []), lambda: 100)
    assert take(3, it0) == [100, 100, 100]

    # Mypy seems to struggle with generics + lambdas
    def plus1(x: int) -> int:
        return x + 1

    it1 = recurrence([1], plus1)
    assert take(5, it1) == [1, 2, 3, 4, 5]

    def concat(x: str, y: str, z: str) -> str:
        return x + y + z

    it2 = recurrence(['a', 'b', 'c'], concat)
    assert take(5, it2) == ['a', 'b', 'c', 'abc', 'bcabc']

def test_triangle_numbers() -> None:
    assert list(take(11, triangle_numbers())) == [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

def test_binomial_coefficient() -> None:
    assert binomial_coefficient(1, 0) == 1
    assert binomial_coefficient(1, 1) == 1
    assert binomial_coefficient(10, 10) == 1
    assert binomial_coefficient(10, 1) == 10
    assert binomial_coefficient(4, 2) == 6

    assert binomial_coefficient(6, 0) == 1
    assert binomial_coefficient(6, 1) == 6
    assert binomial_coefficient(6, 2) == 15
    assert binomial_coefficient(6, 3) == 20
    assert binomial_coefficient(6, 4) == 15
    assert binomial_coefficient(6, 5) == 6
    assert binomial_coefficient(6, 6) == 1
