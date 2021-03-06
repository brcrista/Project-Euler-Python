"""
problem_22_data.txt is a 46K text file containing over five-thousand first names.
Begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import os

from typing import Iterator

from core import fileio

scriptdir = os.path.dirname(os.path.abspath(__file__))

def alphabetic_value(c: str) -> int:
    """The position of `c` in the Latin alphabet (case insensitive)."""
    return ord(c.upper()) - ord('A') + 1

def name_score(name: str, position: int) -> int:
    """
    The sum of alphabetic values of the letters in the name times the lexicographic position
    of the name in some sequence of names.
    """
    return sum(alphabetic_value(c) for c in name) * position

def tokenize_names(raw_names: str) -> Iterator[str]:
    for line in raw_names.splitlines():
        for name in line.split(','):
            token = name.strip('"')
            if token != '':
                yield token

def total_names_score(raw_names: str) -> int:
    sorted_names = sorted(tokenize_names(raw_names))
    return sum(name_score(name, i + 1) for i, name in enumerate(sorted_names))

def solution():
    data_file = os.path.join(scriptdir, 'problem_22_data.txt')
    names = fileio.read_file(data_file)
    return total_names_score(names)
