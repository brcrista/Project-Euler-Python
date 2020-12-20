from .problem_23 import is_abundant, non_abundant_sums, solution

abundants_less_than_100 = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]

def test_is_abundant():
    assert not any(is_abundant(i) for i in range(1, 12))
    assert all(is_abundant(i) for i in abundants_less_than_100)

def test_non_abundant_sums():
    assert non_abundant_sums(12), sum(range(1, 12))

def test_solution():
    assert solution() == 4179871
