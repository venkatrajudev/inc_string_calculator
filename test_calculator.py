from calculator import add

def test_empty_string():
    assert add("") == 0

def test_string_return_single_number():
    assert add("1") == 1


def test_two_number_string():
    assert add("1,5,4,7,3,8,2,9") == 39


