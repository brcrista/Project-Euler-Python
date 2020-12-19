from mathtools.combinatorics import binomial_coefficient

def solution():
    """The number of lattice paths on a 20 x 20 grid."""
    return binomial_coefficient(40, 20)

if __name__ == '__main__':
    print(solution())
