import os

from .problem_08 import largest_product_in_data_file, solution

def test_largest_product_in_data_file():
    assert largest_product_in_data_file(substring_length=4) == 5832

def test_solution():
    assert solution() == 23514624000
