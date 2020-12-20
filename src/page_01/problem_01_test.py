from .problem_01 import multiples_of_3_and_5, solution

def test_multiples_of_3_and_5():
    assert multiples_of_3_and_5(10) == 23

def test_solution():
    assert solution() == 233168
