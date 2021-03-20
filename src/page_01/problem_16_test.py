from .problem_16 import digit_sum, solution

def test_digit_sum():
    assert digit_sum(32768) == 26

def test_solution():
    assert solution() == 1366
