from itertools import count
from mathtools.number_theory import is_prime

def nth_prime(n: int) -> int:
    number_of_primes = 0
    for k in count(start=1):
        if is_prime(k):
            number_of_primes += 1
        if number_of_primes == n:
            return k

def solution():
    return nth_prime(10001)

if __name__ == '__main__':
    print(solution())
