"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def power_digit_sum(n: int) -> int:
    """The sum of the digits of `2 ** n`."""
    return sum(int(c) for c in str(2 ** n))

def solution():
    return power_digit_sum(1000)
