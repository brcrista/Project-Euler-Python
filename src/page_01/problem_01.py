from mathtools import sum_range

def sum_multiples_of_3_or_5(n: int) -> int:
    sum_multiples_of_3 = sum_range(0, n, 3)
    sum_multiples_of_5 = sum_range(0, n, 5)
    sum_multiples_of_3_and_5 = sum_range(0, n, 3 * 5)

    # Multiples of both 3 and 5 have been double-counted.
    return sum_multiples_of_3 + sum_multiples_of_5 - sum_multiples_of_3_and_5

def solution():
    return sum_multiples_of_3_or_5(1000)
