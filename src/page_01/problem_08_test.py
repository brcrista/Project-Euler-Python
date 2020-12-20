import os

from core import fileio

from .problem_08 import largest_product_in_series, solution

scriptdir = os.path.dirname(os.path.abspath(__file__))

def test_largest_product_in_series():
    data_file = os.path.join(scriptdir, 'problem_08_data.txt')
    big_number = fileio.read_file(data_file)
    assert largest_product_in_series(big_number, substring_length=4) == 5832

def test_solution():
    assert solution() == 23514624000
