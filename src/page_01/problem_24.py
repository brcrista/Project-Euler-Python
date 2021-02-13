"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations
from typing import Iterable, Optional

def digits_to_int(digits: Iterable[int]) -> int:
    return int(''.join(map(str, digits)))

def nth_lexicographic_permutation(elements: Iterable[int], n: int) -> Optional[int]:
    """
    Select the `n`th permutation from the lexicographic ordering of the permutations of `elements`.
    """
    for i, p in enumerate(permutations(elements)):
        if i == n - 1:
            return digits_to_int(p)
    return None

def solution():
    return nth_lexicographic_permutation(range(0, 10), 1000000)
