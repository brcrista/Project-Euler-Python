import os

from typing import Iterator

from core import fileio
from mathtools import product

scriptdir = os.path.dirname(os.path.abspath(__file__))

def substrings_of_length(series: str, length: int) -> Iterator[str]:
    """All sequences of `length` consecutive characters from `str`."""
    if length < 0:
        raise ValueError(f'`length` was {length} (must be nonnegative)')

    for starting_point in range(0, len(series) - length + 1):
        yield series[starting_point : starting_point + length]

def largest_product_in_series(big_number: str, substring_length: int) -> int:
    series = ''.join(c for c in big_number if not c.isspace())
    assert series.isdecimal()

    consecutive_digits = [[int(c) for c in s] for s in substrings_of_length(series, substring_length)]
    return max(map(product, consecutive_digits))

def solution():
    data_file = os.path.join(scriptdir, 'problem_08_data.txt')
    big_number = fileio.read_file(data_file)
    return largest_product_in_series(big_number, substring_length=13)
