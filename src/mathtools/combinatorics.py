from itertools import accumulate, count
from math import factorial
from operator import add
from typing import Callable, Iterator, List, TypeVar

from . import product

_T = TypeVar('_T')

def recurrence(start: List[_T], func: Callable[..., _T]) -> Iterator[_T]:
    """
    Return an `Iterator` beginning with `start` where each element is created
    by applying `func` to the previous `len(start)` elements.

    `func()` should take `len(start)` parameters of type `_T`.

    >>> from core.iterable import take
    >>> it = recurrence([1], lambda x: x * 2)
    >>> take(5, it)
    [1, 2, 4, 8, 16]
    """
    yield from start

    window = start
    value = func(*window)
    while True:
        yield value
        window.append(value)
        window = window[1:]
        value = func(*window)

def fibonacci_numbers() -> Iterator[int]:
    """
    The infinite sequence of Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, ...

    >>> import itertools
    >>> fib = fibonacci_numbers()
    >>> list(itertools.islice(fib, 7))
    [0, 1, 1, 2, 3, 5, 8]
    """
    return recurrence([0, 1], add)

def triangle_numbers() -> Iterator[int]:
    """The infinite sequence of triangle numbers, starting with 0 as the 0th triangle number."""
    return accumulate(count(0))

def binomial_coefficient(n: int, k: int) -> int:
    """
    The binomial coefficient "n choose k."

    >>> binomial_coefficient(4, 3)
    4
    >>> binomial_coefficient(10, 6)
    210
    """
    return product((n + 1 - i) for i in range(1, k + 1)) // factorial(k)