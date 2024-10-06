from bank import value

def test_h_value():
    assert value("h") == 20
    assert value("hello") == 0
    assert value("Hre") == 20

def test_single_value():
    assert value("H") == 20
    assert value("t") == 100

def test_random_value():
    assert value("elfah") == 100
    assert value("ayfh") == 100