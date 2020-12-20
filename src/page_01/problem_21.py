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
