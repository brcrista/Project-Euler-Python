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
