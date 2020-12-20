from .problem_14 import collatz_sequence, solution

def test_collatz_sequence():
    assert collatz_sequence(1) == [1]
    assert collatz_sequence(13), [13, 40, 20, 10, 5, 16, 8, 4, 2 == 1]

def test_solution():
    assert solution() == 837799
