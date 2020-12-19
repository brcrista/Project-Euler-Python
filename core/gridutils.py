from typing import List

Grid = List[List[int]]

def parse(grid: str) -> Grid:
    """
    Read a string representing a (possibly jagged) 2-D array of integers into a `Grid`.

    Rows in the grid should be separated by newlines and elements should be separated by spaces.
    """
    return [[int(element) for element in line.split()] for line in grid.splitlines() if line]

def in_bounds(grid: Grid, row_index: int, column_index: int) -> bool:
    """Whether `row_index`, `column_index` are in bounds for the possibly jagged `array_2d`."""
    return 0 <= row_index < len(grid) and 0 <= column_index < len(grid[row_index])
