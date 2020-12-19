"""
Automatically regression test all solved problems.

Solved problems should have a script called 'test.py' that runs tests for that problem,
at minimum verifying the correct answer.
This script assumes it lives in the project root.
"""

import os
import sys

class InDirectory:
    """Context manager for `cd`'ing into a directory and back out again."""
    def __init__(self, destination):
        self.origin = os.getcwd()
        self.destination = destination

    def __enter__(self):
        os.chdir(self.destination)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.origin)

def print_error(x):
    print(x, file=sys.stderr)

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Test core
    core_tests = os.path.join(project_root, 'core', 'tests')
    junitXml = os.path.join(project_root, 'junit-xml', 'core.xml')
    exit_code = os.system(f'pytest {core_tests} --junit-xml={junitXml}')
    if exit_code != 0:
        print_error(f'pytest {core_tests} failed with exit code {exit_code}')

    # Test problems
    euler = os.path.join(project_root, 'euler')
    os.chdir(euler)

    num_errors = 0
    for problem in sorted(os.listdir()):
        try:
            with InDirectory(problem):
                name = os.path.join(problem, 'solution.py')
                print(f'Running {name} ...')
                exit_code = os.system('python solution.py')
                if exit_code != 0:
                    num_errors += 1
                    print_error(f'Running {name} failed with exit code {exit_code}')
                print()

                name = os.path.join(problem, 'test.py')
                print(f'Testing {name} ...')
                junitXml = os.path.join(project_root, 'junit-xml', f'test_{problem}.xml')
                exit_code = os.system(f'pytest test.py --junit-xml={junitXml}')
                if exit_code != 0:
                    num_errors += 1
                    print_error(f'Testing {name} failed with exit code {exit_code}')
                print()
        except Exception as e:
            num_errors += 1
            print_error(f'While processing {problem}, encountered {e}')
    return num_errors

if __name__ == '__main__':
    exit(main())
