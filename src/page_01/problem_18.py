from lib import gridutils

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

class Tree:
    def __init__(self, key, children):
        self.key = key
        self.children = children
        self.max_path = None

def create_binary_tree(grid: gridutils.Grid, i: int, j: int) -> Tree:
    """
    Create a `Tree` from a `grid` where each node has at most two children.

    The children of the element at coordinate `(i, j)` will be
    the elements at `(i + 1, j)` and `(i + 1, j + 1)` if they exist.
    """
    children = [create_binary_tree(grid, row, column)
        for row, column in [(i + 1, j), (i + 1, j + 1)]
        if gridutils.in_bounds(grid, row, column)]

    return Tree(grid[i][j], children)

def longest_tree_path(tree: Tree) -> int:
    if tree.max_path is None:
        child_path_lengths = [longest_tree_path(child) for child in tree.children]
        tree.max_path = tree.key + max(child_path_lengths, default=0)
    return tree.max_path

def longest_path(grid: gridutils.Grid) -> int:
    """
    Find the largest sum along a path through a (possibly jagged) 2-D array of integers.

    Allowed paths begin at element `grid[0][0]` and proceed to one of the adjacent elements
    in the row below. So at coordinate `(i, j)`, the next elements eligible to traverse are
    `(i + 1, j)` and `(i + 1, j + 1)` (assuming they are in bounds).
    """
    return longest_tree_path(create_binary_tree(grid, 0, 0))

def solution():
    triangle = gridutils.parse(TRIANGLE)
    return longest_path(triangle)
