from typing import Any, Callable, Iterable, Tuple, TypeVar

_T = TypeVar('_T')
_U = TypeVar('_U')

def _is_iterable(x: Any) -> bool:
    return hasattr(x, '__iter__')

def identity(x: _T) -> _T:
    """The identity function."""
    return x

def compose(f: Callable[[_T], _U], g: Callable[..., _T]) -> Callable[..., _U]:
    """
    Create the composition of `f` and `g`, where the output of `g` is passed to `f`.

    >>> def f(x):
    ...     return 2 * x
    >>> def g(x, y):
    ...     return x - y
    >>> compose(f, g)(1, 2)
    -2
    """
    return lambda *args: f(g(*args))

def tuple_params(f: Callable[..., _T]) -> Callable[[Tuple], _T]:
    """Convert a function to take a tuple of its parameters."""
    def tupled_f(args: Tuple) -> _T:
        return f(*args)
    return tupled_f

def _map_with_args(f: Callable[..., _U], args: Iterable[_T]) -> Iterable[Tuple[_T, _U]]:
    return zip(args, map(f, args))

def argmin(f: Callable[[_T], Any], args: Iterable[_T], *, key: Callable[..., Any]=identity) -> _T:
    """
    The element in `args` that produces the smallest output of `f`.
    If two values of `f` are minimal, returns the first set of arguments in `args`
    that produces the minimal value of `f`.

    >>> argmin(identity, [0, 1, 5, 3])
    0
    >>> argmin(tuple_params(lambda x, y: x + y), [(0, 1), (1, 5), (3, 2)])
    (0, 1)
    """
    return min(_map_with_args(f, args), key=lambda x: key(x[1]))[0]

def argmax(f: Callable[[_T], Any], args: Iterable[_T], *, key: Callable[..., Any]=identity) -> _T:
    """
    The element in `args` that produces the largest output of `f`.
    If two values of `f` are maximal, returns the first set of arguments in `args`
    that produces the maximal value of `f`.

    >>> argmax(identity, [0, 1, 5, 3])
    5
    >>> argmax(tuple_params(lambda x, y: x + y), [(0, 1), (1, 5), (3, 2)])
    (1, 5)
    """
    return max(_map_with_args(f, args), key=lambda x: key(x[1]))[0]
