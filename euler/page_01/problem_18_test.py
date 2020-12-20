from core import gridutils
from problem_18 import longest_path, solution

TEST_INPUT_1 = """
3
7 4
2 4 6
8 5 9 3
"""

def test_longest_path():
    assert longest_path([[1]]) == 1
    assert longest_path(gridutils.parse(TEST_INPUT_1)) == 23

def test_solution():
    assert solution() == 1074
