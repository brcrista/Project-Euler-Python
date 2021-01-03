from mathtools import sum_range

def sum_multiples_of_3_or_5_less_than(n: int) -> int:
    sum_multiples_of_3 = sum_range(n, step=3)
    sum_multiples_of_5 = sum_range(n, step=5)
    sum_multiples_of_3_and_5 = sum_range(n, step=3 * 5)

    # Multiples of both 3 and 5 have been double-counted.
    return sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_3_and_5

def solution():
    return sum_multiples_of_3_or_5_less_than(1000)
