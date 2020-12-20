import importlib.util
import sys

def print_error(msg):
    """
    Print a message to the stderr stream.
    """
    print(msg, file=sys.stderr)

import sys

def import_file(module_name, file_path):
    """
    Recipe from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly.

    Example:
    >>> problem = import_file('problem_01', 'src/page_01/problem_01.py')
    >>> problem.solution()
    233168
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module