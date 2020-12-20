from .problem_07 import nth_prime, solution

def test_nth_prime():
    assert nth_prime(6) == 13

def test_solution():
    assert solution() == 104743
