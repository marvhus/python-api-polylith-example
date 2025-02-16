from marvhus.service_foo import core


def test_sample():
    assert core is not None


def test_retrieve_some_data():
    assert core.retrieve_some_data("a") == [1, 2, 3]
    assert core.retrieve_some_data("b") == [4, 5, 6]
    assert core.retrieve_some_data("c") == [7, 8, 9]
    assert core.retrieve_some_data("d") is None
