"""
The following iterative sequence is defined for the set of positive integers:

n → n / 2     (n is even)
n → 3 × n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (the Collatz conjecture), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from typing import Dict, List

from mathtools.number_theory import assert_positive, even

def half_or_triple_plus_one(n: int) -> int:
    """"The function defining the recurrence for the Collatz sequence."""
    assert_positive(n)
    if even(n):
        return n // 2
    else:
        return 3 * n + 1

collatz_memo: Dict[int, List[int]] = {}

def collatz_sequence(n: int) -> List[int]:
    """
    The Collatz sequence beginning with `n`.

    Results are memoized.
    """
    if n in collatz_memo:
        return collatz_memo[n]
    elif n == 1:
        return [1]
    else:
        result = [n] + collatz_sequence(half_or_triple_plus_one(n))
        collatz_memo[n] = result
        return result

class CollatzRecord:
    def __init__(self, seed):
        self.seed = seed
        self.length_of_sequence = len(collatz_sequence(seed))

def longest_collatz_sequence(n: int) -> int:
    """The seed value between `1` and `n` that produces longest Collatz sequence."""
    return max([CollatzRecord(i) for i in range(1, n)], key=lambda x: x.length_of_sequence).seed

def solution():
    return longest_collatz_sequence(1000000)
