from .. import gridutils

TRIANGLE = """
3
7 4
2 4 6
"""

def test_parse():
    triangle = gridutils.parse(TRIANGLE)
    assert len(triangle) == 3

    assert triangle[0] == [3]
    assert triangle[1] == [7, 4]
    assert triangle[2] == [2, 4, 6]
