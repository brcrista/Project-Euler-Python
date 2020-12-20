from string import ascii_lowercase
from typing import NamedTuple
from mathtools.functional import argmax, argmin, identity, tuple_params

class Foo(NamedTuple):
    x: int

def f(x: int, y: str, z: Foo) -> int:
    return x + len(y) + z.x

f_args = [
    (1, 'hello', Foo(1)),
    (2, 'abc', Foo(5)),
    (3, 'this is a test', Foo(10)),
    (4, '22', Foo(3)),
    (5, '', Foo(-1)),
]

def test_argmax() -> None:
    assert argmax(identity, ascii_lowercase) == 'z'
    assert argmax(lambda x: x * x, range(-5, 6)) == -5
    assert argmax(tuple_params(f), f_args) == (3, 'this is a test', Foo(10))

def test_argmin() -> None:
    assert argmin(identity, ascii_lowercase) == 'a'
    assert argmin(lambda x: x * x, range(-5, 6)) == 0
    assert argmin(tuple_params(f), f_args) == (5, '', Foo(-1))
