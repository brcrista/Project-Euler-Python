from typing import Iterator

def numbers_on_spiral_diagonals(n: int) -> Iterator[int]:
    k = 1
    yield k

    skip = 2
    end = n * n
    while k < end:
        for _ in range(0, 4):
            k += skip
            yield k
        skip += 2

def sum_of_number_spiral_diagonals(n: int) -> int:
    """
    The sum of the numbers lying on the diagonals of a "number spiral"
    of the numbers `1, ..., n * n`.
    """
    return sum(numbers_on_spiral_diagonals(n))

def solution():
    return sum_of_number_spiral_diagonals(1001)

if __name__ == '__main__':
    print(solution())
