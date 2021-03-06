from mathtools import product, sum_range

def test_product() -> None:
    assert product([]) == 1
    assert product([1, 2, 3]) == 6
    assert product(range(0, 10000)) == 0

def test_sum_range() -> None:
    # Sums of empty ranges
    assert sum_range(0) == 0
    assert sum_range(-1) == 0
    assert sum_range(1, 1) == 0
    assert sum_range(1, 0) == 0
    assert sum_range(1, 10, step=-1) == 0

    # Sums of singleton ranges
    assert sum_range(1) == 0
    assert sum_range(2) == 1
    assert sum_range(1, 2) == 1
    assert sum_range(2, 3) == 2

    # Sums of natural numbers
    assert sum_range(11) == 55
    assert sum_range(31, step=3) == 165
    assert sum_range(10, 21) == 165
    assert sum_range(9, 31, step=3) == 156

    # Sums with negative numbers
    assert sum_range(-1, -11, step=-1) == -55
    assert sum_range(-9, -31, step=-3) == -156
    assert sum_range(-5, 6) == 0
    assert sum_range(-5, 7) == 6
