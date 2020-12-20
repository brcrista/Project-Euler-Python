import pytest
from mathtools.number_theory import divides, even, odd, is_prime, factors, prime_factorization, lcm

def test_divides() -> None:
    assert divides(1, 1) is True
    assert divides(10, 5) is True
    assert divides(5, 10) is False
    assert divides(0, 2) is True

def test_even_odd() -> None:
    evens = [-1000, -4, -2, 0, 2, 4, 1000]
    odds = [-1001, -1, 1, 5, 7, 63]
    for n in evens:
        assert even(n) is True
        assert odd(n) is False
    for n in odds:
        assert even(n) is False
        assert odd(n) is True

def test_is_prime() -> None:
    primes = [2, 3, 5, 7, 11, 13, 41]
    composites = [4, 6, 12, 100, 10000]
    for n in primes:
        assert is_prime(n) is True
    for n in composites:
        assert is_prime(n) is False
    assert is_prime(1) is False
    assert is_prime(0) is False

def test_factors() -> None:
    with pytest.raises(ValueError):
        factors(0)

    assert factors(1) == [1]
    assert factors(2), [1, 2]
    assert factors(8), [1, 2, 4, 8]

def test_prime_factorization() -> None:
    with pytest.raises(ValueError):
        prime_factorization(0)

    assert prime_factorization(24) == [2, 2, 2, 3]
    assert prime_factorization(42) == [2, 3, 7]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(47231016) == [2, 2, 2, 3, 7, 41, 6857]

def test_lcm() -> None:
    assert lcm(0, 100) == 0
    assert lcm(1, 1) == 1
    assert lcm(2, 4) == 4
    assert lcm(1, 123456) == 123456
    assert lcm(4, 6) == 12
    assert lcm(6, 4) == 12
