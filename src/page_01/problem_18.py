import os

from core import fileio, gridutils

scriptdir = os.path.dirname(os.path.abspath(__file__))

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
    data_file = os.path.join(scriptdir, 'problem_18_data.txt')
    triangle_raw = fileio.read_file(data_file)
    triangle = gridutils.parse(triangle_raw)
    return longest_path(triangle)
