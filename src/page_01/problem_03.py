from typing import Optional

from mathtools.number_theory import factors, is_prime

def largest_prime_factor(n: int) -> Optional[int]:
    return max(filter(is_prime, factors(n)), default=None)

def solution():
    return largest_prime_factor(600851475143)
