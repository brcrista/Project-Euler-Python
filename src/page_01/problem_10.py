"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from mathtools.number_theory import eratosthenes

def sum_of_primes_below(n: int) -> int:
    """The sum of all prime numbers less than a given natural number."""
    return sum(eratosthenes(n))

def solution():
    return sum_of_primes_below(2000000)
