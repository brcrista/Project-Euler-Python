import glob
import os
import re
import sys

from helpers import print_error

scriptdir = os.path.dirname(os.path.abspath(__file__))

# The repository root
root = os.path.join(scriptdir, "..")

def index_solutions(project_root):
    """
    Map a problem number to the filepath for each solution relative to the project root.
    """
    src = os.path.join(project_root, "src")
    os.chdir(src)

    problems = {}
    problem_file_regex = re.compile(r"page_\d+/problem_(\d+)\.py")
    for solution_file in glob.glob("page_*/problem_*.py"):
        match = problem_file_regex.match(solution_file)
        if match:
            problem_number = int(match.group(1))
            problems[problem_number] = os.path.join(src, match.group(0))
    return problems