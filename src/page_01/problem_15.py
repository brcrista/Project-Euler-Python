"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

1. right right down  down
2. right down  right down
3. right down  down  right
4. down  right right down
5. down  right down  right
6. down  down  right right

How many such routes are there through a 20×20 grid?
"""

from mathtools.combinatorics import binomial_coefficient

def solution():
    """The number of lattice paths on a 20 x 20 grid."""
    return binomial_coefficient(40, 20)
