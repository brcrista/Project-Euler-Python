from typing import cast, List

from mathtools.iterable import take
from mathtools.combinatorics import binomial_coefficient, recurrence

def test_recurrence() -> None:
    it0 = recurrence(cast(List[int], []), lambda: 100)
    assert take(3, it0) == [100, 100, 100]

    # Mypy seems to struggle with generics + lambdas
    def plus1(x: int) -> int:
        return x + 1

    it1 = recurrence([1], plus1)
    # it1 = recurrence([1], lambda x: x + 1)
    assert take(5, it1) == [1, 2, 3, 4, 5]

    def concat(x: str, y: str, z: str) -> str:
        return x + y + z

    it2 = recurrence(['a', 'b', 'c'], concat)
    # it2 = recurrence(['a', 'b', 'c'], lambda x, y, z: x + y + z)
    assert take(5, it2) == ['a', 'b', 'c', 'abc', 'bcabc']

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
