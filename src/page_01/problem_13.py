import os

from core.fileio import stream_file

scriptdir = os.path.dirname(os.path.abspath(__file__))

def first_10_digits(n: int) -> str:
    return str(n)[0:10]

def solution():
    lines = stream_file(os.path.join(scriptdir, 'problem_13_data.txt'))
    return first_10_digits(sum(int(line) for line in lines))
