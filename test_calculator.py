from calculator import add

def test_empty_string():
    return add("") == 0

def test_string_return_single_number():
    return add("1") == 1


def test_two_number_string():
    return add("1,5") == 6


