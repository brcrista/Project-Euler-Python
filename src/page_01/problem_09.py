"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""

from itertools import count

def pythagorean_triple(a: int, b: int, c: int) -> int:
    assert a < b < c
    return (a * a) + (b * b) == (c * c)

def special_pythagorean_triple() -> int:
    """The product of the Pythagorean triple whose sum equals 1000."""
    return next(a * b * c
        for c in count(3)
        for b in range(2, c)
        for a in range(1, b)
        if pythagorean_triple(a, b, c) and a + b + c == 1000)

solution = special_pythagorean_triple
