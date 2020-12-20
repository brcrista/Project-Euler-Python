"""
Do discrete math in Python.
"""

from functools import reduce
from operator import mul
from typing import overload, Any, Iterable, Union

__all__ = [
    'combinatorics',
    'functional',
    'iterable',
    'number_theory'
]

def product(xs: Iterable[int]) -> int:
    """The product of all numbers in an `Iterable`."""
    return reduce(mul, xs, 1)
