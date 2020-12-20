from typing import List

from mathtools.number_theory import assert_natural

british_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sums(total: int, coin_values: List[int]) -> int:
    if total == 0:
        return 1
    elif coin_values == []:
        return 0
    else:
        number_of_combinations = 0
        next_value = max(coin_values)
        assert_natural(next_value)

        remaining_coin_values = [x for x in coin_values if x < next_value]
        for value_multiple in range(0, total + 1, next_value):
            difference = total - value_multiple
            number_of_combinations += coin_sums(difference, remaining_coin_values)
        return number_of_combinations

def solution():
    return coin_sums(200, british_coins)
