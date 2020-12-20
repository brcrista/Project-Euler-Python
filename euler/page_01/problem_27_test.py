from problem_0027 import consecutive_primes, solution

def test_consecutive_primes():
    assert consecutive_primes(lambda x: (x * x) + x + 41) == 40

def test_solution():
    assert solution() == -59231
