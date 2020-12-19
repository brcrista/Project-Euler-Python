from mathtools.number_theory import assert_natural

def palindrome(s: str) -> bool:
    return s == ''.join(reversed(s))

def largest_palindrome_product(n: int) -> int:
    assert_natural(n)
    n_digit_numbers = range(10 ** (n - 1), 10 ** n)
    products_of_digit_numbers = [x * y for x in n_digit_numbers for y in n_digit_numbers]
    return max(map(int, filter(palindrome, map(str, products_of_digit_numbers))), default=None)

def solution():
    return largest_palindrome_product(3)

if __name__ == '__main__':
    print(solution())
