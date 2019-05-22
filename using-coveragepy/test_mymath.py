import mymath
import pytest


def test_add_integers():
    result = mymath.add(1, 2)
    assert result == 3


def test_add_floats():
    result = mymath.add(10.5, 2)
    assert(result, 12.5)
