from .problem_11 import largest_product_in_grid, solution

DOWN = [
    list(range(0, 5)),
    list(range(0, 5)),
    list(range(0, 5)),
    list(range(0, 5))
]

RIGHT_DIAGONAL = [
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2]
]

def test_largest_product_in_grid():
    assert largest_product_in_grid(DOWN) == 4 ** 4
    assert largest_product_in_grid(RIGHT_DIAGONAL) == 2 ** 4

def test_solution():
    assert solution() == 70600674
