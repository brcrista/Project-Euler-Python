"""
Euler discovered the remarkable quadratic formula

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n = 40, 40^2 + 40 + 41 = 40 × (40 + 1) + 41 is divisible by 41.
(Obviously, when n = 41, 41^2 + 41 + 41 is divisible by 41.)

The incredible formula

    n^2 - 79 × n + 1601

was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form

    n^2 + a × n + b where |a| < 1000 and |b|≤ 1000

    where |n| is the absolute value of n,
    e.g. and |11| = |11| and |-4| = |4|

Find the product of the coefficients a and b for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

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
