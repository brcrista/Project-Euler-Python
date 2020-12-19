from mathtools.number_theory import eratosthenes

def sum_of_primes_below(n: int) -> int:
    """The sum of all primes below `n`."""
    return sum(eratosthenes(n))

def solution():
    return sum_of_primes_below(2000000)

if __name__ == '__main__':
    print(solution())
