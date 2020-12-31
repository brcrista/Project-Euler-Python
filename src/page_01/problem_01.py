from mathtools.number_theory import divides

def sum_multiples_of_3_and_5(n: int) -> int:
    return sum(x for x in range(0, n) if divides(x, 3) or divides(x, 5))

def solution():
    return sum_multiples_of_3_and_5(1000)
