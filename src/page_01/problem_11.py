import os

from typing import Callable, List, NamedTuple

from core import fileio, gridutils
from mathtools import product
from mathtools.combinatorics import recurrence
from mathtools.iterable import take

scriptdir = os.path.dirname(os.path.abspath(__file__))

class Coordinates(NamedTuple):
    row: int
    column: int

NextCoordinates = Callable[[Coordinates], Coordinates]

class WindowCreator:
    """Creates windows for a given coordinate in a grid."""
    def __init__(self, grid: gridutils.Grid, coordinates: Coordinates) -> None:
        self.grid = grid
        self.coordinates = coordinates

    def new_window(self, next_coordinates: NextCoordinates) -> List[int]:
        coordinates = take(4, recurrence([self.coordinates], next_coordinates))
        return [self.grid[i][j] for i, j in coordinates if gridutils.in_bounds(self.grid, i, j)]

def right(window_creator: WindowCreator):
    return window_creator.new_window(lambda x: Coordinates(x[0], x[1] + 1))

def down(window_creator: WindowCreator):
    return window_creator.new_window(lambda x: Coordinates(x[0] + 1, x[1]))

def diagonal_right(window_creator: WindowCreator):
    return window_creator.new_window(lambda x: Coordinates(x[0] + 1, x[1] + 1))

def diagonal_left(window_creator: WindowCreator):
    return window_creator.new_window(lambda x: Coordinates(x[0] + 1, x[1] - 1))

def largest_product_in_grid(grid: gridutils.Grid) -> int:
    largest = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            window_creator = WindowCreator(grid, Coordinates(i, j))
            windows = [
                right(window_creator),
                down(window_creator),
                diagonal_right(window_creator),
                diagonal_left(window_creator),
            ]

            largest = max([product(w) for w in windows] + [largest])

    return largest

def solution():
    data_file = os.path.join(scriptdir, 'problem_11_data.txt')
    grid_raw = fileio.read_file(data_file)
    grid = gridutils.parse(grid_raw)
    assert len(grid) == 20
    assert all(len(row) == 20 for row in grid)
    return largest_product_in_grid(grid)
