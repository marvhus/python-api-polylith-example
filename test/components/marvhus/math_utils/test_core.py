from marvhus.math_utils import core


def test_sample():
    assert core is not None

def test_fibbonacci():
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    for index, expect in enumerate(expected):
        assert core.fib(index) is expect

def test_fibbonacci_invalid():
    assert core.fib(None) is None
    assert core.fib(-1) is None
