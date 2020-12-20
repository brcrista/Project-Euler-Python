from mathtools import product

def test_product() -> None:
    assert product([]) == 1
    assert product([1, 2, 3]) == 6
    assert product(range(0, 10000)) == 0
