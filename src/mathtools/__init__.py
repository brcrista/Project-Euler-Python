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

#pylint: disable=unused-argument,function-redefined
@overload
def product(xs: Iterable[int]) -> int:
    pass

@overload
def product(xs: Iterable[float]) -> float:
    pass

def product(xs: Iterable[Union[int, float]]) -> Union[int, float]:
    """The product of all numbers in an `Iterable`."""
    return reduce(mul, xs, 1)
#pylint: enable=unused-argument,function-redefined
