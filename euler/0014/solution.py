from typing import List

from mathtools.number_theory import assert_natural, even

def half_or_triple_plus_one(n: int) -> int:
    """"The function defining the recurrence for the Collatz sequence."""
    assert_natural(n)
    if even(n):
        return n // 2
    else:
        return 3 * n + 1

collatz_memo = {}

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

if __name__ == '__main__':
    print(solution())
