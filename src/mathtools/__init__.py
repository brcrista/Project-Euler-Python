"""
Do discrete math in Python.
"""

from functools import reduce
from operator import mul
from typing import Iterable

__all__ = [
    'combinatorics',
    'functional',
    'number_theory'
]

def product(xs: Iterable[int]) -> int:
    """The product of all numbers in an `Iterable`."""
    return reduce(mul, xs, 1)

def sum_range(start: int, stop: int=None, step: int=1) -> int:
    """
    Sum a range of values in constant time.
    Functionally equivalent to `sum(range(start, stop, step))`
    """
    if step == 0:
        raise ValueError("sum_range() arg 3 must not be zero")
    if stop is None:
        # If there's only one argument, treat it as `stop`, not `start`.
        stop = start
        start = 0
    return sum(range(start, stop, step))