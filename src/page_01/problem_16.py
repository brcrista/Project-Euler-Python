"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from mathtools.number_theory import assert_natural

def digit_sum(n: int) -> int:
    """The sum of the digits of the natural number `n`."""
    assert_natural(n)
    return sum(int(c) for c in str(n))

def solution():
    return digit_sum(2 ** 1000)
