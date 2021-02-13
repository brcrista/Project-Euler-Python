"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from typing import List

from mathtools.number_theory import proper_divisors

def is_abundant(n: int) -> bool:
    return sum(proper_divisors(n)) > n

def abundant_numbers_less_than(n: int) -> List[int]:
    """All abundant numbers less than `n`."""
    return [i for i in range(1, n) if is_abundant(i)]

def sums_from(addends: List[int]) -> List[int]:
    """All numbers that are the sum of two elements from the list."""
    return [addends[i] + addends[j]
        for i in range(0, len(addends))
        for j in range(i, len(addends))]

def non_abundant_sums(n: int) -> int:
    """The sum of all numbers less than `n` that are not the sum of two abundant numbers."""
    abundants = abundant_numbers_less_than(n)
    sums_of_abundants = {i for i in sums_from(abundants) if i < n}
    return sum(i for i in range(1, n) if i not in sums_of_abundants)

# All integers greater than or equal to this can be written as the sum of two abundant numbers
LOWER_LIMIT_OF_ABUNDANT_SUMS = 28123 + 1

def solution():
    return non_abundant_sums(LOWER_LIMIT_OF_ABUNDANT_SUMS)
