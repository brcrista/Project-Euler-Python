from mathtools.number_theory import divides

def multiples_of_3_and_5(n: int) -> int:
    return sum(x for x in range(0, n) if divides(x, 3) or divides(x, 5))

def solution():
    return multiples_of_3_and_5(1000)

if __name__ == '__main__':
    print(solution())
