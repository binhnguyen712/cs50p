from fuel import gauge
from fuel import convert
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_value_string():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_value_integer():
    assert convert("1/4") == 25
    assert convert ("0/1") == 0
    assert convert("4/4") == 100

def test_print():
    assert gauge(25) == "25%"
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"


