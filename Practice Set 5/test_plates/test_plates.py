from plates import is_valid

def test_is_valid_letters():
    assert is_valid("hhhhrt") == True

def test_is_valid_mix():
    assert is_valid("0uss21") == False
    assert is_valid("h63331") == False
    assert is_valid("00hh31") == False

def test_is_valid_punc():
    assert is_valid("H-8212") == False
    assert is_valid("PI3.14") == False

def test_is_valid_len():
    assert is_valid("CS05") == False
    assert is_valid("Aa21000") == False
    assert is_valid("Aa21") == True
    assert is_valid("Aa21aa") == False
    assert is_valid("Aa") == True
    assert is_valid("2A") == False
    assert is_valid("2") == False
    assert is_valid("00") == False