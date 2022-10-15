import addition
import pytest
from math import pi

print(pi)

def test_add():
    assert addition.add(4,5) == 9


def test_sub():
    assert addition.sub(4,5) == -1