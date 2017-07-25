"""
Test something
"""

import hello_world as hw
from . import test

def test_add():
    assert hw.add(5, 3) == 10
    assert hw.add(3, 5) == 10
