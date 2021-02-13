# `source` this file to start up the dev environment.

scriptdir=$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>&1 > /dev/null && pwd)

venv_dir="$scriptdir/.venv"
if ! [ -d "$venv_dir" ]; then
    echo "No existing virtual environment was found."
    echo "Creating a new virtual environment at $venv_dir ..."
    echo

    python -m venv "$venv_dir"
    make dependencies
    echo
fi

source "$venv_dir/bin/activate"

export PROJECT_ROOT="$scriptdir"
export PYTHONPATH="$PROJECT_ROOT/src"
export MYPYPATH="$PYTHONPATH"
export PYLINTRC="$PROJECT_ROOT/pylintrc"

echo "Welcome!"
echo "Some commands:"
echo "  script/solution PROBLEM_NUMBER  Show the solution to a single problem"
echo "  make tests                      Run all regression tests"
echo "  deactivate                      Leave the virtual environment"
echo
