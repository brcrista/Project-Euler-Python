from itertools import takewhile

from mathtools.number_theory import even
from mathtools.combinatorics import fibonacci_numbers

def sum_even_fibonacci_numbers(n: int) -> int:
    """The sum of even Fibonacci numbers less than `n`."""
    return sum(fib for fib in takewhile(lambda x: x <= n, fibonacci_numbers()) if even(fib))

def solution():
    return sum_even_fibonacci_numbers(4000000)
