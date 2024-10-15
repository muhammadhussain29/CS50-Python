from seasons import userinput
import pytest

def test_userinput_valid():
    assert userinput("2000-01-01") == "2000-01-01"
    with pytest.raises(SystemExit):
        userinput("01-01-2000")