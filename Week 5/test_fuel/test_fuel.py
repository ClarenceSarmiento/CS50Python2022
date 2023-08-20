from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/100") == 1
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("2/1")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")