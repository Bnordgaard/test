from calculations.addition import add


def test_addition_basic():
    assert add(1, 2) == 3


def test_addition_negative():
    assert add(-1, -2) == -3
