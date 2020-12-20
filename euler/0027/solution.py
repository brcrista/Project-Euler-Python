from itertools import count
# TODO 1 from itertools import product as cartesian_product
from functools import partial
from typing import Callable

from mathtools import product
from mathtools.functional import argmax, tuple_params
from mathtools.number_theory import is_prime

def quadratic(n: int, a: int, b: int) -> int:
    return (n * n) + (a * n) + b

def consecutive_primes(unary_func: Callable[[int], int]) -> int:
    """
    The number of consecutive prime outputs produced by `unary_func`
    from inputs starting with 0.
    """
    for k in count():
        if not is_prime(unary_func(k)):
            return k

def quadratic_primes() -> int:
    f = lambda x, y: consecutive_primes(partial(quadratic, a=x, b=y))
    # TODO 1 why did this stop working?
    # args = cartesian_product(range(-999, 1000), range(-1000, 1001))
    args = [(a, b) for a in range(-999, 1000) for b in range(-1000, 1001)]
    return product(argmax(tuple_params(f), args))

solution = quadratic_primes
