from .problem_16 import power_digit_sum, solution

def test_power_digit_sum():
    assert power_digit_sum(15) == 26

def test_solution():
    assert solution() == 1366
