# `source` this file to set environment variables for the build

scriptdir=$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>&1 > /dev/null && pwd)

export PROJECT_ROOT="$scriptdir"
export PYTHONPATH="$PROJECT_ROOT"
export MYPYPATH="$PYTHONPATH"
export PYLINTRC="$PROJECT_ROOT/pylintrc"
