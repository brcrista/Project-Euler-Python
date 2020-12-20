import os

from typing import Iterator

scriptdir = os.path.dirname(os.path.abspath(__file__))

def read_numbers_from_file(filename: str) -> Iterator[int]:
    """Read the list of 50-digit numbers from `filename`"""
    with open(os.path.join(scriptdir, filename)) as fd:
        for line in fd.readlines():
            yield int(line)

def first_10_digits(n: int) -> str:
    return str(n)[0:10]

def solution():
    return first_10_digits(sum(read_numbers_from_file('problem_13_data.txt')))
