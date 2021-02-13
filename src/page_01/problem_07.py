"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from itertools import count

from mathtools.number_theory import is_prime

def nth_prime(n: int) -> int:
    number_of_primes = 0
    for k in count(start=1):
        if is_prime(k):
            number_of_primes += 1
        if number_of_primes == n:
            return k
    assert False

def solution():
    return nth_prime(10001)
