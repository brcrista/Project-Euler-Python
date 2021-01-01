"""
Do discrete math in Python.
"""

from functools import reduce
from operator import mul
from typing import Iterable

from .number_theory import divides

__all__ = [
    'combinatorics',
    'functional',
    'number_theory'
]

def product(xs: Iterable[int]) -> int:
    """The product of all numbers in an `Iterable`."""
    return reduce(mul, xs, 1)

def _sum_naturals(n: int) -> int:
    # The nth partial sum of 1 + 2 + 3 + ...
    # Note that the numerator will always be even
    # since either `n` or `n + 1` must be even.
    return n * (n + 1) // 2

def sum_range(start: int, stop: int=None, step: int=1) -> int:
    """
    Sum a range of values [0 .. n - 1] in constant time.
    Functionally equivalent to `sum(range(start, stop, step))`
    """
    if step == 0:
        raise ValueError("sum_range() arg 3 must not be zero")

    if stop is None:
        # If there's only one argument, treat it as `stop`, not `start`.
        stop = start
        start = 0

    if stop < start:
        return 0

    if step == 1:
        # This is equal to 1 + 2 + 3 + ... plus some offset.
        # Rewrite as 0 + start + 1 + start + 2 + start + ...
        # Note that `_sum_naturals` includes its upper bound while this does not.
        return (stop - start) * start + _sum_naturals(stop - start - 1)
    else:
        # Scale down the series by `step` and compute as the sum of consecutive integers.
        new_start = start // step
        new_stop = stop // step
        if not divides(stop, step):
            # The last number in the range got rounded off by `//`.
            # Add one to re-include the end of the range.
            new_stop += 1

        return step * sum_range(new_start, new_stop, step=1)
