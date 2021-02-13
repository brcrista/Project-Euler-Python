"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

from mathtools.number_theory import lcm

def smallest_multiple(n: int) -> int:
    """The smallest positive number divisible by all integers in [1, `n`]."""
    return reduce(lcm, range(1, n + 1))

def solution():
    return smallest_multiple(20)
