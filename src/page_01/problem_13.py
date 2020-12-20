import os

from core import fileio

scriptdir = os.path.dirname(os.path.abspath(__file__))

def first_10_digits(n: int) -> str:
    return str(n)[:10]

def solution():
    data_file = os.path.join(scriptdir, 'problem_13_data.txt')
    lines = fileio.stream_file(data_file)
    return first_10_digits(sum(int(line) for line in lines))
