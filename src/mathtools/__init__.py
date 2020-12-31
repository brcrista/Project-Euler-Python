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

def sum_range(start: int, end: int=None, step: int=1) -> int:
    """
    Sum a range of values in constant time.
    Functionally equivalent to `sum(range(start, end, step))`
    """
    # if end is None:
    #     # If there's only one argument, treat it as the end.
    #     end = start
    #     start = None
    # TODO
    return sum(range(start, end, step))