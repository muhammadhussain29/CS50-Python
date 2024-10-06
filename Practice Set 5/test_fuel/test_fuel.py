from fuel import convert
from fuel import gauge
import pytest

def test_guage():
    assert gauge(1) == "E"
    assert gauge(5) == "5%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("one/two")
    