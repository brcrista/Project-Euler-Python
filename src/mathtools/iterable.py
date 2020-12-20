import itertools
from typing import Iterable, Iterator, List, Tuple, TypeVar

_T = TypeVar('_T')

def take(n: int, iterable: Iterable[_T]) -> List[_T]:
    "Return the first `n` items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def unzip(tuples: Iterator[Tuple]) -> List[Iterable]:
    """The inverse of the `zip` built-in function."""
    return [list(x) for x in zip(*tuples)]
