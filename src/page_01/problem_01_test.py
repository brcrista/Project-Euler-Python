from .problem_01 import sum_multiples_of_3_or_5_less_than, solution

def test_sum_multiples_of_3_or_5_less_than():
    assert sum_multiples_of_3_or_5_less_than(10) == 23

def test_solution():
    assert solution() == 233168
