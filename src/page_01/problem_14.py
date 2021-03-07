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

from mathtools.functional import argmax, compose
from mathtools.number_theory import assert_positive, even

def half_or_triple_plus_one(n: int) -> int:
    """"The function defining the recurrence for the Collatz sequence."""
    assert_positive(n)
    if even(n):
        return n // 2
    else:
        return 3 * n + 1

_collatz_memo: Dict[int, List[int]] = {}

def _memoize(f):
    def memoized(n):
        if n in _collatz_memo:
            return _collatz_memo[n]
        else:
            result = f(n)
            _collatz_memo[n] = result
            return result
    return memoized

@_memoize
def collatz_sequence(n: int) -> List[int]:
    """
    The Collatz sequence beginning with `n`.
    """
    if n == 1:
        return [1]
    else:
        return [n] + collatz_sequence(half_or_triple_plus_one(n))

def longest_collatz_sequence(n: int) -> int:
    """The seed value between `1` and `n` that produces longest Collatz sequence."""
    return argmax(compose(len, collatz_sequence), range(1, n))

def solution():
    return longest_collatz_sequence(1000000)
