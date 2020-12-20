from .problem_31 import british_coins, coin_sums, solution

def test_coin_sums():
    assert coin_sums(0, [1, 2, 3]) == 1
    assert coin_sums(0, []) == 1
    assert coin_sums(100, []) == 0
    assert coin_sums(1, [1]) == 1
    assert coin_sums(2, [1]) == 1
    assert coin_sums(2, [2, 1]) == 2
    assert coin_sums(10, [2]) == 1
    assert coin_sums(10, [3]) == 0
    assert coin_sums(10, [1, 2, 5]) == 10
    assert coin_sums(10, [1, 2, 5, 10]) == 11

def test_solution():
    assert solution() == 73682
