from .problem_09 import is_pythagorean, solution

def test_is_pythagorean():
    assert is_pythagorean(3, 4, 5)

def test_solution():
    assert solution() == 31875000
