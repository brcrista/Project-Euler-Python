import glob
import os
import re
import sys

from helpers import print_error

scriptdir = os.path.dirname(os.path.abspath(__file__))

# The repository root
root = os.path.join(scriptdir, "..")

class InDirectory:
    """
    Context manager for `cd`'ing into a directory and back out again.
    """
    def __init__(self, destination):
        self.origin = os.getcwd()
        self.destination = destination

    def __enter__(self):
        os.chdir(self.destination)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.origin)

def index_solutions(project_root):
    """
    Map a problem number to the filepath for each solution relative to the project root.
    """
    euler = os.path.join(project_root, "euler")
    os.chdir(euler)

    problems = {}
    problem_file_regex = re.compile("page_\d+/problem_(\d+)\.py")
    for solution_file in glob.glob("page_*/problem_*.py"):
        match = problem_file_regex.match(solution_file)
        if match:
            problem_number = int(match.group(1))
            problems[problem_number] = os.path.join(euler, match.group(0))
    return problems