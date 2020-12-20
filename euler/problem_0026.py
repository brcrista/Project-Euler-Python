from fractions import Fraction
from typing import Iterator, List, Tuple

from mathtools.functional import argmax

def long_division(dividend: int, divisor: int) -> Iterator[Tuple[int, int]]:
    """
    An iterator returning results from the long division algorithm.
    Each result is a pair of `(quotient, remainder)`.
    The first result from the iterator is the result of the integer division.
    Each subsequent result is from the subzero steps of the division, if there was
    a remainder from the integer division.
    Therefore, if `dividend` is divisble by `divisor`, the iterator will yield only
    one pair of `(quotient, 0)`.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    yield quotient, remainder
    while remainder != 0:
        remainder *= 10
        quotient = remainder // divisor
        remainder %= divisor
        yield quotient, remainder

def repetend(fraction: Fraction) -> List[int]:
    """
    The repetend of `fraction`.
    If `fraction` is not a repeating decimal in base 10, returns an empty list.
    """
    division_steps = []
    long_division_iterator = long_division(fraction.numerator, fraction.denominator)
    next(long_division_iterator) # ignore integral part

    for div_step in long_division_iterator:
        if div_step in division_steps:
            # repetend is the sequence of digits seen since the first appearance of `remainder`
            start = division_steps.index(div_step)
            return [q for q, _ in division_steps[start:]]
        else:
            division_steps.append(div_step)
    # if the `for` loop exits, division has terminated and `fraction` is not a repeating decimal
    return []

def longest_reciprocal_repetend(n: int) -> int:
    """
    The positive integer less than `n` whose reciprocal has the longest repetend
    in base 10 representation.
    """
    return argmax(lambda x: len(repetend(Fraction(1, x))), range(1, n))

def solution():
    return longest_reciprocal_repetend(1000)
