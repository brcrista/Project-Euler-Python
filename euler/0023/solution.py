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
