from functools import reduce
from mathtools.number_theory import lcm

def smallest_multiple(n: int) -> int:
    """The smallest positive number divisible by all integers in [1, `n`]."""
    return reduce(lcm, range(1, n + 1))

def solution():
    return smallest_multiple(20)
