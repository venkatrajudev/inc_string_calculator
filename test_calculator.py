from calculator import add

def test_empty_string():
    assert add("") == 0

def test_string_return_single_number():
    assert add("1") == 1


def test_two_number_string():
    assert add("1,5") == 6


def test_multiple_number_string():
    assert add("1,5,9") == 15

def test_new_lines_as_delimiter():
    assert add("1\n2\n3") == 6

def test_custom_delimters():
    assert add("//;\n1;2") == 3


