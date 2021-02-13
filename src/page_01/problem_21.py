"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from typing import Iterator, List

from mathtools.number_theory import proper_divisors

def sums_of_proper_divisors_less_than(n: int) -> Iterator[int]:
    for i in range(1, n):
        yield sum(proper_divisors(i))

def are_amicable(a: int, b: int, sums_of_proper_divisors: List[int]) -> bool:
    return a != b and sums_of_proper_divisors[a] == b and sums_of_proper_divisors[b] == a

def sum_of_amicable_numbers_less_than(n: int) -> int:
    sums_of_proper_divisors = [0] + list(sums_of_proper_divisors_less_than(n))
    return sum(i + j
        for i in range(1, n)
        for j in range(i + 1, n)
        if are_amicable(i, j, sums_of_proper_divisors))

def solution():
    return sum_of_amicable_numbers_less_than(10000)
