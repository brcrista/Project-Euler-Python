"""
Starting with the number 1 and moving to the right in a clockwise direction, a 5×5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

The sum of the numbers on the diagonals is 21 + 7 + 1 + 3 + 13 + 17 + 5 + 9 + 25 = 101.

What is the sum of the numbers on the diagonals in a 1001×1001 spiral formed in the same way?
"""

from typing import Iterator

def numbers_on_spiral_diagonals(n: int) -> Iterator[int]:
    k = 1
    yield k

    skip = 2
    end = n * n
    while k < end:
        for _ in range(0, 4):
            k += skip
            yield k
        skip += 2

def sum_of_number_spiral_diagonals(n: int) -> int:
    """
    The sum of the numbers lying on the diagonals of a "number spiral"
    of the numbers `1, ..., n * n`.
    """
    return sum(numbers_on_spiral_diagonals(n))

def solution():
    return sum_of_number_spiral_diagonals(1001)
