from .problem_01 import sum_multiples_of_3_or_5, solution

def test_sum_multiples_of_3_or_5():
    assert sum_multiples_of_3_or_5(10) == 23

def test_solution():
    assert solution() == 233168
