"""
The sum of the squares of the first ten natural numbers is

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

    (1 + 2 + ... + 10)^2 = 55^2 = 385

Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n: int) -> int:
    return sum(x ** 2 for x in range(1, n + 1))

def square_of_sums(n: int) -> int:
    return sum(range(1, n + 1)) ** 2

def sum_square_difference(n: int) -> int:
    return square_of_sums(n) - sum_of_squares(n)

def solution():
    return sum_square_difference(100)
