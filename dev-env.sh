# `source` this file to start up the dev environment.

scriptdir=$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>&1 > /dev/null && pwd)

venv_dir="$scriptdir/.venv"
if ! [ -d "$venv_dir" ]; then
    python -m venv "$venv_dir"
fi

source "$venv_dir/bin/activate"

export PROJECT_ROOT="$scriptdir"
export PYTHONPATH="$PROJECT_ROOT"
export MYPYPATH="$PYTHONPATH"
export PYLINTRC="$PROJECT_ROOT/pylintrc"
