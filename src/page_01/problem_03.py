"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from typing import Optional

from mathtools.number_theory import factors, is_prime

def largest_prime_factor(n: int) -> Optional[int]:
    return max(filter(is_prime, factors(n)), default=None)

def solution():
    return largest_prime_factor(600851475143)
