"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""

from itertools import count
from typing import Iterator, Tuple

from mathtools import product

def is_pythagorean(a: int, b: int, c: int) -> bool:
    # Using * is about 7x faster than using **
    return (a * a) + (b * b) == (c * c)

pythagorean_triples = (
    (a, b, c)
    for c in count(3)
    for b in range(2, c)
    for a in range(1, b)
    if is_pythagorean(a, b, c)
)

def pythagorean_sum_equals(n: int) -> Iterator[Tuple[int, int, int]]:
    """The Pythagorean triples whose sum equals `n`.."""
    return filter(lambda xs: sum(xs) == 1000, pythagorean_triples)

def solution() -> int:
    return product(next(pythagorean_sum_equals(1000)))