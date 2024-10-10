from um import count

def test_count():
    assert count("um hello um yum") == 2
    assert count("um hello UM yum") == 2