from problem_0024 import nth_lexicographic_permutation, solution

def test_nth_lexicographic_permutation():
    assert nth_lexicographic_permutation(range(0, 3), 4) == 120

def test_solution():
    assert solution() == 2783915460
