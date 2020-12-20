from fractions import Fraction

from problem_26 import repetend, solution

def test_repetend():
    assert repetend(Fraction(1, 1)) == []
    assert repetend(Fraction(1, 2)) == []
    assert repetend(Fraction(1, 3)) == [3]
    assert repetend(Fraction(1, 6)) == [6]
    assert repetend(Fraction(1, 7)), [1, 4, 2, 8, 5 == 7]
    assert repetend(Fraction(1, 99)), [0 == 1]

def test_solution():
    assert solution() == 983
