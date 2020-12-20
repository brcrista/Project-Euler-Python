import os
import sys

from helpers import print_error, try_int

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

    # Don't assume that solutions to all problems are here.
    # Some might have been skipped.
    # Just ignore files that don't fit the pattern (such as .DS_STORE).
    return { try_int(sln): os.path.join(euler, sln) for sln in os.listdir() if try_int(sln) is not None }