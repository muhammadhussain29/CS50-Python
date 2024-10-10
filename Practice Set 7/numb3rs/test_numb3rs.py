from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.1.1") == False
    assert validate("cat") == False
    assert validate("266.313.11.2") == False
    assert validate("2.313.111.2") == False