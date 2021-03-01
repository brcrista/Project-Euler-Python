"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

(See problem_08_data.txt for the number.)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

import os

from typing import Iterable

from core import fileio
from mathtools import product

scriptdir = os.path.dirname(os.path.abspath(__file__))

def substrings_of_length(s: str, length: int) -> Iterable[str]:
    """All substrings of length `length` from `s`."""
    if length < 0:
        raise ValueError(f'`length` was {length} (must be nonnegative)')

    for i in range(0, len(s) - length + 1):
        yield s[i : i + length]

def largest_product_in_string(s: str, substring_length: int) -> int:
    number = ''.join(c for c in s if not c.isspace())
    assert number.isdecimal()

    consecutive_digits = [[int(c) for c in s] for s in substrings_of_length(number, substring_length)]
    return max(map(product, consecutive_digits))

def solution():
    data_file = os.path.join(scriptdir, 'problem_08_data.txt')
    big_number = fileio.read_file(data_file)
    return largest_product_in_string(big_number, substring_length=13)
