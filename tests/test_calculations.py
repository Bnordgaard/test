import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculations.addition import add
from calculations.multiplication import multiply


def test_add_basic():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_multiply_basic():
    assert multiply(2, 3) == 6


def test_multiply_zero():
    assert multiply(5, 0) == 0
