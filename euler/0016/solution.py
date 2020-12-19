def power_digit_sum(n: int) -> int:
    """The sum of the digits of `2 ** n`."""
    return sum(int(c) for c in str(2 ** n))

def solution():
    return power_digit_sum(1000)

if __name__ == '__main__':
    print(solution())
