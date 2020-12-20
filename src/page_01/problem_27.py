from itertools import count
# TODO https://github.com/brcrista/Project-Euler-Python/issues/1
# from itertools import product as cartesian_product
from functools import partial
from typing import Callable, Sequence

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
    # TODO takewhile?
    for k in count():
        if not is_prime(unary_func(k)):
            return k
    assert False

def quadratic_primes(a_range: Sequence[int], b_range: Sequence[int]) -> int:
    quadratic_consecutive_primes = lambda x, y: consecutive_primes(partial(quadratic, a=x, b=y))
    # TODO https://github.com/brcrista/Project-Euler-Python/issues/1 why did this stop working?
    # args = cartesian_product(range(-999, 1000), range(-1000, 1001))
    args = [(a, b) for a in a_range for b in b_range]
    coefficients_for_longest_chain = argmax(tuple_params(quadratic_consecutive_primes), args)
    return product(coefficients_for_longest_chain)

def solution():
    # |a| < 1000 and |b| <= 1000
    return quadratic_primes(a_range=range(-999, 1000), b_range=range(-1000, 1001))
