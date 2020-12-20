from .problem_06 import solution, sum_square_difference

def test_sum_square_difference():
    assert sum_square_difference(10) == 2640

def test_solution():
    assert solution() == 25164150
