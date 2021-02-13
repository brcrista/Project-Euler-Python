"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from typing import Optional

from mathtools.number_theory import assert_natural

def palindrome(s: str) -> bool:
    return s == ''.join(reversed(s))

def largest_palindrome_product(n: int) -> Optional[int]:
    assert_natural(n)
    n_digit_numbers = range(10 ** (n - 1), 10 ** n)
    products_of_digit_numbers = [x * y for x in n_digit_numbers for y in n_digit_numbers]
    return max(map(int, filter(palindrome, map(str, products_of_digit_numbers))), default=None)

def solution():
    return largest_palindrome_product(3)
