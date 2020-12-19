def distinct_powers(n: int) -> int:
    """Number of distinct values of `a ** b` for `2 <= a, b <= n`."""
    powers = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            powers.add(a ** b)
    return len(powers)

def solution():
    print(distinct_powers(100))

if __name__ == '__main__':
    print(solution())
