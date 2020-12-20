from .problem_29 import distinct_powers

def test_distinct_powers():
    assert distinct_powers(5) == 15
    assert distinct_powers(100) == 9183
