from core.iterable import take

from .problem_12 import first_triangle_number_with_more_divisors_than, solution, triangle_numbers

def test_triangle_numbers():
    assert list(take(10, triangle_numbers())) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

def test_first_triangle_number_with_more_divisors_than():
    assert first_triangle_number_with_more_divisors_than(5) == 28

def test_solution():
    assert solution() == 76576500
