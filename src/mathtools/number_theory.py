from itertools import chain
from math import floor, gcd, sqrt
from typing import List, Tuple

def assert_natural(n: int) -> None:
    """Raise a `ValueError` if `n` is not a natural number (starting with 0)."""
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'{n} is not a natural number')

def assert_positive(n: int) -> None:
    """Raise a `ValueError` if `n` is not a positive integer."""
    if not (isinstance(n, int) and n >= 1):
        raise ValueError(f'{n} is not a positive integer')

def divides(a: int, b: int) -> bool:
    """Whether `a` is a multiple of `b`."""
    return a % b == 0

def even(n: int) -> bool:
    """Whether an integer `n` is even."""
    return divides(n, 2)

def odd(n: int) -> bool:
    """Whether an integer `n` is odd."""
    return even(n + 1)

def factor_pairs(n: int) -> List[Tuple[int, int]]:
    """The pairs of factors of a positive integer `n`, computed using trial division."""
    assert_positive(n)
    return [(x, n // x) for x in range(1, floor(sqrt(n)) + 1) if divides(n, x)]

def factors(n: int) -> List[int]:
    """The factors of an integer `n`."""
    if n < 0:
        positive_factors = factors(-n)
        negative_factors = [-k for k in positive_factors]
        return list(reversed(negative_factors)) + positive_factors
    elif n == 0:
        return [0]
    else:
        return sorted(set(chain.from_iterable(factor_pairs(n))))

def proper_divisors(n: int) -> List[int]:
    """All divisors of a positive integer `n`, not including `n`."""
    return factors(n)[:-1]

def is_prime(n: int) -> bool:
    """Whether a number `n` is prime."""
    return n > 1 and factors(n) == [1, n]

def _prime_factorization(n: int) -> List[int]:
    if n == 1:
        return []
    else:
        first_prime = next(fac for fac in factors(n) if is_prime(fac))
        return [first_prime] + _prime_factorization(n // first_prime)

def prime_factorization(n: int) -> List[int]:
    """
    The prime factors of a natural number `n`, including duplicates.

    >>> prime_factorization(1)
    []
    >>> prime_factorization(2)
    [2]
    >>> prime_factorization(12)
    [2, 2, 3]
    """
    assert_positive(n)
    return _prime_factorization(n)

def eratosthenes(n: int) -> List[int]:
    """All primes less than a natural number `n`, computed with the Sieve of Eratosthenes."""
    assert_natural(n)
    maybe_prime = [False, False] + [True for k in range(2, n)]
    for i in range(2, floor(sqrt(n)) + 1):
        if maybe_prime[i]:
            for j in range(2 * i, n, i):
                maybe_prime[j] = False
    return [k for k in range(2, n) if maybe_prime[k]]

def lcm(a: int, b: int) -> int:
    """The least common multiple of `a` and `b`."""
    if a == 0 or b == 0:
        return 0
    else:
        return a * b // gcd(a, b)
